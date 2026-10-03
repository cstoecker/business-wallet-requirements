---
name: ebw-requirements-review
description: Review draft requirements for fidelity, quality, priority and architecture clustering, and prepare the review worklist. Use after importing requirements or when asked to review, prioritise or cluster them.
---

# Review, prioritise and cluster requirements

Outputs live in `_data/review/requirement-review.yml` (generated) and are shown at `/requirements/review/` and in the Excel download. Requirement files are not changed by a review proposal.

## Passes

1. **Quality and clustering pass** (parallel reviewers, about 50 requirements each, shards by category). Each reviewer reads statement, quote and rationale in `_requirements/<ID>.md` and writes a YAML list with: `id, fidelity (ok | broader-than-quote | narrower | derived-unmarked), verdict (ok | reword | split | merge-with:<ID> | drop | recategorise:<CAT>), corrected_statement, applicability (core | wallet-general | provider-side | relying-party-side | authority-side | horizontal), priority (P1 mandatory and architecture-shaping | P2 mandatory but local or standard-derived | P3 peripheral), priority_reason, clusters (1 to 3 of K01 to K17, primary first), verification_ready, note`. Tell reviewers that `quote` fields exist (an earlier pass wrongly reported none) and that provenance D items state their derivation in the rationale.
2. **Merge:** `python3 scripts/merge_review.py R1.yml R2.yml ...` (validates ids, clusters, categories; must report 0 problems and cover every requirement).
3. **Fidelity pass against the full text** for items flagged broader-than-quote or derived-unmarked (the stored quote is truncated at 25 words, so the extract alone cannot prove or disprove overreach). Verifier agents read the clause in the original, then return `supported | overreach | derived | wrong-location` with a corrected statement and a longer verbatim passage. Apply with `python3 scripts/apply_fidelity.py F.yml` (updates statement, location, provenance, rationale, `full_quote`, `fidelity_checked`, `revision_note`).
4. **Apply verdicts only after a human decides** merge, split, drop and recategorise (IDs are immutable; a recategorisation renames the file and the ID).

## Reading the results

Counts per cluster and priority are on the review page; clusters with many P1 requirements and several plausible options become decisions (`ebw-decision-page` skill). Look for systematic issues: recitals phrased as duties, wrong duty-holders, protocol-specific text in a technology-neutral category, authority-side procedures rated P1.
