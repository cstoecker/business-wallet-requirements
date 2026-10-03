#!/usr/bin/env python3
"""Weekly watch of official sources, standards and ecosystem specifications.

  scripts/watch_sources.py [--update] [--report FILE]

Reads _data/watch/watchlist.yml, fetches entries with fetch: auto, compares with _data/watch/state.json and writes a Markdown report.
With --update the state file is rewritten. Fetch failures are reported, never fatal. Entries with fetch: agent are listed for the weekly agent.
The script reports facts (new version strings, changed page hash, new feed entries). It never edits site content and never concludes what a change means.
"""
import hashlib, json, os, re, sys, urllib.request, datetime, html
import yaml
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
WL = os.path.join(ROOT, "_data/watch/watchlist.yml"); ST = os.path.join(ROOT, "_data/watch/state.json")
UA = "Mozilla/5.0 (compatible; EBW-requirements-watch/1.0; +https://github.com/spherity/business-wallet-requirements)"
def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=40) as r: return r.read().decode("utf-8", "replace")
def norm(t):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", t); t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()
def main():
    update = "--update" in sys.argv; out = sys.argv[sys.argv.index("--report") + 1] if "--report" in sys.argv else None
    wl = yaml.safe_load(open(WL, encoding="utf-8")); state = json.load(open(ST)) if os.path.exists(ST) else {}
    new_state, changes, errors, agent = {}, [], [], []
    for w in wl:
        if w["fetch"] == "agent": agent.append(w); continue
        try: body = fetch(w["url"])
        except Exception as e: errors.append((w, str(e)[:160])); new_state[w["id"]] = state.get(w["id"]); continue
        old = state.get(w["id"])
        if w["check"] == "versions":
            cur = sorted(set(re.findall(w["pattern"], body)))
            new_state[w["id"]] = {"versions": cur}
            added = [v for v in cur if old and v not in old.get("versions", [])]
            if added: changes.append((w, "new versions: " + ", ".join(added)))
            elif not old: changes.append((w, "baseline recorded: " + ", ".join(cur[-3:])))
        elif w["check"] == "atom":
            entries = re.findall(r"<entry>.*?<title[^>]*>(.*?)</title>.*?<updated>(.*?)</updated>", body, re.S)[:5]
            cur = [{"title": html.unescape(t.strip()), "updated": u.strip()} for t, u in entries]
            new_state[w["id"]] = {"latest": cur}
            seen = {e["updated"] for e in (old or {}).get("latest", [])}
            fresh = [e for e in cur if e["updated"] not in seen]
            if old and fresh: changes.append((w, "new entries: " + "; ".join(f"{e['title']} ({e['updated'][:10]})" for e in fresh)))
            elif not old: changes.append((w, "baseline recorded"))
        else:
            h = hashlib.sha256(norm(body).encode()).hexdigest()
            new_state[w["id"]] = {"hash": h, "length": len(norm(body))}
            if old and old.get("hash") != h: changes.append((w, "page content changed (length %s -> %s)" % (old.get("length"), len(norm(body)))))
            elif not old: changes.append((w, "baseline recorded"))
    today = datetime.date.today().isoformat()
    lines = [f"# Weekly watch report {today}", "", "Facts only. A person or the weekly agent decides what a change means. Official sources, standards and ecosystem specifications only.", ""]
    lines += ["## Changes detected", ""] + ([f"- **{w['title']}** ({w['id']}): {m}. {w['url']}" + (f" Affects concepts: {', '.join(w.get('concepts', []))}." if w.get("concepts") else "") for w, m in changes] or ["- none"])
    lines += ["", "## Fetch errors", ""] + ([f"- {w['title']} ({w['id']}): {e}" for w, e in errors] or ["- none"])
    lines += ["", "## For the weekly agent (not fetchable by script)", ""] + [f"- {w['title']} ({w['id']}): {w['url']}" for w in agent]
    rep = "\n".join(lines) + "\n"
    if out: open(out, "w", encoding="utf-8").write(rep)
    print(rep)
    if update: json.dump(new_state, open(ST, "w"), indent=1, sort_keys=True)
main()
