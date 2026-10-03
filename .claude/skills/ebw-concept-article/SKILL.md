---
name: ebw-concept-article
description: Write or update a concept article (for example Trust list, Control plane) on the European Business Wallet site, with sources, two figures, FAQ and checks. Use when asked for a concept article or when a registry entry moves from planned to draft.
---

# Concept article

Standard and checks: `docs/03-concept-articles.md`; registry `_data/graph/concepts.yml`; stubs by `python3 scripts/new_concept.py`; skeleton by `python3 scripts/new_concept.py --draft CON-ID`.

## Workflow

1. **Pick the concept** and read its registry entry (related concepts, requirement categories, definition). Related links must be symmetric.
2. **Research** in primary sources only (see `ebw-add-requirements` for retrieval tips). Register new sources first. Mark anything not read as `<span class="vtag v-todo">to verify</span>`; read ones may use `v-ok`.
3. **Write** all fifteen sections in order: Summary, Definition (include `concept-definition.html`), Why it matters, How it works (figure 1), Interaction flow (figure 2), Roles and responsibilities, Related concepts (`concept-ref.html`), Requirements and obligations, Standards and specifications, Design choices and alternatives, Examples, Open questions and limitations, Terms introduced, References (source IDs), Change log. Answer-first summary; no more than two em-dashes; no intensity words (seamless, unlock, leverage, empower, streamline, supercharge, world-class, enterprise-grade, next-generation); no emoji.
4. **Front matter:** `layout: concept`, `concept`, `parent: Concepts`, `grand_parent: Start here`, `permalink: /concepts/<slug>/`, `schema_type: TechArticle`, `figures` (one or two), `faq` (visible Q and A, they become FAQPage JSON-LD). Set the registry status to `draft` and remove `noindex` and `sitemap: false` (the checker requires them exactly while the status is planned or proposed).
5. **Figures:** copy the style of `scripts/gen_trustlist_figs.py` (tokens only, Archivo and IBM Plex Mono, straight lines, 12 px radius, SVG `<title>`, `<desc>` and `<metadata>`), render with `bash scripts/render-figures.sh`, add `_figures/<slug>.md` with alt, caption, description, keywords and `used_in`.
6. **Checks and publish:** `ebw-site-build-preview`; add a changelog entry.
