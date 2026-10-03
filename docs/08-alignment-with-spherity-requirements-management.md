# 08 — Alignment with the Spherity requirements-management plugin

Status: DRAFT analysis. Source read: `spherity/claude-plugins`, plugin `spherity-requirements-management` (README, skill descriptions, glossary and review-format references). Not read in depth: the individual skill bodies and the Notion databases they use.

## 1. What the plugin is

Spherity's internal SDLC skills over Notion databases. Chain: **CR → SR → SwR → ARCH → WI → TC / Test Run → PRB → REL** (customer requirement, system requirement, software requirement, architecture item, work item, test case and run, problem report, release). Roles: sales, product owner, architect, developer, tester, release manager. It is product- and customer-driven and not public.

This site is different in purpose: a public requirements baseline derived from law, standards and ecosystem specifications. Chain: **source clause → obligation → requirement → building block → standard clause → conformance check ← scenario**. The two chains meet where an EBW requirement from this site becomes a customer-facing or product requirement in Spherity's own process. That bridge is out of scope here and should not be built without the product owner.

## 2. Mapping of concepts

| Plugin | This site | Note |
|---|---|---|
| CR (customer requirement) | ecosystem requirement statement or source obligation | origin outside the team |
| SR / SwR | EBW-CAT-NNN requirement (technology-neutral) | this site stops before software requirements |
| ARCH item | building block / architecture alternative | planes and ADRs |
| TC / Test Run | conformance check / test case | against conformance specifications |
| Feasibility Review (gate 2→3) | review gate before a requirement is `agreed` | adopt |
| Baselined ARCH, approved SR | tagged baseline release (SemVer, DOI) | adopt |
| Change Request with impact analysis | change to a published requirement | adopt |
| RTM check before release | coverage metrics and release check | adopt |
| Notion databases | `_data/graph/*.yml` in Git | different store, same discipline |

## 3. Rules to adopt as they are

1. **Propose, then write.** The authoring skills show the intended change and wait for approval; additive, self-evidencing records may use a one-line confirmation.
2. **Approval is a human act.** No skill marks a requirement approved, sets a baseline, or passes a release check.
3. **Unknown stays unknown.** Coverage and verification are never inferred; unknowns are reported as unknowns.
4. **Verbatim sources.** Quotes from law and standards are stored verbatim with the clause pointer.
5. **One name per thing.** A glossary decides the term; collisions (for example PR as pull request versus problem report) are resolved once.
6. **Change control.** Any change to an approved requirement needs a change record with the list of downstream artefacts that need re-approval; the graph computes the list from the edges.

## 4. Concrete changes proposed for this repository (not yet made)

- Requirement lifecycle in the schema: `draft`, `in-review`, `agreed`, `verified`, `obsolete` with explicit definitions (our docs/01 uses draft, proposed, agreed, verified; unify).
- A **review page template** for the review gate (verdict per requirement: ready, ready with conditions, not ready; numbered findings; recommendation), modelled on the plugin's feasibility review format, published under `/requirements/reviews/`.
- A **change request template** (`.github/ISSUE_TEMPLATE/change-request.yml`) with impact analysis fields generated from graph edges.
- A **release check** script that fails when a baseline contains requirements without source, without verification criterion, or with unresolved review findings (extends `check_concepts.py`).
- A glossary file with canonical terms and retired terms.

## 5. Where the plugin's conventions should not be copied

- Emoji verdict markers: fine on internal Notion pages, refused on the public Spherity-branded site (design hard rules); use text verdicts and shape.
- Customer-specific coverage vocabularies: not applicable to a public, source-driven baseline.
- Notion as store: we keep Git as the single source of truth so the site stays reproducible and citable.

## 6. Open questions

Does the product owner want an export from this site into the internal CR database? Which role signs the review gate for law-derived requirements (legal reviewer) and for standards-derived requirements (architect)? Should internal product facts (for example about VERA or EIDA) ever appear on this neutral requirements baseline? The default is no; the site describes requirements, not products.
