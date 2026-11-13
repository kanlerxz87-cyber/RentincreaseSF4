# T54 — Suggestions & Review page, and the 2026-11-13 re-verification pass

Session `arena-87a91aec`, branch `arena/87a91aec-rentincreasesf4`, 2026-11-13 UTC.

Scope of this record:

1. The official sources re-opened directly on 2026-11-13, with what was checked and the result.
2. The new **Suggestions & Review** page (`pages/suggestions.html`), how its rows are grounded, and how
   the "review before implementing" workflow is enforced.
3. The full-tree gates run before publication and what they do **not** prove.

This record is not a claim that every inherited row was re-verified today. Each source in the ledger
keeps its own verification date, and only the sources listed below carry a 2026-11-13 note.

---

## 1. Sources opened directly on 2026-11-13

Each page below was fetched with `fetch_page` from its official URL on 2026-11-13 UTC. Quotations are
verbatim from the fetched content.

| Source ID | Official page opened 2026-11-13 | What was checked | Result |
| --- | --- | --- | --- |
| S07 | [The Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | Reporting duty, March 1 deadline, licence generation, licence-on-effective-date rule, penalty position, publicity of the filing, tenant portal check | Unchanged. "All owners of residential property are required to report."; licence "automatically generated for non-owner occupied units"; "A landlord must have a current rent increase license on file with the Rent Board before any annual or banked rent increase can go into effect."; "The Rent Board does not assess monetary penalties for filing after the deadline."; "The information entered in the housing inventory submission is public."; a tenant "can search the Rent Board Portal to see if their landlord is up to date with their rent increase license". Also confirms that requesting a Rent Board Fee exemption "does not satisfy Rent Board Housing Inventory reporting requirements". |
| S56 | [The Rent Board Fee](https://www.sf.gov/rent-board-fee) | Amount, due date, penalty ladder, delinquency referral, exemption window, 50% recovery test, fee cycle timeline | Unchanged. "$59.00 per dwelling unit" for the 2026-2027 tax year; "March 1 of each year for the Rent Board Fee"; "A 5% late penalty will be added to the amount of the fee every month following March 1 (for a maximum penalty of 15%)"; "Fees that have not been paid in full by June 1 will be referred to the Bureau of Delinquent Revenue with additional costs added"; exemption deadline "December 14, 2026"; 50% recoverable from tenants "in occupancy of each unit if the tenant has been living in the unit as of November 1 of the applicable tax year"; penalties may not be recovered. The page states the timeline in two places that differ on when referral happens — already published as flag F38, unchanged. |
| S25 | [Report an unlawful rent increase or request a review of your rent history](https://www.sf.gov/report-unlawful-rent-increase-or-request-review-your-rent-history) | Cost, filing deadline, form, hearing, attorney requirement | Unchanged. "There is no charge for filing the petition"; "There is no time limit for filing a petition"; hearing "before a Rent Board Administrative Law Judge"; "The hearing process is designed so that no one needs an attorney, although parties are entitled to have an attorney or other authorized representative assist them at the hearing." |
| S24 | [Speak with a Rent Board counselor](https://www.sf.gov/speak-rent-board-counselor) | Cost, languages, limits, contact details | Unchanged. Cost "Free"; help "in Spanish, Cantonese, and Mandarin" with interpretation for other languages; "We cannot give legal advice"; "Calls are generally limited to 5 minutes"; "Have your questions written down before you speak with us"; phone counseling Monday to Friday 9–12 and 1–4; counselor 415-252-4600. |
| S16 | [Rent Increases Under Section 6.14 And Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins) | Unlimited-increase conditions, 6.14 notice, co-tenant vs sub-tenant, petition | Unchanged. Section 6.14 "provides for an unlimited rent increase on remaining occupants when the last original occupant vacates the unit, as long as the landlord timely served all remaining occupants with a written '6.14 notice.'"; "Generally, sixty days is considered reasonable"; "a co-tenant, as opposed to a subtenant, is not subject to such a rent increase"; no petition is required but a tenant may petition. |
| S26 | [Rent Board Forms Center](https://www.sf.gov/reports--rent-board-forms-forms-center) | Forms list; proposed-changes notice | Confirmed. Lists 516A, 516B, 516C, 516D and 517 with English and translated PDFs, and carries the "Notice: Proposed Changes to Rent Increase Limitations" posted November 9, 2026 for File No. 261020, stating "This legislation has not been enacted and is subject to change." |
| S73 | [Rent Board Rules Part XIII (Rule 13.14)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent) | Rule 13.14 licensing text and applicability dates | Unchanged verbatim. "Any rent increase under Ordinance Sections 37.3(a)(1)-(2) purporting to be effective while the landlord is unlicensed shall render the entire rent increase null and void; provided, however, that the effective date of the rent increase, not the date of service, shall be used to determine whether or not the increase conforms with the provisions of this section." Applies to increases effective on or after July 1, 2022, and for condominiums and buildings with fewer than ten residential units to increases effective on or after March 1, 2023. |
| S42 | [24 CFR 100.500 — Discriminatory effect prohibited](https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/part-100/subpart-G/section-100.500) | Currency of the regulation | Current. Page states "up to date as of 11/10/2026" and "Title 24 was last amended 8/20/2026"; the discriminatory-effect standard (liability without proof of intent; substantial legitimate nondiscriminatory interest; no less discriminatory alternative) is unchanged. |
| S72 | [Proposed-changes notice, second and third locations](https://www.sf.gov/learn-about-rent-increases-san-francisco) | Where the notice appears | The File 261020 notice appears on the rent-increase page (S01), the Current Rates page (S02) **and now also the Forms Center (S26)**. Recorded as a 2026-11-13 note on S72 and S26. Still not enacted. |

### The four rate-bearing pages, reopened the same day

A separate pass on the same day re-opened the four pages that carry the figures the site is built on.

| Source ID | Official page opened 2026-11-13 | What was checked | Result |
| --- | --- | --- | --- |
| S01 | [Learn about rent increases in San Francisco](https://www.sf.gov/learn-about-rent-increases-san-francisco), chunks 0–1 | Current rate, licence rule, base-rent-only rule, no rounding up, notice periods and contents, anniversary date, additional-occupant rule, the published examples | Unchanged. 1.6% effective March 1, 2026 through February 28, 2027; "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases on a tenant"; base rent only and "Rent increases cannot be rounded up to the nearest dollar"; 30-day notice, 90-day if more than 10%, 5 more days if mailed; "The landlord should use the percentage that will be in effect on the date of the increase"; additional occupants. The November 9, 2026 notice is still present and still marked not enacted. |
| S02 | [Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit), chunk 0 | Rate table, deposit interest, bankable fees, capital-improvement rates, F45 hyperlink defect, absence of a 2027-28 rate | Unchanged. 1.6% / 1.4% / 1.7% for the three published periods; security deposit interest 4.2%; bankable Rent Board Fees $29.50. **F45 is still live:** the link labelled "575 Cap. Imp. Labor Rates" still points to `https://www.sf.gov/documents/34916/574_Cap._Imp._Imputed_Interest_26-27_7.26.pdf`, the Form 574 Imputed Interest PDF. No rate for increases effective on or after March 1, 2027 is published (F27). |
| S05 | [Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | 24-month banking rule, no compounding, licence, notice contents, the published example | Unchanged. "A skipped increase is only banked if at least 24 full months pass without any rent increase"; percentages are added, never compounded or prorated; the licence is required; the notice must state the dollar amount, percentage, effective date and which part is banked. **F02 is still live:** the example says to add the banked 5.3% to "the annual allowable rent increase in effect on August 1, 2024 (1.4%)", while Form 571 shows 1.7% for March 1, 2024 – February 28, 2025. |
| S27 | [The California Tenant Protection Act of 2019 (AB 1482)](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482), chunk 0 | SF cap, the CPI used, the interaction with local law, the two-unit exemption, the in-law-unit rule | Unchanged. "The maximum rent increase for units under AB 1482 from August 1, 2026 to July 31, 2027 is 8.8% in San Francisco"; "This does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance"; the applicable CPI is 3.8%, so 5% + 3.8% = 8.8%; the two-unit exemption requires the second unit to have been occupied by an owner for the entire tenancy; the single-family exemption does not apply where there is more than one dwelling unit on the same lot or a second residential unit that cannot be sold separately, such as an in-law unit. |

**Flags re-confirmed live against the pages today:** F01 (S01 example says 1.6% for June 1, 2025 while Current Rates show 1.4%), F02 (S05 example says 1.4% for August 1, 2024 while Form 571 shows 1.7%), F03 (S01 example banks an increase after 12 full months while S05 requires 24 full months) and F45 (the "575" link defect on S02). All four remain accurate as published; none was closed or reworded by this session.

### Ledger changes from this pass

- `scripts/site_sources.py`: `DATE` moved from `2026-11-11` to `2026-11-13` (the ledger was updated
  today). The twelve sources above gained an explicit "Re-verified 2026-11-13" statement; S72 gained a
  note about the third location of the proposed-changes notice.
- `SOURCES.md`: the same notes were added to the hand-maintained table, and the header records this
  session's pass.
- `scripts/validate_site.py`: the pending-cap check now also accepts the 2026-11-13 ledger date.

---

## 2. The Suggestions page

### Why it was needed

The owner asked for *"a section dedicated for suggestions so someone can review suggestions and choose the best path before implementing any changes"*, and for *"suggestions ... to discover missing information"*. A line-by-line review of the published tree found no such section: the word "suggest" appeared only inside `data/questions.json`, `pages/questions.html` and `TENANT_ASSISTANCE_RESEARCH.md`. That gap is what this session set out to close.

### A scope collision, and how it was resolved

While this session was building its own Suggestions page, the concurrent session `arena-415e54ea` merged **PR #51** to `main` with a **Suggestions review queue** of its own (`SUG-P*`, `SUG-A*`, `SUG-B*`, `SUG-C*`), plus a **Decision Readiness** register (`pages/decision.html`), the **state-vs-local** answer to the owner's question, and sources S88–S91.

Both sets of work are kept. The page is now one canonical Suggestions page with the concurrent session's groups first and this session's groups appended:

| Group | Source | Rows | Content |
| --- | --- | --- | --- |
| Review process | `arena-415e54ea` | SUG-P1…P5 | The 5-step review workflow: read, check the evidence, choose, record, only then implement |
| A | `arena-415e54ea` | SUG-A1…A7 | Closing information gaps before deciding (owner actions) |
| B | `arena-415e54ea` | SUG-B1…B6 | Improving this site so it supports a decision |
| C | `arena-415e54ea` | SUG-C1…C6 | How to approach the increase itself (decision paths, not legal advice) |
| **D** | `arena-87a91aec` | SUG-D1…D12 | **Compliance gates** — licence status on the effective date, Housing Inventory filing tracker, fee calendar with the Nov 1 occupancy switch, effective-date rate engine, banked-increase ledger, pending-legislation watch row, retaliation-window screen, uniform-criteria record, §6.14 fact screen, coverage determination sheet, notice assembly, petition routing |
| **E** | `arena-87a91aec` | SUG-E1…E5 | **Evidence and defensibility** — case-file completeness checklist, tenant-side challenge walkthrough, printable attorney-review handoff packet, neutral-language bank, Housing Inventory public-records disclosure note |
| **F** | `arena-87a91aec` | SUG-F1…F4 | **Discovering the missing information** — missing-information register, the facts only the owner can supply, the Rent Board counsel call script, the pre-decision gate sequence |
| **G** | `arena-87a91aec` | SUG-G1…G6 | **Internal site quality** — per-row verification date, source link/content monitor, unchanged-column consistency, blank-means-unknown convention, print and mobile review mode, review-cycle date |
| **H** | `arena-87a91aec` | CL-D1…CL-G6 | **Review checklist** — one blank reviewer row per D–G proposal, with its own `CL-` identifiers so a checklist row is never confused with the proposal it refers to |

Where the two sessions' proposals touch the same ground — the link monitor, the owner-only facts list, the counsel call script, the uniform-criteria record — the row's notes name the related row instead of restating it. Nothing is presented twice as if it were two proposals. The concurrent session's **Decision Readiness** page and its state-vs-local answer are kept unchanged.

### How each row is grounded

| Field | Rule |
| --- | --- |
| `notes` | The official rule or fact that motivates the proposal, quoted or closely paraphrased from the official source, plus any cross-reference to a related row. |
| `source_ids` | One or more official source IDs. Every row resolves to an official-domain URL, and the validator fails the build otherwise. |
| `value` | What changes and why it helps the decision. |
| `effort` | Build cost and expected effect on the quality of the decision. Both are site-work estimates, not statements about law. |
| `review_status` | Starts at `Review` (this session's rows) or `open for review` (the concurrent session's group A rows). Nothing is pre-approved. |

Five rows (SUG-G1 to SUG-G5) are proposals about how the site itself should work. Their notes carry the exact marker `Internal site-design proposal`, and the validator enforces three things: a row marked internal must carry the marker, a row not marked internal must not carry it, and exactly the five expected rows carry it. SUG-G6 is the one row with a mixed basis — it cites the published rate period, the pending cap, the fee amount and the licensing rule — so it is not marked internal. These rows still resolve to the project record (S68), so every rendered row keeps an official-domain link and no source was invented merely to fill a cell.

### The review-before-implementing workflow

- Every proposal row renders a review-status badge reading `Review` or `open for review`. The validator checks that no row is pre-approved.
- The **Review checklist** section repeats every D–G proposal ID with a blank Decision, Reviewer, Date and Review note cell, each labelled "(blank - to be completed by the reviewer)". The validator checks the blank count.
- The 5-step review process (published by the concurrent session) states that accepting a suggestion is a decision by the owner, that nothing auto-applies, and that implementation means editing `scripts/site_*.py` and rebuilding.

### Groups published by this session

Group F is the direct answer to the owner's request for a clear list of the questions, information and answers needed before a decision can reasonably be made. It separates the questions an official record can answer from the facts only the owner can supply, and names the official route for each. The same content is cross-linked from the Executive Summary, and the concurrent session's Decision Readiness page answers the same question for this case with five ordered gates, 20 open questions and four decision paths.

## 3. Gates run before publication

| Gate | Result |
| --- | --- |
| `python3 scripts/build_site.py` | Clean. 24 data files, 22 page HTML files, `index.html`, `assets/site.css`, `.nojekyll` and 3 markdown deliverables. Re-running produces byte-identical `data/` and `pages/`. |
| `python3 scripts/validate_site.py` | **151 checks, 0 errors** (91 official sources, 71 flags, 451 rows, 0 broken internal links). Six new checks cover this session's contribution: official basis, effort and review status on every D-G row; the internal-marker rule; no pre-approved row; one blank checklist row per proposal; the rendered blank reviewer cells; and no approval or guarantee language. |
| `python3 research/b87_notice_kit/validate_kit.py` | 19 checks, 0 errors. |
| `python3 research/c72_2026-11-11_audit/validate_c72.py` | 19 checks, 0 errors; 23 HTML pages scanned with 0 broken links, 0 broken anchors and 0 stored digests. The audit's page-count check was updated as pages were added and is now a lower bound, so a new page cannot break it. |
| `python3 research/n08_qa/privacy_check.py` | 0 fingerprint matches in the current tree. |
| Independent HTMLParser link crawl | 0 broken internal links across all pages. |

The approval-language check was rewritten during this session. The first version used a bare substring
test and produced a false positive on the sentence "It does not state that any rent increase is
lawful, approved or safe from challenge." The replacement matches the phrases against a negation
window, so a negated statement is not treated as a claim. The underlying text was also reworded where
it was ambiguous about the retaliation analysis (now SUG-D7), so it describes the exposure as
independent of whether the increase amount itself is permitted rather than implying the amount is
permitted.

Two further defects were found and fixed while integrating with the concurrent session's work: the
review-checklist rows initially reused their proposal IDs, which made row IDs non-unique on the site
(they now carry their own `CL-` identifiers, and the validator checks uniqueness); and the section
renderer had no way to show the per-section introduction paragraphs that both sessions' groups use
(the renderer now emits them).

### The merge with the concurrent session

The gate numbers above are for the **merged** tree, not for this session's branch alone. The merge
was mechanical and non-destructive: generated files were taken from the merged side and then
regenerated from the merged generator; `COORDINATION.md` keeps both session records verbatim; the
shared generator files were taken as the merged base and this session's delta re-applied on top. No
row, source, flag or research record from either session was dropped. Two research records that
existed only on stale pull requests were also recovered and preserved verbatim with provenance
headers: `research/f4i_2026-11-11_qa/README.md` (from PR #48) and
`research/current_audit/2026-11-08_source_repo_audit.md` (from PR #25).

### What these gates do not prove

- They are structural and link checks. They are **not** legal verification and **not** a certification
  that any increase in this case is lawful.
- They do not establish attorney review, challenge immunity, or the absence of a future complaint,
  inquiry or lawsuit.
- The privacy check covers the current tree only. The historical exposure of short identifiers in this
  public repository's git history and pull-request diffs (F44, F51) is unchanged and remains
  owner-actionable; nothing in this session claims a history purge.
- External links were not exhaustively re-crawled. The eight pages re-fetched today are the ones listed
  above; every other source keeps its own earlier verification date.
- F27 (no published rate for increases effective on or after March 1, 2027) and F46 (File 261020 not
  enacted) are unchanged and still open.

---

## 4. Flagged items

No new flag was required by this session. Nothing found in the 2026-11-13 pass contradicts a published
figure or a published source link. The Suggestions page itself publishes no legal finding, and its
rows that touch the two units in this case describe *proposals and open questions*, not determinations.
