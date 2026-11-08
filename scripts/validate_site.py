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

PROJECT_DOMAINS = {"github.com", "kanlerxz87-cyber.github.io"}

OFFICIAL_DOMAINS = {
    "sf.gov", "media.api.sf.gov", "sfplanninggis.org", "default.sfplanning.org",
    "commissions.sfplanning.org", "leginfo.legislature.ca.gov", "calcivilrights.ca.gov",
    "hud.gov", "huduser.gov", "ecfr.gov", "govinfo.gov", "sec.gov", "api.github.com",
    "sfrb.org",
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

def project_domain(url):
    host = urlparse(url).netloc.lower()
    return any(host == d or host.endswith("." + d) for d in PROJECT_DOMAINS)

def source_kind(src):
    return src.get("kind", "official")

def source_url_ok(src):
    return project_domain(src["url"]) if source_kind(src) == "project" else official_domain(src["url"])

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
    check("source URLs use official or project-record domains", all(source_url_ok(s) for s in sources_list),
          "{} official sources, {} project records".format(
              sum(1 for s in sources_list if source_kind(s) == "official"),
              sum(1 for s in sources_list if source_kind(s) == "project")))
    check("every source has id, title, agency, category and statement",
          all(all(k in s for k in ("id", "title", "agency", "category", "statement", "url")) for s in sources_list))

    row_count = 0
    needs_review_count = 0
    owner_rows = []
    project_rows = []
    row_errors = []
    for slug, page in pages.items():
        for sec in page["sections"]:
            for r in sec["rows"]:
                row_count += 1
                rid = r.get("id", "?")
                if r.get("status") == "owner supplied":
                    owner_rows.append(rid)
                    if r.get("source_ids"):
                        row_errors.append("{} is owner-supplied but carries official source_ids".format(rid))
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
                    elif not source_url_ok(source_map[sid]):
                        row_errors.append("{} references a URL outside its source class for {}".format(rid, sid))
                if r.get("status") == "project record":
                    project_rows.append(rid)
                    if not r.get("value"):
                        row_errors.append("{} is a project record but has no value".format(rid))
                    for sid in r["source_ids"]:
                        if sid in source_map and source_kind(source_map[sid]) != "project":
                            row_errors.append("{} is a project record but cites official source {}".format(rid, sid))
                    continue
                for sid in r["source_ids"]:
                    if sid in source_map and source_kind(source_map[sid]) == "project" and r.get("status") != "needs review":
                        row_errors.append("{} cites a project record but its status is {}".format(rid, r.get("status")))
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
    row_errors = list(dict.fromkeys(row_errors))
    check("every table row has a valid official or project-record source link", not row_errors,
          "{} rows checked, {} project records; {}".format(row_count, len(project_rows), "; ".join(row_errors[:5])))
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
            elif not source_url_ok(source_map[sid]):
                flag_errors.append("{} references a URL outside its source class for {}".format(f["id"], sid))
    check("every flag is published with a valid official or project-record link", not flag_errors, "; ".join(flag_errors[:5]))

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

    # One-way fingerprints keep the privacy regression test portable without
    # committing private intake or printing identifiers in public reports.
    import hashlib
    private_fingerprints = ['27c9478468718ed43669f8b2bbac3694d1f03287a6347d4c9adadc9d12f9ecf5', '158dc33a8be8ae49804b3fa72e2e116edb683730b51752bdb552435f31f0ba5a', '569ec6135d377e8ac326be2be2fd4cd8f3538fc3c23f33a89e81a4ed83671b7e', '399ad8e221e6815cd19b54cd7f313335f9bab0ecc681615af552c64ea3901b0f', '01efd0141d7d80509ee44bbbb2dee48875711d55358bd9a91bf22d5208ffa93d', '0b28c4215599de9c8f7019402d7eaeccc8cbdc5103aeca7427774222c2bf2f16']
    check("private intake file is excluded from git", "internal/" in (ROOT / ".gitignore").read_text(encoding="utf-8"))
    privacy_hits = []
    for p in public_files:
        text = p.read_text(encoding="utf-8")
        candidates = re.findall(r"(?<![A-Za-z])[A-Z]\s+[A-Z](?![A-Za-z])|(?<![A-Za-z])[A-Z]{2}(?![A-Za-z])", text)
        for candidate in candidates:
            normalized = " ".join(candidate.split())
            if hashlib.sha256(normalized.encode()).hexdigest() in private_fingerprints:
                privacy_hits.append(str(p.relative_to(ROOT)))
    check("privacy fingerprint baseline present", len(private_fingerprints) == 6, "6 one-way fingerprints; no private intake required")
    check("no raw tenant identifiers in public files", not privacy_hits, "; ".join(privacy_hits[:5]))

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

    # Counts must be generated from the data, not typed in (F36).
    req_json = json_load(DATA / "requirements.json")
    req_rows = {r["id"]: r for sec in req_json["sections"] for r in sec["rows"]}
    expected_inventory = "{} flagged items published: {} numeric flags F01-F{} plus {} case/analysis flags T03-F01-T03-F10".format(
        len(D.FLAGS),
        len([f for f in D.FLAGS if f["id"].startswith("F") and f["id"][1:].isdigit()]),
        [f["id"] for f in D.FLAGS if f["id"].startswith("F") and f["id"][1:].isdigit()][-1][1:],
        len([f for f in D.FLAGS if f["id"].startswith("T03")]))
    check("flag inventory count in the requirements table is generated from the data",
          req_rows.get("REQ-08", {}).get("value") == expected_inventory, req_rows.get("REQ-08", {}).get("value", ""))
    check("Sources page counts are generated from the data",
          "Official sources ({} entries)".format(len(D.OFFICIAL_SOURCES)) in sources_html
          and "Project records ({} entries)".format(len(D.PROJECT_SOURCES)) in sources_html)
    check("Flagged page count is generated from the data",
          "All {} flagged items".format(len(D.FLAGS)) in flagged_html)
    check("AN-15 flag count is generated from the data",
          "{} flagged items".format(len(D.FLAGS)) in req_rows.get("AN-15", {}) or "{} flagged items".format(len(D.FLAGS)) in "".join(
              r.get("value", "") for sec in json_load(DATA / "analysis.json")["sections"] for r in sec["rows"] if r["id"] == "AN-15"))

    check("project records are labelled separately on the Sources page",
          "Project records" in sources_html_unescaped and "P01" in sources_html_unescaped and "P02" in sources_html_unescaped)
    project_sourced_rows = [r["id"] for pg in pages.values() for sec in pg["sections"] for r in sec["rows"]
                            if r.get("status") == "project record" and not all(source_kind(source_map[s]) == "project" for s in r["source_ids"] if s in source_map)]
    check("project-record rows cite only project records", not project_sourced_rows, ", ".join(project_sourced_rows[:5]))
    check("every project record is used by at least one row or flag",
          all(any(sid in r["source_ids"] for pg in pages.values() for sec in pg["sections"] for r in sec["rows"])
              or any(sid in f["source_ids"] for f in flags)
              for sid in D.PROJECT_SOURCES),
          ", ".join(sorted(D.PROJECT_SOURCES)))

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

    # Fragment links must land on a real id.
    id_map = {}
    html_files = [ROOT / "index.html"] + sorted(PAGES.glob("*.html"))
    for f_ in html_files:
        id_map[f_.resolve()] = set(re.findall(r'id="([^"]+)"', f_.read_text(encoding="utf-8")))
    bad_fragments = []
    for f_ in html_files:
        for href in re.findall(r'href="([^"]+)"', f_.read_text(encoding="utf-8")):
            if href.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            path_part, _, frag = href.partition("#")
            if not frag:
                continue
            target = (f_.parent / path_part).resolve() if path_part else f_.resolve()
            if target in id_map and frag not in id_map[target]:
                bad_fragments.append("{} -> {}".format(f_.relative_to(ROOT), href))
    check("no broken internal anchors", not bad_fragments, "; ".join(bad_fragments[:5]))

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
    check("executive summary page has no unrendered markdown",
          not re.search(r"<p>\s*#|\*\*|\]\(", summary_html))
    check("executive summary states the fee/licence distinction and retaliation rule",
          "$59.00" in summary_html and "1942.5" in summary_html and "in-law unit" in summary_html.lower())

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
