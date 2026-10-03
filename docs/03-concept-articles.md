# 03 — Concept articles: standard, figures and the future authoring skill

Status: DRAFT · Date: 2026-10-03 · Applies to `/concepts/*`

## 1. Purpose

Each basic concept (control plane and policy engine, data plane, trust plane, knowledge graph, evidence graph, DSP/DCP integration, wallet and connector binding, B2G reporting, B2G registry obligations, authority access, trusted AI with agent mandate, AISP and AI safety, multi-trust domains, cross-sector credential use, trust list, trust list discovery, levels of assurance, EBW and EUDI Wallet interaction, EBW and DPP integration, and the proposed additions) is one article. Articles are modular: they reference each other through the registry, so an article can be read alone and the set can grow.

The registry is `_data/graph/concepts.yml` (29 entries: 21 planned, 8 proposed). Each entry is a `Concept` entity in the knowledge graph with `related` edges (kept symmetric by the checker).

## 2. Standard article structure (in this order)

| # | Section | Rule |
|---|---|---|
| 1 | Summary | 2-3 sentences, self-contained, quotable by an answer engine without losing qualifications |
| 2 | Definition | `include concept-definition.html`; add what the concept is not |
| 3 | Why it matters | problem, affected parties, effect on B2B, B2G and B2C |
| 4 | How it works | mechanism in plain language; **Figure 1** (concept model) |
| 5 | Interaction flow | steps over time; **Figure 2** (flow) |
| 6 | Roles and responsibilities | actors and duties |
| 7 | Related concepts | `include concept-ref.html`, one sentence per relationship |
| 8 | Requirements and obligations | linked requirement IDs and legal sources |
| 9 | Standards and specifications | clause-level references |
| 10 | Design choices and alternatives | options and trade-offs |
| 11 | Examples | 2-3 short scenarios from different domains |
| 12 | Open questions and limitations | what is unsettled; "to verify" tags |
| 13 | Terms introduced | feeds the glossary |
| 14 | References | source register IDs (`SRC-*`) with version and date |
| 15 | Change log | date, change, reviewer |

Front matter: `title`, `layout: concept`, `concept` (registry ID), `parent: Concepts`, `grand_parent: Start here`, `description` (120-300 characters, answer-first), `permalink`, `schema_type: TechArticle`, `keywords`, `last_verified`, `figures` (1-2 figure slugs), `faq` (visible question and answer pairs that also produce FAQ JSON-LD). While the status is `planned` or `proposed` the page is `noindex` and excluded from the sitemap; the checker enforces this and flips it when the status becomes `draft` or higher.

`scripts/new_concept.py --draft CON-ID` writes the skeleton with all sections and a hint under each.

## 3. Definitions and sources

- One-sentence working definition in the registry; the article owns the full, referenced definition.
- Sources only from the source register: official documents, standards, ecosystem specifications and the OID 2025 paper. Anything else is background reading outside the graph.
- A claim that could not be verified in a source that was read carries a "to verify" tag. Legal text is analysis, not legal advice.
- AISP and AI safety have no verified definition yet; they stay `planned` until the cited sources are read (the acronym is not expanded without a source).

## 4. Figures

Each article has one or two conceptual figures.

- **Figure 1, concept model:** entities as boxes, relationships as labelled lines with cardinality marks, bands for planes or domains; the wallet or subject of the article is the one highlighted entity (Cyan). This follows the WE BUILD concept-model convention.
- **Figure 2, flow:** boxes and labelled arrows over time, group frames for who is responsible, a loop for rejection or retry, a dark box for the checked outcome. This follows the WE BUILD process-figure convention.
- **Brand adaptation.** The Spherity design system refuses hand-drawn wobbly-line SVG and a second accent colour. The figures therefore keep the WE BUILD structure (concept-model layout, group frames, labelled arrows, loop) but use Petrol, Off-White and Cyan tokens, Archivo and IBM Plex Mono, straight lines and 12px radius. If a literal WE BUILD look is wanted for an external audience, that needs a conscious exception.
- **Files:** `assets/figures/<slug>.svg` (with `<title>`, `<desc>` and Dublin Core/CC `<metadata>`), `<slug>.png` (rendered by `scripts/render-figures.sh`), and `_figures/<slug>.md` with `title`, `alt`, `caption`, `description`, `keywords`, `figure_type`, `used_in`, `width`, `height`, `last_verified`. Each figure gets its own landing page (`/figures/<slug>/`), a gallery entry, `ImageObject` JSON-LD and an image entry in the sitemap.
- Alt text describes the content (at least 40 characters); the caption states what the reader should take away.

## 5. Quality gates (automated and human)

Automated (CI, every pull request and weekly): `scripts/check_concepts.py` (IDs, references, symmetry, sections and their order, 1-2 figures, figure metadata, SVG title/desc/metadata, noindex rule, no emoji, no intensity words, at most two em-dashes) and `scripts/check_site.py` (title, description, canonical, Open Graph, one h1, one valid JSON-LD graph, no duplicate `@id`, figure pages with `ImageObject`, robots.txt, sitemap with images, llms.txt, IndexNow key, internal links, every concept page in llms.txt, sitemap and the concepts index).

Human: named reviewer; legal reviewer for law-derived content; Spherity brand review (`spherity-brand-review` skill); search-language review (`_data/search-research.yml`, to be completed in Google Trends).

## 6. Specification of the future skill "concept-article"

Goal: write one article per run and update the site.

1. **Pre-flight:** pick the concept ID (registry), confirm status, audience and perspectives (B2B, B2G, B2C).
2. **Research:** read the official sources and standards named in the registry and source register; read the ecosystem pages; record new sources in `sources.yml` with version, date, URL and verification state. No unregistered source may be cited.
3. **Draft:** run `new_concept.py --draft`, write all sections; summary answer-first; 2-3 examples from different domains; "to verify" tags where needed.
4. **Figures:** one concept model and one flow in the Spherity-token style, with SVG metadata, PNG, `_figures` page; alt text and caption.
5. **Cross-links:** update `related` on both sides; reference at least two other concepts; add terms to the glossary.
6. **Site updates:** registry status, front matter (`noindex` off when `draft`), `faq`, knowledge-graph edges to requirements and sources, `llms.txt` and sitemap are generated.
7. **Quality review:** run both checkers; self-review against the structure, brand rules and the claims list; invoke the brand and compliance skills; request a named human review.
8. **Handover:** pull request with the checklist from `.github/pull_request_template.md`.

Open decisions: who approves status changes from `draft` to `published`; whether the glossary becomes its own generated page (proposed: `_data/graph/terms.yml` plus `/glossary/`).
