# T09 — QA and integration of the D16 outputs (session `arena-abb34cd1`, 2026-11-08)

Scope: take over the stale D16-B (QA) and D16-C (integration) claims, integrate the Rent Board Fee research and the privacy-history finding into the published site, repair the inherited defects, re-verify every changed row against a freshly fetched official page, and publish through a PR to `main`.

## Inherited QA findings and their disposition

| # | Finding (inherited from D16-B) | Where it was | Fix | Verified by |
| --- | --- | --- | --- | --- |
| Q1 | Flag count stale: "38 flags" while the registry held 40 | `REQ-08`, `AN-15` | Both now compute `len(FLAGS)` at build time (`scripts/site_pages.py`) | Validator check "dashboard flag count matches the flag registry" |
| Q2 | Source count stale: "All 52 official sources" while the registry held 55 | `pages/sources.html` header (`scripts/build_site.py`) | Header and the landing-page quick-navigation description now compute `len(D.SOURCES)` | Validator check "Sources page header count is generated, not hardcoded" |
| Q3 | "30 source-quality flags F01-F30" was stale and mis-described the later flags | `FLAGGED_FOR_REVIEW.md` (`scripts/site_text.py`) | Rewritten: total computed, flags grouped F01-F24, F25-F38, T03-F01-F10, plus "what the owner must still do" | Rebuild diff; `FLAGGED_FOR_REVIEW.md` |
| Q4 | Rows about the project's own deliverables cited S43 (HUD Fair Market Rents) as their official source | `REQ-01/02/04/06/08/13/14/19/20`, `AN-15` | New `project record` status: no official source IDs, a repository-artifact link instead, labelled on the page and disclosed as F38 | Validator rejects a project row that carries official source IDs |
| Q5 | Rent Board Fee research merged into the repo but absent from the site | `research/rent_board_fee/README.md` on `main` | New `pages/fee.html` with 26 source-linked rows, new nav entry, new dashboard card, new executive-summary section, sources S56-S62 | Every value re-fetched 2026-11-08 (`VERIFICATION.md` R25-R31) |
| Q6 | Privacy-history finding merged into the repo but absent from the site | `research/privacy/HISTORY_EXPOSURE.md` on `main` | Published as flag F36 with the file as its repository record | File exists; flag visible on `pages/flagged.html` |
| Q7 | Unresolved Git conflict markers were committed inside the published `COORDINATION.md` | `COORDINATION.md` at `d63dee4` | Both sides of the record kept verbatim; the three marker lines removed; validator now fails the build on any marker in a published file | Validator check "no merge-conflict markers in published files" |

## Structural verification performed

- `python3 scripts/build_site.py` then `python3 scripts/validate_site.py`: 21 data files, 19 page HTML files, 62 official sources, 48 flags, 269 table rows (23 owner-supplied, 21 project records, 46 needs-review rows). Result: **99 checks, 0 errors**.
- Every fee row's source IDs are constrained by a validator check to the fee block (S56-S62) plus S53/S07 (business-registration-number field) and S02 (deposit-interest rate), so no fee claim can silently borrow an unrelated source.
- Privacy: the fingerprint regression test still runs with no private intake present, and the initials scan of `data/case.json` / `pages/case.html` still passes.

## Limits of this QA pass

- This is structural and source-word verification, not legal advice and not an attorney review. No attorney has approved any increase.
- The fee arithmetic ($118.00 / $59.00 / $17.70) is conditional on owner-supplied unit counts; the January 2027 Annual Notice does not exist yet (F33).
- The absence finding in F32 ("no official page links fee payment to a valid increase") is an absence, not an official statement that the two are unrelated.
- Two surfaces cannot be checked from inside a session: the deploy status of the commit that contains this very file, and the residual copies of the raw tokens outside GitHub (F36).
