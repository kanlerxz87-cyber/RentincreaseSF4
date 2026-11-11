# T53 — Closing the open C72-D04–D07 items (2026-11-11 UTC)

**Session:** `arena-f7ac76e9` · **Branch:** `arena/f7ac76e9-rentincreasesf4` · **Base:** `a560c27`
**Scope:** the four items the previous integration session (`arena-3e6655be`, PR #45) explicitly left open and published as flag F50: C72-D04, D05, D06 and D07.

Everything below was opened directly with `fetch_page` on 2026-11-11. No value was taken from a search snippet, and no value was inferred. Where a fact could not be read unambiguously from the official page, the cell was left blank.

## 1. C72-D06 — official HUD `94122` SAFMRs (previously blank)

| Source | URL opened 2026-11-11 | Values read |
| --- | --- | --- |
| HUD USER FY 2027 ZIP calculation, ZIP 94122 | <https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360> | Efficiency **$2,370**; 1BR **$2,770**; 2BR **$3,410**; 3BR **$4,460**; 4BR **$5,020** (ZIP base rent $2,622) |
| HUD USER FY 2026 ZIP calculation, ZIP 94122 | <https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=94122&metro_code=METRO41860MM7360&year=2026> | Efficiency **$2,280**; 1BR **$2,730**; 2BR **$3,310**; 3BR **$4,230**; 4BR **$4,380** (ZIP base rent $2,512) |

Rows changed: `FED-07` (both years, status `verified`), `MKT-07` (FY2026), `MKT-08` (FY2027, moved into the FY2027 section). New sources **S83** and **S84**.

New flag **F52** and row `MKT-10` record the limit: a SAFMR is HUD's 40th-percentile gross-rent benchmark used for voucher payment standards. It is not a market-rent appraisal, not a lawful rent ceiling, and not a basis for an increase. A comparison with the case contract rents would require each unit's bedroom count and utility treatment, which are not published — so no comparison, percentage or "market rent" conclusion is asserted, and the bedroom cells stay blank.

## 2. C72-D07 — SEC filings (previously "Equity Residential dead end")

| Source | URL opened 2026-11-11 | Values read |
| --- | --- | --- |
| Essex Property Trust, Form 8-K Exhibit 99.1, Q4 2025 earnings release and supplemental data | <https://www.sec.gov/Archives/edgar/data/920522/000114036126003709/ef20064474_ex99-1.htm> | Page S-9, *Same-Property Revenue Results by County*: **San Francisco County** — 1,356 apartment homes; 2.4% of actual NOI; average monthly rental rate **$2,966** in Q4 2025 vs **$2,897** in Q4 2024 (**+2.4%**); financial occupancy **95.5%** vs 96.1% (−0.6%); gross revenues **$12,580k** vs **$12,336k** (**+2.0%**); sequential gross revenues **−1.2%** vs Q3 2025. Page S-7 corroborates 1,356 consolidated San Francisco apartment homes at a $2,966 average monthly rental rate and shows a further 537 unconsolidated homes at $3,469. Footnote 7 states FY2025 **blended same-property net effective rate growth was 2.5%** portfolio-wide. |
| Equity Residential, Form 10-K for the fiscal year ended December 31, 2025 | <https://www.sec.gov/Archives/edgar/data/931182/000119312526051433/eqr-20251231.htm> | Filing confirmed filed and retrievable. No San Francisco-specific figure was extracted, so **no EQR figure is published** and `CORP-09` stays blank. |

Rows changed: `CORP-07` (Essex San Francisco County, verified), `CORP-08` (Essex FY2025 blended growth, portfolio-wide, verified), `CORP-09` (EQR 10-K, blank, `needs review`). New sources **S85** and **S86**. Flag **F15** updated from "dead end" to "partly resolved" and keeps the limitation that county and portfolio averages are not a legal benchmark.

**Deliberately not published:** the quarterly new/renewal lease-tradeout percentages on page S-8, because the column labels were not captured unambiguously in the fetched chunk. Only the footnote's FY2025 blended figure is published.

## 3. C72-D05 — File 261020 draft text (not enacted)

| Source | URL opened 2026-11-11 | Values read |
| --- | --- | --- |
| Board of Supervisors, File 261020, **Leg Ver1** attachment | <https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E> | Proposed new **Sec. 37.3(h)**: combined banked (`§ 37.3(a)(2)`) and capital-improvement (`§ 37.3(a)(3)`) increases may not raise a tenant's rent by more than **10% of the lowest base rent in effect at any time in the 12 months before the increase takes effect**; applies to banked increases noticed, and pass-throughs based on petitions filed, **on or after September 15, 2026**; in effect **until December 31, 2029** unless extended; excess may be accumulated and imposed **on or after January 1, 2030**. |

New source **S87**; flag **F47** rewritten to separate what the draft now shows (duration and the measurement basis) from what no official page resolves (whether increases noticed between 9/15/2026 and enactment are caught, and how the 10% interacts with the separate annual allowable increase under `§ 37.3(a)(1)`). The status remains **Pending Committee Action — not enacted**; this is not current law and no case-specific banked or capital-improvement amount is asserted.

## 4. C72-D04 — `SOURCES.md` ledger drift

`SOURCES.md` stopped at S71 and still said "the source count is 70". It now:

- carries S72–S87 with official links and verified statements (S72–S82 were already in `scripts/site_sources.py` but missing from the ledger);
- marks the old "70 sources" sentence as historical and states the current computed count;
- is guarded by two new validator checks: **every catalogued source ID must appear in `SOURCES.md`**, and a stale hand-typed total fails the build.

## 5. Source summaries restored with verified detail

The earlier emergency repair of C72-D01 replaced three corrupted statements with short summaries, which removed verified detail. S57 (Cal. Civ. Code § 1942.5), S59 (new-construction partial exemption) and S61 (SF evictions) were re-read in full on 2026-11-11 and rewritten to state only what those pages say, including the 180-day conditions, the once-per-12-months limitation, the damages and fee provisions, and the Certificate of Occupancy / prior-use conditions.

## 6. Gates and scope limits

- `python3 scripts/build_site.py` → 22 data files, 20 page HTML files, index, CSS, `.nojekyll`, 3 markdown deliverables.
- `python3 scripts/validate_site.py` → **125 checks, 0 errors** (87 sources, 70 flags, 351 rows; includes the new SOURCES.md, SAFMR, resolved-gap and SF corporate checks).
- `python3 research/b87_notice_kit/validate_kit.py` → **19 checks, 0 errors**.
- `python3 research/c72_2026-11-11_audit/validate_c72.py` → **19 checks, 0 errors** (21 pages, 1,860 hrefs/anchors, 0 broken, 0 stored digests).
- **Not done / not claimed:** no attorney review; no guarantee against a tenant petition, complaint or lawsuit; no fresh independent legal verification of every inherited row; external links were not exhaustively crawled for reachability; the historical privacy exposure (F44, F51) is unchanged and no history rewrite was attempted; the draft ordinance is not enacted and must be re-checked before any notice is served.
