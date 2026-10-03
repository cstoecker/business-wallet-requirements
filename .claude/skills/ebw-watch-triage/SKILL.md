---
name: ebw-watch-triage
description: Triage the weekly source-watch pull request of the European Business Wallet site (changes in laws, standards and ecosystem specifications) and turn confirmed changes into updates. Use when the weekly watch PR or its report arrives, or when asked what changed in the sources.
---

# Weekly watch triage

Design: `docs/11-weekly-watch.md`; watchlist `_data/watch/watchlist.yml`; state `_data/watch/state.json`; script `scripts/watch_sources.py`; workflow `.github/workflows/weekly-watch.yml` (Mondays 07:00 Europe/Berlin; extra sources: the Council working party on the EBW proposal and BMDS). The agent that opens the pull request never merges, approves or edits `robots.txt`.

## Steps

1. Read the changes per source (new version, date, hash). Open each changed original and read the relevant clause; the watch report is a pointer, not evidence.
2. Classify: law (proposal, Council text, Parliament report, adoption), standard (version change), ecosystem (new release or ADR), or noise.
3. For each real change: update the source entry (version, date, `retrieved`, note), re-check the requirements citing it (`grep -l <SRC-ID> _requirements/`), run the fidelity check for those whose clause moved, add or retire requirements, and add a `_data/changelog.yml` entry (type law, standard or ecosystem).
4. If the EBW proposal text changes, re-check the `legal_status: proposal` requirements and the roadmap page (`/legal/roadmap/`, `scripts/gen_roadmap.py`), and note which decisions in `/architecture/decisions/` are affected.
5. Run `ebw-site-build-preview`. Report what changed, what was verified in the original, and what remains to verify.
