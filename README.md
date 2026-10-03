# European Business Wallet Requirements

Open, traceable requirements for European Business Wallets and trust infrastructure: from law and standards to obligations, requirements, building blocks, conformance checks and industry scenarios. Draft for review. Based on the Commission proposal COM(2025) 838, which may change. Analysis, not legal advice.

- Method, structure and plans: `docs/` (01 methodology and site structure, 02 research and project plan, 03 concept articles, 04 SEO/AEO/GEO and indexing, 05 navigation and deployment, 06 presentation plan, 07 discussions).
- Site: Jekyll with the Just the Docs theme and Spherity design tokens. Data in `_data/graph/` (sources, ecosystems, use cases, ecosystem requirements, concepts); articles in `concepts/`; figures in `assets/figures/` and `_figures/`.
- Checks: `python3 scripts/check_concepts.py` and, after `bundle exec jekyll build`, `python3 scripts/check_site.py _site`.
- Contact: info@spherity.com. Discussions: https://github.com/spherity/business-wallet-requirements/discussions
