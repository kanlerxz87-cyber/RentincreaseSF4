#!/usr/bin/env python3
"""Count-only privacy regression check. Never print or write identifier values.

Uses the existing validator's one-way fingerprints; does not duplicate private
intake. Scans tracked files and optional new QA files. If the historical report
is available, read it into memory only to prove the detector catches that leak.
A clean current tree is NOT a git-history purge.
"""
import ast
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATTERN = re.compile(r"(?<![A-Za-z])[A-Z]\s+[A-Z](?![A-Za-z])|(?<![A-Za-z])[A-Z]{2}(?![A-Za-z])")


def fingerprints():
    tree = ast.parse((ROOT / "scripts/validate_site.py").read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "private_fingerprints" for t in node.targets):
            values = ast.literal_eval(node.value)
            if len(values) != 6 or any(not re.fullmatch(r"[0-9a-f]{64}", v) for v in values):
                raise ValueError("Expected six SHA-256 fingerprints; no values printed")
            return set(values)
    raise ValueError("Existing privacy fingerprint baseline not found")


def count_matches(text, baseline):
    return sum(hashlib.sha256(" ".join(m.split()).encode()).hexdigest() in baseline for m in PATTERN.findall(text))


def main():
    baseline = fingerprints()
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    additions = [str(p.relative_to(ROOT)) for p in (ROOT / "research/n08_qa").rglob("*")
                 if p.is_file() and "node_modules" not in p.parts]
    paths = sorted(set(filter(None, tracked + additions)))
    current_files = []
    for name in paths:
        p = ROOT / name
        try:
            count = count_matches(p.read_text(encoding="utf-8"), baseline)
        except (UnicodeDecodeError, OSError):
            continue
        if count:
            current_files.append({"file": name, "matching_candidates": count})
    result = {
        "baseline_fingerprints": len(baseline),
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
        result["historical_fixture_matching_candidates"] = count_matches(old, baseline)
        result["historical_fixture_note"] = "Known historical report read into memory only; detector count recorded, values withheld."
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        pass
    print(json.dumps(result, indent=2))
    out = ROOT / "research/n08_qa/privacy-result.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 1 if current_files else 0


if __name__ == "__main__":
    sys.exit(main())
