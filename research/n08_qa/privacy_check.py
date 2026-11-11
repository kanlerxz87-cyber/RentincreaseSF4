#!/usr/bin/env python3
"""Count-only privacy regression check. Never print or write identifier values.

Allowlist-only scan (C72-D02 fix, 2026-11-11 I1D): stores ZERO tokens or
digests derived from any private person's name or initials. Standalone
2-letter uppercase tokens must be in the explicit allowlist below; any
other such token is counted (values withheld). Scans tracked files and
optional new QA files. If the historical report is available, read it into
memory only to prove the detector catches that leak. A clean current tree
is NOT a git-history purge.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
URL_RE = re.compile(r"https://[^\s)>\]]+")
TWO_UPPER_RE = re.compile(r"(?<![A-Za-z0-9_-])[A-Z]{2}(?![A-Za-z0-9_-])")
SPACED_RE = re.compile(r"(?<![A-Za-z])[A-Z]\s+[A-Z](?![A-Za-z])")

ALLOWED_TWO_UPPER_TOKENS = {
    "AA", "AB", "AK", "AL", "AN", "AZ", "BR", "CA", "CH", "CI", "EX",
    "FR", "FY", "ID", "IV", "LL", "LP", "NO", "OF", "OR", "PO",
    "PR", "QA", "SB", "SF", "ST", "TO", "TT", "UI", "US",
}


def count_matches(text):
    scrubbed = URL_RE.sub(" ", text)
    # Strip long integrity/hash strings (e.g. package-lock sha512) so their
    # substrings are not mistaken for standalone tokens.
    scrubbed = re.sub(r"[A-Za-z0-9+/=]{20,}", " ", scrubbed)
    count = sum(1 for tok in TWO_UPPER_RE.findall(scrubbed) if tok not in ALLOWED_TWO_UPPER_TOKENS)
    if SPACED_RE.search(scrubbed.replace("Q&A", " ")):
        count += 1
    return count


def main():
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    additions = [str(p.relative_to(ROOT)) for p in (ROOT / "research/n08_qa").rglob("*")
                 if p.is_file() and "node_modules" not in p.parts]
    paths = sorted(set(filter(None, tracked + additions)))
    current_files = []
    for name in paths:
        p = ROOT / name
        try:
            count = count_matches(p.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, OSError):
            continue
        if count:
            current_files.append({"file": name, "matching_candidates": count})
    result = {
        "baseline_allowlisted_tokens": len(ALLOWED_TWO_UPPER_TOKENS),
        "baseline_digests_stored": 0,
        "files_scanned": len(paths),
        "current_tree_matching_candidates": sum(x["matching_candidates"] for x in current_files),
        "current_tree_files_with_matches": current_files,
        "historical_fixture_matching_candidates": None,
        "historical_fixture_note": "Not available in this checkout; no history conclusion drawn.",
        "privacy_values_printed": False,
        "scope_limit": "Current-tree cleanliness does not remove git history, PR diffs, other branches, forks, caches or prior downloads.",
    }
    try:
        old = subprocess.check_output(["git", "show", "0ede010:data/validation_report.json"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
        result["historical_fixture_matching_candidates"] = count_matches(old)
        result["historical_fixture_note"] = "Known historical report read into memory only; detector count recorded, values withheld."
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        pass
    print(json.dumps(result, indent=2))
    out = ROOT / "research/n08_qa/privacy-result.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 1 if current_files else 0


if __name__ == "__main__":
    sys.exit(main())
