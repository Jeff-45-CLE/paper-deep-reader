# Publishing Checklist

## Before the first public release

- [ ] Choose the final repository name.
- [ ] Confirm the repository URL in `CITATION.cff`.
- [ ] Confirm the author name and license year.
- [ ] Read the synthetic example and verify every value is labeled as constructed.
- [ ] Run `python -m unittest discover -s tests`.
- [ ] Run `python scripts/validate_note.py examples/toy-paper/note.zh-CN.md`.
- [ ] Check all local Markdown links.
- [ ] Create a clean repository without generated caches.
- [ ] Tag the first release as `v0.1.0`.

## Suggested GitHub About text

```text
An open skill for closed-loop paper understanding, terminology preservation, claim-evidence mapping, and Feishu-ready research notes.
```

## Suggested topics

```text
academic-papers
literature-review
research-notes
ai-agents
agent-skills
paper-reading
feishu
markdown
```

## Suggested first release title

```text
Paper Deep Reader v0.1.0 — Closed-loop paper learning notes
```

## Release assets

- source archive;
- `SKILL.md` as a standalone file;
- one generated example note;
- changelog excerpt.

## After publishing

- Add a repository social preview image when available.
- Pin the repository on the GitHub profile.
- Use Issues to collect failure cases from different paper types.
- Add real-paper examples only when redistribution and quotation rights are clear.
