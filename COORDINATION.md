# COORDINATION.md — shared task board

Session ID: `arena-73f5f1a2`
Branch: `arena/73f5f1a2-rentincreasesf4`
Last updated: 2026-11-06 UTC

## Status legend

- `unclaimed` — no session has claimed the task.
- `in progress` — claimed; only the owning session edits the listed file scope.
- `done` — sources, verification and irregularities recorded below.
- `needs review` — item is published on the site's **Flagged for Review** page; it does **not** block other work or the merge.

## Platform / branch note

Arena fixes this session to the single branch `arena/73f5f1a2-rentincreasesf4` and does not permit creating, switching to, or pushing additional branches. The requested `session-<id>/<task>` branches are therefore replaced by **exclusive, non-overlapping file scopes on the one permitted branch**. No other sessions or task claims were present when work began: the repository contained only `README.md` at commit `4a404e7`.

GitHub Pages is already enabled on this repository with legacy source `main` / `/` at `https://kanlerxz87-cyber.github.io/RentincreaseSF4/`. The published site is therefore built at the repository root, not in a `docs/` folder. A `.nojekyll` file will be added so static HTML is served as-is.

Push procedure: the first push created the remote branch; every subsequent push is preceded by `git pull --rebase origin arena/73f5f1a2-rentincreasesf4`. Merge conflicts are logged in the "Conflict / handoff log" section below and resolved without discarding another session's work. A claim older than 60 minutes with no commits may be taken over by another session, which must note the handoff here.

## Task board

| ID | Task | Status | Owner | File scope (exclusive) | Sources / verification performed | Irregularities / flags |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | Coordination, repo review, privacy boundary | `done` | `arena-73f5f1a2` | `COORDINATION.md`, `.gitignore`, `REPO_REVIEW.md`, `internal/` (untracked/private only) | `git status`, `git log`, `git ls-remote`, `cat README.md`, `find`, `gh repo view`, `gh api .../pages`; line-by-line review recorded in `REPO_REVIEW.md`. | Branch constraint; Pages source is root `/`; no code/data/site at start; all case facts user-provided/unverified; raw identifiers confined to gitignored `internal/`. |
| T02 | Official-source research and line-by-line verification ledger | `in progress` | `arena-73f5f1a2` (claimed 2026-11-06 UTC) | `SOURCES.md`, `VERIFICATION.md`, `research/sources/`, `research/verification/` | — | — |
| T03 | Anonymized case facts, calculations, flags (research copies) | `unclaimed` | — | `research/case_facts.md`, `research/calculations.md`, `research/flags.md` | — | — |
| T04 | Final integration: shared table data, site generation, index/navigation, build + broken-link validation | `unclaimed` | — | `data/`, `scripts/`, `index.html`, `pages/`, `assets/`, `.nojekyll`, `EXECUTIVE_SUMMARY.md`, `FLAGGED_FOR_REVIEW.md`, `README.md` | — | — |
| T05 | Pull request, merge, GitHub Pages deploy confirmation, record PR/merge result | `unclaimed` | — | `COORDINATION.md` (final update only) | — | — |

## Final integration session

Only after T01–T03 are `done`, the final integration session (this session, since no other sessions were detected) claims T04, merges the research into the shared `data/` files, re-verifies every row line by line, confirms the site builds with no broken internal links, and publishes. T05 then opens the PR to `main`, merges it, confirms the Pages deployment, and records the PR link and merge result here. Flagged and unverified items are published on the clearly labeled **Flagged for Review** page and do not block the merge.

## Conflict / handoff log

- 2026-11-06 UTC: no conflicts at start; remote contained only `main` at `4a404e7`. First push (`4008ae6`) created `arena/73f5f1a2-rentincreasesf4` on origin. No other sessions detected, no handoffs, no conflicting claims.

## Requests to other sessions

- None. No files outside this session's claimed scopes will be edited. `COORDINATION.md` is the shared task board: each task owner may make status/log edits to it, while substantive files remain in the listed exclusive scopes.

## Sources / verification / irregularities by task

- **T01 — done.** Sources: local git/gh inspection and GitHub Pages API response (2026-11-06 UTC). Verification: initial tree contained `README.md` only (line 1: `# RentincreaseSF4`); one commit; remote `main` only; Pages `status: built`, `build_type: legacy`, `source.branch: main`, `source.path: /`; repository `viewerPermission: ADMIN`. Irregularities: platform branch constraint; Pages root source; no project data; all case facts unverified; privacy boundary created with `.gitignore` and untracked `internal/tenant-identifiers.local.md`. Full detail: `REPO_REVIEW.md`.
- **T02 — not started.**
- **T03 — not started.**
- **T04 — not started.**
- **T05 — not started.**
