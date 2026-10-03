# 04 — SEO, AEO and GEO: schema, crawlers, discovery, measurement

Status: DRAFT proposal. Follows the Spherity site SEO skill (domain-wide layer). This is a proposal that needs review by the responsible roles; it is not a final decision.

Property: this repository's GitHub Pages site (planned `https://spherity.github.io/business-wallet-requirements`) · Type: research-style property with a public requirements baseline · Article level: the concept articles also need the structure check of the article-level SEO skill (not installed in this account; the structure rules are built into the concept template).

## 1. Schema.org graph strategy (implemented)

One `@graph` per page (`_includes/head_custom.html`) with stable `@id`s: `Organization` (publisher Spherity GmbH) and `WebSite` on every page; `WebPage`, `CollectionPage` or `TechArticle` per page type; `BreadcrumbList` from the navigation hierarchy; `DefinedTerm` inside a `DefinedTermSet` for concepts; `FAQPage` only when the same questions are visible on the page; `ImageObject` for every figure (name, caption, description, contentUrl, width, height, keywords, licence, creator) on the figure page and on every page that uses it. Open Graph and Twitter cards on every page. Rule kept: no schema without visible, true content.

## 2. Crawler permissions (robots.txt) — decision pending

- Classic search crawlers and user-initiated answer-engine fetchers are allowed explicitly (Googlebot, Bingbot, DuckDuckBot, Applebot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, social preview bots).
- **AI model-training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot and similar): no decision has been taken.** The skill requires explicit approval after Legal review, documented with date and reason. Until then they fall under the catch-all group; the file says this in a comment. Open item for Legal.
- Note for comparison: the existing Spherity research site documents an explicit open-access policy including training crawlers; whether this site follows it is the same decision.

## 3. Discovery (implemented)

- `sitemap.xml` generated with canonical URLs, `lastmod` from `last_verified` and image entries for every figure; pages that are `noindex` are excluded.
- `llms.txt` generated from the registry (published concepts only), ecosystem pages, methodology and figures; states that it is a discovery aid, not a ranking or training promise.
- **IndexNow** (the requested "inspectnow", interpreted as IndexNow; tell us if something else was meant): key file in the repository root, `scripts/notify-indexnow.mjs`, a `notify-indexnow` deployment job after the Pages deploy; the key can be overridden with the repository secret `INDEXNOW_KEY`. The job never fails a deployment.
- Canonical URL on every page; the production host must be fixed before launch (custom domain or GitHub Pages) and then set in `_config.yml` (`url`, `baseurl`) and the workflow variable `SITE_URL`.
- Thin stubs (`planned`, `proposed`) are `noindex` until an article exists.

## 4. Search-language research

`_data/search-research.yml` holds authority terms (European Business Wallet, EBW, EBWOID, legal person identity, business wallet requirements, requirements traceability), discovery terms and audience questions. **Google Trends was not queried**: it is a manual research tool and the automated build and the authoring assistant cannot use it. A person must compare the terms in Trends Explore (past 12 months and 5 years; Germany, other EU markets, worldwide; Web and News), record the result and set `status: reviewed`. Trends data informs wording only; it never validates technical or legal claims.

## 5. Measurement after launch

Google Search Console (indexed pages, sitemap processing, queries, impressions, clicks, rich-result problems) and Bing Webmaster Tools; compare at least 8-12 weeks; treat AI-referrer data as incomplete; report only observed data, never promised rankings, snippets or citations.

## 6. Launch blockers (not SEO, but required for a public Spherity-branded site)

Imprint and privacy notice (set `imprint_url`, `privacy_url`; the footer shows them when set, the checker warns); fonts: the design system loads Archivo and IBM Plex Mono from Google Fonts, which transfers visitor IP addresses to a third party, so self-host the licensed font files before launch; confirm CC BY 4.0 and the code licence; decide on contact-form handling (currently a mailto form, no data stored).
