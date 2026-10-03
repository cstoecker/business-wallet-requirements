---
name: ebw-decision-page
description: Create or update an architecture decision page (DEC-nn) for the European Business Wallet from the clustered requirements and research notes. Use when a cluster has several P1 requirements and several plausible options, or when asked to derive design decisions, patterns or alternatives.
---

# Architecture decision page

Chain: requirement -> cluster (K01 to K17) -> decision (DEC-nn) -> pattern -> building block. Register in `_data/graph/decisions.yml` (id, title, question, clusters, status planned or draft, page). A cluster becomes a decision when it has several P1 requirements and at least two options that differ on criteria that matter; otherwise it is a constraint set. Method text: `/architecture/decisions/` and `docs/13-from-requirements-to-decisions.md`.

## Research first

Run a research pass that returns facts only (verbatim quotes of at most 25 words, location, read state, source ID), a neutral list of criteria and, per option, what the sources enable, restrict and leave open. Save it under `docs/research/`. No recommendation in the research.

## Page form (`architecture/decisions/dec-nn.md`, `parent: Architecture decisions`)

Question; What the requirement set says (`{% include cluster-drivers.html cluster="K0x" %}`); Facts from the sources; Decision criteria (each marked **source** with reference or **driver**, an architecture or business driver no source states, class A until a stakeholder confirms); Options with Enables, Restricts, Leaves open; Assessment against the criteria ("Not stated" is not a negative); Preliminary reading (labelled as this project's analysis) with conditions and what would change it; Gaps and next steps; References (source IDs).

## Rules

- Do not rank without saying what would change the reading; weights belong to stakeholders.
- Say plainly what could not be read (annexes, paywalled standards, outcomes of meetings).
- The Commission proposal and the Council text differ; cite which one.
- Keep requirements protocol-neutral; protocol-specific text becomes a profile.
- After the page: write the requirements the gaps imply (`ebw-add-requirements`), update the decision status and the review page links, run `ebw-site-build-preview`.
