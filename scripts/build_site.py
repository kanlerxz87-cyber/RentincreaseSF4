"""Build the static GitHub Pages site from canonical site_data.

Run: python3 scripts/build_site.py
Generates data/*.json, index.html, pages/*.html, assets/site.css, .nojekyll,
README.md, EXECUTIVE_SUMMARY.md and FLAGGED_FOR_REVIEW.md.
"""

import json
import re
from html import escape
from pathlib import Path
import site_data as D

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PAGES = ROOT / "pages"
ASSETS = ROOT / "assets"

def e(value):
    return escape(str(value), quote=True)

def source_links(ids):
    parts = []
    for sid in ids:
        src = D.SOURCES.get(sid)
        if not src:
            continue
        parts.append(
            '<a href="{}" target="_blank" rel="noopener" title="{}">{}</a>'.format(
                e(src["url"]), e(src["title"]), e(sid)
            )
        )
    return '<span class="src">' + " ".join(parts) + "</span>"

def badge(status):
    if status == "owner supplied":
        return '<span class="badge owner">owner-supplied</span>'
    cls = {"verified": "verified", "needs review": "review", "analysis": "analysis"}.get(status, "analysis")
    label = {"verified": "verified", "needs review": "needs review", "analysis": "analysis"}.get(status, status)
    return '<span class="badge {}">{}</span>'.format(cls, e(label))

def flag_link(flag_id, in_pages):
    if not flag_id:
        return ""
    href = "flagged.html#{}".format(e(flag_id)) if in_pages else "pages/flagged.html#{}".format(e(flag_id))
    return '<a class="flaglink" href="{}">{}</a>'.format(href, e(flag_id))


def render_suggestion_table(section, in_pages=True):
    """Render the Suggestions page: ID, Suggestion, Why, Sources, Effort, Review status."""
    out = ['<div class="tablewrap" tabindex="0" role="region" aria-label="{} &mdash; scrollable table"><table><thead><tr>'.format(e(section["title"]))]
    for c in ("ID", "Suggestion", "Why it helps the decision", "Official source(s)", "Effort", "Review status"):
        out.append('<th scope="col">{}</th>'.format(c))
    out.append("</tr></thead><tbody>")
    for r in section["rows"]:
        notes = e(r.get("notes", ""))
        fl = flag_link(r.get("flag_id", ""), in_pages)
        if fl:
            notes = "{} &nbsp; {}".format(notes, fl) if notes else fl
        out.append("<tr>")
        out.append('<td><span class="small">{}</span></td>'.format(e(r["id"])))
        out.append("<td><strong>{}</strong></td>".format(e(r["label"])))
        why = "<td>{}</td>".format(e(r.get("value", "")))
        if notes:
            why = why[:-5] + '<br><span class="small">{}</span></td>'.format(notes)
        out.append(why)
        out.append("<td>{}</td>".format(source_links(r.get("source_ids", []))))
        out.append('<td><span class="badge analysis">{}</span></td>'.format(e(r.get("effort", ""))))
        out.append('<td><span class="badge review">{}</span></td>'.format(e(r.get("review_status", ""))))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)

def render_table(section, in_pages=True):
    cols = section["columns"]
    if "Effort" in cols and "Review status" in cols:
        return render_suggestion_table(section, in_pages)
    out = ['<div class="tablewrap" tabindex="0" role="region" aria-label="{} — scrollable table"><table><thead><tr>'.format(e(section["title"]))]
    for c in cols:
        out.append("<th scope=\"col\">{}</th>".format(e(c)))
    out.append("</tr></thead><tbody>")
    for r in section["rows"]:
        value = r.get("value", "")
        value_cell = '<td class="blank">(blank - not officially confirmed)</td>' if value == "" else "<td>{}</td>".format(e(value))
        notes = e(r.get("notes", ""))
        fl = flag_link(r.get("flag_id", ""), in_pages)
        if fl:
            notes = "{} &nbsp; {}".format(notes, fl) if notes else fl
        out.append("<tr>")
        out.append("<td><strong>{}</strong><br><span class=\"small\">{}</span></td>".format(e(r["label"]), e(r["id"])))
        out.append(value_cell)
        out.append("<td>{}</td>".format(badge(r["status"])))
        if r.get("status") == "owner supplied" and r.get("source_note"):
            out.append('<td><span class="owner-src">{}</span><br>{}</td>'.format(e(r["source_note"]), source_links(r.get("source_ids", []))))
        else:
            out.append("<td>{}</td>".format(source_links(r.get("source_ids", []))))
        out.append("<td>{}</td>".format(notes))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)

def nav_html(active, in_pages):
    prefix = "" if in_pages else "pages/"
    home = "../index.html" if in_pages else "index.html"
    parts = ['<div class="wrap"><a href="{}">Home</a>'.format(home)]
    for slug, title in D.NAV:
        cls = ' class="active"' if slug == active else ""
        parts.append('<a{} href="{}{}.html">{}</a>'.format(cls, prefix, e(slug), e(title)))
    parts.append("</div>")
    return "".join(parts)

def header_html(title, subtitle, active, in_pages):
    css = "../assets/site.css" if in_pages else "assets/site.css"
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Rental increase SF</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<header><div class="wrap"><h1>{title}</h1><p>{subtitle}</p><p class="small">Research ledger dated {date} UTC &middot; official-source-linked research</p></div></header>
<nav>{nav}</nav>
<main>
""".format(title=e(title), subtitle=e(subtitle), date=e(D.DATE), css=css, nav=nav_html(active, in_pages))

def footer_html(in_pages):
    p = "../" if in_pages else ""
    return """</main>
<footer><div class="wrap">
<p>{disclaimer}</p>
<p>Manual review: <a href="{p}SOURCES.md">SOURCES.md</a> &middot; <a href="{p}VERIFICATION.md">VERIFICATION.md</a> &middot; <a href="{p}EXECUTIVE_SUMMARY.md">Executive summary</a> &middot; <a href="{p}FLAGGED_FOR_REVIEW.md">Flagged for Review</a> &middot; <a href="{p}data/validation_report.json">Validation report</a></p>
<p class="small">Unverified values are blank and flagged. Personal information uses placeholders. Structural validation is not legal verification. See <a href="{p}FOLLOWUP_AUDIT.md">follow-up audit and verification limits</a>.</p>
</div></footer>
</body>
</html>
""".format(disclaimer=e(D.DISCLAIMER), p=p)

_URL_RE = re.compile(r"https?://[^\s)<>,]+")

def _inline(text):
    """Escape then apply the tiny subset of markdown used by the summaries."""
    out = e(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    def link(m):
        url = m.group(0)
        return '<a href="{0}" target="_blank" rel="noopener">{0}</a>'.format(url)
    return _URL_RE.sub(link, out)

def md_to_html(text):
    """Render the subset of markdown used in the executive summary text."""
    blocks, para, items, kind = [], [], [], [None]

    def flush_para():
        if para:
            blocks.append("<p>{}</p>".format(_inline(" ".join(para))))
            para.clear()

    def flush_items():
        if items:
            tag = kind[0] or "ul"
            blocks.append("<{0}>{1}</{0}>".format(
                tag, "".join("<li>{}</li>".format(_inline(i)) for i in items)))
            items.clear()
            kind[0] = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_items(); continue
        if line.startswith("# ") and not line.startswith("## "):
            # The page header already renders the document title.
            flush_para(); flush_items(); continue
        if line.startswith("## "):
            flush_para(); flush_items()
            blocks.append("<h2>{}</h2>".format(_inline(line[3:])))
            continue
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            flush_para()
            if kind[0] not in (None, "ol"):
                flush_items()
            kind[0] = "ol"; items.append(m.group(1)); continue
        if line.startswith("- "):
            flush_para()
            if kind[0] not in (None, "ul"):
                flush_items()
            kind[0] = "ul"; items.append(line[2:]); continue
        flush_items(); para.append(line.strip())
    flush_para(); flush_items()
    return "".join(blocks)

def summary_page_with_narrative(page):
    out = [header_html(page["title"], page["description"], "summary", True)]
    out.append('<section class="hero"><h2>{}</h2><p>{}</p><div class="disclaimer">{}</div></section>'.format(
        e(page["title"]), e(page["description"]), e(D.DISCLAIMER)))
    out.append('<section class="narrative">{}'.format(md_to_html(counts(D.EXECUTIVE_SUMMARY_TEXT))))
    out.append('<p class="small">The same text is available as <a href="../EXECUTIVE_SUMMARY.md">EXECUTIVE_SUMMARY.md</a> for manual review.</p></section>')
    for sec in page["sections"]:
        out.append("<section><h2>{}</h2>{}</section>".format(e(sec["title"]), render_table(sec, True)))
    out.append(footer_html(True))
    return "".join(out)

def counts(text):
    """Substitute the computed source/flag counts so no total is ever typed by hand."""
    return (text.replace("{{SOURCES}}", str(len(D.SOURCES)))
                .replace("{{FLAGS}}", str(len(D.FLAGS)))
                .replace("{{SOURCE_FLAGS}}", str(len([f for f in D.FLAGS if not f["id"].startswith(("T03-", "B87-"))]))))

def page_html(slug, page):
    out = [header_html(page["title"], page["description"], slug, True)]
    out.append('<section class="hero"><h2>{}</h2><p>{}</p><div class="disclaimer">{}</div></section>'.format(
        e(page["title"]), e(page["description"]), e(D.DISCLAIMER)
    ))
    for sec in page["sections"]:
        out.append("<section><h2>{}</h2>{}</section>".format(e(sec["title"]), render_table(sec, True)))
    out.append(footer_html(True))
    return "".join(out)

def sources_page_html():
    out = [header_html("Sources", "All {} official sources used for verification, with manual-review links.".format(len(D.SOURCES)), "sources", True)]
    out.append('<section class="hero"><h2>Official source ledger</h2><p>Every published table row links to one or more of these official government or SEC sources.</p><div class="disclaimer">{}</div></section>'.format(e(D.DISCLAIMER)))
    rows = []
    for sid, src in sorted(D.SOURCES.items()):
        rows.append({
            "id": sid,
            "label": "{} | {}".format(src["agency"], src["title"]),
            "value": src["statement"],
            "status": "verified",
            "source_ids": [sid],
            "notes": src["category"],
            "flag_id": "",
        })
    section = {"title": "Sources", "columns": D.COLUMNS, "rows": rows}
    out.append("<section><h2>Official sources</h2>{}</section>".format(render_table(section, True)))
    out.append(footer_html(True))
    return "".join(out)

def flagged_page_html():
    out = [header_html("Flagged for Review", "Clearly labeled irregularities and unverified items with official source links.", "flagged", True)]
    out.append('<div class="flagged-banner"><h2>Flagged for Review</h2><p>Status <strong>needs review</strong> means the item is published with official source links for manual review and does <strong>not</strong> block any task or the merge. Unverified value cells are blank.</p></div>')
    out.append('<section class="hero"><div class="disclaimer">{}</div></section>'.format(e(D.DISCLAIMER)))
    out.append("<section><h2>All {} flagged items</h2>".format(len(D.FLAGS)))
    for f in D.FLAGS:
        out.append('<div class="flagitem" id="{}"><h3><span class="id">{}</span> &mdash; {}</h3><p>{}</p><p>{} &middot; <strong>{}</strong></p></div>'.format(
            e(f["id"]), e(f["id"]), e(f["title"]), e(f["detail"]), source_links(f["source_ids"]), e(f["status"])
        ))
    out.append("</section>")
    out.append(footer_html(True))
    return "".join(out)

def page_sources(page):
    ids = []
    for sec in page.get("sections", []):
        for r in sec["rows"]:
            for sid in r["source_ids"]:
                if sid not in ids:
                    ids.append(sid)
    return ids

def index_html():
    out = [header_html("Rental increase SF", "Executive-summary dashboard for an anonymized San Francisco rent-increase case.", "", False)]
    out.append('<section class="hero"><h2>Start here: is the \'inform the Rent Board\' rule a state law or a local law?</h2>'
               '<p><strong>Local.</strong> The duty to report a rent-controlled unit and hold a <strong>Rent Increase License</strong> is a <strong>San Francisco ordinance</strong> — Administrative Code Chapter 37, Section 37.15, added by Ordinance No. 265-20, effective <strong>January 18, 2021</strong>. It is not a California state statute and not a federal rule.</p>'
               '<p>The <strong>2023</strong> date is the <strong>local</strong> operative date for small buildings: condominiums and buildings with <strong>1-9 residential units</strong> have had to report since <strong>March 1, 2023</strong> (buildings with 10+ units began July 1, 2022). The actual 2023 state law was <strong>SB 567</strong>, which amended the statewide rent cap and just-cause rules and became operative <strong>April 1, 2024</strong> — it creates no rent-board reporting duty. {} &middot; {} &middot; {}</p>'
               '<p><a class="cta" href="pages/local.html">See the layer-by-layer table (LAW-01 to LAW-09) &rarr;</a> <a class="cta" href="pages/suggestions.html">Review the options and record your choice before implementing anything &rarr;</a></p>'
               '<div class="disclaimer">{}</div></section>'.format(
                   source_links(["S53"]), source_links(["S90"]), source_links(["S88", "S73"]), e(D.DISCLAIMER)))
    out.append('<section class="hero"><h2>Next: do I need a Rent Board license as an individual owner?</h2>'
               '<p><strong>Yes.</strong> A landlord must have a current Rent Increase License on file with the SF Rent Board before an annual or banked rent increase can take effect, and every owner of residential property must report into the Rent Board Housing Inventory first. Owners of buildings with fewer than 10 residential units have had to report since <strong>March 1, 2023</strong>. No individual-owner, small-portfolio or fewer-than-10-unit exemption was found in the official sources.</p>'
               '<p>Reporting is free and is done in the Rent Board Portal. A notice that goes into effect while the unit is unlicensed may be null and void, and the tenant may be owed a refund. {} &middot; {} &middot; {}</p>'
               '<p>A second, separate Rent Board obligation also applies: the annual <strong>Rent Board Fee</strong> - <strong>$59.00 per dwelling unit for 2026-2027</strong>, due March 1, with an exemption window closing December 14, 2026. Paying it does not create a license, and a license does not pay it.</p>'
               '<p><a class="cta" href="pages/process.html">Read the step-by-step license and notice process &rarr;</a> &nbsp; <a class="cta" href="pages/fee.html">Rent Board Fee, penalties and tenant recovery &rarr;</a></p>'
               '<div class="disclaimer">{}</div></section>'.format(
                   source_links(["S01"]), source_links(["S07"]), source_links(["S08", "S53"]), e(D.DISCLAIMER)))
    out.append('<section class="hero"><h2>How to read this dashboard</h2>'
               '<p>Every finding row carries a <span class="badge verified">verified</span> badge and one or more official source links (SF.gov, the Rent Ordinance, California statute, eCFR, HUD, SEC). '
               '<span class="badge analysis">analysis</span> means a reasoned conclusion drawn from those rules plus the owner-supplied facts. '
               '<span class="badge review">needs review</span> means the value could not be confirmed officially, so the cell is left blank and the item is published on the Flagged for Review page. '
               '<span class="badge owner">owner-supplied</span> marks the owner\'s own case facts, which are anonymized and are not official findings.</p>'
               '<p class="small">Start with the Executive Summary for the answer, the Step-by-Step License page for the order of operations, the Anonymized Case for the two units, and the Flagged for Review page for anything still open.</p></section>')
    out.append('<div class="cards">')
    for label, value, slug, desc in D.CARDS:
        if value == "auto:sources":
            value = str(len(D.SOURCES))
        elif value == "auto:flags":
            value = str(len(D.FLAGS))
        out.append('<div class="card"><div class="k">{}</div><div class="v">{}</div><div class="d">{}</div><a href="pages/{}.html">Open {} &rarr;</a></div>'.format(
            e(label), e(value), e(desc), e(slug), e(label)
        ))
    out.append("</div>")
    out.append('<section><h2>Quick navigation</h2><div class="tablewrap"><table><thead><tr><th>Category</th><th>What it contains</th><th>Official source(s)</th></tr></thead><tbody>')
    for slug, title in D.NAV:
        if slug == "sources":
            desc = "All {} official sources with manual-review links.".format(len(D.SOURCES))
            sids = ["S01", "S07", "S53", "S27", "S43"]
        elif slug == "flagged":
            desc = "Clearly labeled irregularities and unverified items, each with official source links."
            sids = ["S01", "S07", "S08", "S02"]
        else:
            page = D.PAGES[slug]
            desc = page["description"]
            sids = page_sources(page)[:6]
        out.append('<tr><td><a href="pages/{}.html">{}</a></td><td>{}</td><td>{}</td></tr>'.format(
            e(slug), e(title), e(desc), source_links(sids)
        ))
    out.append("</tbody></table></div></section>")
    out.append(footer_html(False))
    return "".join(out)

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def main():
    for d in (DATA, PAGES, ASSETS):
        d.mkdir(parents=True, exist_ok=True)
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    write(ASSETS / "site.css", D.CSS_TEXT)

    sources_json = [dict(id=sid, **src) for sid, src in sorted(D.SOURCES.items())]
    write(DATA / "sources.json", json.dumps(sources_json, indent=2, ensure_ascii=False) + "\n")
    write(DATA / "flags.json", json.dumps(D.FLAGS, indent=2, ensure_ascii=False) + "\n")
    write(DATA / "pages.json", json.dumps(D.PAGES, indent=2, ensure_ascii=False) + "\n")
    for slug, page in D.PAGES.items():
        write(DATA / "{}.json".format(slug), json.dumps(page, indent=2, ensure_ascii=False) + "\n")

    for slug, page in D.PAGES.items():
        html = summary_page_with_narrative(page) if slug == "summary" else page_html(slug, page)
        write(PAGES / "{}.html".format(slug), html)
    write(PAGES / "sources.html", sources_page_html())
    write(PAGES / "flagged.html", flagged_page_html())
    write(ROOT / "index.html", index_html())

    write(ROOT / "EXECUTIVE_SUMMARY.md", counts(D.EXECUTIVE_SUMMARY_TEXT))
    write(ROOT / "FLAGGED_FOR_REVIEW.md", counts(D.FLAGGED_TEXT))
    write(ROOT / "README.md", counts(D.README_TEXT))
    print("Built {} data files, {} page HTML files, index.html, assets/site.css, .nojekyll and 3 markdown deliverables.".format(
        len(list(DATA.glob("*.json"))), len(list(PAGES.glob("*.html")))
    ))

if __name__ == "__main__":
    main()
