# 11 — Weekly watch of laws and standards

Status: DRAFT design. The script, the watchlist, the baseline and the weekly workflow exist in the repository; the research agent is specified here and has not been scheduled.

## 1. Goal

Keep the site current without losing control of quality: find new or changed laws, implementing acts, standards and ecosystem specifications every week, propose precise updates and let a person decide.

## 2. Two layers

**Layer 1: watch script (deterministic, every Monday 06:00 UTC, before the agent).** `scripts/watch_sources.py` reads `_data/watch/watchlist.yml` (23 sources: ETSI trusted-list and identity standards, ARF releases, W3C, OpenID, Eclipse DSP and DCP, Catena-X, WE BUILD, plus entries for sources it cannot fetch, including the Council working party documents and the BMDS). It records version strings, page hashes or feed entries in `_data/watch/state.json` and writes a facts-only report. The GitHub workflow `.github/workflows/weekly-watch.yml` runs it and opens a pull request labelled `needs-review` with `docs/watch/<date>.md` and the new state. A baseline was recorded on 2026-10-03: for example TS 119 612 has versions 2.2.1, 2.3.1 and 2.4.1 in the ETSI folder, which confirms V2.4.1 as the newest listed there.

Limits found in the first run: the ARF, WE BUILD and rulebook GitHub feeds returned HTTP 403 from the build sandbox (they are expected to work from GitHub Actions; to be confirmed on the first scheduled run); the ETSI TS 119 472 folder name differs by part, so it is left to the agent; EUR-Lex pages block automated fetching, so legal sources are checked by the agent through search and the Legislative Observatory.

**Layer 2: research agent (weekly, after the script).** Reads the script report, checks the sources marked `fetch: agent` (the EBW procedure 2025/0358(COD) incl. Council and Parliament documents, eIDAS consolidated versions and implementing acts, ESPR and DPP delegated acts, NIS2/CRA/AI Act/DORA reporting rules, CEN and ETSI work programmes, IDTA publications), and for each real change prepares a pull request that:

1. adds or updates the entry in `_data/graph/sources.yml` (version, date, URL, verification state);
2. adds an entry to `_data/changelog.yml` (shown on `/changelog/` and in the RSS feed);
3. lists affected concepts, ecosystem pages and requirement candidates (using the `concepts` and `sources` links in the watchlist and the graph edges);
4. edits articles only where the change is clear; otherwise leaves a "to verify" note and a question in the pull request;
5. runs `check_concepts.py` and `check_site.py`.

## 3. Rules for the agent

- Official sources, standards and ecosystem specifications only; no blogs, press or vendor material as basis. News articles may point the agent to a primary document, but only the primary document is cited.
- Never merges, never approves, never marks a requirement agreed. A named human reviews every pull request.
- Quote verbatim with the article or clause number; mark anything it could not read as "to verify"; state when a source was unreachable.
- Treat proposals as proposals: no statement that a draft is law.
- Propose, then write: show the intended change first when it touches a published article.
- Report "no relevant change" explicitly instead of padding.

## 4. Agent prompt (for a scheduled routine)

"Every Monday after the weekly watch report: read `docs/watch/<latest>.md` in the repository `<repo>`. For each detected change and for each `fetch: agent` source in `_data/watch/watchlist.yml`, check the primary official source. Follow `docs/11-weekly-watch.md` section 3. Prepare one pull request on a new branch with source register, changelog and, where clear, article edits, and list uncertainties for the reviewer. If nothing relevant changed, post a one-line note and stop."

Schedule (decided 2026-10-03): Mondays at 07:00 Europe/Berlin, as a routine that starts a fresh session each time; it writes only to a branch `watch/<date>` of `cstoecker/business-wallet-requirements` and opens a pull request for review. Added sources by the owner's request: Council working party documents on the EBW proposal and the German Federal Ministry for Digital and State Modernisation (BMDS).

## 5. Open points

Which sources to add (Council working party documents, national transposition of NIS2, EDPB guidance, UNECE and other sector standards); whether the weekly report should also notify by email or chat; who owns the review rota.
