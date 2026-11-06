"""Build the static GitHub Pages site from canonical site_data.

Run: python3 scripts/build_site.py
Generates data/*.json, index.html, pages/*.html, assets/site.css, .nojekyll,
README.md, EXECUTIVE_SUMMARY.md and FLAGGED_FOR_REVIEW.md.
"""

import json
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
    cls = {"verified": "verified", "needs review": "review", "analysis": "analysis"}.get(status, "analysis")
    label = {"verified": "verified", "needs review": "needs review", "analysis": "analysis"}.get(status, status)
    return '<span class="badge {}">{}</span>'.format(cls, e(label))

def flag_link(flag_id, in_pages):
    if not flag_id:
        return ""
    href = "flagged.html#{}".format(e(flag_id)) if in_pages else "pages/flagged.html#{}".format(e(flag_id))
    return '<a class="flaglink" href="{}">{}</a>'.format(href, e(flag_id))

def render_table(section, in_pages=True):
    cols = section["columns"]
    out = ['<div class="tablewrap"><table><thead><tr>']
    for c in cols:
        out.append("<th>{}</th>".format(e(c)))
    out.append("</tr></thead><tbody>")
    for r in section["rows"]:
        value = r.get("value", "")
        value_cell = '<td class="blank">(blank)</td>' if value == "" else "<td>{}</td>".format(e(value))
        notes = e(r.get("notes", ""))
        fl = flag_link(r.get("flag_id", ""), in_pages)
        if fl:
            notes = "{} &nbsp; {}".format(notes, fl) if notes else fl
        out.append("<tr>")
        out.append("<td><strong>{}</strong><br><span class=\"small\">{}</span></td>".format(e(r["label"]), e(r["id"])))
        out.append(value_cell)
        out.append("<td>{}</td>".format(badge(r["status"])))
        out.append("<td>{}</td>".format(source_links(r["source_ids"])))
        out.append("<td>{}</td>".format(notes))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)

def nav_html(active, in_pages):
    prefix = "" if in_pages else "pages/"
    home = "index.html" if in_pages else "../index.html"
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
<header><div class="wrap"><h1>{title}</h1><p>{subtitle}</p><p class="small">Verified {date} UTC &middot; official-source-linked research</p></div></header>
<nav>{nav}</nav>
<main>
""".format(title=e(title), subtitle=e(subtitle), date=e(D.DATE), css=css, nav=nav_html(active, in_pages))

def footer_html(in_pages):
    p = "../" if in_pages else ""
    return """</main>
<footer><div class="wrap">
<p>{disclaimer}</p>
<p>Manual review: <a href="{p}SOURCES.md">SOURCES.md</a> &middot; <a href="{p}VERIFICATION.md">VERIFICATION.md</a> &middot; <a href="{p}EXECUTIVE_SUMMARY.md">Executive summary</a> &middot; <a href="{p}FLAGGED_FOR_REVIEW.md">Flagged for Review</a> &middot; <a href="{p}data/validation_report.json">Validation report</a></p>
<p class="small">No hallucinations: unverified values are blank and flagged. Personal information is anonymized with placeholders.</p>
</div></footer>
</body>
</html>
""".format(disclaimer=e(D.DISCLAIMER), p=p)

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
    out = [header_html("Sources", "All 52 official sources used for verification, with manual-review links.", "sources", True)]
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

def index_html():
    out = [header_html("Rental increase SF", "Executive-summary dashboard for an anonymized San Francisco rent-increase case.", "", False)]
    out.append('<section class="hero"><h2>Clean landing page / dashboard</h2><p>Official-source-linked findings, local / state / federal rules, anonymized case facts, calculations, analysis, and a clearly labeled Flagged for Review page.</p><div class="disclaimer">{}</div></section>'.format(e(D.DISCLAIMER)))
    out.append('<div class="cards">')
    for label, value, slug, desc in D.CARDS:
        out.append('<div class="card"><div class="k">{}</div><div class="v">{}</div><div class="d">{}</div><a href="pages/{}.html">Open {} &rarr;</a></div>'.format(
            e(label), e(value), e(desc), e(slug), e(label)
        ))
    out.append("</div>")
    out.append('<section><h2>Quick navigation</h2><div class="tablewrap"><table><thead><tr><th>Category</th><th>What it contains</th><th>Official source(s)</th></tr></thead><tbody>')
    for slug, title in D.NAV:
        out.append('<tr><td><a href="pages/{}.html">{}</a></td><td>Source-linked findings and easy-read tables.</td><td>{}</td></tr>'.format(
            e(slug), e(title), source_links(["S01", "S43"])
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
        write(PAGES / "{}.html".format(slug), page_html(slug, page))
    write(PAGES / "sources.html", sources_page_html())
    write(PAGES / "flagged.html", flagged_page_html())
    write(ROOT / "index.html", index_html())

    write(ROOT / "EXECUTIVE_SUMMARY.md", D.EXECUTIVE_SUMMARY_TEXT)
    write(ROOT / "FLAGGED_FOR_REVIEW.md", D.FLAGGED_TEXT)
    write(ROOT / "README.md", D.README_TEXT)
    print("Built {} data files, {} page HTML files, index.html, assets/site.css, .nojekyll and 3 markdown deliverables.".format(
        len(list(DATA.glob("*.json"))), len(list(PAGES.glob("*.html")))
    ))

if __name__ == "__main__":
    main()
