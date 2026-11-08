"""Standalone markdown deliverables and stylesheet for the static site."""

from site_flags import FLAGS
from site_sources import SOURCES

EXECUTIVE_SUMMARY_TEXT = """# Executive Summary - Rental increase SF

Date: 2026-11-08 UTC (Rent Board license, Housing Inventory, banked-increase and Rent Board Fee pages re-fetched and re-verified 2026-11-08). Informational compliance research, not legal advice.

## FOREFRONT: Rent Board & Rent Increase License — yes, an individual owner must comply

**Question:** "I am just an individual property owner and not part of a corporation — do I still need to apply for the license and inform the Rent Board before notifying tenants of a rent increase?"

**Answer: Yes.** SF.gov states: "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases on a tenant." No individual-owner exception is stated. The requirement has applied since July 1, 2022 — and since **March 1, 2023 for condominiums and buildings with 1-9 residential units** — so a small individual-owned building in San Francisco is covered now. "Informing the Rent Board" and "getting the license" are the same process: you report into the **Rent Board Housing Inventory**, and the license is generated from that report.

**Step by step (do these in order, before any tenant notice takes effect):**

1. **Confirm the unit is covered** by the SF Rent Ordinance (check the property in the SF Planning Property Information Map; many units built on/before June 13, 1979 are covered — the owner-supplied "built in 1940" fact is unverified, see Flagged for Review).
2. **Report into the Rent Board Housing Inventory** via the Rent Board Portal (https://portal.sfrb.org/). SF.gov: "All owners of residential property are required to report." Reporting is free, online 24/7, due **March 1 every year**, and is submitted under penalty of perjury. The information entered is public.
3. **Receive the Rent Increase License.** Owners who report a unit as tenant-occupied receive a rent increase license; it is **automatically generated for non-owner-occupied units**. The license does **not** need to be included with your notice to tenants.
4. **Check the license is current and on file before the increase's effective date.** SF.gov: "A landlord must have a current rent increase license on file with the Rent Board before any annual or banked rent increase can go into effect," and a rent increase notice "will not be enforceable without having a rent increase license on the effective date of the notice." Tenants can search the Portal to check whether you are up to date; if you miss the deadline, the Rent Board may notify your tenants that you are not in compliance. (Exact consequence wording differs between SF.gov pages — see flag F25.)
5. **Late?** You can still report and receive a license after March 1; the Rent Board assesses **no monetary penalty** for late filing — but that does not make a notice enforceable for an effective date on which no license was on file.
6. **Only then notify tenants**, in writing: 30 days (90 days if the increase, alone or combined with another increase in the same year, exceeds 10%; +5 days if mailed), stating the dollar amount, percentage, and effective date, using the rate in effect on the increase date. Complying with the license rule does not replace any other local or state rent-increase law.

Official links for manual review: SF.gov "Learn about rent increases in San Francisco" (https://www.sf.gov/learn-about-rent-increases-san-francisco) and SF.gov "The Rent Board Housing Inventory" (https://www.sf.gov/rent-board-housing-inventory).

**What the Rent Ordinance itself says:**

- **Sec. 37.3(a)(1):** "A landlord who has reported the required information about their rental unit to the Rent Board as set forth in Section 37.15 shall have a license to impose annually a rent increase which does not exceed a tenant's base rent by more than 60% of said published increase. In no event, however, shall the allowable annual increase be greater than 7%." - https://www.sf.gov/information--sec-373-rent-limitations
- **Sec. 37.15(e):** a substantially compliant owner "shall receive a license to impose rent increases"; if not, "the license to impose rent increases shall be temporarily suspended ... but a tenant shall not be obligated to pay the increased rent for months during the period of suspension." Added by Ord. 265-20. - https://www.sf.gov/information--sec-3715-reporting-obligations-licensing
- **Form 571 (Rent Board):** the annual increase may be imposed "without filing a petition at the Rent Board." - https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf

**Scope limits:** SF.gov states the license rules apply ONLY to rent-controlled units, and that the license is not required for Section 6.14/Costa-Hawkins increases or for passthroughs allowed under the Rent Ordinance (https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory, https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins). The Housing Inventory information you submit is **public**, including the owner's name and business contact information.

**Full step-by-step tables:** the site's Step-by-Step License page (`pages/process.html`) carries 12 numbered steps with an official link on every step, the ordinance text, and the case application for both units. For this case, Housing Inventory reporting and a current license for either unit are **unconfirmed** (blank, flagged T03-F05) — no increase should be treated as effective until that is confirmed.


## Separate obligation: the annual Rent Board Fee (this is not the license)

Paying the Rent Board Fee does **not** replace the Housing Inventory report, and reporting into the Housing Inventory does **not** satisfy a fee-exemption request. Every owner of a residential unit owes a per-unit fee unless a current exemption is on file.

- **Amount for the 2026-2027 tax year:** **$59.00 per dwelling unit** ($29.50 per guest/SRO room) - https://www.sf.gov/rent-board-fee
- **Deadline:** **March 1 each year** (next: March 1, 2027), with a 5% penalty each month after March 1, capped at 15%; unpaid fees are referred to the Bureau of Delinquent Revenue after June 1. Ordinance text (Sec. 37A.1, 37A.4, 37A.6): https://www.sf.gov/sites/default/files/2022-09/901%20Rent%20Board%20Fee%20Ch.%2037A.pdf
- **Exemption window for the 2027 fee:** request by **December 14, 2026**; an exemption request is required every year, and only an owner-occupied unit that is not rented at any time qualifies (with an Assessor Homeowners' Exemption or a Rent Board affidavit). - https://www.sf.gov/notice-of-rent-board-fee-and-housing-inventory-requirement
- **Recovering 50% from the tenant:** after paying in full, up to **$29.50 per dwelling unit** for the 2026-27 fee, only from tenants in occupancy on November 1, never penalties; by deducting it from the security-deposit interest payment (4.2% for 3/1/26-2/28/27) or, only where SF.gov allows it, by a bill stating the amount, the purpose and a 30-day due date. - https://www.sf.gov/information--recover-part-your-rent-board-fee-tenant
- **City business registration:** an individual whose only San Francisco business is rental income from one residential structure consisting of fewer than four units is not, by reason of that fact alone, required to register. - https://sftreasurer.org/information-lessors-residential-real-estate

**No official page states that fee payment affects whether a rent increase is valid.** The license under Sec. 37.15(e) turns on substantially complying with the reporting obligation. That absence is published as flag F32; pay the fee on time regardless, because it has its own penalties and collection route. Conditional arithmetic for the two units (2 x $59.00 = $118.00; maximum recovery $59.00) is on the Rent Board Fee page and flagged F33 - the January 2027 Annual Notice, which is the actual bill, does not exist yet.

## Bottom line

For a unit covered by the San Francisco Rent Ordinance, the current ordinary annual allowable increase is **1.6% effective 3/1/26-2/28/27**, once every 12 months on the tenant's anniversary date. A current Rent Increase License must be on file before the increase takes effect; the increase is calculated on base rent only, is not rounded up, and requires written notice. California's state-only AB 1482 cap is **8.8% for San Francisco 8/1/26-7/31/27**, but SF.gov says it does **not** apply to units already under the SF Rent Ordinance's rent-increase limits. No official general federal private-rent cap was found; HUD FMR/SAFMR figures are voucher payment standards, not rent caps.

## Case handling

The owner-supplied case facts are anonymized. Dates and dollar amounts are preserved: Unit 1 last lease start February 1, 2025 at $3,995; Unit 1 continuing tenancy/current tenants April 1, 2026 at $3,995; Unit 2 last lease start June 1, 2019 at $3,150. Tenant identifiers are replaced with placeholders Tenant A-F. No exact street address, real name, initial, or contact detail is published. The case facts themselves are now published in full on the site as clearly labelled **owner-supplied (anonymized)** rows - ZIP 94122, 1940, two units, lease dates and rents, Tenant A-F - because you asked for the entries to be readable; they are explicitly not official findings. The separate official-verification rows stay blank and flagged: exact-address coverage, the official building-year record, license status, prior increases and notice history, whether the April 1, 2026 continuation restarted the anniversary date, and the legal status of the continuing occupants were not official-verified.

Arithmetic using owner-supplied amounts and official rates only: Unit 1 $3,995 x 1.6% = $63.92 -> $4,058.92; Unit 2 $3,150 x 1.6% = $50.40 -> $3,200.40. These are illustrative only, not a recommendation or eligibility determination. No banked increase is inferred.

Unit 1's roommate change does not by itself permit extra rent. SF.gov prohibits charging more rent merely because a new/additional roommate moved in. Section 6.14 / Costa-Hawkins market-rate reset rules require specific facts about the last original occupant and the continuing occupant's legal status; those facts are unverified. SF.gov and the Rent Board strongly encourage legal advice, and Jan. 13, 2026 minutes denied an appeal because the landlord did not prove the last original occupant no longer permanently resides. No market-rate reset is recommended.

## Notice checklist

Verify coverage in SF Planning PIM; obtain a current Rent Increase License after Housing Inventory reporting; verify 12-month/anniversary eligibility; use the rate in effect on the increase date; give written 30-day notice (90-day if >10% alone/combined in same year, +5 days if mailed) with dollar amount, percentage, effective date and banked portion if any; follow Civil Code 827 delivery rules; file any required petition/worksheet before notice; keep identical neutral records for each eligible unit.

## Discrimination and one-vs-both

The federal FHA, 24 CFR 100.500 disparate-impact rule, California FEHA and SF tenant-harassment rules apply. Intent is not required for a discriminatory-effect claim; a substantial legitimate nondiscriminatory interest and no less discriminatory alternative matter. No official source requires raising both units, but an identical written neutral policy applied to each eligible unit is the conservative approach. If only one unit is raised, document neutral eligibility/anniversary reasons, not tenant identity. Nothing here claims attorney approval or guarantees that no complaint, inquiry or lawsuit will occur.

## Corporate / individual evidence

SEC filings show IRT Q4 2025 same-store new -3.7%, renewal 2.9%, blended 0.8% and Invitation Homes 2025 total-portfolio renewal +4.6%, new -0.8%. These are portfolio-level, not SF-specific and not legal benchmarks. SF Rent Board June 2024 workload stats show 23 landlord petitions/154 units (18 capital-improvement petitions covering 148 units) and 73 tenant petitions/73 units; this is narrow formal-petition evidence only. An earlier draft listed 19 capital-improvement petitions / 148 units - the unit count belonged to the capital-improvement line while the 19 was the subtotal including one Costa-Hawkins petition; corrected and flagged as F29. No official source proves what all large corporations or all individual SF owners do.

## Banked increases and the 10% notice threshold

A skipped increase is only banked if at least 24 full months pass without any rent increase; banked percentages are added, never compounded or prorated, and never carry over to a new tenant. Two-or-more-year increases are imposed by adding the allowable percentages and need no Rent Board petition. If a correctly banked total plus the current annual rate exceeds 10%, the notice must be 90 days rather than 30 days. No banked amount is asserted for either unit here, because neither rent history was supplied - both are blank and flagged. **Conditional arithmetic only (not a finding, not a recommendation):** if literally no increase had been imposed on Unit 2 since June 1, 2019, the official rates for the skipped years (1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = 11.5%) plus the current 1.6% would total 13.1%, i.e. $412.65 on $3,150, or $3,562.65; a combined increase above 10% requires 90 days' written notice. Because the increase history is unconfirmed, this figure is flagged (F30) and is not relied on anywhere. (https://www.sf.gov/information--banked-rent-increases, https://www.sf.gov/information--annual-rent-increase-multiple-years)

## Unit 1, Section 6.14 and privacy

Extra rent for an additional occupant is unlawful, and adding an occupant is not a market-rate reset. A Section 6.14 or Costa-Hawkins unlimited increase requires the last original occupant to have vacated plus a timely written 6.14 notice (served within a reasonable time, generally 60 days, after the landlord knew or should have known of the occupancy); co-tenants are not subject to a Costa-Hawkins increase at all. Whether a 6.14 notice was served on the April 2026 occupant, and whether that occupant is a co-tenant or a subtenant, was not supplied - blank and flagged (F28). Separately: replacing tenant identifiers with Tenant A-F, keeping dates and amounts, withholding any street address, and keeping the raw-identifier intake out of git is this project's privacy rule; the Rent Board's own inventory filing is public by design. (https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.53.&lawCode=CIV, https://www.sf.gov/rent-board-housing-inventory)

## Flagged for Review

All __FLAGCOUNT__ irregularities and unverified items are published on the clearly labeled Flagged for Review page with official source links. They include SF.gov example inconsistencies, Form 571 title metadata, SF 37.10B footnote conflict, temporary CPI methodology, stale snippets, 404 URL variants, unparsed 94122 SAFMR data, unverified case facts, the absence of any official federal cap / attorney approval / both-units rule, the differing SF.gov wording on the consequence of an unlicensed increase (F25), a privacy defect found 2026-11-07 in the earlier validation report and now fixed (F26), the next year's allowable rate not yet being published (F27), Unit 1's unknown Section 6.14 notice history (F28), a corrected capital-improvement petition count (F29), the conditional (not asserted) banked-increase illustration (F30), the fee-page collection-timing difference (F31), the absence of any official statement linking fee payment to a rent increase's validity (F32), unverified fee billing details for this case (F33), Form 573 period metadata (F34), a stale 2023 date on an older fee service page (F35), the residual presence of raw identifier tokens in public git history (F36), published merge-conflict markers that were repaired (F37), and the use of repository artifacts rather than official sources for rows about this project's own deliverables (F38). Flagged items do not block the site or merge.

## Sources

__SRCCOUNT__ official sources are catalogued in SOURCES.md and on the Sources page. Every published table row links to at least one official source. Unverified values are blank and flagged. No value is inferred or filled from a nonofficial snippet.
"""

FLAGGED_TEXT = """# Flagged for Review

This page is clearly labeled **Flagged for Review**. Status `needs review` means the item is published for manual review with source links or a repository record and does **not** block any task or the merge.

Full detail is in `research/sources/irregularities.md`, `research/sources/unverified.md`, `research/flags.md`, `research/rent_board_fee/README.md`, `research/privacy/HISTORY_EXPOSURE.md` and `pages/flagged.html`.

## Summary of flags

All **__FLAGCOUNT__** flagged items are published on `pages/flagged.html`, each with official source links or an explicit repository artifact.

**Source-quality and legal-interpretation flags F01-F24:** SF.gov example inconsistencies (rates in worked examples versus Form 571), Form 571 PDF title metadata, the SF 37.10B Larson footnote, the temporary CPI methodology adopted in the January 2026 Commission minutes, stale search snippets, a chunk-split artifact, 404 URL variants, GovInfo substitution for a failed U.S. Code page, the HUD Fair Housing Act redirect, FY2026/FY2027 HUD effective dates, unparsed 94122 SAFMR data, the SEC Equity Residential dead end, a duplicated block on the tenant-petition page, the Rent Ordinance not being the official record, the Tenant Right to Counsel report 404, the GitHub Pages root source, and the platform branch constraint.

**Case, privacy and process flags F25-F38:** F25 differing SF.gov wording on the consequence of an unlicensed increase; F26 the earlier validation report that published raw identifier tokens (fixed); F27 next year's allowable rate not yet published; F28 Unit 1's unknown Section 6.14 notice history; F29 a corrected capital-improvement petition count (18 petitions / 148 units, not 19 / 148); F30 the 13.1% banked figure for Unit 2 being conditional arithmetic rather than a finding; F31 the fee page's collection-referral timing differing inside one page (June 1 versus a July notice plus 30 days); F32 the absence of any official statement linking Rent Board Fee payment to the validity of a rent increase; F33 this case's fee billing, exemption and unit-count facts being unverified; F34 Form 573 covering 7/1999-6/2026 only; F35 a stale 2023 date on the older fee service page; F36 raw identifier tokens still reachable in public git history and PR diffs; F37 unresolved merge-conflict markers that were published and have been repaired; F38 rows about this project's own deliverables citing repository artifacts instead of official sources.

**Case and analysis flags T03-F01 to T03-F10:** owner-supplied facts, anonymization, the unverified address/year/coverage, Unit 1's unknown legal status, unknown banked/license/notice history, illustrative arithmetic, the blank 94122 SAFMR row, the absence of any cap/attorney-approval/both-units rule, narrow corporate and individual evidence, and the conservative-checklist framing.

**What the owner must still do:** confirm the property's coverage and official records; confirm Housing Inventory reporting and Rent Increase License status for both units; confirm any prior increases and notice history; and confirm the fee billing record when the January 2027 Annual Notice arrives. None of these can be established from the sources read here.

Unverified value cells are blank. Nothing on this site is legal advice, and no attorney has approved any increase.
"""

README_TEXT = """# RentincreaseSF4

Public GitHub Pages research site for "Rental increase SF": executive summary, official-source-linked tables, anonymized case dashboard, analysis, and a clearly labeled Flagged for Review page.

Live site: https://kanlerxz87-cyber.github.io/RentincreaseSF4/

- `index.html` - clean landing page / dashboard.
- `pages/` - category subpages with easy-read tables, including `pages/fee.html` (Rent Board Fee) and `pages/process.html` (step-by-step license).
- `data/` - JSON source of truth; every legal/fee finding row has official source IDs, and rows about this project's own deliverables link a repository artifact and are labelled `project record`.
- `SOURCES.md` / `VERIFICATION.md` / `research/` - official source ledger and line-by-line verification.
- `EXECUTIVE_SUMMARY.md` - standalone executive summary.
- `FLAGGED_FOR_REVIEW.md` / `pages/flagged.html` - flagged irregularities with links.
- `REPO_REVIEW.md` - line-by-line repository review.
- `COORDINATION.md` - shared task board, PR and merge record.
- `scripts/build_site.py` / `scripts/validate_site.py` - static site build and validation.

Privacy: personal information is anonymized with placeholders; raw identifiers are internal-only and excluded from git and the published site. Dates and dollar amounts are preserved. No exact address is published.

Not legal advice. No attorney approval or guarantee of no complaint/lawsuit is claimed. Any increase is framed as a conservative compliance checklist capable of tenant-lawyer review.
"""

CSS_TEXT = r"""
:root{--ink:#14213d;--muted:#5b6b84;--bg:#f5f7fb;--card:#fff;--line:#dce3ef;--accent:#0b6e4f;--accent2:#1f4e79;--warn:#9a6700;--warnbg:#fff8e1;--okbg:#eaf6ef;--flagbg:#fff1f1;--flag:#a12424;--owner:#5b4b8a;--ownerbg:#f1eefc}
*{box-sizing:border-box}
body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55}
a{color:var(--accent2);text-decoration:none}
a:hover{text-decoration:underline}
header{background:linear-gradient(135deg,#0b2545,#134e4a);color:#fff;padding:2.2rem 1rem}
header .wrap{max-width:1120px;margin:0 auto}
header h1{margin:0 0 .35rem;font-size:2rem;letter-spacing:-.02em}
header p{margin:.2rem 0;color:#dbeafe}
nav{background:#0b2545;position:sticky;top:0;z-index:10;border-bottom:1px solid rgba(255,255,255,.15)}
nav .wrap{max-width:1120px;margin:0 auto;display:flex;flex-wrap:wrap;gap:.15rem;padding:.45rem 1rem}
nav a{color:#e8eef8;font-size:.86rem;padding:.35rem .55rem;border-radius:6px}
nav a:hover,nav a.active{background:rgba(255,255,255,.14);text-decoration:none}
main{max-width:1120px;margin:0 auto;padding:1.5rem 1rem 3rem}
.hero{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1.4rem;margin-bottom:1.4rem;box-shadow:0 2px 10px rgba(15,35,70,.05)}
.hero h2{margin-top:0;font-size:1.5rem}
.disclaimer{background:var(--warnbg);border-left:4px solid var(--warn);padding:.8rem 1rem;border-radius:6px;font-size:.92rem;margin:1rem 0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;margin:1.2rem 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1rem;box-shadow:0 2px 10px rgba(15,35,70,.04)}
.card .k{font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.card .v{font-size:1.7rem;font-weight:700;margin:.2rem 0;color:var(--accent2)}
.card .d{font-size:.88rem;color:var(--muted)}
.card a{font-weight:600}
section{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1rem;margin:1.2rem 0;overflow:hidden}
section>h2{margin:0 0 .8rem;font-size:1.2rem}
.tablewrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:.9rem}
th,td{text-align:left;vertical-align:top;padding:.65rem .6rem;border-bottom:1px solid var(--line)}
th{background:#eef3fa;color:#253b5b;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;position:sticky;top:0}
tr:last-child td{border-bottom:0}
td.blank{color:var(--muted);font-style:italic}
.badge{display:inline-block;padding:.15rem .45rem;border-radius:999px;font-size:.72rem;font-weight:700;white-space:nowrap}
.badge.verified{background:var(--okbg);color:var(--accent)}
.badge.review{background:var(--warnbg);color:var(--warn)}
.badge.analysis{background:#e8eefc;color:var(--accent2)}
.badge.owner{background:var(--ownerbg);color:var(--owner)}
.badge.project{background:#eef7fb;color:#155e75}
.artifact{font-size:.78rem;color:#155e75}
.owner-src{font-size:.78rem;color:var(--owner)}
td.blank{color:var(--warn);font-style:italic}
@media print{nav,.cta{display:none}section,.hero{box-shadow:none}}
.src a{display:inline-block;margin:0 .25rem .2rem 0;font-size:.78rem;background:#eef3fa;border:1px solid #d3ddef;padding:.1rem .35rem;border-radius:5px}
.flaglink{font-weight:700;color:var(--flag)}
.flagged-banner{background:var(--flagbg);border:1px solid #f0c2c2;border-left:5px solid var(--flag);padding:1rem;border-radius:10px;margin:1rem 0}
.flagitem{border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem;margin:.7rem 0;background:#fff}
.flagitem h3{margin:0 0 .25rem;font-size:1rem}
.flagitem .id{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--flag);font-weight:700}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;padding:1.2rem;text-align:center}
footer .wrap{max-width:1120px;margin:0 auto}
.small{font-size:.82rem;color:var(--muted)}
ul{margin:.4rem 0 .4rem 1.2rem}
@media(max-width:700px){header h1{font-size:1.55rem}nav .wrap{padding:.35rem .5rem}main{padding:1rem .6rem 2rem}th,td{padding:.5rem .45rem}}
"""

# Counts are generated from the registries so they cannot go stale (QA finding fixed 2026-11-08).
_COUNT_SUBS = {"__FLAGCOUNT__": str(len(FLAGS)), "__SRCCOUNT__": str(len(SOURCES))}
for _name in ("EXECUTIVE_SUMMARY_TEXT", "FLAGGED_TEXT", "README_TEXT"):
    _text = globals()[_name]
    for _key, _value in _COUNT_SUBS.items():
        _text = _text.replace(_key, _value)
    globals()[_name] = _text
