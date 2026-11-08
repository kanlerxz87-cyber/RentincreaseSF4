# D16-B — Independent QA of the integrated site, 2026-11-08

Session `arena-18eafb4c` · QA date 2026-11-08 (UTC) · scope: every published table row, source statement, flag, count and internal link after the T08 branch was merged. Informational compliance research, not legal advice.

## What was checked, and how

| Check | Method | Result |
| --- | --- | --- |
| Official pages behind the new/changed rows | Direct `fetch_page` on 2026-11-08: sf.gov/rent-board-fee (both chunks), sf.gov/recover-part-your-rent-board-fee-tenant, Chapter 37A PDF (both chunks), Form 573 PDF, the 2027 informational notice, the Treasurer's lessor page, the security-deposit page, CIV 1942.5, the Costa-Hawkins single-family page and the new-construction exemption page | 10 pages re-read; one wording defect found (F36), one citation defect found (F37) |
| Every row has an official source | `scripts/validate_site.py` row loop: source ID exists, URL on an approved official domain, status valid, `needs review` rows blank and flagged | 296 rows, 0 errors |
| Flag integrity | Every flag `needs review`, every flag has official sources, numeric IDs unique and contiguous, every referenced flag ID published | 54 flags, 0 errors |
| Counts vs. reality | Source count, flag count and page count are now computed at build time; the validator fails on any leftover `{{...}}` placeholder or any stale hard-coded total | 70 sources, 54 flags, 19 pages |
| Broken internal links | Every `href`/`src` in `index.html` and `pages/*.html` resolved against the file tree | 0 broken links |
| Privacy | Fingerprint regression test for the six raw identifiers; no exact street address; placeholder IDs only; dates and amounts preserved | 0 hits |
| Source integrity (semantic) | Each requirements/analysis row's cited source read against the row's claim | 10 rows cited HUD FMR irrelevantly -> F37, corrected |
| Statement accuracy | Each source `statement` compared word by word with the page it summarises | S60 in-law nuance wrong -> F36, corrected |
| Committed conflict markers | Regex scan of every public `.md`, `.json`, `.html` | `COORDINATION.md` markers removed; validator now fails if any reappear (F31) |

## Defects found and corrected in this session

1. **F36 — in-law exemption nuance.** SF.gov says a **legal** in-law unit makes a two-unit building that is not exempt, and an **illegal** one is not exempt **unless both units are rented together as a single tenancy**. The site (S60, LOC-23, Q-20, F35, executive summary) merged the two rules. Corrected in all five places plus `VERIFICATION.md` R20.
2. **F37 — requirements rows cited an unrelated official source.** REQ-01/02/04/06/08/13/14/19/20 and AN-15 cited S43 (HUD Fair Market Rents) for claims about this website. They now cite the project record (S68 repository, S69 Pages build API); the two project-record sources are labelled and excluded from legal/rent findings.
3. **Stale totals.** "38 flags" (actual count had moved on), "All 52 official sources" and "30 source-quality flags" were typed by hand. All are now computed at build time, and the validator fails on any stale total.
4. **F19/F20 stale.** REQ-19 and REQ-20 still described a pending pull request; updated with the verified merge and Pages-build record.
5. **Committed conflict markers.** `COORDINATION.md` on `main` carried `<<<<<<<` / `=======` / `>>>>>>>` lines (F31). Removed, both sessions' records kept, validator check added.

## New material integrated

* **Rent Board Fee page** (`pages/fee.html`): 28 source-linked rows covering who pays, the 2026-2027 amount ($59.00 per dwelling unit), the March 1 deadline, the 5%/5%/5% penalty ladder, the June 1/July referral question (F38), exemptions, the December 14, 2026 exemption deadline, the 50% tenant recovery and its two permitted methods, banking, the Small Claims rule, the 4.2% deposit-interest rate, City business registration, and case arithmetic ($118.00 for two units; $59.00 maximum recovery; $17.70 maximum penalty illustration).
* **Flags F38–F43** (fee-specific) and **F44** (privacy: the raw identifiers remain in this public repository's git history and pull-request diffs; remediation is an owner action, listed in `research/privacy/HISTORY_EXPOSURE.md`).

## Not verified — left blank and flagged

* Whether either unit is reported into the Housing Inventory or currently licensed (T03-F05).
* The official building year, lot configuration, coverage determination and exact address (existing flags).
* The fee billed, exemption status or business-registration status for these two units (F43).
* Prior rent-increase history, so no banked percentage is asserted (F30).
* Whether a Section 6.14 notice was served on the April 2026 occupant (F28).
* The 3/1/2027–2/28/2028 allowable rate, which SF.gov had not published (F27).
* The 94122 SAFMR row, whose official ZIP row was not obtained (F13).

## Limits of this QA

Structural and textual checks are not a legal review, and no attorney has approved any proposed increase. The site states this on every page. Passing these checks does not guarantee that a tenant, a tenant-side lawyer, the Rent Board or a court would accept a particular increase.
