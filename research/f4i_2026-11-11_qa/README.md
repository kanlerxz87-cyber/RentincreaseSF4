> **Provenance (recovered 2026-11-13 by session `arena-87a91aec`, final integration).**
> This record was written by session `arena-47e44bbe` on branch `arena/47e44bbe-rentincreasesf4` and
> reached `main` only through the still-open pull request #48, whose owner was stale by more than
> 60 minutes with no commits. It is reproduced here **verbatim** so that no session's work is
> discarded, and the owner branch / pull request are logged in `COORDINATION.md`. The figures it
> records were independently re-opened at the same official URLs on 2026-11-13 by session
> `arena-87a91aec` and still hold; see `research/t54_suggestions/README.md`. Pull request #48's
> own shared-file edits were yielded by its owner to PR #47 and are not reproduced here.

# F4I — independent re-verification of `C72-D01`–`C72-D08` and handoff to the `I1D` session

**Session:** `arena-47e44bbe` · **Branch:** `arena/47e44bbe-rentincreasesf4` (fixed by Arena) · **Date:** 2026-11-11 UTC
**Outcome:** this session's shared-file work was **yielded** to the concurrently active session `arena-1d1e5d2d` (`I1D`, PR #47), which covers the same defect ledger with a superset of sources. This directory keeps only the independent verification record, which is unique to this session and complements `I1D` rather than duplicating it.

Privacy: placeholders only; dates, amounts, ZIP and the two rents unchanged; no street address; **no hash, digest or encoding of any personal identifier anywhere**.

Not legal advice. No attorney approval and no guarantee that no complaint or petition will occur is claimed.

---

## 1. Claim, discovery, and the decision to yield

- **04:20 UTC** — read `COORDINATION.md`, all 33 remote session branches and `gh pr list --state all`. `origin/main` was `49126b0`; **no open PRs**; every prior claim (`T49`–`T52`, `C72`, `EA4`) was stale by more than 60 minutes with no commits. Under the board's takeover rule this session claimed `F4I-A` and pushed the claim (`6723b8d`) before editing anything.
- **04:22–04:25 UTC** — independently fixed and re-verified all eight defects `C72-D01`–`C72-D08`, reaching **129 checks / 0 errors** with four new guard checks.
- **04:26 UTC** — discovered that **two other sessions woke up and pushed while this session was working**: PR #46 (`arena-3e6655be`) merged into `main` as `3aa3b6d`, and PR #47 (`arena-1d1e5d2d`, `I1D`) opened at 04:23 UTC and still active.
- **Decision:** verify what each had already fixed, then **yield** rather than merge a competing duplicate of the same shared files.

## 2. Verification of what actually landed

### PR #46 (`main` = `3aa3b6d`) — independently checked, and correct

| Defect | Verified on `main` after PR #46 | Verdict |
| --- | --- | --- |
| `D01` | `S56` (the fee page) still carries the fee sentence, correctly. `S57`, `S59`, `S61` no longer contain `$59.00` and each states its own subject ("…statutory conditions and remedies", "…certificate of occupancy after June 13, 1979 and no prior residential use", "…Eviction Defense Collaborative"). | **Fixed** |
| `D02` | `scripts/validate_site.py` on `main` contains **zero** occurrences of `sha256` or `private_fingerprints`; `research/n08_qa/privacy_check.py` was reduced accordingly. | **Fixed** |
| `D03` | `build_site.py` now filters `not f["id"].startswith(("T03-", "B87-"))`, so the published flag total is 67 and not 75. | **Fixed** |
| `D04`–`D08` | **Still open on `main`**: `SOURCES.md` has no `S83`–`S86` rows; `FED-07` is still the blank "Official ZIP row not obtained" row; no SF-County SEC row. | **Open — covered by PR #47** |

`main` at `3aa3b6d` passes `scripts/validate_site.py` (**119 checks, 0 errors**) — re-run by this session after the yield.

### PR #47 (`arena/1d1e5d2d`, `I1D`) — covers `D04`–`D08` as a superset

`I1D` adds nine new sources `S80`–`S90`, including `S83`/`S84` (File 261020 `Leg Ver1` **and** `Leg Dig Ver1`), `S85`/`S86` (FY2027 and FY2026 94122 SAFMR summaries), `S87`/`S88` (FY2027 HMFA FMR + HUD reevaluation notice) and `S89`/`S90` (Essex **and** Equity Residential SEC filings). It also rewrites `F13` and `F15` as partly-resolved rather than blank.

**Source-ID collision, resolved by yielding.** This session had independently numbered its own additions `S83`–`S86`, but with **different subjects** (`S83` = FY2027 SAFMR here vs `S83` = File 261020 Leg Ver1 in `I1D`). Keeping both numbering schemes would make a source ID ambiguous. Because `I1D` was alive and covers a strict superset, this session **discarded its own shared-file edits** and kept only this record. Any session reading this should treat `S80`–`S90` as owned by `I1D`.

## 3. Independent verification work retained here (unique to this session)

These figures were each opened directly at the official URL on 2026-11-11 and are recorded here so that `I1D`'s equivalents have a second pair of eyes.

| Official source | What this session read and confirmed |
| --- | --- |
| [SF.gov — Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | Allowed increase **1.6%**, effective **March 1, 2026 – February 28, 2027**, being 60% of the Bay Area CPI-U increase. "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases." Licence requirement effective **July 1, 2022**, or **March 1, 2023** for condominiums and buildings with 1–9 residential units. 30-day notice, 90-day if more than 10% alone or combined in the same year, **+5 days if mailed**; state the dollar amount, percentage and effective date; use the rate in effect on the increase **date**. No rounding up. **No extra rent for an additional roommate, even if the lease says so.** The File 261020 notice is still labelled "**has not been enacted and is subject to change**". |
| [SF.gov — Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | "**All owners of residential property are required to report.**" Free, online 24/7, **March 1** every year, **under penalty of perjury**, and "**the information entered in the housing inventory submission is public**". "A rent increase license will be automatically generated for non-owner occupied units"; the landlord "must have a current rent increase license on file … before any annual or banked rent increase can go into effect"; the licence "does not need to be included with your rent increase notice"; and a notice "will not be enforceable without having a rent increase license **on the effective date of the notice**". "**The Rent Board does not assess monetary penalties for filing after the deadline.**" |
| [SF.gov — The Rent Board Fee](https://www.sf.gov/rent-board-fee) | 2026-2027: **$59.00 per dwelling unit**, $29.50 per guest unit; recover **50% ($29.50)** from tenants in occupancy on **November 1**; **March 1** deadline; **5% per month to a 15% maximum**; unpaid by **June 1** referred to the Bureau of Delinquent Revenue; exemption window closes **December 14, 2026**; "**requesting a Rent Board Fee exemption does not satisfy Rent Board Housing Inventory reporting requirements**"; vacant units are **not** exempt. |
| [SF.gov — Partial exemption, newly constructed units](https://www.sf.gov/information--partial-exemption-newly-constructed-rental-units) | Exemption needs a first Certificate of Occupancy **after June 13, 1979** **and** no prior residential use; live/work adds a building-wide condition. Just-cause protections and the annual fee still apply, and the unit "may be covered by the California Tenant Protection Act … which limits annual rent increases to no more than 5% plus the percentage increase in the local CPI". |
| [HUD USER — FY2027 SAFMR, ZIP 94122](https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360) | **$2,370 / $2,770 / $3,410 / $4,460 / $5,020** (0–4 BR). 2 BR build-up: $2,622 ZIP base × 1.183 recent-mover × 1.0352 inflation × 1.0604 trend = $3,410. |
| [HUD USER — FY2026 SAFMR, ZIP 94122](https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026zip_code_calc.odn?zcta=94122&metro_code=METRO41860MM7360&year=2026) | **$2,280 / $2,730 / $3,310 / $4,230 / $4,380**. |
| [Legistar — File 261020 Leg Ver1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E) | Proposed **§ 37.3(h)**: no banked (§ 37.3(a)(2)) and/or capital-improvement (§ 37.3(a)(3)) increases that raise rent by more than **10% of the lowest base rent in effect at any time in the preceding 12 months**; applies to banked notices provided on or after **9/15/2026** and capital-improvement petitions filed on or after that date; in effect **until 12/31/2029** unless extended; excess may be accumulated and imposed **on or after 1/1/2030**. It does **not** amend the § 37.3(a)(1) annual allowable increase. **Pending Committee Action — not enacted.** |
| [SEC — Essex Property Trust 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/920522/000114036126003709/ef20064474_ex99-1.htm) | **San Francisco County**: 1,356 apartment homes, 2.4% of actual NOI, average monthly rent **$2,966 (Q4 2025) vs $2,897 (Q4 2024) = +2.4%**, financial occupancy **95.5% vs 96.1%**, gross revenues **+2.0%** YoY and **−1.2%** sequentially. Company-wide Q4 2025: new **−2.4%**, renewal **+4.8%**, blended **+1.9%**; FY2025 blended same-property net effective rate growth **2.5%**. |

## 4. Case arithmetic re-run (`Decimal`, no rounding up — SF.gov prohibits rounding up)

- **Unit 1:** $3,995.00 × 1.6% = **$63.92** → **$4,058.92**
- **Unit 2:** $3,150.00 × 1.6% = **$50.40** → **$3,200.40**
- **Rent Board Fee, two units:** $59.00 × 2 = **$118.00**; 50% recoverable = **$29.50 per unit / $59.00 total**; 15% capped penalty = $8.85 per unit

Illustrative applications of the published rate only — not a recommendation, not an eligibility determination, and not an assertion that either unit is eligible on a given date. **No banked amount is asserted**: no increase history was supplied.

## 5. Flagged for review — carried forward, deliberately not resolved

- **File 261020 retroactivity.** Leg Ver1 reaches banked notices served from **9/15/2026**, but the ordinance was introduced that same day and the Rent Board notice was posted **11/9/2026**. The text therefore reaches notices served before the proposal was public, and **no official page says how such a notice is treated**. Pending and not enacted — re-check the committee status on the day any notice is served.
- **Subject-unit comparison.** The ZIP SAFMRs are now published, but the **bedroom count, size and condition of both units were never supplied**, so no subject-unit HUD comparison exists. Nothing is inferred.
- **`F44` — privacy exposure in history.** The raw tenant identifiers remain reachable in this public repository's earlier git history and in PR #1's diff. **Only the repository owner can remediate** (history rewrite or a GitHub Support purge). PR #46 removed the last *derived* form of that exposure from the current tree, but a clean current tree is **not** a history purge.
- **Owner-supplied case rows** are labelled as such and are not official verification; the corresponding official cells stay blank.
- **SF.gov page-internal inconsistencies** recorded earlier (licence-consequence wording, fee referral timing, the stale 2023 fee page, the Form 573 historical rows, the unstated co-tenant split of a 50% recovery, the Current Rates hyperlink defect) are retained as published flags, none inferred away.

## 6. What an owner should still confirm before serving anything

1. Coverage of both units on the SF Planning Property Information Map — "built 1940" is owner-supplied and **unverified**.
2. Current Housing Inventory reporting **and** a current rent increase licence on file for each unit on the intended **effective** date.
3. The anniversary date for each unit, and whether Unit 1's April 1, 2026 continuation restarted it.
4. Whether Unit 1's April 2026 occupant triggers any § 6.14 / Costa-Hawkins analysis — unverified; no market-rate reset is recommended.
5. Any fixed-term lease bar, open habitability issue, or tenant repair/organising activity in the previous 180 days.
6. The committee status of File 261020 on the day the notice is served.
