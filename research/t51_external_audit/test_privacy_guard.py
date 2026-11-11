#!/usr/bin/env python3
"""Regression tests use synthetic values only; no private case input needed."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import privacy_guard


class PrivacyGuardTests(unittest.TestCase):
    def test_placeholders_are_checked_and_tampering_is_detected(self):
        case = json.loads((ROOT / "data/case.json").read_text(encoding="utf-8"))
        self.assertEqual(privacy_guard.check_case_placeholders(case), (0, 0))
        rows = {r["id"]: r for sec in case["sections"] for r in sec["rows"]}
        rows["CASE-10"]["value"] = "unexpected occupant text"
        rows["MAP-1"]["label"] = "unexpected label"
        self.assertEqual(privacy_guard.check_case_placeholders(case), (1, 1))

    def test_generic_weak_hash_detector_reports_path_not_digest(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            good = root / "good.txt"
            bad = root / "bad.txt"
            good.write_text(hashlib.sha256(b"non-personal long sample").hexdigest())
            bad.write_text(hashlib.sha256(b"Z Z").hexdigest())
            self.assertEqual(privacy_guard.weak_digest_files([good, bad], root), ["bad.txt"])


if __name__ == "__main__":
    unittest.main()
