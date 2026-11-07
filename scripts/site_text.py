"""Standalone markdown deliverables and stylesheet for the static site."""

EXECUTIVE_SUMMARY_TEXT = """# Executive Summary - Rental increase SF

Date: 2026-11-07 UTC. Informational compliance research, not legal advice. SF Rent Board license/Housing Inventory guidance was rechecked on 2026-11-07.

## First: the Rent Board process for an individual owner

**Yes—an individual owner is included.** SF.gov says all residential property owners must report their property through the Rent Board Housing Inventory; owners reporting a tenant-occupied unit receive a Rent Increase License after submission. The official instructions require a current license **by the effective date** of an annual or banked increase. They also say the license **does not need to accompany the tenant notice**. So the ordinary sequence is: (1) report the property through the Housing Inventory, (2) ensure a current license is on file for the effective date, and (3) give the tenant legally compliant written notice. On the official pages reviewed, a separate filing of each routine annual increase with the Board before tenant notice is not listed. This is different from petition/worksheet increases, for which Rent Board procedures can require filing before notice. A license is not a Rent Board approval of the proposed amount and cannot prevent a tenant from challenging it.

Official links: [Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) and [Learn about rent increases in San Francisco](https://www.sf.gov/learn-about-rent-increases-san-francisco). Housing Inventory submissions contain some public information, including owner/business contact details; review the official form and privacy implications before submitting. Do not publish personal owner or tenant data on this site.

## Bottom line

For a unit covered by the San Francisco Rent Ordinance, the current ordinary annual allowable increase is **1.6% effective 3/1/26-2/28/27**, once every 12 months on the tenant's anniversary date. The increase is calculated on base rent only, is not rounded up, and requires written notice. California's state-only AB 1482 cap is **8.8% for San Francisco 8/1/26-7/31/27**, but SF.gov says it does **not** apply to units already under the SF Rent Ordinance's rent-increase limits. No official general federal private-rent cap was found; HUD FMR/SAFMR figures are voucher payment standards, not rent caps.

## Case handling

The owner-supplied case facts are anonymized. Dates and dollar amounts are preserved: Unit 1 last lease start February 1, 2025 at $3,995; Unit 1 continuing tenancy/current tenants April 1, 2026 at $3,995; Unit 2 last lease start June 1, 2019 at $3,150. Tenant identifiers are replaced with placeholders Tenant A-F. No exact street address, real name, initial, or contact detail is published. All case-specific official-source cells are blank and flagged because address, building year, rent-control coverage, license, prior increases, notice history and tenant legal status were not official-verified.

Arithmetic using owner-supplied amounts and official rates only: Unit 1 $3,995 x 1.6% = $63.92 -> $4,058.92; Unit 2 $3,150 x 1.6% = $50.40 -> $3,200.40. These are illustrative only, not a recommendation or eligibility determination. No banked increase is inferred.

Unit 1's roommate change does not by itself permit extra rent. SF.gov prohibits charging more rent merely because a new/additional roommate moved in. Section 6.14 / Costa-Hawkins market-rate reset rules require specific facts about the last original occupant and the continuing occupant's legal status; those facts are unverified. SF.gov and the Rent Board strongly encourage legal advice, and Jan. 13, 2026 minutes denied an appeal because the landlord did not prove the last original occupant no longer permanently resides. No market-rate reset is recommended.

## Notice checklist

Verify coverage in SF Planning PIM; obtain a current Rent Increase License after Housing Inventory reporting; verify 12-month/anniversary eligibility; use the rate in effect on the increase date; give written 30-day notice (90-day if >10% alone/combined in same year, +5 days if mailed) with dollar amount, percentage, effective date and banked portion if any; follow Civil Code 827 delivery rules; file any required petition/worksheet before notice; keep identical neutral records for each eligible unit.

## Discrimination and one-vs-both

The federal FHA, 24 CFR 100.500 disparate-impact rule, California FEHA and SF tenant-harassment rules apply. Intent is not required for a discriminatory-effect claim; a substantial legitimate nondiscriminatory interest and no less discriminatory alternative matter. No official source requires raising both units, but an identical written neutral policy applied to each eligible unit is the conservative approach. If only one unit is raised, document neutral eligibility/anniversary reasons, not tenant identity. Nothing here claims attorney approval or guarantees that no complaint, inquiry or lawsuit will occur.

## Corporate / individual evidence

SEC filings show IRT Q4 2025 same-store new -3.7%, renewal 2.9%, blended 0.8% and Invitation Homes 2025 total-portfolio renewal +4.6%, new -0.8%. These are portfolio-level, not SF-specific and not legal benchmarks. SF Rent Board June 2024 workload stats show 23 landlord petitions/154 units and 73 tenant petitions/73 units; this is narrow formal-petition evidence only. No official source proves what all large corporations or all individual SF owners do.

## Flagged for Review

All 34 irregularities and unverified items are published on the clearly labeled Flagged for Review page with official source links. They include SF.gov example inconsistencies, Form 571 title metadata, SF 37.10B footnote conflict, temporary CPI methodology, stale snippets, 404 URL variants, unparsed 94122 SAFMR data, unverified case facts, and the absence of any official federal cap / attorney approval / both-units rule. Flagged items do not block the site or merge.

## Sources

52 official sources are catalogued in SOURCES.md and on the Sources page. Every published table row links to at least one official source. Unverified values are blank and flagged. No value is inferred or filled from a nonofficial snippet.
"""

FLAGGED_TEXT = """# Flagged for Review

This page is clearly labeled **Flagged for Review**. Status `needs review` means the item is published with official source links for manual review and does **not** block any task or the merge.

Full detail is in `research/sources/irregularities.md`, `research/sources/unverified.md`, `research/flags.md` and `pages/flagged.html`.

## Summary of flags

- 24 source-quality flags F01-F24: SF.gov example inconsistencies, Form 571 title metadata, SF 37.10B Larson footnote, temporary CPI methodology, stale snippets, chunk split, 404 URL variants, GovInfo substitution, HUD FHA redirect, FY2027/FY2026 effective dates, unparsed 94122 SAFMR data, SEC EQR dead end, duplicate page block, Rent Ordinance not-official-record note, TRC report 404, Pages root source, platform branch constraint, unverified case facts, missing federal/attorney/both-units sources, narrow corporate/individual evidence, and old 1.7% example.
- 10 case/analysis flags T03-F01-F10: owner-supplied facts, anonymization, address/year/coverage, Unit 1 legal status, banked/license/notice history, illustrative arithmetic, 94122 SAFMR blank, no cap/approval/both-units guarantee, narrow corporate/individual evidence, and conservative checklist only.

Every flag on the site includes official source links. Unverified value cells are blank.
"""

README_TEXT = """# RentincreaseSF4

Public GitHub Pages research site for "Rental increase SF": executive summary, official-source-linked tables, anonymized case dashboard, analysis, and a clearly labeled Flagged for Review page.

Live site: https://kanlerxz87-cyber.github.io/RentincreaseSF4/

- `index.html` - clean landing page / dashboard.
- `pages/` - category subpages with easy-read tables.
- `data/` - JSON source of truth; every row has official source IDs.
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
:root{--ink:#14213d;--muted:#5b6b84;--bg:#f5f7fb;--card:#fff;--line:#dce3ef;--accent:#0b6e4f;--accent2:#1f4e79;--warn:#9a6700;--warnbg:#fff8e1;--okbg:#eaf6ef;--flagbg:#fff1f1;--flag:#a12424}
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
