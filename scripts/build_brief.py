#!/usr/bin/env python3
"""Select the key requirements for the stakeholder brief from the review data.
Rules (docs/15): priority P1, wallet relevant (core, wallet-general, horizontal), not a duplicate (no merge-with), at most 3 per theme,
plus pinned conflict items; cap 30. Writes _data/brief-selection.yml."""
import glob, yaml, sys
ROOT = __file__.rsplit('/scripts/', 1)[0]
themes = yaml.safe_load(open(f'{ROOT}/_data/brief-themes.yml'))
rev = yaml.safe_load(open(f'{ROOT}/_data/review/requirement-review.yml'))
if isinstance(rev, dict) and 'requirements' in rev: rev = rev['requirements']
if isinstance(rev, dict): rev = list(rev.values())
rev = {x['id']: x for x in rev}
req = {}
for f in glob.glob(f'{ROOT}/_requirements/*.md'):
    fm = yaml.safe_load(open(f).read().split('---')[1]); req[fm['req_id']] = fm
PINS = {'T4': ['EBW-INT-095'], 'T3': ['EBW-NFR-119'], 'T1': [], 'T6': []}
OK_APPL = {'core': 0, 'wallet-general': 1, 'horizontal': 1}
PROV = {'L': 0, 'S': 1, 'D': 2, 'A': 3}
used, out = set(), []
for t in themes:
    cl = t['clusters']
    cands = []
    for rid, v in rev.items():
        if v.get('priority') != 'P1' or v.get('applicability') not in OK_APPL: continue
        if str(v.get('verdict', 'ok')).startswith(('merge-with', 'drop')): continue
        if v.get('fidelity') in ('derived-unmarked',): continue
        cs = v.get('clusters', [])
        hit = [c for c in cs if c in cl]
        if not hit: continue
        r = req[rid]
        key = (cs.index(hit[0]) if hit[0] in cs else 9, 0 if hit[0] == cl[0] else 1, OK_APPL[v['applicability']], PROV.get(r.get('provenance'), 4), rid)
        cands.append((key, rid))
    cands.sort()
    pick = [p for p in PINS.get(t['id'], []) if p in req and p not in used]
    for _, rid in cands:
        if len(pick) >= 3 + len(PINS.get(t['id'], [])): break
        if rid in used or rid in pick: continue
        pick.append(rid)
    for rid in pick:
        used.add(rid)
    items = []
    for rid in pick:
        r, v = req[rid], rev.get(rid, {})
        items.append({'id': rid, 'title': r['title'], 'statement': r['statement'], 'provenance': r.get('provenance'), 'legal_status': r.get('legal_status'),
                      'source': r['sources'][0]['id'], 'location': r['sources'][0].get('location', ''), 'plane': r.get('plane'),
                      'reword': str(v.get('verdict', '')).startswith('reword'), 'check': v.get('verification_ready')})
    out.append({'theme': t['id'], 'requirements': items})
n = sum(len(o['requirements']) for o in out)
yaml.safe_dump(out, open(f'{ROOT}/_data/brief-selection.yml', 'w'), sort_keys=False, width=200, allow_unicode=True)
print(n, 'requirements selected for', len(out), 'themes')
if n > 30: sys.exit('more than 30')
