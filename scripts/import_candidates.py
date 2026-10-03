#!/usr/bin/env python3
"""Turn reviewed research candidates (YAML lists) into _requirements/EBW-<CAT>-<NNN>.md files.

  scripts/import_candidates.py FILE.yml [FILE2.yml ...]   (dry run unless --write)

Numbering continues per category. Every candidate gets status draft, reviewer pending. New sources listed
under `new_sources` (top-level mapping form) are NOT written here; register them in _data/graph/sources.yml first.
"""
import os, re, sys, yaml
ROOT = os.path.join(os.path.dirname(__file__), "..")
write = "--write" in sys.argv
files = [a for a in sys.argv[1:] if not a.startswith("--")]
rdir = os.path.join(ROOT, "_requirements")
cats = {c["code"] for c in yaml.safe_load(open(os.path.join(ROOT, "_data/categories.yml")))}
sources = {s["id"] for s in yaml.safe_load(open(os.path.join(ROOT, "_data/graph/sources.yml")))}
concepts = {c["id"] for c in yaml.safe_load(open(os.path.join(ROOT, "_data/graph/concepts.yml")))}
nxt = {}
for f in os.listdir(rdir):
    m = re.fullmatch(r"EBW-([A-Z]{3})-(\d{3})\.md", f)
    if m: nxt[m.group(1)] = max(nxt.get(m.group(1), 0), int(m.group(2)))
n_new = 0
for path in files:
    data = yaml.safe_load(open(path, encoding="utf-8"))
    items = data["requirements"] if isinstance(data, dict) else data
    for it in items:
        if "key" not in it and "statement" not in it: continue
        cat = it["category"]
        errs = []
        if cat not in cats: errs.append("category")
        if not re.search(r"\bshall\b", it["statement"]): errs.append("shall")
        if it["source"] not in sources: errs.append("source " + it["source"])
        cons = [c for c in it.get("concepts", []) if c in concepts]
        if errs: print("SKIP", it.get("key"), errs); continue
        nxt[cat] = nxt.get(cat, 0) + 1
        rid = f"EBW-{cat}-{nxt[cat]:03d}"
        fm = {"req_id": rid, "title": it["title"], "category": cat, "statement": it["statement"].strip(), "rationale": it["rationale"].strip(),
              "sources": [{"id": it["source"], "location": it["location"]}], "provenance": it["provenance"], "legal_status": it["legal_status"],
              "plane": it.get("plane", "governance"), "perspectives": it.get("perspectives", []), "actors": it.get("actors", []),
              "verification_method": it.get("verification_method", "inspection"), "status": "draft", "reviewer": "pending",
              "concepts": cons, "created": "2026-10-03", "last_verified": "2026-10-03"}
        if it.get("quote"): fm["quote"] = it["quote"].strip()
        body = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n"
        n_new += 1
        if write: open(os.path.join(rdir, rid + ".md"), "w", encoding="utf-8").write(body)
        print(("WROTE " if write else "would write ") + rid, "|", it["title"])
print(n_new, "requirements" + (" written" if write else " (dry run)"))
