#!/usr/bin/env python3
"""Scoped B87 notice-kit validator. Run: python3 research/b87_notice_kit/validate_kit.py"""
import json, re, sys
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
OFFICIAL = ("sf.gov", "media.api.sf.gov", "codelibrary.amlegal.com", "leginfo.legislature.ca.gov", "dre.ca.gov", "www.dre.ca.gov", "sfplanninggis.org", "courts.ca.gov", "selfhelp.courts.ca.gov", "www4.courts.ca.gov")
errors=[]
checks=0

def check(name, ok, detail=""):
    global checks
    checks += 1
    print(("PASS " if ok else "FAIL ") + name + (f" - {detail}" if detail else ""))
    if not ok: errors.append(f"{name}: {detail}")

def official(url):
    h=urlparse(url).netloc.lower()
    return any(h==d or h.endswith("."+d) for d in OFFICIAL)

data=json.loads((ROOT/"worksheet.json").read_text())
sources={s["id"]:s for s in data["sources"]}
flags={f["id"]:f for f in data["flags"]}
rows=data["rows"]
check("JSON parses", True, f"{len(rows)} rows, {len(sources)} sources, {len(flags)} flags")
check("source URLs official", all(official(s["url"]) for s in sources.values()))
check("row IDs unique", len({r["id"] for r in rows})==len(rows))
bad=[]
for r in rows:
    if not r["source_ids"]: bad.append(r["id"]+" no source")
    for sid in r["source_ids"]:
        if sid not in sources: bad.append(r["id"]+" unknown "+sid)
        elif not official(sources[sid]["url"]): bad.append(r["id"]+" nonofficial "+sid)
    for fid in r.get("flag_ids",[]):
        if fid not in flags: bad.append(r["id"]+" unknown flag "+fid)
    if r["status"]=="needs review" and r.get("value","")!="": bad.append(r["id"]+" needs review but value not blank")
    if r["status"]=="needs review" and not r.get("flag_ids"): bad.append(r["id"]+" needs review but no flag")
check("every JSON row has official sources and valid flags; unverified values blank", not bad, "; ".join(bad[:5]))
fbad=[]
for f in flags.values():
    if f["status"]!="needs review": fbad.append(f["id"]+" status")
    if not f["source_ids"]: fbad.append(f["id"]+" no source")
    for sid in f["source_ids"]:
        if sid not in sources or not official(sources[sid]["url"]): fbad.append(f["id"]+" bad source "+sid)
check("every JSON flag published with official sources", not fbad, "; ".join(fbad))

# Markdown table rows must carry an official URL. Header/separator rows are skipped.
md_bad=[]
md_rows=0
for p in sorted(ROOT.glob("*.md")):
    for n,line in enumerate(p.read_text().splitlines(),1):
        if not line.strip().startswith("|"): continue
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not re.match(r"B87-[A-Z0-9]+", cells[0]): continue
        md_rows+=1
        urls=re.findall(r"https?://[^\s)>\]]+", line)
        if not urls or not any(official(u) for u in urls):
            md_bad.append(f"{p.name}:{n} {cells[0]}")
check("every B87 markdown table row has an official source URL", not md_bad, f"{md_rows} rows; "+"; ".join(md_bad[:5]))

text="\n".join(p.read_text() for p in ROOT.glob("*.md"))+(ROOT/"worksheet.json").read_text()
check("no conflict markers", not re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.M))
check("no unresolved template braces", "{{" not in text and "}}" not in text)
check("placeholder tenants only", all(x in text for x in ["Tenant A","Tenant D","Tenant E","Tenant F"]) and not re.search(r"\bTenant [G-Z]\b", text))
check("no exact street address pattern", not re.search(r"\b\d{3,5}\s+[A-Za-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)\b", text, re.I))
check("dates and amounts preserved", all(x in text for x in ["February 1, 2025","$3,995","April 1, 2026","June 1, 2019","$3,150"]))
check("no attorney approval/guarantee claimed", "No attorney" in text and "guarantee" in text)
for phrase in ["approved by a tenant lawyer","certified lawful","guaranteed no lawsuit"]:
    check("forbidden phrase absent: "+phrase, phrase not in text.lower())

check("Unit 1 arithmetic", Decimal("3995.00")*Decimal("0.016")==Decimal("63.92") and Decimal("3995.00")+Decimal("63.92")==Decimal("4058.92"))
check("Unit 2 arithmetic", Decimal("3150.00")*Decimal("0.016")==Decimal("50.40") and Decimal("3150.00")+Decimal("50.40")==Decimal("3200.40"))
check("conditional totals present", "$4,058.92" in text and "$3,200.40" in text)

# Relative markdown links in README must resolve.
link_bad=[]
for m in re.finditer(r"\]\(([^)]+)\)", (ROOT/"README.md").read_text()):
    u=m.group(1)
    if u.startswith(("http://","https://","#")): continue
    if not (ROOT/u).exists(): link_bad.append(u)
check("README relative links resolve", not link_bad, "; ".join(link_bad))

print(f"\nB87 kit validation {'PASSED' if not errors else 'FAILED'} ({checks} checks, {len(errors)} errors).")
sys.exit(1 if errors else 0)
