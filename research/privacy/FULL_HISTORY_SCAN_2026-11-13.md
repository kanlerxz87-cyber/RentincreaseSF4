# Full-history privacy re-scan — 2026-11-13 (session `arena-3b66c553`, task T58)

This file deliberately contains **no raw identifier**. Patterns were supplied only through a shell variable during the scan and are not written here.

## Why this scan was run

The earlier history counts (flag F56 before this correction: "12 distinct commits dated 2026-11-06 to 2026-11-11", also in `REPO_REVIEW.md` and `research/s23_2026-11-13/README.md`) could not be reproduced. A local clone of this repository is shallow (depth 1), so any count taken from it is incomplete. This re-scan uses a complete mirror of every ref.

## Method (reproducible without printing any token)

```
git clone --bare https://github.com/kanlerxz87-cyber/RentincreaseSF4.git full.git   # complete history, all refs
cd full.git
git rev-list --all --count                               # commits
git for-each-ref | wc -l                                 # refs
# Per commit: does the commit's tree contain any of the six tokens?
for c in $(git rev-list --all); do
  git grep -l -E "$PATTERN" "$c" -- . >/dev/null && echo "$c"
done
# Per ref tip: same test on the tip tree
for r in $(git for-each-ref --format='%(refname)'); do
  c=$(git rev-parse "$r^{commit}")
  git grep -q -E "$PATTERN" "$c" -- . && echo "TIP: $r"
done
```

`$PATTERN` is the six-token word-boundary expression held in a local shell variable (the tokens themselves are never written to a tracked file).

## Results (scan date 2026-11-13 UTC)

| Measure | Result |
| --- | --- |
| Commits in complete mirror | 258 |
| Refs in complete mirror (branches and tags) | 43 |
| Commits whose tree contains any of the six tokens | **14** |
| Date range of those 14 commits | 2026-11-06 to 2026-11-08 |
| File in which the tokens appear | `data/validation_report.json` only |
| Ref tips whose tree contains the tokens | `arena/73f5f1a2-rentincreasesf4` (tip `5784c29`) and `arena/fce57ebb-rentincreasesf4` (tip `a5923e9`) |
| Current `main` (`ad20650`) and this branch | **Clean** — no token |

Commits whose tree contains a token (short hashes and dates only): `0ede010` 11-06, `94cdb9f` 11-06, `5784c29` 11-06, `a0591c3` 11-06, `40dc3e7` 11-07, `c3333ef` 11-07, `821879b` 11-07, `a439535` 11-07, `f4e4b9a` 11-07, `c29476e` 11-07, `9751ed9` 11-07, `a5923e9` 11-07, `dd65349` 11-07, `e06575e` 11-08.

Commits that **add** a token line: only `0ede010` (2026-11-06).

## Consequence

- The exposure is confined to the history of one generated file, and the current tree is clean.
- It is still public: the repository is public and the commits above are reachable from the mirror.
- Remediation (history rewrite, force-push, branch deletion, GitHub Support request, or making the repository private) needs an explicit owner decision. No agent in this session rewrote history, force-pushed, or deleted a branch.
- Published as flags F44, F51 and F56 on the Flagged for Review page.
