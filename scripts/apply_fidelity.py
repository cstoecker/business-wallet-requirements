#!/usr/bin/env python3
"""Apply fidelity-check results (YAML lists with id, verdict, corrected_statement, corrected_location, provenance,
corrected_rationale, full_quote, note) to _requirements/<ID>.md. Only supported/overreach/derived/wrong-location are applied."""
import os, re, sys, yaml
ROOT = os.path.join(os.path.dirname(__file__), "..")
n = 0
for path in sys.argv[1:]:
    for e in yaml.safe_load(open(path, encoding="utf-8")):
        f = os.path.join(ROOT, "_requirements", e["id"] + ".md")
        t = open(f, encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n?(.*)", t, re.S); fm = yaml.safe_load(m.group(1)); body = m.group(2)
        v = e["verdict"]
        if v not in ("supported", "overreach", "derived", "wrong-location"): print("skip", e["id"], v); continue
        if v in ("overreach", "derived") and e.get("corrected_statement"):
            if " shall " not in " " + e["corrected_statement"] + " ": print("skip (no shall)", e["id"]); continue
            fm["statement"] = e["corrected_statement"].strip()
        if e.get("corrected_location"): fm["sources"][0]["location"] = e["corrected_location"]
        if e.get("provenance") in ("L", "S", "D"): fm["provenance"] = e["provenance"]
        if e.get("corrected_rationale"): fm["rationale"] = e["corrected_rationale"].strip()
        if e.get("full_quote"): fm["full_quote"] = e["full_quote"].strip()
        fm["fidelity_checked"] = "2026-10-03"
        if v in ("overreach", "derived", "wrong-location"):
            fm["revision_note"] = {"overreach": "Statement narrowed to what the clause contains after a check against the full text.", "derived": "Marked as derived: the statement follows from the clause but is not literal.", "wrong-location": "Source location corrected."}[v]
        open(f, "w", encoding="utf-8").write("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n" + body)
        n += 1
print(n, "requirements updated")
