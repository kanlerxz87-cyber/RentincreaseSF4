# D16-P — Git-history / PR-diff exposure of the raw tenant-identifier tokens

Session `arena-d16cbfc8` · audit date 2026-11-07 (UTC). **This file deliberately contains no raw identifier.** The six identifiers are referred to only as "the six raw tokens" (initials-style strings the user supplied; the public placeholders are Tenant A-F).

## Finding (FACT, reproducible)

The first generated validation report, `data/validation_report.json`, printed the six raw tokens in the `detail` field of one check (line 318 of the file). It was committed in `0ede010` (2026-11-06 14:09 UTC) and published by merging PR #1 (`a0591c3`). The leak was found independently on 2026-11-07 by sessions `arena-6f344b80` and `arena-2e273eee`; the validator was changed to report counts/fingerprints only (PRs #2 and #4, merged 2026-11-07 ~20:02 UTC). The site's flag **F26** records that the file was regenerated.

**What F26 does not say, and this audit adds:** removing the line from the latest commit does not remove it from the public repository.

## Where the tokens are still reachable (verified 2026-11-07 ~20:20 UTC)

| Surface | Status | How verified |
| --- | --- | --- |
| Repository visibility | **Public** (`isPrivate: false`), 0 forks, 0 stars, 0 watchers | `gh repo view --json isPrivate`; `gh api repos/<owner>/<repo>` |
| Git history of `main` | **Contains the tokens** in every commit from `0ede010` until the fix (about 30 hours of history; also visible inside the PR #1 merge `a0591c3`) | `git log --all -S<string>`; `git show <commit>:data/validation_report.json` |
| Pull-request diffs | PRs **#1, #2, #4, #5 (closed) and #9** each contain at least one commit whose diff shows the tokens (added or removed lines) | per-PR commit list from `gh pr view <n> --json commits`, then `git show --format= <sha> -- data/validation_report.json` |
| Branch tips (any ref still pointing at an old report) | `origin/arena/73f5f1a2-rentincreasesf4` (tip `5784c29`) and `origin/arena/fce57ebb-rentincreasesf4` (tip `a5923e9`) **still contain the tokens in their current tree**; every other branch tip, including `main` (`c2a7116` at audit time), does not | `git grep` with in-shell word-boundary patterns on each tip |
| Current `main` working tree and this branch | **Clean** — no raw token in any tracked file | `git grep` on the working tree |
| Live GitHub Pages file `/data/validation_report.json` | **Clean** on 2026-11-07 (fetched; privacy checks now read "6 one-way fingerprints; no private intake required") | `fetch_page` of the deployed file |
| Anything outside GitHub's control (anyone's earlier clone or download from 2026-11-06 14:09 UTC to 2026-11-07 ~20:02 UTC, search-engine or web-archive snapshots, earlier Pages deployments cached elsewhere) | **Unknown / cannot be checked or removed by this project** | not verifiable |

## Severity (assessment, not a legal conclusion)

* Exposed: six initials-style tokens. Not exposed by this defect: full names, street address, phone, email.
* The same public site shows ZIP 94122, a build year, unit rents and lease dates (all as the user asked, anonymized with Tenant A-F), so tokens plus those facts could in principle help a reader who already knows the tenants link them to the case. This is a judgment call for the owner; the project's rule is that tenant identifiers are internal-only, so the exposure is reported rather than minimized.

## What agents did and did not do

* Done: validator rewritten to report counts/one-way fingerprints (no raw tokens) — PRs #2/#4; report regenerated; CI (`.github/workflows/validate.yml`) rebuilds and fails on drift; this audit documents every remaining surface.
* **Not done, on purpose:** rewriting history, force-pushing `main` or any other session's branch, deleting other sessions' branches, or contacting GitHub Support. Session rules allow each session to push only its own branch, and a history rewrite is destructive (see GitHub's own list of side effects below), so it needs the repository owner's decision.

## Owner remediation options (choose; none is required to read the site)

1. **Decide whether the exposure matters** (initials only). If acceptable, no further action is needed beyond the disclosure on the site's Flagged for Review page (flag F26 today; the history-exposure flag is added in D16-C).
2. **Delete the two stale branches whose tips still carry the tokens** (`arena/73f5f1a2-rentincreasesf4`, `arena/fce57ebb-rentincreasesf4`) in the GitHub UI (Branches page) — they belong to finished sessions; their work is already merged (PR #1 and PR #3).
3. **Purge history** with `git filter-repo` on a fresh mirror clone, replacing the literal check-detail string in `data/validation_report.json` across all commits, then force-push all refs. GitHub's guidance: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository . It lists the side effects: commit hashes change; open and closed PR diff views break; other clones can re-introduce the data; signatures are lost.
4. **Ask GitHub Support to remove cached views and pull-request references** after a rewrite. GitHub states Support removes "cached views and references to the sensitive data in pull requests", but "will only assist in the removal of sensitive data in cases where we determine that the risk can't be mitigated by rotating affected credentials" — personal-data requests may be declined.
5. **Stopgap:** make the repository private while remediating. This also takes the GitHub Pages dashboard offline unless the owner's plan serves Pages from a private repository.

## Recurrence control (already in the repo)

`scripts/validate_site.py` stores only one-way fingerprints of the six tokens, scans every public file for them, and fails the build on a match; CI runs it on every push and pull request. Do not add the raw tokens to any file, commit message, issue or PR text.

## Reproduce without printing the tokens

```
# patterns must come from the private intake or a local shell variable, never from a tracked file
for ref in $(git for-each-ref --format='%(refname)' refs/remotes/origin); do
  git grep -l -I -E "$PRIVATE_TOKEN_REGEX" "$(git rev-parse "$ref")" -- . && echo "EXPOSED at tip of $ref"
done
git log --all --format='%h %ad %s' -S"$PRIVATE_LEAKED_STRING"
```
