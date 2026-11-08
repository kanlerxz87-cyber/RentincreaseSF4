# RentincreaseSF4

Public GitHub Pages research dashboard for "Rental increase SF": an individual-owner Rent Board action plan, official-source-linked tables, anonymized two-unit case, analysis, and a clearly labeled Flagged for Review page.

Live site: https://kanlerxz87-cyber.github.io/RentincreaseSF4/

## Read first

1. `index.html` / `pages/summary.html` — direct license/reporting answer and executive summary.
2. `pages/process.html` — ordered Housing Inventory, license, tenancy, calculation and notice steps.
3. `pages/case.html` and `pages/calculations.html` — anonymized owner intake and conditional arithmetic.
4. `pages/flagged.html` — all 59 open/source/project flags.
5. `pages/sources.html` and `SOURCES.md` — 77 entries, 76 distinct official URLs.

## Repository map

- `scripts/site_*.py` — canonical source registry, rows, flags, text and styles.
- `scripts/build_site.py` — generates `data/`, `pages/`, `index.html`, CSS/JS and markdown deliverables.
- `scripts/validate_site.py` — structural, privacy, source-integrity and internal-link checks; writes `data/validation_report.json`.
- `VERIFICATION.md`, `REPO_REVIEW.md`, `research/current_audit/` — verification limits and current audit.
- `COORDINATION.md` — shared claims, stale takeover, PR/merge/deploy record.

## Privacy

Current public files use Tenant A-F placeholders, preserve supplied dates/amounts and omit the exact address. **Earlier public Git history/PR exposure is not remediated by current-tree anonymization.** See `research/privacy/HISTORY_EXPOSURE.md` and flag F44. Raw intake is internal-only and gitignored; no raw identifier is reproduced in the public site.

## Build and validate

```bash
python3 scripts/build_site.py
python3 scripts/validate_site.py
git diff --exit-code
```

Not legal advice. No attorney approval or guarantee of no complaint/lawsuit is claimed. Any increase is framed as a conservative compliance checklist capable of tenant-lawyer review.
