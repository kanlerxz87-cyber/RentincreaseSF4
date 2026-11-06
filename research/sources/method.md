# Verification method

Session `arena-73f5f1a2`, 2026-11-06 UTC.

1. **Source discovery:** `web_search` was used only to locate official government/SEC URLs. Search snippets were never treated as the final authority for a published value.
2. **Direct verification:** every cited page was opened with `fetch_page`. Long HTML pages, PDFs and SEC filings were read in chunks; remaining chunks of CA Civil Code §§827, 1947.12, 1954.53, CA Gov Code §12955, SF Admin Code §37.10B, GovInfo 42 USC 3604, SF Rent Board minutes, AB 1482 and SF.gov "Learn about rent increases" were fetched before final publication.
3. **Cross-checking:**
   - 1.6% / 1.4% / 1.7% cross-checked across SF.gov Learn, Current Rates, Jan. 14, 2026 announcement and Form 571.
   - State cap cross-checked across SF.gov AB 1482 report and Civil Code §1947.12.
   - §6.14/Costa-Hawkins cross-checked across SF.gov pages, Civil Code §1954.53, and Jan. 13, 2026 Rent Board minutes.
   - FMR/SAFMR figures cross-checked across HUD USER documentation pages and FY2026/FY2027 schedules.
   - Corporate figures cross-checked against SEC EDGAR exhibit/10-K text, not press summaries.
4. **No inference:** owner-supplied case facts are inputs only, not official-verified facts. Dates and dollar amounts are preserved on the public site, but all tenant identifiers are replaced with placeholders and source cells for those facts are blank.
5. **Blank-and-flag rule:** if a value could not be confirmed from an official source — notably the 94122 SAFMR row, exact address, building year, license status, rent history, tenant legal status, attorney approval, or a federal private-rent cap — the value cell is blank and the item is listed in `unverified.md` and on the site's **Flagged for Review** page with source links.
6. **Irregularities:** every stale snippet, 404, PDF title mismatch, example inconsistency, footnote conflict, temporary CPI methodology and unparsed data file is recorded in `irregularities.md`.
7. **Final integration:** `scripts/validate_site.py` re-reads every `data/*.json` row line by line, requires official source links, blank unverified values, flagged-page coverage, privacy scanning and internal-link resolution before merge.

## Tools / evidence

- `fetch_page` for official SF.gov, SF Rent Board, SF Planning, CA Legislative Information, CA CRD, HUD USER, eCFR, GovInfo, SEC EDGAR, MOHCD and GitHub Pages API.
- `web_search` only for official leads.
- `git`/`gh` for repository, PR, merge and Pages status.
- `bash` for local validation, link checks and static-site verification.
