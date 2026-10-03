---
name: ebw-add-requirements
description: Research and add requirements to the European Business Wallet catalogue from official sources, categorised and traced. Use when new law, standards or ecosystem specifications come into scope, when gaps are found, or when the user asks for research on requirements.
---

# Add requirements from sources

Rules (from docs/01 and docs/08): sources are official documents, standards and ecosystem specifications (Catena-X, Gaia-X, IDTA, WE BUILD, Manufacturing-X and related) plus the OID 2025 paper; no blogs or vendor pages; only high-level requirements from AAS, Catena-X and IDSA (AAS is an implementation artefact). One obligation per requirement, EARS style with the word "shall", technology-neutral. Provenance L (law in force or proposal text), S (standard or specification), D (derived, derivation stated in the rationale), A (assumption). Never present unverified legal facts as verified; use "to verify". No emoji.

## Workflow

1. **Scope and duplicates.** Name the instrument and articles. Grep `_requirements/` for the citation first. Categories are in `_data/categories.yml` (FUN, NFR, INT, TRU, CER, GOV, LEG, DAT, OPS, DOM, AIF, BIZ, CON, TRN); clusters in `_data/graph/clusters.yml`.
2. **Research agents.** Give each agent one instrument family, the schema in `scripts/import_candidates.py` (keys: key, title, category, statement, rationale, source, location, quote, provenance, legal_status, plane, perspectives, actors, verification_method, concepts), and these rules: read the full text (EUR-Lex returns an empty bot-challenge page; use `publications.europa.eu/resource/celex/<CELEX>` with `Accept: application/xhtml+xml`), quote verbatim at most 25 words, put the exact article or clause in `location`, register new sources in a separate `new_sources` file.
3. **Verify.** Machine-check every quote as a whitespace-normalised substring of the source text. Reject statements that exceed the clause (typical errors: wrong duty-holder, dropped conditions, "should" hardened to "shall", recitals phrased as duties). A directive binds Member States; GDPR binds the controller, CRA the manufacturer, NIS2 essential and important entities, AI Act the provider or deployer: a wallet provider mapping is a derivation (class D).
4. **Register sources:** `python3 scripts/register_sources.py FILE.yml`. Classes: official, standard, ecosystem-specification, paper, academic.
5. **Import:** `python3 scripts/import_candidates.py FILE.yml` (dry run), then `--write`. IDs continue per category as `EBW-<CAT>-<NNN>`; IDs are immutable once published. Legal status `proposal` must cite the proposal or the Council text.
6. **Tag and review:** run the `ebw-requirements-review` skill so every requirement gets clusters, priority and a review proposal.
7. **Checks and publish:** `ebw-site-build-preview` skill. Add a changelog entry in `_data/changelog.yml`.

## Quality bar

Statement within the quote's reach; location exact; rationale one sentence; actors named as in the source; no duplicates (merge instead); status `draft`, reviewer `pending` until a named human reviews.
