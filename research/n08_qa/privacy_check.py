#!/usr/bin/env python3
"""Limited case-file privacy check; does not claim a repository/history audit."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
paths = [ROOT / "data/case.json", ROOT / "pages/case.html"]
pattern = re.compile(r"\b[A-Z]{1,2}\s[A-Z]{1,2}\b")
hits = [str(p.relative_to(ROOT)) for p in paths if pattern.search(p.read_text(encoding="utf-8"))]
print("Case-file privacy check:", "review required" if hits else "no matching initials pattern")
print("Scope: case files only; does not check git history, PRs, or all personal data.")
sys.exit(bool(hits))
