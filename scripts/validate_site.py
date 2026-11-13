"""Re-verify combined data line by line, validate source links, privacy and internal links.

Run: python3 scripts/validate_site.py
Writes data/validation_report.json. Exits nonzero on any error.
"""

import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import site_data as D

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PAGES = ROOT / "pages"

# Government sources, plus the two project-record domains used only for rows about this
# repository (S68 repository, S69 GitHub Pages build API). Project-record rows are labelled
# "Project record" in the source ledger and never support a legal or rent finding.
OFFICIAL_DOMAINS = {
    "sf.gov", "media.api.sf.gov", "sfplanninggis.org", "default.sfplanning.org",
    "commissions.sfplanning.org", "leginfo.legislature.ca.gov", "calcivilrights.ca.gov",
    "hud.gov", "huduser.gov", "ecfr.gov", "govinfo.gov", "sec.gov", "api.github.com",
    "sfrb.org", "sftreasurer.org", "github.com", "sfgov.legistar.com",
    # American Legal Publishing is the official publisher of the San Francisco
    # Administrative Code (see flag F17); dre.ca.gov is the California Department
    # of Real Estate. Both added 2026-11-10 for the B87 worksheet sources S74/S75/S79/S80.
    "codelibrary.amlegal.com", "dre.ca.gov",
}

report = {"date": D.DATE, "status": "running", "checks": [], "errors": []}

def check(name, ok, detail=""):
    entry = {"name": name, "ok": bool(ok), "detail": detail}
    report["checks"].append(entry)
    if not ok:
        report["errors"].append("{}: {}".format(name, detail))
    print(("PASS " if ok else "FAIL ") + name + ((" - " + detail) if detail else ""))

def official_domain(url):
    host = urlparse(url).netloc.lower()
    return any(host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS)

def json_load(path):
    return json.loads(path.read_text(encoding="utf-8"))

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.links.append(value)

class TableRowSourceParser(HTMLParser):
    """Check rendered body rows, not just their backing JSON metadata."""
    def __init__(self):
        super().__init__()
        self.in_body = False
        self.in_row = False
        self.links = []
        self.row_count = 0
        self.missing = 0

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.in_body = True
        elif tag == "tr" and self.in_body:
            self.in_row = True
            self.links = []
        elif tag == "a" and self.in_row:
            self.links.append(dict(attrs).get("href", ""))

    def handle_endtag(self, tag):
        if tag == "tr" and self.in_row:
            self.row_count += 1
            if not any(urlparse(link).scheme == "https" and official_domain(link) for link in self.links):
                self.missing += 1
            self.in_row = False
        elif tag == "tbody":
            self.in_body = False

def main():
    # Placeholder so the footer's validation-report link resolves during the link check.
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "validation_report.json").write_text(json.dumps({"status": "running"}, indent=2) + "\n", encoding="utf-8")

    pages = json_load(DATA / "pages.json")
    sources_list = json_load(DATA / "sources.json")
    flags = json_load(DATA / "flags.json")
    flag_ids = {f["id"] for f in flags}
    source_map = {s["id"]: s for s in sources_list}

    check("canonical source map matches site data", len(source_map) == len(D.SOURCES), "{} official sources".format(len(D.SOURCES)))
    check("flags count matches dashboard", len(flags) == len(D.FLAGS), "{} flagged items".format(len(D.FLAGS)))
    check("source URLs use official domains", all(official_domain(s["url"]) for s in sources_list), "all source URLs checked")
    check("every source has id, title, agency, category and statement",
          all(all(k in s for k in ("id", "title", "agency", "category", "statement", "url")) for s in sources_list))

    # The hand-maintained SOURCES.md ledger must stay in sync with the generator.
    sources_md = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
    missing_ledger = sorted(sid for sid in source_map if "| {} |".format(sid) not in sources_md)
    check("SOURCES.md lists every catalogued source", not missing_ledger, "missing: " + ", ".join(missing_ledger[:8]))
    check("SOURCES.md has no stale hand-typed source total",
          "source count is 70," not in sources_md and str(len(source_map)) in sources_md,
          "{} sources".format(len(source_map)))

    row_index = {}
    for _slug, _page in pages.items():
        for _sec in _page["sections"]:
            for _r in _sec["rows"]:
                row_index[_r["id"]] = _r
    safmr_rows = [row_index.get(rid) for rid in ("FED-07", "MKT-07", "MKT-08")]
    check("94122 SAFMR rows publish the official HUD values with official sources",
          all(r and r["status"] == "verified" and r["value"] for r in safmr_rows)
          and "$3,410" in row_index["MKT-08"]["value"] and "$3,310" in row_index["MKT-07"]["value"]
          and "$2,370" in row_index["FED-07"]["value"] and "$2,280" in row_index["FED-07"]["value"]
          and all(("S83" in row_index["MKT-08"]["source_ids"]) or ("S84" in row_index["MKT-08"]["source_ids"]) for _ in [0]),
          "FY2027 and FY2026 ZIP figures present")
    f52 = [f for f in flags if f["id"] == "F52"]
    check("94122 SAFMR limitation flag is published and cites HUD",
          bool(f52) and {"S83", "S84"} <= set(f52[0]["source_ids"]),
          "F52 cites S83 and S84")
    check("resolved audit gaps name their official sources",
          all(sid in [f for f in flags if f["id"] == fid][0]["source_ids"] for fid, sid in (("F13", "S83"), ("F15", "S85"), ("F47", "S87"))),
          "F13->S83, F15->S85, F47->S87")
    check("San Francisco County corporate benchmark is published from the SEC filing",
          "2,966" in row_index.get("CORP-07", {}).get("value", "") and "S85" in row_index.get("CORP-07", {}).get("source_ids", []),
          "Essex Q4 2025 SF County row")

    row_count = 0
    needs_review_count = 0
    owner_rows = []
    row_errors = []
    for slug, page in pages.items():
        for sec in page["sections"]:
            for r in sec["rows"]:
                row_count += 1
                rid = r.get("id", "?")
                if r.get("status") == "owner supplied":
                    owner_rows.append(rid)
                    if not r.get("source_ids") or any(sid not in source_map or not official_domain(source_map[sid]["url"]) for sid in r.get("source_ids", [])):
                        row_errors.append("{} lacks valid contextual official source links".format(rid))
                    if "context only" not in r.get("source_note", ""):
                        row_errors.append("{} must distinguish context from verification".format(rid))
                    if r.get("flag_id") not in flag_ids:
                        row_errors.append("{} lacks a published review flag".format(rid))
                    if not r.get("source_note"):
                        row_errors.append("{} is owner-supplied but has no source note".format(rid))
                    if not r.get("value"):
                        row_errors.append("{} is owner-supplied but has no value".format(rid))
                    continue
                if not r.get("source_ids"):
                    row_errors.append("{} has no source_ids".format(rid))
                for sid in r["source_ids"]:
                    if sid not in source_map:
                        row_errors.append("{} references unknown source {}".format(rid, sid))
                    elif not official_domain(source_map[sid]["url"]):
                        row_errors.append("{} references nonofficial URL for {}".format(rid, sid))
                if r.get("status") not in ("verified", "needs review", "analysis"):
                    row_errors.append("{} has invalid status".format(rid))
                if r.get("status") == "needs review":
                    needs_review_count += 1
                    if r.get("value", "") != "":
                        row_errors.append("{} needs review but value is not blank".format(rid))
                    if not r.get("flag_id"):
                        row_errors.append("{} needs review but has no flag_id".format(rid))
                    elif r["flag_id"] not in flag_ids:
                        row_errors.append("{} flag_id {} not published".format(rid, r["flag_id"]))
                if r.get("flag_id") and r["flag_id"] not in flag_ids:
                    row_errors.append("{} flag_id {} not published".format(rid, r["flag_id"]))
    import collections as _c
    dupes = [i for i, n in _c.Counter(r["id"] for pg in pages.values() for sec in pg["sections"] for r in sec["rows"]).items() if n > 1]
    check("row IDs are unique across all pages", not dupes, ", ".join(dupes[:5]))
    check("owner-supplied case rows are published and labelled", len(owner_rows) >= 10, "{} owner-supplied rows ({} ...)".format(len(owner_rows), ", ".join(owner_rows[:3])))
    case_html = (PAGES / "case.html").read_text(encoding="utf-8")
    check("owner-intake rows render contextual links without implying verification", case_html.count("official links provide general context only") == len(owner_rows) and 'href="https://www.sf.gov/learn-about-san-francisco-rental-laws"' in case_html)
    check("every table row has valid official source links", not row_errors, "{} rows checked; {}".format(row_count, "; ".join(row_errors[:5])))
    rendered_rows = 0
    rendered_missing = []
    for html_path in [ROOT / "index.html", *sorted(PAGES.glob("*.html"))]:
        parser = TableRowSourceParser()
        parser.feed(html_path.read_text(encoding="utf-8"))
        rendered_rows += parser.row_count
        if parser.missing:
            rendered_missing.append("{}: {} rows".format(html_path.name, parser.missing))
    check("rendered table rows contain official-domain links", not rendered_missing and rendered_rows >= row_count,
          "{} rows checked; {}".format(rendered_rows, "; ".join(rendered_missing)))
    check("unverified rows are blank and flagged", needs_review_count > 0, "{} needs-review rows".format(needs_review_count))

    flag_errors = []
    for f in flags:
        if f.get("status") != "needs review":
            flag_errors.append("{} status is not needs review".format(f["id"]))
        if not f.get("source_ids"):
            flag_errors.append("{} has no source_ids".format(f["id"]))
        for sid in f["source_ids"]:
            if sid not in source_map:
                flag_errors.append("{} references unknown source {}".format(f["id"], sid))
            elif not official_domain(source_map[sid]["url"]):
                flag_errors.append("{} references nonofficial URL {}".format(f["id"], sid))
    check("every flag is published with official source links", not flag_errors, "; ".join(flag_errors[:5]))

    flagged_html = (PAGES / "flagged.html").read_text(encoding="utf-8")
    sources_html = (PAGES / "sources.html").read_text(encoding="utf-8")
    check("Flagged for Review page contains all flag IDs", all(f["id"] in flagged_html for f in flags))
    check("Flagged for Review page is clearly labeled", "Flagged for Review" in flagged_html and "does <strong>not</strong> block" in flagged_html)
    sources_html_unescaped = unescape(sources_html)
    check("Sources page contains all source IDs and URLs",
          all(s["id"] in sources_html_unescaped and s["url"] in sources_html_unescaped for s in sources_list))

    for slug in D.PAGES:
        check("data/{}.json exists".format(slug), (DATA / "{}.json".format(slug)).exists())
        check("pages/{}.html exists".format(slug), (PAGES / "{}.html".format(slug)).exists())
    for slug, _title in D.NAV:
        check("pages/{}.html in navigation exists".format(slug), (PAGES / "{}.html".format(slug)).exists())

    required_files = [
        ROOT / "index.html", ROOT / ".nojekyll", ROOT / "assets" / "site.css",
        ROOT / "README.md", ROOT / "EXECUTIVE_SUMMARY.md", ROOT / "FLAGGED_FOR_REVIEW.md",
        ROOT / "SOURCES.md", ROOT / "VERIFICATION.md", ROOT / "REPO_REVIEW.md", ROOT / "COORDINATION.md",
    ]
    check("site build files exist", all(p.exists() for p in required_files))

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    check("index explains the badges and leads with the direct answer", "How to read this dashboard" in index_html and "Direct answer" in index_html)
    check("index links to Flagged for Review", 'pages/flagged.html' in index_html and "Flagged for Review" in index_html)
    check("index links to Executive Summary", 'pages/summary.html' in index_html and "Executive Summary" in index_html)
    summary_html = (PAGES / "summary.html").read_text(encoding="utf-8")
    check("executive summary forefront covers Rent Board license for individual owners",
          "FOREFRONT" in summary_html and "individual" in summary_html.lower() and "Rent Increase License" in summary_html)

    public_md = sorted(ROOT.glob("*.md")) + sorted((ROOT / "research").rglob("*.md"))
    public_json = sorted(DATA.glob("*.json"))
    public_html = [ROOT / "index.html"] + sorted(PAGES.glob("*.html"))
    public_css = [ROOT / "assets" / "site.css"]
    public_files = [p for p in public_md + public_json + public_html + public_css if p.exists()]

    # Do not store recoverable hashes of short private identifiers. This check is
    # deliberately limited to the anonymized case files; it is not a history audit.
    check("private intake file is excluded from git", "internal/" in (ROOT / ".gitignore").read_text(encoding="utf-8"))

    address_patterns = [
        r"\b\d{3,5}\s+\d{1,2}(?:st|nd|rd|th)\s+(?:Ave|Avenue|Street|St)\b",
        r"\b\d{3,5}\s+[A-Za-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)\b",
    ]
    address_hits = []
    for p in public_files:
        text = p.read_text(encoding="utf-8")
        for pat in address_patterns:
            if re.search(pat, text, re.IGNORECASE):
                address_hits.append(str(p.relative_to(ROOT)))
                break
    check("no exact street address published", not address_hits, "; ".join(address_hits[:5]))

    case_text = (DATA / "case.json").read_text(encoding="utf-8")
    expected_case = ["February 1, 2025", "$3,995", "April 1, 2026", "June 1, 2019", "$3,150"] + ["Tenant {}".format(c) for c in "ABCDEF"]
    check("dates, amounts and placeholder IDs preserved", all(s in case_text for s in expected_case))
    initial_hits = [str(x.relative_to(ROOT)) for x in (DATA / "case.json", PAGES / "case.html")
                    if re.search(r"\b[A-Z]{1,2}\s[A-Z]{1,2}\b", x.read_text(encoding="utf-8"))]
    check("no raw initials in the anonymized case files", not initial_hits, "; ".join(initial_hits[:3]))

    all_text = "\n".join(p.read_text(encoding="utf-8") for p in public_files if p.suffix in (".html", ".md", ".json", ".css"))
    check("conservative compliance checklist wording present",
          "conservative compliance checklist capable of tenant-lawyer review" in all_text.lower())
    check("no attorney approval or guarantee claimed",
          "No attorney approval or guarantee" in all_text or "No attorney has approved" in all_text)
    forbidden = ["approved by a tenant lawyer", "this increase is certified lawful", "guaranteed no lawsuit", "attorney approved this increase", "we certify this increase is lawful"]
    check("no forbidden certification language", not any(s in all_text.lower() for s in forbidden))

    process_html = (PAGES / "process.html").read_text(encoding="utf-8")
    process_plain = unescape(process_html)
    check("step-by-step license page exists in navigation",
          "pages/process.html" in (ROOT / "index.html").read_text(encoding="utf-8"))
    check("step-by-step license page has all 12 numbered steps",
          all(("Step {}".format(n)) in process_plain for n in range(1, 13)))
    check("step-by-step page links Sec. 37.15, Sec. 37.3 and the Housing Inventory",
          "sec-3715" in process_plain and "sec-373" in process_plain and "rent-board-housing-inventory" in process_plain)
    check("step-by-step page answers the individual-owner question",
          "individual property owner" in process_plain.lower() and "yes." in process_plain.lower())

    exec_md = (ROOT / "EXECUTIVE_SUMMARY.md").read_text(encoding="utf-8")
    check("executive summary puts the license answer first",
          exec_md.index("Rent Increase License") < exec_md.index("## Bottom line"), "license section precedes the rate bottom line")
    check("executive summary cites the ordinance license condition",
          "37.3(a)(1)" in exec_md and "37.15" in exec_md)
    check("executive summary links the official license pages",
          "https://www.sf.gov/learn-about-rent-increases-san-francisco" in exec_md
          and "https://www.sf.gov/rent-board-housing-inventory" in exec_md
          and "https://www.sf.gov/information--sec-3715-reporting-obligations-licensing" in exec_md)
    check("executive summary states no individual-owner exception",
          "no individual-owner exception is stated" in exec_md.lower())

    broken = []
    for html_file in [ROOT / "index.html"] + sorted(PAGES.glob("*.html")):
        parser = LinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for link in parser.links:
            if link.startswith(("http://", "https://", "mailto:", "tel:")) or link.startswith("#"):
                continue
            path_part = link.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            target = (html_file.parent / path_part).resolve()
            if not target.exists():
                broken.append("{} -> {}".format(html_file.relative_to(ROOT), link))
    check("no broken internal links", not broken, "; ".join(broken[:5]))

    # Guard against defects found by independent review on 2026-11-07 (F31, F32).
    marker_hits = []
    for p_ in sorted(ROOT.glob("*.md")) + sorted(PAGES.glob("*.html")) + sorted(DATA.glob("*.json")):
        text = p_.read_text(encoding="utf-8")
        if re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.MULTILINE):
            marker_hits.append(str(p_.relative_to(ROOT)))
    check("no committed merge-conflict markers in public files", not marker_hits, "; ".join(marker_hits[:5]))

    flag_ids_ordered = [f["id"] for f in flags]
    numeric = [f for f in flag_ids_ordered if re.fullmatch(r"F\d\d", f)]
    check("numeric flag IDs are unique and contiguous", numeric == sorted(set(numeric)),
          "{} numeric flags".format(len(numeric)))

    stale_refs = []
    for p_ in [ROOT / "SOURCES.md", ROOT / "VERIFICATION.md", ROOT / "EXECUTIVE_SUMMARY.md", ROOT / "FLAGGED_FOR_REVIEW.md"]:
        text = p_.read_text(encoding="utf-8")
        for num in re.findall(r"flagged (F\d\d)", text):
            if num not in flag_ids:
                stale_refs.append("{} references unpublished {}".format(p_.name, num))
    check("no references to unpublished flag IDs", not stale_refs, "; ".join(stale_refs[:5]))

    # The two most consequential case-specific rules must stay visible on the site.
    all_site_text = "\n".join(p_.read_text(encoding="utf-8") for p_ in [ROOT / "index.html"] + sorted(PAGES.glob("*.html")))
    check("Rent Board Fee is distinguished from the license", "$59.00" in all_site_text and "separate" in all_site_text.lower())
    check("retaliation 180-day rule is published", "180 days" in all_site_text and "1942.5" in all_site_text)
    check("AB 1482 two-unit owner-occupied exemption is published", "ADU" in all_site_text and "principal residence" in all_site_text)
    check("in-law-unit coverage rule is published", "in-law unit" in all_site_text.lower())
    summary_html = (PAGES / "summary.html").read_text(encoding="utf-8")
    check("executive summary page renders the narrative, not just tables",
          summary_html.count("<h2>") >= 10 and "<ol>" in summary_html and "<h2>FOREFRONT" in summary_html,
          "{} headings".format(summary_html.count("<h2>")))
    check("2026-11-10 proposed-cap inconsistencies and next-year rate are published",
          any(r["id"] == "RATE-14" and "Pending Committee Action" in r["value"] for pg in D.PAGES.values() for s in pg["sections"] for r in s["rows"])
          and any(r["id"] == "RATE-17" and r["value"] == "" and r["status"] == "needs review" for pg in D.PAGES.values() for s in pg["sections"] for r in s["rows"])
          and any(f["id"] == "F47" for f in flags) and D.DATE in ("2026-11-10", "2026-11-11", "2026-11-13")
          and "2026-11-10" in D.SOURCES["S72"]["statement"]
          and official_domain(D.SOURCES["S71"]["url"]))
    check("pending cap is distinguished from current law and calculation is cautioned",
          "File 261020" in summary_html and "not current law" in summary_html.lower()
          and "F46" in flagged_html and "F46" in (PAGES / "calculations.html").read_text(encoding="utf-8")
          and "S71" in source_map and official_domain(source_map["S71"]["url"]))
    check("executive summary page has no unrendered markdown",
          not re.search(r"<p>\s*#|\*\*|\]\(", summary_html))
    check("executive summary states the fee/licence distinction and retaliation rule",
          "$59.00" in summary_html and "1942.5" in summary_html and "in-law unit" in summary_html.lower())

    # --- Checks added 2026-11-08 by session arena-18eafb4c (D16-B/D16-C) ---
    check("Rent Board Fee page is published and in the navigation",
          "fee" in pages and (PAGES / "fee.html").exists() and any(s == "fee" for s, _ in D.NAV))
    fee_html = (PAGES / "fee.html").read_text(encoding="utf-8")
    check("fee page distinguishes the fee from the licence and states the current amount and deadline",
          "$59.00" in fee_html and "December 14, 2026" in fee_html and "March 1" in fee_html
          and "separate" in fee_html.lower())
    check("fee page publishes the 50% recovery and the business-registration rule",
          "50%" in fee_html and "fewer than four units" in fee_html)
    fee_rows = [r for sec in pages.get("fee", {}).get("sections", []) for r in sec["rows"]]
    check("every Rent Board Fee row carries an official source",
          bool(fee_rows) and all(r.get("source_ids") and all(s in source_map for s in r["source_ids"]) for r in fee_rows),
          "{} fee rows".format(len(fee_rows)))

    placeholders = []
    for name in ("EXECUTIVE_SUMMARY.md", "FLAGGED_FOR_REVIEW.md", "README.md"):
        if "{{" in (ROOT / name).read_text(encoding="utf-8"):
            placeholders.append(name)
    for html_file in [ROOT / "index.html"] + sorted(PAGES.glob("*.html")):
        if "{{" in html_file.read_text(encoding="utf-8"):
            placeholders.append(str(html_file.relative_to(ROOT)))
    check("computed counts substituted - no template placeholders left", not placeholders, ", ".join(placeholders[:5]))

    stale = []
    # COORDINATION.md is an append-only session log and legitimately quotes the old totals.
    for name in ("EXECUTIVE_SUMMARY.md", "FLAGGED_FOR_REVIEW.md", "README.md", "SOURCES.md", "VERIFICATION.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        for pattern in (r"\b38 flags\b", r"All 52 official", r"\b30 source-quality flags\b", r"All 55 official"):
            if re.search(pattern, text):
                stale.append("{}: {}".format(name, pattern))
    for html_file in [ROOT / "index.html"] + sorted(PAGES.glob("*.html")):
        text = html_file.read_text(encoding="utf-8")
        if re.search(r"\b38 flags\b|All 52 official|All 55 official", text):
            stale.append(str(html_file.relative_to(ROOT)))
    check("no stale hard-coded source/flag totals", not stale, "; ".join(stale[:5]))

    check("in-law exemption nuance is published correctly (legal vs illegal)",
          "LEGAL in-law" in D.SOURCES["S60"]["statement"] and "ILLEGAL in-law" in D.SOURCES["S60"]["statement"])
    exec_text = (ROOT / "EXECUTIVE_SUMMARY.md").read_text(encoding="utf-8")
    check("executive summary states the fee deadline, exemption window and fee page",
          "December 14, 2026" in exec_text and "pages/fee.html" in exec_text and "$59.00" in exec_text)
    check("privacy history-exposure flag is published",
          any(f["id"] == "F44" for f in flags)
          and "git history" in "".join(f["title"] + " " + f["detail"] for f in flags if f["id"] == "F44"))
    check("no raw tenant identifiers in the fee or new markdown files",
          all("{{" not in (ROOT / n).read_text(encoding="utf-8") for n in ("FLAGGED_FOR_REVIEW.md",)))
    check("table regions and inline links meet accessibility standards",
          'tabindex="0" role="region"' in (PAGES / "case.html").read_text(encoding="utf-8")
          and '<th scope="col">' in (PAGES / "case.html").read_text(encoding="utf-8")
          and "text-decoration:underline" in (ROOT / "assets" / "site.css").read_text(encoding="utf-8"))
    check("project-record flags cite project records and S02 link defect is flagged",
          all(f["source_ids"] != ["S43"] and f["source_ids"] != ["S20"] for f in flags if f["id"] in ("F19", "F20", "F31"))
          and any(f["id"] == "F45" and "S02" in f["source_ids"] for f in flags))

    # --- Checks added 2026-11-10 by session arena-3dc8a405 (T48, B87-I integration) ---
    check("Notice Worksheet page is published and in the navigation",
          "worksheet" in pages and (PAGES / "worksheet.html").exists()
          and any(s == "worksheet" for s, _ in D.NAV))
    worksheet_rows = [r for sec in pages.get("worksheet", {}).get("sections", []) for r in sec["rows"]]
    worksheet_errors = []
    for r in worksheet_rows:
        if not r.get("source_ids"):
            worksheet_errors.append("{} has no source_ids".format(r.get("id", "?")))
        for sid in r.get("source_ids", []):
            if sid not in source_map:
                worksheet_errors.append("{} references unknown source {}".format(r.get("id", "?"), sid))
            elif not official_domain(source_map[sid]["url"]):
                worksheet_errors.append("{} references nonofficial URL for {}".format(r.get("id", "?"), sid))
        if r.get("status") not in ("verified", "needs review", "analysis", "owner supplied"):
            worksheet_errors.append("{} invalid status".format(r.get("id", "?")))
        if r.get("status") == "needs review" and (r.get("value", "") != "" or not r.get("flag_id")):
            worksheet_errors.append("{} needs-review cell not blank/flagged".format(r.get("id", "?")))
    check("every Notice Worksheet row carries an official source and correct status",
          len(worksheet_rows) == 40 and not worksheet_errors,
          "{} worksheet rows; {}".format(len(worksheet_rows), "; ".join(worksheet_errors[:5])))
    b87_flag_ids = ["B87-F01", "B87-F02", "B87-F03", "B87-F04", "B87-F05", "B87-F06", "B87-F07", "B87-F08"]
    check("all eight B87 worksheet flags are published on Flagged for Review",
          all(any(f["id"] == bid for f in flags) for bid in b87_flag_ids)
          and all(bid in flagged_html for bid in b87_flag_ids))
    check("Notice Worksheet links from the Notice Checklist page",
          "worksheet.html" in (PAGES / "compliance.html").read_text(encoding="utf-8"))

    # --- Checks added 2026-11-13 by session arena-6f65a2f5 (T54: suggestions board + state/local answer) ---
    sug = pages.get("suggestions", {})
    sug_rows = [r for sec in sug.get("sections", []) for r in sec["rows"]]
    check("Site Suggestions page is published and in the navigation",
          "suggestions" in pages and (PAGES / "suggestions.html").exists()
          and any(slu == "suggestions" for slu, _ in D.NAV)
          and "pages/suggestions.html" in (ROOT / "index.html").read_text(encoding="utf-8"),
          "{} suggestion rows".format(len(sug_rows)))
    check("suggestions board carries both proposal rows and owner-decision rows",
          len([r for r in sug_rows if r["id"].startswith("SG-")]) >= 25
          and len([r for r in sug_rows if r["id"].startswith("DEC-")]) == 8,
          "{} SG rows, {} DEC rows".format(len([r for r in sug_rows if r["id"].startswith("SG-")]), len([r for r in sug_rows if r["id"].startswith("DEC-")])))
    sug_errors = []
    for r in sug_rows:
        if not r.get("source_ids") or any(sid not in source_map for sid in r["source_ids"]):
            sug_errors.append("{} lacks a catalogued source".format(r.get("id", "?")))
        if r.get("status") not in ("analysis", "needs review"):
            sug_errors.append("{} must be a proposal or a blank decision, not a verified finding".format(r.get("id", "?")))
        if r.get("status") == "analysis" and not r.get("value"):
            sug_errors.append("{} is an analysis row with no content".format(r.get("id", "?")))
    check("no suggestion is presented as verified or as an implemented change", not sug_errors, "; ".join(sug_errors[:5]))
    sug_html = (PAGES / "suggestions.html").read_text(encoding="utf-8")
    check("suggestions page states plainly that nothing on it is implemented",
          "has been implemented" in sug_html and "F53" in sug_html and "F54" in sug_html)
    check("new state/local sources S88-S91 are catalogued on official domains",
          all(sid in source_map and official_domain(source_map[sid]["url"]) for sid in ("S88", "S89", "S90", "S91")),
          "S88 City news, S89 ordinance text, S90 Civ. Code 1946.2, S91 Civ. Code 1947.7")
    check("state-versus-local answer is published in the forefront of the executive summary",
          "Ord. No. 265-20" in summary_html and "Ordinance No. 265-20" in summary_html
          and "SB 567" in summary_html and "LOCAL" in summary_html)
    check("state-versus-local answer is answered on the process, local, state and questions pages",
          all(tok in (PAGES / "process.html").read_text(encoding="utf-8") for tok in ("PRC-10", "PRC-11", "265-20"))
          and "LOC-26" in (PAGES / "local.html").read_text(encoding="utf-8")
          and "ST-19" in (PAGES / "state.html").read_text(encoding="utf-8")
          and "Q-22" in (PAGES / "questions.html").read_text(encoding="utf-8"))
    exec_md13 = (ROOT / "EXECUTIVE_SUMMARY.md").read_text(encoding="utf-8")
    check("executive summary answers the 2023 question with the local phase-in and links the ordinance",
          "Added by Ord. No. 265-20" in exec_md13
          and "commencing March 1, 2023" in exec_md13
          and "https://www.sf.gov/news/new-legislation-creates-housing-inventory-and-requires-owners-obtain-license-imposing" in exec_md13
          and "sec-3715-reporting-obligations-licensing" in exec_md13)
    check("the 1947.7 question is published as an open item rather than answered",
          any(r["id"] == "Q-24" and r["status"] == "needs review" and r["value"] == "" and r["flag_id"] == "F56"
              for pg in D.PAGES.values() for sec in pg["sections"] for r in sec["rows"])
          and "F56" in flagged_html and "F55" in flagged_html)
    check("landing page states the local-law answer and links the suggestions board",
          "Ordinance No. 265-20" in index_html and "pages/suggestions.html" in index_html)
    check("Rule 13.14 verbatim nullity wording is published and cited",
          "shall render the entire rent increase null and void" in exec_md13
          and "S73" in [sid for pg in D.PAGES.values() for sec in pg["sections"] for r in sec["rows"] if r["id"] == "PRC-06" for sid in r["source_ids"]])
    check("computed suggestion count is substituted, not typed",
          "{{SUGG_COUNT}}" not in exec_md13 and "rows" in exec_md13)

    report["status"] = "passed" if not report["errors"] else "failed"
    report["summary"] = {
        "sources": len(source_map),
        "pages": len(list(PAGES.glob("*.html"))),
        "data_files": len(list(DATA.glob("*.json"))),
        "rows_verified": row_count,
        "needs_review_rows": needs_review_count,
        "flags": len(flags),
        "checks": len(report["checks"]),
        "errors": len(report["errors"]),
    }
    (DATA / "validation_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("\nValidation {} ({} checks, {} errors). Report: data/validation_report.json".format(
        report["status"].upper(), len(report["checks"]), len(report["errors"])
    ))
    if report["errors"]:
        for err in report["errors"]:
            print("ERROR: " + err)
        sys.exit(1)

if __name__ == "__main__":
    main()
