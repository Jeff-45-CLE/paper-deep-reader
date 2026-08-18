#!/usr/bin/env python3
"""Validate a Paper Deep Reader Markdown note.

The checker uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class Issue:
    severity: str
    rule_id: str
    line: int
    message: str
    excerpt: str


def load_config(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Config file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON config: {path}: {exc}") from exc


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def clean_excerpt(value: str, limit: int = 120) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value if len(value) <= limit else value[: limit - 1] + "…"


def mask_non_prose(markdown: str) -> str:
    """Mask fenced code, inline code, tables, and display equations.

    Line count and character offsets are preserved where practical.
    """

    def preserve_newlines(match: re.Match[str]) -> str:
        block = match.group(0)
        return "".join("\n" if char == "\n" else " " for char in block)

    masked = re.sub(r"```.*?```", preserve_newlines, markdown, flags=re.DOTALL)
    masked = re.sub(r"\$\$.*?\$\$", preserve_newlines, masked, flags=re.DOTALL)
    masked = re.sub(r"`[^`\n]+`", lambda match: " " * len(match.group(0)), masked)

    lines: list[str] = []
    for line in masked.splitlines(keepends=True):
        stripped = line.lstrip()
        is_table = stripped.startswith("|") and "|" in stripped[1:]
        is_h1 = stripped.startswith("# ")
        if is_table or is_h1:
            lines.append("".join("\n" if char == "\n" else " " for char in line))
        else:
            lines.append(line)
    return "".join(lines)


def find_pattern_issues(
    text: str,
    rules: Iterable[dict[str, Any]],
    severity: str,
) -> list[Issue]:
    issues: list[Issue] = []
    for rule in rules:
        try:
            pattern = re.compile(rule["regex"], flags=re.MULTILINE | re.DOTALL)
        except re.error as exc:
            raise SystemExit(f"Invalid regex in rule {rule.get('id')}: {exc}") from exc

        matches = list(pattern.finditer(text))
        if severity == "warning" and "max_count" in rule:
            matches = matches[int(rule["max_count"]):]

        for match in matches:
            issues.append(
                Issue(
                    severity=severity,
                    rule_id=rule["id"],
                    line=line_number(text, match.start()),
                    message=rule["message"],
                    excerpt=clean_excerpt(match.group(0)),
                )
            )
    return issues


def check_required_sections(markdown: str, config: dict[str, Any]) -> list[Issue]:
    headings = [
        match.group(1).strip()
        for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)\s*$", markdown)
    ]
    issues: list[Issue] = []

    for section in config.get("required_sections", []):
        alternatives = section["alternatives"]
        found = any(
            any(alt.lower() in heading.lower() for alt in alternatives)
            for heading in headings
        )
        if not found:
            issues.append(
                Issue(
                    severity="error",
                    rule_id=f"missing-section:{section['id']}",
                    line=1,
                    message=f"Missing required section. Expected one of: {', '.join(alternatives)}",
                    excerpt="",
                )
            )

    for section in config.get("removed_sections", []):
        for pattern_text in section["patterns"]:
            match = re.search(re.escape(pattern_text), markdown, flags=re.IGNORECASE)
            if match:
                issues.append(
                    Issue(
                        severity="error",
                        rule_id=f"removed-section:{section['id']}",
                        line=line_number(markdown, match.start()),
                        message=f"Removed section reintroduced: {pattern_text}",
                        excerpt=clean_excerpt(match.group(0)),
                    )
                )
    return issues


def check_placeholders(markdown: str, config: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for pattern_text in config.get("placeholder_patterns", []):
        pattern = re.compile(pattern_text, flags=re.IGNORECASE)
        for match in pattern.finditer(markdown):
            issues.append(
                Issue(
                    severity="error",
                    rule_id="placeholder",
                    line=line_number(markdown, match.start()),
                    message="Unresolved template placeholder.",
                    excerpt=clean_excerpt(match.group(0)),
                )
            )
    return issues


def split_sentences(text: str) -> list[tuple[int, str]]:
    """Split prose into sentences without merging unrelated Markdown lines."""

    sentences: list[tuple[int, str]] = []
    global_offset = 0
    boundary = re.compile(r"[。！？!?][”’\"']?|(?<!\d)\.(?:\s|$)")

    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        if not content.strip() or content.lstrip().startswith("#"):
            global_offset += len(line)
            continue

        local_start = 0
        for match in boundary.finditer(content):
            local_end = match.end()
            sentence = content[local_start:local_end]
            if sentence.strip():
                sentences.append((global_offset + local_start, sentence))
            local_start = local_end

        tail = content[local_start:]
        if tail.strip():
            sentences.append((global_offset + local_start, tail))
        global_offset += len(line)

    return sentences


def check_lengths(text: str, config: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    max_cn = int(config.get("max_chinese_sentence_chars", 90))
    max_en = int(config.get("max_english_sentence_words", 35))
    max_paragraph = int(config.get("max_paragraph_chars", 450))

    for start, sentence in split_sentences(text):
        compact = re.sub(r"\s+", "", sentence)
        cjk_count = len(re.findall(r"[\u3400-\u9fff]", sentence))
        if cjk_count >= 5 and len(compact) > max_cn:
            issues.append(
                Issue(
                    severity="warning",
                    rule_id="long-chinese-sentence",
                    line=line_number(text, start),
                    message=f"Chinese sentence exceeds {max_cn} characters.",
                    excerpt=clean_excerpt(sentence),
                )
            )
        elif cjk_count < 5:
            words = re.findall(r"\b[\w'-]+\b", sentence)
            if len(words) > max_en:
                issues.append(
                    Issue(
                        severity="warning",
                        rule_id="long-english-sentence",
                        line=line_number(text, start),
                        message=f"English sentence exceeds {max_en} words.",
                        excerpt=clean_excerpt(sentence),
                    )
                )

    offset = 0
    for paragraph in re.split(r"\n\s*\n", text):
        index = text.find(paragraph, offset)
        if index == -1:
            index = offset
        offset = index + len(paragraph)
        plain = re.sub(r"(?m)^#{1,6}\s+", "", paragraph).strip()
        if len(plain) > max_paragraph and not plain.startswith("|"):
            issues.append(
                Issue(
                    severity="warning",
                    rule_id="long-paragraph",
                    line=line_number(text, index),
                    message=f"Paragraph exceeds {max_paragraph} characters.",
                    excerpt=clean_excerpt(plain),
                )
            )
    return issues


def check_evidence_anchor(markdown: str, config: dict[str, Any]) -> list[Issue]:
    anchor_pattern = config.get("evidence_anchor_regex")
    if not anchor_pattern:
        return []
    if re.search(anchor_pattern, markdown, flags=re.IGNORECASE):
        return []
    return [
        Issue(
            severity="warning",
            rule_id="missing-evidence-anchor",
            line=1,
            message="No Section, Equation, Figure, Table, Algorithm, or Appendix anchor was found.",
            excerpt="",
        )
    ]


def validate(markdown: str, config: dict[str, Any]) -> list[Issue]:
    prose = mask_non_prose(markdown)
    issues: list[Issue] = []
    issues.extend(check_required_sections(markdown, config))
    issues.extend(check_placeholders(markdown, config))
    issues.extend(find_pattern_issues(prose, config.get("forbidden_patterns", []), "error"))
    issues.extend(find_pattern_issues(prose, config.get("discouraged_patterns", []), "warning"))
    issues.extend(find_pattern_issues(prose, config.get("vague_claim_patterns", []), "warning"))
    issues.extend(check_lengths(prose, config))
    issues.extend(check_evidence_anchor(markdown, config))
    return sorted(issues, key=lambda issue: (issue.line, issue.severity, issue.rule_id))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a Paper Deep Reader Markdown note.")
    parser.add_argument("note", type=Path, help="Markdown note to validate.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "config" / "style_rules.json",
        help="Path to style_rules.json.",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return a non-zero exit code when warnings exist.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.note.exists():
        print(f"Note file not found: {args.note}", file=sys.stderr)
        return 2

    config = load_config(args.config)
    markdown = args.note.read_text(encoding="utf-8")
    issues = validate(markdown, config)

    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]

    if args.json:
        payload = {
            "note": str(args.note),
            "errors": len(errors),
            "warnings": len(warnings),
            "issues": [asdict(issue) for issue in issues],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if not issues:
            print(f"PASS: {args.note}")
        else:
            for issue in issues:
                excerpt = f" | {issue.excerpt}" if issue.excerpt else ""
                print(
                    f"{issue.severity.upper():7} L{issue.line:<4} "
                    f"{issue.rule_id}: {issue.message}{excerpt}"
                )
            print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s).")

    if errors:
        return 1
    if warnings and args.fail_on_warning:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
