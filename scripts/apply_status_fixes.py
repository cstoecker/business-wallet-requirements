#!/usr/bin/env python3
"""Apply verified legal-status fixes (YAML list: id, field, new_value, mode, reason, evidence_source) to requirements and sources.

  scripts/apply_status_fixes.py FILE.yml
Fields: statement, quote, rationale (mode append adds a sentence once), sources[0].location (requirements); title, note (SRC-* ids in sources.yml).
Requirements get last_verified today and a revision_note naming the reason when the statement or quote changed.
"""
import os, re, sys, yaml, datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
fixes = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
today = datetime.date.today().isoformat(); n = 0; srcs = None
sp = os.path.join(ROOT, "_data/graph/sources.yml")
for x in fixes:
    i, f, v = x["id"], x["field"], x.get("new_value")
    if i.startswith("SRC-"):
        if f not in ("title", "note"): continue
        txt = open(sp, encoding="utf-8").read(); data = yaml.safe_load(txt)
        for s in data:
            if s["id"] == i: s[f] = v
        open(sp, "w", encoding="utf-8").write("# Source register (graph entity type: Source). Only official sources, ecosystem specifications\n# and the OID 2025 paper are allowed here (docs/01 principle 8).\n# class: official | standard | ecosystem-specification | paper | academic; verification: read | snippet | unverified\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000)); n += 1; continue
    p = os.path.join(ROOT, "_requirements", i + ".md")
    if not os.path.exists(p): print("missing", i); continue
    t = open(p, encoding="utf-8").read(); m = re.match(r"---\n(.*?)\n---\n?(.*)", t, re.S); fm = yaml.safe_load(m.group(1))
    if f == "statement": fm["statement"] = v; fm["revision_note"] = "Statement updated after a check of the current legal text: " + x.get("reason", "")
    elif f == "quote": fm["quote"] = v
    elif f == "sources[0].location": fm["sources"][0]["location"] = v
    elif f == "rationale":
        if x.get("mode") == "append":
            if v not in fm["rationale"]: fm["rationale"] = fm["rationale"].rstrip() + " " + v
        else: fm["rationale"] = v
    else: continue
    fm["last_verified"] = today; n += 1
    open(p, "w", encoding="utf-8").write("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n" + m.group(2))
print(n, "fixes applied")
