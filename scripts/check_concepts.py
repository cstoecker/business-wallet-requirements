#!/usr/bin/env python3
"""Validate graph data, the concept registry, concept articles and figure pages. Exit 1 on any error.

Checks: unique IDs, resolvable references (sources, ecosystems, related concepts), symmetric `related`,
one article per concept, standard section order for articles with status draft/reviewed/published,
1-2 figures per published article, figure metadata completeness (alt, caption, description, keywords, files exist).
"""
import os, re, sys, yaml
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def load(p): return yaml.safe_load(open(os.path.join(ROOT, p), encoding="utf-8")) or []
errors = []
def err(m): errors.append(m)

sources = load("_data/graph/sources.yml"); ecos = load("_data/graph/ecosystems.yml")
ucs = load("_data/graph/usecases.yml"); reqs = load("_data/graph/ecosystem-requirements.yml"); concepts = load("_data/graph/concepts.yml")
for name, items in (("sources", sources), ("ecosystems", ecos), ("usecases", ucs), ("ecosystem-requirements", reqs), ("concepts", concepts)):
    ids = [x["id"] for x in items]
    for d in {i for i in ids if ids.count(i) > 1}: err(f"{name}: duplicate id {d}")
cid_all = {c["id"] for c in concepts}; sid = {s["id"] for s in sources}; eid = {e["id"] for e in ecos}; cid = {c["id"]: c for c in concepts}
for e in ecos:
    for s in e.get("sources", []):
        if s not in sid: err(f"{e['id']}: unknown source {s}")
for x in ucs + reqs:
    if x["ecosystem"] not in eid: err(f"{x['id']}: unknown ecosystem {x['ecosystem']}")
    if x["source"] not in sid: err(f"{x['id']}: unknown source {x['source']}")
for s in sources:
    if s.get("class") not in ("official", "standard", "ecosystem-specification", "paper", "academic"): err(f"{s['id']}: class must be official, standard, ecosystem-specification, paper or academic")

cases = load("_data/graph/business-cases.yml"); claims = load("_data/graph/claims.yml")
bid = {b["id"] for b in cases}
for c in claims:
    if c["case"] not in bid: err(f"{c['id']}: unknown business case {c['case']}")
    if c["source"] not in sid: err(f"{c['id']}: unknown source {c['source']}")
    if c.get("verification") not in ("read", "snippet", "unverified"): err(f"{c['id']}: verification must be read, snippet or unverified")
    if not c.get("caveat") and c.get("type") in ("upper-bound", "lower-bound", "estimate"): err(f"{c['id']}: estimates and bounds need a caveat")
cids = [c["id"] for c in claims]
for d in {i for i in cids if cids.count(i) > 1}: err(f"claims: duplicate id {d}")
for b in cases:
    if not any(c["case"] == b["id"] for c in claims): err(f"{b['id']}: business case has no claims")
for u in ucs:
    pass
cats = {c["code"] for c in load("_data/categories.yml")}
rdir = os.path.join(ROOT, "_requirements"); rids = []
for f in sorted(os.listdir(rdir)) if os.path.isdir(rdir) else []:
    t = open(os.path.join(rdir, f), encoding="utf-8").read(); m = re.match(r"---\n(.*?)\n---", t, re.S); r = yaml.safe_load(m.group(1)); rids.append(r["req_id"])
    if f != r["req_id"] + ".md": err(f"requirement file {f} must be named {r['req_id']}.md")
    if not re.fullmatch(r"EBW-[A-Z]{3}-\d{3}", r["req_id"]) or r["req_id"].split("-")[1] != r["category"]: err(f"{r['req_id']}: ID must be EBW-<CATEGORY>-<NNN> matching the category")
    if r["category"] not in cats: err(f"{r['req_id']}: unknown category {r['category']}")
    if not re.search(r"\bshall\b", r["statement"]): err(f"{r['req_id']}: statement must contain 'shall'")
    if r["provenance"] not in ("L", "S", "D", "A"): err(f"{r['req_id']}: provenance must be L, S, D or A")
    if r["status"] not in ("draft", "in-review", "agreed", "verified", "obsolete"): err(f"{r['req_id']}: bad status")
    if r["status"] in ("agreed", "verified") and r.get("reviewer") in (None, "", "pending"): err(f"{r['req_id']}: agreed or verified requires a named reviewer")
    if not r.get("sources") and r["provenance"] != "A": err(f"{r['req_id']}: needs at least one source unless provenance is A")
    for x in r.get("sources", []):
        if x["id"] not in sid: err(f"{r['req_id']}: unknown source {x['id']}")
    for cc in r.get("concepts", []):
        if cc not in cid_all: err(f"{r['req_id']}: unknown concept {cc}")
    if r["legal_status"] == "proposal" and not any(x["id"] in ("SRC-EBW-PROPOSAL", "SRC-COUNCIL-ST-9684-26", "SRC-COUNCIL-ST-7659-26", "SRC-COM-2026-321") for x in r["sources"]): err(f"{r['req_id']}: legal_status proposal must cite a Commission proposal or the Council text")
for d in {i for i in rids if rids.count(i) > 1}: err(f"requirements: duplicate id {d}")
SECTIONS = ["Summary", "Definition", "Why it matters", "How it works", "Interaction flow", "Roles and responsibilities", "Related concepts",
            "Requirements and obligations", "Standards and specifications", "Design choices and alternatives", "Examples",
            "Open questions and limitations", "Terms introduced", "References", "Change log"]
figs = {}
fdir = os.path.join(ROOT, "_figures")
for f in sorted(os.listdir(fdir)) if os.path.isdir(fdir) else []:
    t = open(os.path.join(fdir, f), encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    slug = f[:-3]; figs[slug] = fm
    for k in ("title", "image", "image_png", "width", "height", "alt", "caption", "description", "keywords", "figure_type", "used_in", "last_verified"):
        if not fm.get(k): err(f"figure {slug}: missing {k}")
    for k in ("image", "image_png"):
        if fm.get(k) and not os.path.exists(os.path.join(ROOT, fm[k].lstrip("/"))): err(f"figure {slug}: file missing {fm[k]}")
    if fm.get("alt") and len(fm["alt"]) < 40: err(f"figure {slug}: alt text too short")
    svg = os.path.join(ROOT, (fm.get("image") or "").lstrip("/"))
    if os.path.exists(svg):
        s = open(svg, encoding="utf-8").read()
        for tag in ("<title", "<desc", "<metadata"):
            if tag not in s: err(f"figure {slug}: SVG lacks {tag}")

for c in concepts:
    for r in c.get("related", []):
        if r not in cid: err(f"{c['id']}: related {r} unknown")
        elif c["id"] not in cid[r].get("related", []): err(f"{c['id']} <-> {r}: related is not symmetric")
    path = os.path.join(ROOT, "concepts", c["slug"] + ".md")
    if not os.path.exists(path): err(f"{c['id']}: missing article concepts/{c['slug']}.md"); continue
    t = open(path, encoding="utf-8").read()
    fm = yaml.safe_load(re.match(r"---\n(.*?)\n---", t, re.S).group(1))
    thin = c["status"] in ("planned", "proposed")
    if bool(fm.get("noindex")) != thin or (fm.get("sitemap") is False) != thin: err(f"{c['slug']}: noindex/sitemap:false must be set exactly while status is planned or proposed")
    if fm.get("permalink") != f"/concepts/{c['slug']}/": err(f"{c['slug']}: permalink must be /concepts/{c['slug']}/")
    if fm.get("concept") != c["id"]: err(f"{path}: concept front matter must be {c['id']}")
    if c["status"] in ("draft", "reviewed", "published"):
        heads = re.findall(r"^## (.+)$", t, re.M)
        if [h for h in heads if h in SECTIONS] != SECTIONS: err(f"{c['slug']}: sections must be, in order: {', '.join(SECTIONS)}")
        used = fm.get("figures") or []
        if not 1 <= len(used) <= 2: err(f"{c['slug']}: needs 1-2 figures in front matter `figures`")
        for u in used:
            if u not in figs: err(f"{c['slug']}: figure {u} not found")
        if len(re.findall(r"include figure\.html", t)) != len(used): err(f"{c['slug']}: figure includes must match front matter figures")
        if not fm.get("description"): err(f"{c['slug']}: description required")
        for q in fm.get("faq") or []:
            if not q.get("q") or not q.get("a"): err(f"{c['slug']}: faq entries need q and a")
        for ref in re.findall(r"CON-[A-Z0-9-]+", t):
            if ref not in cid: err(f"{c['slug']}: unknown concept reference {ref}")
        for ref in re.findall(r"SRC-[A-Z0-9-]+", t):
            if ref not in sid: err(f"{c['slug']}: unknown source reference {ref}")
        if re.search(r"[\U0001F300-\U0001FAFF✅✔]", t): err(f"{c['slug']}: emoji are not allowed")
        if len(re.findall("—", t)) > 2: err(f"{c['slug']}: more than two em-dashes")
        for w in ("seamless", "unlock", "leverage", "empower", "streamline", "supercharge", "world-class", "enterprise-grade", "next-generation"):
            if re.search(w, t, re.I): err(f"{c['slug']}: intensity word '{w}'")
if "--report" in sys.argv:
    from collections import Counter
    print("Concept articles by status:", dict(Counter(c["status"] for c in concepts)))
print(f"{len(rids)} requirements")
print(f"{len(cases)} business cases, {len(claims)} claims")
print(f"{len(concepts)} concepts, {len(figs)} figures, {len(sources)} sources checked")
if errors:
    print("\n".join("ERROR " + e for e in errors)); sys.exit(1)
print("OK")
