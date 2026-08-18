from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_note.py"
CONFIG = ROOT / "config" / "style_rules.json"

spec = importlib.util.spec_from_file_location("validate_note", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ValidateNoteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG.read_text(encoding="utf-8"))

    def test_valid_note_has_no_errors(self) -> None:
        text = (ROOT / "tests" / "fixtures" / "valid_note.md").read_text(encoding="utf-8")
        issues = module.validate(text, self.config)
        errors = [issue for issue in issues if issue.severity == "error"]
        self.assertEqual(errors, [])

    def test_invalid_note_has_multiple_errors(self) -> None:
        text = (ROOT / "tests" / "fixtures" / "invalid_note.md").read_text(encoding="utf-8")
        issues = module.validate(text, self.config)
        errors = [issue for issue in issues if issue.severity == "error"]
        rule_ids = {issue.rule_id for issue in errors}
        self.assertGreaterEqual(len(errors), 6)
        self.assertIn("cn-not-but", rule_ids)
        self.assertIn("cn-worth-noting", rule_ids)
        self.assertIn("removed-section:what-to-remember", rule_ids)
        self.assertIn("placeholder", rule_ids)


if __name__ == "__main__":
    unittest.main()
