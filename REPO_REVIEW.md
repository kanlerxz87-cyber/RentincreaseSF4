# Repository review — line by line

Reviewed: 2026-11-06 UTC by session `arena-73f5f1a2` on branch `arena/73f5f1a2-rentincreasesf4`.
Base commit: `4a404e7a5e6c4d996f17b581bfd2c54a717f7448` ("Initial commit").

## Initial tree

| Line / file | Observed content | Verification | Flag |
| --- | --- | --- | --- |
| `README.md` line 1 | `# RentincreaseSF4` | `cat README.md`; `git show 4a404e7:README.md` | No project description, requirements, data, or source links. |
| Repository root | Only `.git/` and `README.md` | `find . -path ./.git -prune -o -type f -print` | No site, data, tests, scripts, or coordination file at start. |
| Git history | One commit: `4a404e7 Initial commit` | `git log --oneline -8` | No prior work to preserve or merge. |
| Remote branches at start | `main` only, at `4a404e7` | `git ls-remote --heads origin` | Session branch had to be created on first push. |
| GitHub Pages | `status: built`, `build_type: legacy`, `source.branch: main`, `source.path: /`, `https_enforced: true`, URL `https://kanlerxz87-cyber.github.io/RentincreaseSF4/` | `gh api repos/kanlerxz87-cyber/RentincreaseSF4/pages` | Pages already serves the repository **root** of `main`; the site must be built at root, not `/docs`. |
| Repository permissions | `viewerPermission: ADMIN`, default branch `main` | `gh repo view --json nameWithOwner,defaultBranchRef,viewerPermission` | PR creation and merge are available. |

## Irregularities / review items

1. **No `COORDINATION.md` existed.** Created and claimed in T01 before other repo work; first claim commit pushed immediately as `4008ae6`.
2. **Platform branch constraint.** Arena fixes this session to `arena/73f5f1a2-rentincreasesf4`; the requested `session-<id>/<task>` branches cannot be created. Exclusive file scopes are used instead and recorded in `COORDINATION.md`.
3. **GitHub Pages source is root `/`.** A `.nojekyll` file and root-level `index.html` / `pages/` are required; a `docs/` folder would not be published without changing the Pages source.
4. **All case facts are user-provided and unverified.** No building year, address, tenancy dates, rent amounts, tenant names, or rent-control coverage were present in the repository. They are treated as inputs only, anonymized, and flagged on the site's **Flagged for Review** page.
5. **Privacy boundary.** Raw tenant identifiers are stored only in the untracked, gitignored `internal/` directory and are excluded from git and from the published site.

## Manual review links

- Repository: https://github.com/kanlerxz87-cyber/RentincreaseSF4
- Session branch: https://github.com/kanlerxz87-cyber/RentincreaseSF4/tree/arena/73f5f1a2-rentincreasesf4
- GitHub Pages settings (API): https://api.github.com/repos/kanlerxz87-cyber/RentincreaseSF4/pages
- Live site (after deploy): https://kanlerxz87-cyber.github.io/RentincreaseSF4/

Official legal sources used for the substantive findings are catalogued in `SOURCES.md` and `VERIFICATION.md` (T02) and on the site's **Sources** page.

## Re-review 2026-11-07 (session `arena-5cbd3f13`)

The repository had moved from `a0591c3` to `cd42189` through PRs #2–#9 by other sessions. This branch was rebased onto the current `main` and only the deltas below were re-applied, so no other session's work was overwritten.

| Line / file | Finding | Verification | Action |
| --- | --- | --- | --- |
| `scripts/site_pages.py` — case page | Every case value was blank. That satisfies the "blank if unverified" rule but leaves the site without the entries the user asked to see. | Read the built `pages/case.html` and `data/case.json`. | Case facts are now published as clearly labelled `owner-supplied` rows (anonymized, dates and amounts unchanged), beside a separate verification table that stays blank and flagged. |
| `scripts/site_pages.py` — `IND-03` | "19 petitions / 148 units" for capital improvements did not match the source. | Re-fetched S29: the PDF shows capital improvements 18 petitions / 148 units and a subtotal of 19 / 149 that includes one Costa-Hawkins petition. | Corrected to 18 / 148 with a note; recorded as F29. |
| `scripts/validate_site.py` | Source and flag totals were hardcoded (`== 55`, `== 38`), so adding a source or flag would silently break the check or hide a stale dashboard. | Code read. | Counts now come from `len(D.SOURCES)` and `len(D.FLAGS)`. |
| `scripts/validate_site.py` | No duplicate row-ID check; two pages could reuse an ID and links would still resolve to the wrong row. | Ran a counter over all rows during development (two `RATE-09`-style duplicates were found and renamed to `HIST-*` before this pass). | `row IDs are unique across all pages` check added. |
| `scripts/validate_site.py` | No check that owner-supplied rows are labelled and carry no official source; no raw-initial scan of the public case files. | Code read. | Both checks added; `data/case.json` and `pages/case.html` are scanned for initial patterns. |
| `scripts/build_site.py` | The index carried a placeholder hero heading ("Clean landing page / dashboard") and the validator tested for that placeholder. | Rendered `index.html`. | Placeholder replaced with a badge legend and a "start here" pointer; the validator now tests for the direct answer and the legend instead. |
| `scripts/site_flags.py` — `CARDS` | Dashboard totals were typed in by hand. | Code read. | Cards resolve `auto:sources` / `auto:flags` at build time. |
| `.github/workflows/validate.yml` | CI rebuilds and fails if generated outputs are not committed. | `git diff --exit-code` after a rebuild returns clean. | Rebuild outputs are committed with each change. |
| `pages/*.html`, `data/*.json` | Generated files changed by other sessions between this branch's base and `main`. | `git diff --stat a0591c3 origin/main`. | Not merged blindly; branch rebased onto `main` first. |
