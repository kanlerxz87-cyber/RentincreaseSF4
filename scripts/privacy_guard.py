"""Privacy checks that do not publish private names or their fingerprints.

These are structural safeguards, not proof of anonymity or a git-history purge.
Never write private identifiers, candidate strings, or digest values to reports.
"""

import hashlib
import itertools
import json
import re
import string
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHA256 = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
TENANT_GROUP = re.compile(r"Tenant [A-F](?:(?:, | and )Tenant [A-F])*")
EXPECTED_MAP = {f"MAP-{i}": f"Tenant {letter}" for i, letter in enumerate("ABCDEF", 1)}
GROUP_IDS = ("CASE-10", "CASE-11", "CASE-16")


def tracked_and_new_files():
    """Return tracked and unignored files; never traverse .git or private intake."""
    names = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
    ).decode("utf-8").split("\0")
    paths = []
    for name in sorted(set(filter(None, names))):
        p = ROOT / name
        if name.startswith("internal/") or not p.is_file() or p.is_symlink():
            continue
        paths.append(p)
    return paths


def check_case_placeholders(case):
    """Check case-specific placeholder fields without needing secret input."""
    rows = {r["id"]: r for sec in case["sections"] for r in sec["rows"]}
    group_errors = sum(
        1 for rid in GROUP_IDS
        if rid not in rows or not TENANT_GROUP.fullmatch(rows[rid].get("value", ""))
    )
    map_errors = sum(
        1 for rid, expected in EXPECTED_MAP.items()
        if rid not in rows or rows[rid].get("label") != expected
    )
    return group_errors, map_errors


def weak_digest_files(paths, root):
    """Find reversible two-letter hashes and report file names only."""
    # An unsalted hash of a very short identifier is not anonymization. Detect
    # *any* two-letter uppercase or spaced-initial digest, not a secret baseline.
    # Candidate hashes exist only in memory and are never printed or saved.
    weak_digests = {
        hashlib.sha256(candidate.encode("ascii")).hexdigest()
        for a, b in itertools.product(string.ascii_uppercase, repeat=2)
        for candidate in (a + b, a + " " + b)
    }
    weak_files = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if any(digest in weak_digests for digest in SHA256.findall(text)):
            weak_files.append(str(path.relative_to(root)))
    return weak_files


def inspect():
    """Return only counts and paths, never the private-looking text or digests."""
    case = json.loads((ROOT / "data/case.json").read_text(encoding="utf-8"))
    group_errors, map_errors = check_case_placeholders(case)
    paths = tracked_and_new_files()
    weak_files = weak_digest_files(paths, ROOT)
    return {
        "files_scanned": len(paths),
        "tenant_group_errors": group_errors,
        "placeholder_map_errors": map_errors,
        "files_with_recoverable_two_letter_hashes": weak_files,
        "scope_limit": (
            "Structural checks only: not a complete personal-information audit, "
            "not proof of anonymity, and not a git-history, PR-diff, branch or cache purge."
        ),
    }
