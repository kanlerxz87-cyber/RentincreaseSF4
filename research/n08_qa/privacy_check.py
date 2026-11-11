#!/usr/bin/env python3
"""Run generic, count-only privacy safeguards; never publish private baselines.

This checks current tracked/unignored files, not git history, PR diffs, other
branches, caches, or downloaded copies. Passing is not proof of anonymity.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from privacy_guard import inspect


def main():
    result = inspect()
    result["privacy_values_printed"] = False
    result["status"] = "passed" if (
        not result["tenant_group_errors"]
        and not result["placeholder_map_errors"]
        and not result["files_with_recoverable_two_letter_hashes"]
    ) else "failed"
    print(json.dumps(result, indent=2))
    (ROOT / "research/n08_qa/privacy-result.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
