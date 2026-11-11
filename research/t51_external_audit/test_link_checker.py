#!/usr/bin/env python3
"""No-network tests of source-link diagnostic classification."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from check_external_links import classify


class LinkCheckerTests(unittest.TestCase):
    def test_http_status_classification(self):
        self.assertEqual(classify(200, "application/pdf"), "reachable")
        self.assertEqual(classify(404), "broken")
        self.assertEqual(classify(410), "broken")
        for status in (401, 403, 405, 429, 500, 503):
            self.assertEqual(classify(status), "inconclusive")

    def test_soft_404(self):
        self.assertEqual(classify(200, "text/html", b"<title>Page not found | Agency</title>"), "broken")
        self.assertEqual(classify(200, "text/html", b"<h1>Official information</h1>"), "reachable")
        self.assertEqual(classify(200, "text/html", b"Invalid parameters"), "broken")


if __name__ == "__main__":
    unittest.main()
