#!/usr/bin/env python3
"""Append new sources from research files (top key new_sources) to _data/graph/sources.yml, skipping IDs already present.
Usage: scripts/register_sources.py FILE.yml ...   Class overrides: informative whitepapers and protocol specs by their owners are ecosystem-specification."""
import os, sys, yaml
ROOT = os.path.join(os.path.dirname(__file__), "..")
p = os.path.join(ROOT, "_data/graph/sources.yml")
have = {s["id"] for s in yaml.safe_load(open(p, encoding="utf-8"))}
ALLOWED = {"official", "standard", "ecosystem-specification", "academic", "paper"}
OVERRIDE = {"SRC-AP2": "ecosystem-specification", "SRC-OIDF-AGENTIC": "ecosystem-specification", "SRC-W3C-AIAP-ID": "ecosystem-specification"}
out = ""; n = 0
for f in sys.argv[1:]:
    d = yaml.safe_load(open(f, encoding="utf-8")) or {}
    for s in (d.get("new_sources") if isinstance(d, dict) else d) or []:
        if s["id"] in have: continue
        have.add(s["id"]); n += 1
        s["class"] = OVERRIDE.get(s["id"], s.get("class"))
        if s["class"] not in ALLOWED: s["class"] = "ecosystem-specification"
        s.setdefault("retrieved", "2026-10-03"); s.setdefault("verification", "read")
        order = [k for k in ["id", "title", "issuer", "class", "url", "version", "date", "retrieved", "verification", "note"] if k in s]
        order += [k for k in s if k not in order]
        out += "- " + "\n  ".join(f"{k}: " + yaml.safe_dump(str(s[k]), allow_unicode=True, default_style="'", width=1000).strip().replace("\n...", "") for k in order) + "\n"
open(p, "a", encoding="utf-8").write(out)
print(n, "sources added")
