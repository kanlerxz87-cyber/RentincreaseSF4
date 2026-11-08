"""Standalone markdown deliverables, stylesheet and progressive-enhancement script."""

from site_sources import SOURCES
from site_flags import FLAGS

SOURCE_COUNT = len({s["url"] for s in SOURCES.values()})
SOURCE_ENTRY_COUNT = len(SOURCES)
FLAG_COUNT = len(FLAGS)

EXECUTIVE_SUMMARY_TEXT = f"""# Executive Summary - Rental increase SF

Research ledger dated 2026-11-08 UTC. Informational compliance research, not legal advice. No attorney has approved a proposed increase; this is a conservative compliance checklist capable of tenant-lawyer review, not a guarantee against a petition, complaint or lawsuit.

## FOREFRONT: the individual-owner Rent Board answer

**Yes — an individual owner of a covered rent-controlled unit must use the Rent Board Housing Inventory/licensing process before an annual or banked increase takes effect.** There is no individual-owner or small-building exemption on the official pages reviewed. The official condition is a current license **before the increase's effective date**; the pages do not expressly require a separate Board filing before mailing an ordinary annual/banked notice. The safest order is: report, verify the license, check the tenancy, then serve a compliant notice.

1. **Confirm coverage privately.** Use the SF Planning Property Information Map and the Rent Board Portal with the exact address/APN. The public site intentionally omits the address. The supplied 1940 year and two-unit description point toward coverage but are not an official determination. In-law unit/ADU and separate-parcel facts can change state and local coverage; verify them before relying on any exemption.
2. **Report each residential unit into the Housing Inventory.** Use https://portal.sfrb.org/. Reporting is free, due annually by March 1, and submitted under penalty of perjury. Inventory information is public, including owner/business contact information.
3. **Verify the Rent Increase License.** For non-owner-occupied units the license is generated from the inventory report. Check that it is current for the unit and the intended effective date. Keep a dated portal record.
4. **Check the tenancy before calculating.** Confirm fixed-term versus periodic status, any express mid-term increase clause, anniversary date, prior increases, base rent, occupant status and retaliation/discrimination risk. Do not infer a market reset from a roommate change.
5. **Calculate only what is supported.** The current ordinary annual rate is 1.6% for increases effective March 1, 2026 through February 28, 2027. Multiply base rent by the rate; do not round up. No banked total is asserted here because history and banking eligibility are unverified and SF.gov's banking text/examples conflict.
6. **Serve and document the notice.** For a periodic tenancy, give at least 30 days' written notice, or 90 days if the increase alone or combined with another increase in the prior 12 months exceeds 10%; mailing within California adds 5 days. State the dollar amount, percentage, effective date and any banked portion. Use personal delivery or mail as Civil Code 827/CCP 1013 require, and keep proof.

Official links: https://www.sf.gov/learn-about-rent-increases-san-francisco ; https://www.sf.gov/rent-board-housing-inventory ; https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory ; https://www.sf.gov/information--sec-3715-reporting-obligations-licensing ; https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827&lawCode=CIV .

**Ordinance basis.** Sec. 37.3(a)(1) ties the annual increase license to reporting under Sec. 37.15; Sec. 37.15(e) suspends the license during noncompliance and says the tenant is not obligated to pay the increased rent during suspension. Form 571 says the ordinary annual increase may be imposed without a Rent Board petition. SF.gov's Rent Board text is a convenience version; American Legal is the official code publisher.

**Do not confuse the license with the Rent Board Fee.** The fee is separate: $59.00 per dwelling unit for the 2026-2027 tax year, due March 1, 2027, with narrow exemptions and a December 14, 2026 exemption-request deadline for that cycle. A fee exemption does not satisfy Housing Inventory reporting. If the owner pays the fee in full, up to 50% ($29.50 per dwelling unit) may be recovered from qualifying November 1 occupants by the statutory deposit-interest/billing method; penalties are not recoverable. This is not base rent. For two supplied units the illustrative fee is $118.00 and the illustrative maximum recovery is $59.00 total, not a confirmed bill.

## Bottom line for the two anonymized units

- **Unit 1:** supplied rent $3,995. $3,995 x 1.6% = $63.92, giving $4,058.92 as an illustration only.
- **Unit 2:** supplied last-lease rent $3,150. $3,150 x 1.6% = $50.40, giving $3,200.40 as an illustration only.

These are **not approved amounts or effective dates**. Coverage, license status, current base rent, lease type, anniversary, prior notices, occupant status and retaliation history are unverified. No proposed effective date was supplied, so notice-deadline cells are blank rather than invented. California's state-only AB 1482 cap is 8.8% for San Francisco for August 1, 2026 through July 31, 2027, but it does not replace the stricter SF rent-control cap for covered units. No general federal private-rent cap was found; HUD FMR/SAFMR figures are voucher standards, not a lawful increase benchmark.

## Privacy warning — current anonymization is not history remediation

The current public tree uses Tenant A-F placeholders, preserves the supplied dates/amounts, and omits the exact address. **Earlier public Git history and PR diffs exposed raw identifier tokens. That exposure is not remediated by cleaning the current tree.** Clones, forks, cached views and low-entropy fingerprints may persist. The site does not claim confidentiality has been restored. Owner options and limits are documented in research/privacy/HISTORY_EXPOSURE.md and GitHub's sensitive-data guidance: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository .

## Roommates, banking and fixed-term leases

Extra rent merely because a roommate was added is unlawful, even if the lease says otherwise. A Section 6.14 increase requires the last original occupant to have vacated and a timely written 6.14 notice to subsequent occupants; generally 60 days is considered reasonable. Costa-Hawkins has different lawful-subtenant/assignee conditions and does not apply to co-tenants. The April 1, 2026 continuing-tenancy facts do not establish either route. No market-rate reset is recommended.

Banking is not computed. SF.gov says a skipped increase is banked only after 24 full months without any increase, but its examples describe 12 months since a skipped opportunity. Percentages are added, not compounded or prorated, and do not carry to a new tenant. Verify the actual history and obtain counselor/legal review before relying on any banked amount. An earlier conditional Unit 2 banked illustration was withdrawn.

The California DRE guide says rent generally cannot be raised during a fixed term unless the agreement expressly allows it. The supplied lease dates do not establish lease type or a mid-term clause, so that issue is flagged.

## Discrimination, retaliation and one versus both units

No official rule requiring both units to be raised was found. Use neutral, unit-based eligibility criteria and document anniversary/history reasons if only one unit is raised. Raising both units does not immunize discrimination or retaliation. Federal Fair Housing Act rules, California FEHA, SF tenant-harassment rules and Civil Code 1942.5 all matter. The eCFR discriminatory-effect regulation remains in the source ledger even though the current HUD overview describes a different enforcement emphasis; do not assume agency policy overrides the regulation.

Civil Code 1942.5 has conditional 180-day retaliation provisions and broader protection for tenant organizing/lawful rights. It is not an automatic bar for every repair request: statutory triggers, tenant default, causation, good-faith stated cause and the once-per-12-month limit require fact review. No repair/complaint history was supplied here.

## Corporate and individual evidence

SEC filings show IRT Q4 2025 same-store new leases -3.7%, renewals +2.9%, blended +0.8%, and Invitation Homes 2025 total-portfolio renewals +4.6%, new leases -0.8%. These are portfolio-level, not SF-specific and not legal benchmarks. June 2024 Rent Board workload statistics show 23 total landlord petitions/154 units, including 18 capital-improvement petitions/148 units; the 19/149 subtotal includes one Costa-Hawkins petition. This is narrow formal-petition evidence, not proof of what all individual owners do.

## Flagged for Review

All {FLAG_COUNT} flags are published on the Flagged for Review page with official links. They include source conflicts, unverified case facts, the missing 94122 SAFMR row, no federal cap/attorney approval/both-units rule, historical privacy exposure, fixed-term/effective-date gaps, fee/registration gaps, and the static site's inability to self-certify its own final merge/deploy. Flagged items are nonblocking for publication, but they are not treated as verified.

## Sources and verification limits

{SOURCE_ENTRY_COUNT} source entries ({SOURCE_COUNT} distinct URLs) are catalogued in SOURCES.md and on the Sources page. Every published table row links to official rule or project-platform sources; owner-supplied rows say explicitly that the links are governing rules, not proof of intake. Structural validation checks generated files, links, privacy patterns and consistency. It is not legal verification and does not confirm the owner's property records.
"""

def _md_escape(text):
    return str(text).replace("|", "\\|").replace("\n", " ")

_flag_rows = "\n".join(
    "| {id} | {title} | {detail} | {sources} |".format(
        id=_md_escape(f["id"]),
        title=_md_escape(f["title"]),
        detail=_md_escape(f["detail"]),
        sources="; ".join("[{sid}]({url})".format(sid=sid, url=SOURCES[sid]["url"]) for sid in f["source_ids"]),
    )
    for f in FLAGS
)
FLAGGED_TEXT = f"""# Flagged for Review

This page is clearly labeled **Flagged for Review**. Status `needs review` means the item is published with official source links for manual review and does **not** block publication. Unverified case value cells are blank. Nonblocking does not mean verified.

| Flag | Issue | Detail | Official source(s) |
| --- | --- | --- | --- |
{_flag_rows}

See also `pages/flagged.html`, `research/flags.md`, `research/sources/irregularities.md`, `research/sources/unverified.md` and `research/current_audit/`.
"""

README_TEXT = f"""# RentincreaseSF4

Public GitHub Pages research dashboard for "Rental increase SF": an individual-owner Rent Board action plan, official-source-linked tables, anonymized two-unit case, analysis, and a clearly labeled Flagged for Review page.

Live site: https://kanlerxz87-cyber.github.io/RentincreaseSF4/

## Read first

1. `index.html` / `pages/summary.html` — direct license/reporting answer and executive summary.
2. `pages/process.html` — ordered Housing Inventory, license, tenancy, calculation and notice steps.
3. `pages/case.html` and `pages/calculations.html` — anonymized owner intake and conditional arithmetic.
4. `pages/flagged.html` — all {FLAG_COUNT} open/source/project flags.
5. `pages/sources.html` and `SOURCES.md` — {SOURCE_ENTRY_COUNT} entries, {SOURCE_COUNT} distinct official URLs.

## Repository map

- `scripts/site_*.py` — canonical source registry, rows, flags, text and styles.
- `scripts/build_site.py` — generates `data/`, `pages/`, `index.html`, CSS/JS and markdown deliverables.
- `scripts/validate_site.py` — structural, privacy, source-integrity and internal-link checks; writes `data/validation_report.json`.
- `VERIFICATION.md`, `REPO_REVIEW.md`, `research/current_audit/` — verification limits and current audit.
- `COORDINATION.md` — shared claims, stale takeover, PR/merge/deploy record.

## Privacy

Current public files use Tenant A-F placeholders, preserve supplied dates/amounts and omit the exact address. **Earlier public Git history/PR exposure is not remediated by current-tree anonymization.** See `research/privacy/HISTORY_EXPOSURE.md` and flags F26/F38. Raw intake is internal-only and gitignored; no raw identifier is reproduced in the public site.

## Build and validate

```bash
python3 scripts/build_site.py
python3 scripts/validate_site.py
git diff --exit-code
```

Not legal advice. No attorney approval or guarantee of no complaint/lawsuit is claimed. Any increase is framed as a conservative compliance checklist capable of tenant-lawyer review.
"""

CSS_TEXT = r"""
:root{--ink:#17233b;--muted:#5c6b82;--bg:#f6f7f9;--card:#fff;--line:#d9e0ea;--accent:#0b6e4f;--accent2:#24527a;--warn:#8a5a00;--warnbg:#fff6df;--okbg:#e8f5ee;--flagbg:#fff0f0;--flag:#a12626;--owner:#5b4b8a;--ownerbg:#f0edfa;--project:#e8eefc;--radius:12px;--max:1160px}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55}
a{color:var(--accent2)}
a:hover{text-decoration-thickness:2px}
.skip-link{position:absolute;left:-9999px;top:0;background:#fff;color:#000;padding:.6rem;z-index:100}
.skip-link:focus{left:0}
header{background:#12263f;color:#fff;padding:1.6rem 1rem 1.2rem}
.wrap,main,footer .wrap{max-width:var(--max);margin:0 auto}
header h1{margin:0 0 .3rem;font-size:clamp(1.5rem,3vw,2.15rem);letter-spacing:-.02em}
header p{margin:.2rem 0;color:#dbe6f5}
.meta{font-size:.84rem;color:#c7d5e8}
.privacy-strip{background:#fff0f0;border-bottom:1px solid #efc7c7;color:#7a1f1f;padding:.65rem 1rem;font-size:.9rem}
.privacy-strip .wrap{display:flex;gap:.6rem;align-items:flex-start}
.privacy-strip a{color:#7a1f1f;font-weight:700}
nav{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}
nav .wrap{display:flex;flex-wrap:wrap;gap:.45rem;align-items:center;padding:.55rem 1rem}
nav a{font-size:.88rem;text-decoration:none;padding:.35rem .55rem;border-radius:7px}
nav a:hover,nav a.active{background:#eaf0f7}
.nav-groups{position:relative}
.nav-groups summary{cursor:pointer;font-size:.88rem;font-weight:700;color:var(--accent2);padding:.35rem .55rem}
.nav-panel{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:.8rem;padding:.8rem 1rem;border-top:1px solid var(--line);background:#fbfcfe}
.nav-panel h3{margin:0 0 .35rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.nav-panel a{display:block;padding:.22rem 0}
main{padding:1.2rem 1rem 3rem}
.hero,.panel,section{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:1.1rem;margin:1rem 0;box-shadow:0 1px 5px rgba(20,35,60,.04)}
.hero h2{margin:0 0 .6rem;font-size:1.35rem}
.hero ol{margin:.6rem 0 .8rem 1.3rem;padding:0}
.hero li{margin:.4rem 0}
.disclaimer{background:var(--warnbg);border-left:4px solid var(--warn);padding:.75rem .9rem;border-radius:8px;font-size:.9rem;margin:.9rem 0}
.cta{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;font-weight:700;padding:.6rem .9rem;border-radius:8px;margin:.35rem .4rem .35rem 0}
.cta.secondary{background:#fff;color:var(--accent2);border:1px solid var(--line)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.9rem;margin:1rem 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:1rem}
.card .k{font-size:.76rem;text-transform:uppercase;letter-spacing:.07em;color:var(--muted)}
.card .v{font-size:1.45rem;font-weight:750;margin:.2rem 0;color:var(--accent2)}
.card .d{font-size:.88rem;color:var(--muted)}
.card a{font-weight:700}
.unit-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:.9rem}
.unit{border:1px solid var(--line);border-radius:var(--radius);padding:1rem;background:#fbfcfe}
.unit h3{margin:0 0 .4rem}
.unit .amount{font-size:1.35rem;font-weight:750;color:var(--accent)}
.legend{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.badge{display:inline-block;padding:.16rem .5rem;border-radius:999px;font-size:.73rem;font-weight:750;white-space:nowrap}
.badge.verified{background:var(--okbg);color:var(--accent)}
.badge.project{background:var(--project);color:var(--accent2)}
.badge.review{background:var(--warnbg);color:var(--warn)}
.badge.analysis{background:#e8eefc;color:var(--accent2)}
.badge.owner{background:var(--ownerbg);color:var(--owner)}
.badge.listed{background:#eef1f5;color:var(--muted)}
.searchbar{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin:.8rem 0}
.searchbar input{flex:1;min-width:220px;padding:.6rem .75rem;border:1px solid var(--line);border-radius:8px;font:inherit}
.searchbar .count{font-size:.85rem;color:var(--muted)}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px}
table{width:100%;border-collapse:collapse;font-size:.9rem;min-width:760px}
th,td{text-align:left;vertical-align:top;padding:.65rem .6rem;border-bottom:1px solid var(--line)}
th{background:#eef3fa;color:#253b5b;font-size:.76rem;text-transform:uppercase;letter-spacing:.04em}
tr:last-child td{border-bottom:0}
tbody tr:nth-child(even){background:#fbfcfe}
td.blank{color:var(--warn);font-style:italic}
.src a{display:inline-block;margin:0 .3rem .3rem 0;font-size:.78rem;background:#eef3fa;border:1px solid #d3ddef;padding:.15rem .4rem;border-radius:6px;text-decoration:none;max-width:340px}
.src a:hover{background:#e2ebf6}
.src-id{color:var(--muted);font-size:.72rem}
.owner-src{font-size:.8rem;color:var(--owner);display:block;margin-bottom:.3rem}
.flaglink{font-weight:750;color:var(--flag)}
.flagged-banner{background:var(--flagbg);border:1px solid #efc7c7;border-left:5px solid var(--flag);padding:1rem;border-radius:var(--radius);margin:1rem 0}
.small{font-size:.83rem;color:var(--muted)}
.narrative h2{margin:1.3rem 0 .5rem;font-size:1.16rem;color:var(--accent2);border-bottom:1px solid var(--line);padding-bottom:.3rem}
.narrative p{margin:.6rem 0}
.narrative ol,.narrative ul{margin:.5rem 0 .9rem 1.3rem;padding:0}
.narrative li{margin:.35rem 0}
.narrative a{word-break:break-word}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;padding:1.2rem;text-align:center}
footer a{color:var(--accent2)}
[hidden]{display:none!important}
@media(max-width:700px){header{padding:1.2rem .8rem .9rem}main{padding:.8rem .6rem 2rem}.hero,.panel,section{padding:.85rem}.privacy-strip .wrap{display:block}table{min-width:680px;font-size:.84rem}th,td{padding:.5rem .45rem}.src a{max-width:240px}}
@media print{nav,.cta,.searchbar,.privacy-strip{display:none}section,.hero{box-shadow:none;break-inside:avoid}body{background:#fff}}
"""

JS_TEXT = r"""
(function () {
  var input = document.querySelector('[data-table-search]');
  if (!input) return;
  var tables = Array.prototype.slice.call(document.querySelectorAll('main table'));
  var count = document.querySelector('[data-search-count]');
  function filter() {
    var q = input.value.trim().toLowerCase();
    var visible = 0, total = 0;
    tables.forEach(function (table) {
      Array.prototype.forEach.call(table.tBodies, function (body) {
        Array.prototype.forEach.call(body.rows, function (row) {
          total += 1;
          var show = !q || row.textContent.toLowerCase().indexOf(q) !== -1;
          row.hidden = !show;
          if (show) visible += 1;
        });
      });
    });
    if (count) count.textContent = q ? visible + ' of ' + total + ' rows match' : total + ' rows';
  }
  input.addEventListener('input', filter);
  filter();
})();
"""
