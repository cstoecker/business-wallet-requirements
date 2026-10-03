# 05 — Header and side navigation, and the deployment checks

Status: DRAFT · Date: 2026-10-03

## 1. Do we need a header navigation and a side navigation?

Yes, with different jobs. A single bar cannot carry a deep content tree (29 concepts, hundreds of requirements, ecosystem and legal pages) and the global actions at the same time.

| Element | Job | Content |
|---|---|---|
| **Side navigation** | where am I in the content, and what is next to it | the 8 entries (Start here with Concepts and Figure gallery, Requirements, Perspectives, Legal and compliance, Domains, Architecture, Traceability and graph, Ecosystem), collapsible, current page highlighted; Discussions as an external menu item |
| **Header bar** | global, content-independent actions | search, Discussions, Contact, GitHub; the logo returns home |
| **Status banner** | honesty about maturity | "Draft for review. Based on COM(2025) 838, which may change. Analysis, not legal advice." on every page |
| **Breadcrumbs** | orientation and deep links | theme breadcrumbs; the same hierarchy feeds BreadcrumbList JSON-LD |
| **Footer** | trust and legal | publisher, licence, Contact, Discussions, GitHub, Figures, llms.txt, sitemap, imprint and privacy (required before launch) |
| **On-page** | reading | related concepts in the article header, FAQ, figure captions with links to figure pages |

What is still missing, in priority order: imprint and privacy pages and self-hosted fonts (launch blockers); a generated glossary page; a "cite this page" block (BibTeX/CSL); previous/next links inside concept groups; a visible version and "last verified" date on every page; a 404 page with search; a cookie-free analytics decision (none is set up); a German-language decision (English only for now); a print stylesheet for PDF export; dark mode (the design system defines light surfaces only, so none is provided).

## 2. Deployment process

`.github/workflows/deploy.yml` runs on every pull request, on every push to `main`, weekly (Monday 05:17 UTC) and on demand.

1. Validate data, concept registry, concept articles and figures (`check_concepts.py`) and print counts by status.
2. Build with Jekyll (production environment, Pages base path).
3. Check the built site (`check_site.py`): metadata, one h1, valid JSON-LD graph, figure pages, robots.txt, sitemap with images, llms.txt, IndexNow key, broken internal links, and that **every concept page is in llms.txt, the sitemap and the concepts index** (or is correctly `noindex` while in preparation).
4. Link check on the built HTML (internal on every run).
5. On `main` only: publish the IndexNow key proof, upload and deploy the Pages artifact, then notify IndexNow with the deployed sitemap.

So whenever a concept article (or a figure, a source, an ecosystem page) is added, the same full set of checks runs again, and a pull request cannot merge in a state that CI rejects (enable branch protection with the build job as a required check). The pull request template carries the human checklist (research, sources, figures, brand review, named reviewer).

Not yet in the pipeline, to add: external link checking on the weekly run, an accessibility scan (axe or pa11y) and a spelling check. GitHub Pages must be enabled with source "GitHub Actions" by a repository admin.
