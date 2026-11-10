# T48 — B87-I worksheet integration and final verification record

Session `arena-3dc8a405`, branch `arena/3dc8a405-rentincreasesf4`. Date: **2026-11-10 UTC**.

This session integrated the B87 notice-worksheet kit (`research/b87_notice_kit/`, task **B87-I**, explicitly yielded to the final integration owner) into the shared site, re-verified every **newly published** source with direct `fetch_page` reads on 2026-11-10, rebuilt, and re-ran every gate. No other session's work was reverted, renumbered or discarded.

## 1. Fresh official-source verification (direct fetch_page, 2026-11-10)

Every one of the 11 sources that the integration added or relied on was opened directly this session. Quotes below are excerpts from those fetches.

| New site ID | Kit ID | Official URL | Fetch result (2026-11-10) | Exact short quote / verified content |
| --- | --- | --- | --- | --- |
| S73 | B87-S03 | https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent | chunk 0, complete | Rule 13.14: an increase "purporting to be effective while the landlord is unlicensed shall render the entire rent increase null and void; provided, however, that the effective date of the rent increase, not the date of service, shall be used"; applies to increases effective on/after July 1, 2022 and, for condos/buildings under 10 units, on/after March 1, 2023. |
| S74 | B87-S04 | https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-70881 | chunk 18 | "SEC. 37.3. RENT LIMITATIONS." text located, including the annual-increase subsection opening "On March 1 of each year, the Board shall publish the increase in the CPI for the preceding 12 months". American Legal Publishing is the official publisher (flag F17). |
| S75 | B87-S06 | https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-16540 | chunk 15 | "SEC. 37.15. REPORTING OBLIGATIONS; LICENSING." — reporting under penalty of perjury; base rent in $250 increments for tenant-occupied units; buildings with fewer than 10 units report commencing March 1, 2023 and annually by March 1; contact changes within 30 days; (e) substantial compliance yields a license. |
| S76 | B87-S07 | https://media.api.sf.gov/documents/625_RR_Complete_1-13-26.pdf | chunk 0 | Cover: "Effective Date: January 13, 2026"; table of contents confirms Rule 1.11 Anniversary Date, 1.12 Annual Rent Increase (1/13/26 amendment for the missing October 2025 CPI), 4.10 Notice, 4.12 Banking, 13.14 Licensing. |
| S77 | B87-S08 | https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring | chunk 0 | Rule 4.10(a) written notice must state which portion is annual and/or banked (plus the other listed components); 4.10(b) nonconforming increase null and void unless it equals no more than the allowable annual and banked increase(s), good-faith tolerance one-half of one percent. |
| S78 | B87-S10 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1013.&lawCode=CCP | chunk 0 | Service by mail complete at deposit; +5 calendar days if both places in California, +10 if either outside CA but within the US, +20 if outside the US; the copy "shall bear a notation of the date and place of mailing or be accompanied by an unsigned copy of the affidavit or certificate of mailing". |
| S79 | B87-S11 | https://www.dre.ca.gov/publications/ResourceGuidebook/2026_Landlord_Tenant_Guide.pdf | chunk 9 | Fixed-term: "the landlord cannot raise the tenant's rent during the tenancy, unless the rental agreement expressly allows rent increases." |
| S80 | B87-S12 | https://www.dre.ca.gov/publications/ResourceGuidebook/gb08_living.html | chunks 0, 2 | Notice must be in writing; personal delivery or first-class mail to the rental unit; +5 days from within California (35/95-day examples); "the local ordinance may impose stricter rent limits and additional requirements on the landlord." |
| S81 | B87-S19 | https://www.sf.gov/information--operating-and-maintenance-expense-petitions | chunk 0, complete | "The landlord must file the O&M petition before serving the notice of increase"; "If the notice is issued before the petition is filed, the notice is void"; granted O&M becomes base rent, imposed only on the anniversary date after proper written notice. |
| S82 | B87-S24 | https://www.sf.gov/information--failure-repair-and-maintain-petitions | chunk 0, complete | "The petition must be filed no later than 60 days following the tenant's receipt of the rent increase notice"; tenant pays the disputed increase pending decision and is refunded if granted; "The tenant's anniversary date is not affected by the deferral." |
| S26 (statement extended) | B87-S27 | https://www.sf.gov/rent-board-forms-forms-center | chunks 0, 5, 6, 7 | Forms 516A–517, 571–579, 581–595 confirmed. Form 583: "This form is used to share a list of specific documents that you delivered to the other parties in your case." No mandatory annual rent-increase notice template found. The page also carries the same November 9, 2026 File 261020 notice as S01/S02/S72 (consistent). |

Re-fetch of the primary pages backing existing rows used by the kit (not re-listed as new): S01 (learn-about-rent-increases, chunk 0 — 1.6% 3/1/26–2/28/27, licence rule, notice rules, File 261020 notice all re-confirmed).

## 2. Integration performed (B87-I)

| Change | File | Detail |
| --- | --- | --- |
| 10 new official sources | `scripts/site_sources.py` | S73–S82 added with agencies, categories and 2026-11-10 statements; S26 statement extended with the Form 583 finding. Sources total 72 → **82**. |
| Two new official domains | `scripts/validate_site.py` | `codelibrary.amlegal.com` (official Administrative Code publisher, per F17) and `dre.ca.gov` (California Department of Real Estate) added to `OFFICIAL_DOMAINS` with an explanatory comment. |
| 8 worksheet flags | `scripts/site_flags.py` | B87-F01–B87-F08 appended with source IDs mapped to canonical site sources (meaning unchanged). Flags total 57 → **65**. |
| Navigation + card | `scripts/site_flags.py` | `("worksheet", "Notice Worksheet")` inserted after the Notice Checklist; one dashboard card added. |
| New page (40 rows) | `scripts/site_pages.py` | `worksheet` page loaded from `research/b87_notice_kit/worksheet.json` at build time (kit stays the single source of truth); B87 source IDs mapped via `B87_SOURCE_MAP`; status `verified rule` → `verified`; needs-review cells kept **blank** with flag links; extra flags appended to notes. Six sections: owner inputs (4), pre-service gates (12), notice contents (10), conditional arithmetic (2), service rules (8), service log (4). |
| Cross-link | `scripts/site_pages.py` | New `CHK-18` row on the Notice Checklist page links to the worksheet. |
| Text deliverables | `scripts/site_text.py` | Executive summary paragraph, README bullet and Flagged summary line added for the worksheet/B87 flags. |
| Validator guards (4 new) | `scripts/validate_site.py` | Worksheet published + in nav; all 40 rows carry official sources with valid statuses and blank flagged needs-review cells; all 8 B87 flags on the Flagged page; worksheet linked from the Notice Checklist page. |
| Coordination dedupe | `COORDINATION.md` | The duplicated `arena-5c09f807` T46 section (flagged by T47) — the earlier incomplete copy was removed and the complete copy (with the PR #31 record) kept verbatim; no record content discarded. |

## 3. Gates run after the integration (all on the final tree)

| Gate | Command | Result |
| --- | --- | --- |
| Site build | `python3 scripts/build_site.py` | 22 data files, 20 page HTML files, index, CSS, `.nojekyll`, 3 markdown deliverables |
| Line-by-line validation | `python3 scripts/validate_site.py` | **119 checks, 0 errors** — 82 sources, 65 flags, 347 rows, 67 needs-review rows, 0 broken internal links, no conflict markers, privacy fingerprints 0 current-tree matches |
| B87 kit still valid | `python3 research/b87_notice_kit/validate_kit.py` | **19 checks, 0 errors** |
| Privacy regression | `python3 research/n08_qa/privacy_check.py` | **0 current-tree fingerprint matches** (historical exposure unchanged — F44) |
| Broken-link sweep (independent) | local HTMLParser sweep of `index.html` + all `pages/*.html` | **0 broken internal links** |

## 4. Irregularities found this session (do not block)

1. **Task-ID collision (process).** This session initially claimed "T47"; `arena-7dafb029` had already used T47 on `main`. Resolved by renumbering this claim to **T48** during the merge; both records kept verbatim.
2. **Forms Center URL variant.** The kit cites `https://www.sf.gov/rent-board-forms-forms-center`; the site's S26 uses `https://www.sf.gov/reports--rent-board-forms-forms-center`. Both paths serve the same official Forms Center page; rows are mapped to S26 rather than duplicating the source. Verified at the kit's path this session.
3. **Duplicate T46 coordination section** (previously reported by T47): deduped this session as described above; the complete copy retained.
4. **Stale PRs #18/#19/#25 left open.** T45's record states they were deliberately "left open, not closed or merged, to preserve that work", and T47 re-confirmed their contents are superseded or divergent. This session did **not** close them, preserving both sessions' decision; closing them remains an owner call.
5. **No new legal irregularity.** Every worksheet figure re-checked: $3,995 × 1.6% = $63.92 → $4,058.92 and $3,150 × 1.6% = $50.40 → $3,200.40 (Python `Decimal`), matching the B87 kit and the site's Calculations page. The 1.6% rate, $59.00 fee, licence rule, 24-month banking, 30/90-day notice and 8.8% AB 1482 figures were unchanged by this integration.

## 5. Privacy

No raw tenant identifier appears in any file this session created or edited. The worksheet publishes only placeholders (Tenant A–F), the owner-supplied dates (`February 1, 2025`, `April 1, 2026`, `June 1, 2019`) and amounts (`$3,995`, `$3,150`) exactly as supplied, with all unverified cells blank and flagged (B87-F01). Current-tree cleanliness is not a history purge; F44 remains open and owner-actionable.
