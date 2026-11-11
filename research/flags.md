# Flagged for Review — research copy (T03)

Session `arena-73f5f1a2`, 2026-11-06 UTC. This is the research copy of the items that must appear on the public site's clearly labeled **Flagged for Review** page. Status `needs review` means published with source links and does **not** block any task or the merge. Final integration publishes these from `data/flags.json` to `pages/flagged.html`.

## T03-specific flags

| ID | Flag | Published value / wording | Official source(s) | Status |
| --- | --- | --- | --- | --- |
| T03-F01 | Case facts are owner-supplied, not official-verified. | Dates and amounts preserved; source cells blank. | [SF.gov rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws), [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [Tenant petition](https://www.sf.gov/report-unlawful-rent-increase-or-request-review-your-rent-history) | needs review |
| T03-F02 | Personal information is top priority. | Placeholders only; no real names, initials, contact details, or exact address; raw identifiers remain internal-only and gitignored. | [SF.gov tenant resources](https://www.sf.gov/tenant-and-landlord-resources) (for official resources only) | needs review |
| T03-F03 | Exact address, 1940 building year, and rent-control coverage not officially verified. | Blank; 1940 is before June 13, 1979 cutoff but property-specific coverage must be checked in PIM. | [SF.gov rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws), [SF Planning PIM](https://sfplanninggis.org/PIM/) | needs review |
| T03-F04 | Unit 1 continuing tenancy / current tenants on April 1, 2026: legal status unknown. | No inference about original occupant, co-tenant, subtenant, assignee, or new tenancy. No market-rate reset recommended. | [§6.14/Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins), [Petition determination](https://www.sf.gov/information--petition-determination-pursuant-section-614-andor-costa-hawkins), [Civil Code §1954.53](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.53.&lawCode=CIV), [Jan. 13, 2026 minutes](https://media.api.sf.gov/documents/minutes_011326.pdf) | needs review |
| T03-F05 | Prior increases, banked increases, license, notice history and anniversary dates unknown. | Blank; no banked increase computed. | [Banked rent increases](https://www.sf.gov/information--banked-rent-increases), [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | needs review |
| T03-F06 | Arithmetic is illustrative only. | Owner-supplied amounts × official rates; not a recommendation, not eligibility determination, not attorney-approved. | [Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco), [Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit), [Form 571](https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf) | needs review |
| T03-F07 | 94122 FY2026/FY2027 Small Area FMR row not obtained from official data. | Blank; no nonofficial ZIP estimate substituted. | [SAFMR index](https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html), [FY2026 SAFMR schedule](https://www.huduser.gov/portal/datasets/fmr/fmr2026/FY2026_Small_Area_FMR_Schedule.pdf), [FY2027 schedule](https://www.huduser.gov/portal/datasets/fmr/fmr2027/FY2027_Small_Area_FMR_Schedule.pdf), [FY2027 xlsx](https://www.huduser.gov/portal/datasets/fmr/fmr2027/FY27_safmrs.xlsx) | needs review |
| T03-F08 | No official general federal private-rent cap, attorney approval, guarantee of no complaint/lawsuit, or both-units requirement found. | Blank; conservative checklist only. | [HUD FMR page](https://www.huduser.gov/portal/datasets/fmr.html), [24 CFR 100.500](https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/part-100/subpart-G/section-100.500), [Tenant resources](https://www.sf.gov/tenant-and-landlord-resources), [Rent Board counseling](https://www.sf.gov/speak-rent-board-counselor) | needs review |
| T03-F09 | No official comparative source proves what all large corporations or all individual SF owners do. | SEC and Rent Board figures are portfolio-level or formal-petition counts only. | [IRT SEC exhibit](https://www.sec.gov/Archives/edgar/data/1466085/000143774926003792/ex_895776.htm), [Invitation Homes 10-K](https://www.sec.gov/Archives/edgar/data/1687229/000168722926000016/invh-20251231.htm), [June 2024 workload](https://www.sf.gov/file/workload-stats-june-2024pdf) | needs review |
| T03-F10 | Any increase must be framed as a conservative compliance checklist capable of tenant-lawyer review. | No claim of actual attorney approval or guarantee. | [Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco), [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [Civil Code §827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827&lawCode=CIV), [24 CFR 100.500](https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/part-100/subpart-G/section-100.500) | needs review |

## T02 source-quality flags carried forward

All 24 flags F01–F24 in `research/sources/irregularities.md` are also published on the **Flagged for Review** page with their official source links. They include:

- SF.gov rent-increase and banked-increase example inconsistencies (F01–F03).
- Form 571 PDF title metadata mismatch (F04).
- SF §37.10B Larson footnote conflict (F05).
- Temporary CPI methodology in Jan. 13, 2026 Rent Board minutes (F06).
- Stale search snippets, chunk split, 404 URL variants, GovInfo substitution and HUD FHA redirect (F07–F11, F16, F18).
- FY2027 vs FY2026 HUD effective dates and unparsed 94122 SAFMR data (F12–F14).
- SEC Equity Residential search dead end and narrow corporate/individual evidence (F15, F23).
- Rent Ordinance "not official record" note, Pages root source, platform branch constraint, unverified case facts, and missing federal/attorney/both-units sources (F17, F19–F22, F24).

See `research/sources/irregularities.md` and `research/sources/unverified.md` for the complete list and links.

## Added 2026-11-07 (`arena-c007d556`)

- F25 — Next year's allowable rate not yet published: the Current Rates page lists 1.6% only through 2/28/27 on 2026-11-07; an increase effective on or after 3/1/27 needs the next published rate. Sources: S02, S01. Value left blank.
- F26 — Unit 1 §6.14 notice history unknown: whether a written 6.14 notice was served on the occupant added April 1, 2026 (within a reasonable time, generally 60 days) and whether that occupant is a co-tenant or a subtenant was not supplied. Sources: S16, S15, S37. No market-rate reset inferred.


## Added 2026-11-07 (session `arena-5cbd3f13`)

- F29 — **Correction, capital-improvement petition count.** The June 2024 workload statistics show 18 capital-improvement petitions covering 148 units; the 19 / 149 subtotal includes one Costa-Hawkins petition. The site previously published "19 petitions / 148 units", which mixed the subtotal with the capital-improvement unit count. Corrected in `data/individual.json`, `pages/individual.html` and the executive summary. Source: S29.
- F30 — **Banked-increase illustration is conditional.** A 13.1% total for Unit 2 (1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 skipped years, plus 1.6% current = 13.1%, i.e. $412.65 on $3,150) is published as arithmetic only. It assumes no increase since June 1, 2019, which the owner has not confirmed, and it would require 90 days' written notice. It is not a recommendation and is not relied on elsewhere. Sources: S05, S04, S02.
- Case facts are published as `owner-supplied` rows (anonymized) rather than blank cells; the official-verification rows for the same facts stay blank and flagged. No raw initials are published: the validator now scans `data/case.json` and `pages/case.html` for initial patterns.

## T09 additions (2026-11-08, session `arena-abb34cd1`)

| ID | Flag | Detail | Source / record |
| --- | --- | --- | --- |
| F31 | Fee-page collection timing differs inside one SF.gov page | Summary and Sec. 37A.4 say referral after June 1; the same page's timeline says a July Notice of Delinquent Payment then 30 days | S56, S58 |
| F32 | No official statement links fee payment to a rent increase's validity | Absence finding across S56, S57, S58 and Sec. 37.15; the license turns on the reporting obligation | S53, S56, S57, S58 |
| F33 | Case fee billing/exemption/unit-count facts unverified | No Annual Notice, exemption status or portal data; $118.00 / $59.00 / $17.70 are conditional arithmetic | S56, S59, S60 |
| F34 | Form 573 covers 7/1999-6/2026 and is titled 25-26 | 2026-27 amount comes from the SF.gov fee page, not the form | S56, S59 |
| F35 | Older fee service page still shows 2023 dates | "March 1, 2023" / "June 1, 2023" on `sf.gov/pay-your-rent-board-fee` | S56, S60 |
| F36 | Raw identifier tokens remain reachable in public git history | Commits from the 2026-11-06 report to the fix, PR diffs #1/#2/#4/#5/#9, two branch tips; agents cannot rewrite history | `research/privacy/HISTORY_EXPOSURE.md` |
| F37 | Published merge-conflict markers | Three marker lines were committed in `COORDINATION.md` at `d63dee4`; repaired, validator hardened | `COORDINATION.md` |
| F38 | Project-deliverable rows cite repository artifacts, not official sources | No government source can confirm a website build or a PR; labelled `project record` | `pages/requirements.html` |

## T44-A / T44-B canonical flag-ID reconciliation and F45 addition (2026-11-08, session `arena-44eac0b7`)

The `T09 additions` table above recorded session `arena-abb34cd1`'s pre-reconciliation local numbering (`F31`–`F38`). In the canonical published registry (`scripts/site_flags.py`, `data/flags.json`, `pages/flagged.html`, and `FLAGGED_FOR_REVIEW.md`), the merged numbering is `F31`–`F45`:

| Canonical Flag ID | Published Title & Scope | Source IDs |
| --- | --- | --- |
| F19 | GitHub Pages deployment record (repaired in T44-B from `S43` HUD FMR to project records `S68`, `S69`) | S68, S69 |
| F20 | Platform branch constraint (repaired in T44-B from `S20` SF Rent Ordinance to project record `S68`) | S68 |
| F31 | Merge-conflict markers were committed to `COORDINATION.md` (repaired in T44-B from `S20` to `S68`) | S68 |
| F32 | Flag cross-references in `SOURCES.md` were out of sequence | S02, S03 |
| F33 | Rent Board Fee and Rent Increase License are separate obligations | S56, S07, S53 |
| F34 | Two-unit owner-occupied AB 1482 exemption is conditional and unverified here | S58, S60, S59 |
| F35 | In-law or second structure on the lot changes coverage | S60, S59, S06 |
| F36 | QA correction: in-law-unit exemption wording (legal vs. illegal in-law unit) | S60 |
| F37 | QA correction: project-management rows cited HUD FMR (`S43`) instead of project records (`S68`, `S69`) | S68, S69 |
| F38 | Referral timing for an unpaid Rent Board Fee differs inside the SF.gov fee page | S56, S63 |
| F39 | Older SF.gov "Pay your Rent Board fee" service page still shows 2023 dates | S70, S56 |
| F40 | Form 573 fee history title/row lag and two historical rows (`7/03-6/04` and `7/01-6/02`) not showing a 50% tenant share | S64, S56 |
| F41 | No official statement links Rent Board Fee payment to licence validity | S56, S63, S53, S65 |
| F42 | How a 50% fee recovery is divided among co-tenants is not stated officially | S62, S63 |
| F43 | Case-specific fee, exemption, and business-registration facts are unverified | S56, S64, S66 |
| F44 | Privacy: raw tenant identifiers remain in public git history and pull-request diffs (owner-only remediation) | S68 |
| F45 | SF.gov Current Rates page (`S02`) link labeled `575 Cap. Imp. Labor Rates` points to `574_Cap._Imp._Imputed_Interest_26-27_7.26.pdf` (Form 574 Imputed Interest instead of Form 575) | S02 |
| F46 | Proposed File 261020 (10% combined banked + capital-improvement cap) is not enacted; status must be re-checked | S71, S72, S87 |
| F47 | Proposed-cap notice, Legistar record and draft text do not fully align on retroactivity or on how the 10% interacts with the annual allowable increase | S71, S72, S87 |
| F48 | Earlier overbroad retaliation wording corrected against Civil Code 1942.5 | S57 |
| F49 | Owner-intake rows are not official verification; official cells stay blank | S06, S01, S07 |
| F50 | Independent audit integration status: most items now integrated; historical privacy exposure and non-enactment remain open | S71, S83, S85, S87 |
| F51 | Recoverable short-identifier hashes were removed from the validator but remain in public history | S68 |
| F52 | The 94122 SAFMR is a voucher benchmark, not a market rent, cap or comparison for these units | S83, S84, S43 |
