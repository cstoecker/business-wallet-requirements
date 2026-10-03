#!/usr/bin/env python3
"""Create or refresh concept article files from _data/graph/concepts.yml.

  scripts/new_concept.py            -> (re)create stub files for registry entries that have none
  scripts/new_concept.py --draft ID -> write the standard article skeleton (all sections) for ID
Existing article bodies are never overwritten unless --force is given.
"""
import sys, os, yaml
ROOT = os.path.join(os.path.dirname(__file__), "..")
reg = yaml.safe_load(open(os.path.join(ROOT, "_data/graph/concepts.yml"), encoding="utf-8"))
SECTIONS = [
 ("Summary", "Two or three sentences that answer the question on their own. Write them so that an answer engine can quote them without losing qualifications."),
 ("Definition", "Use the include `{% include concept-definition.html id=\"" + "{ID}" + "\" %}` and add what the concept is not."),
 ("Why it matters", "The problem, who is affected, and what changes for B2B, B2G and B2C."),
 ("How it works", "Mechanism in plain language. Figure 1 (concept model) goes here: `{% include figure.html id=\"...\" no=1 %}`."),
 ("Interaction flow", "Step-by-step flow. Figure 2 (flow) goes here: `{% include figure.html id=\"...\" no=2 %}`."),
 ("Roles and responsibilities", "Actors and what each must do."),
 ("Related concepts", "Reference other concept articles with `{% include concept-ref.html id=\"CON-...\" %}`; explain each relationship in one sentence."),
 ("Requirements and obligations", "Linked requirement IDs and legal sources; categories from the registry."),
 ("Standards and specifications", "Clause-level references; official sources and ecosystem specifications only."),
 ("Design choices and alternatives", "Options, trade-offs and when to choose which."),
 ("Examples", "Two or three short scenarios from different domains."),
 ("Open questions and limitations", "What is not yet settled, with 🔎 markers."),
 ("Terms introduced", "Glossary terms with one-line definitions."),
 ("References", "Source register IDs (`SRC-...`) with version and date."),
 ("Change log", "Date, change, reviewer."),
]
def write(c, body, force=False):
    path = os.path.join(ROOT, "concepts", c["slug"] + ".md")
    if os.path.exists(path) and not force and open(path, encoding="utf-8").read().count("\n## ") > 0:
        return False
    desc = c["summary"].replace('"', '\\"')
    thin = c['status'] in ('planned', 'proposed')
    NOINDEX = 'noindex: true\nsitemap: false\n' if thin else ''
    fm = f'''---
title: "{c['title']}"
layout: concept
concept: {c['id']}
parent: Concepts
grand_parent: Start here
description: "{desc}"
permalink: /concepts/{c['slug']}/
{NOINDEX}schema_type: TechArticle
keywords: [{c['title']}, European Business Wallet, {c['group']}]
last_verified: "2026-10-03"
figures: []
faq: []
---
'''
    open(path, "w", encoding="utf-8").write(fm + body)
    return True
args = sys.argv[1:]
if args and args[0] == "--draft":
    c = next(x for x in reg if x["id"] == args[1])
    body = "\n".join(f"## {h}\n\n<!-- {hint.replace('{ID}', c['id'])} -->\n" for h, hint in SECTIONS)
    write(c, body, force="--force" in args)
else:
    n = 0
    for c in reg:
        if not os.path.exists(os.path.join(ROOT, "concepts", c["slug"] + ".md")):
            n += write(c, "")
    print(f"created {n} stubs")
