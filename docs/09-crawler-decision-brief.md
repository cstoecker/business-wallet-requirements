# 09 — Decision brief: AI crawler permissions (for Legal)

Status: PROPOSAL for review by Legal. Not a decision. Prepared following the Spherity site SEO skill, which requires an explicit, documented decision for AI model-training crawlers and Legal escalation.

## 1. Question

Which AI crawlers may fetch the public European Business Wallet Requirements site, and does Spherity reserve rights against use of its content for model training?

## 2. Categories (current state in `robots.txt`)

| Category | Examples | Current state |
|---|---|---|
| Classic search | Googlebot, Bingbot, DuckDuckBot, Applebot | allowed explicitly |
| Answer-engine fetchers (user-initiated, live retrieval, with attribution) | ChatGPT-User, Perplexity-User, Claude-User, OAI-SearchBot, Claude-SearchBot, PerplexityBot | allowed explicitly |
| AI model-training crawlers | GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended and others | **no decision**; they fall under the catch-all group, which allows everything |

## 3. Facts that matter

- The site content is intended to be CC BY 4.0 (to be confirmed). That licence allows reuse with attribution, which is separate from crawler permissions.
- The existing Spherity research site documents an explicit open-access policy including training crawlers.
- The site's goal is to be cited and understood by policy makers, researchers and implementers, including through AI answer engines.
- The content is public, source-based analysis; it contains no personal data beyond author names and the contact address.
- Whether a robots.txt entry counts as a machine-readable reservation of rights under the EU text and data mining exception (Directive (EU) 2019/790, Article 4) and how that interacts with a CC BY licence are legal questions for Legal. Not verified here.

## 2. Options

| Option | robots.txt effect | For | Against |
|---|---|---|---|
| A. Allow all, documented | explicit `Allow` for training crawlers | maximum reach and citation; consistent with CC BY and the research site | no control over training use |
| B. Allow search and answer engines, disallow training | explicit `Disallow` for named training crawlers | keeps visibility in answer engines; reserves rights against training | inconsistent with CC BY intent; list of bots must be maintained; some bots ignore it |
| C. Allow, with conditions | A plus a published AI use policy and attribution request | signals expectations | not enforceable by robots.txt |

No recommendation is made here. The skill requires Legal to decide.

## 3. Snippets

Option A: add `User-agent: GPTBot` / `ClaudeBot` / `Google-Extended` / `CCBot` each followed by `Allow: /`.
Option B: the same user agents each followed by `Disallow: /`.

## 4. Decision record (to be completed by Legal)

| Field | Value |
|---|---|
| Decision | A / B / C |
| Date | |
| Decided by (name, role) | |
| Reason | |
| Scope (this site only, or all Spherity research properties) | |
| Review date | |
| robots.txt updated in commit | |

Escalation path: Design lead, then Legal (decision), then Information Security if sitemap or schema exposes non-public structure (not expected on this public site).
