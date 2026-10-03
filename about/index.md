---
title: About
parent: Start here
nav_order: 6
permalink: /about/
description: "About the European Business Wallet Requirements site: purpose, publisher, how requirements are sourced, drafted and reviewed, disclosure of AI assistance and of the publisher's interests, corrections, licence and how to cite."
keywords: [about, European Business Wallet Requirements, methodology, publisher, corrections policy, how to cite]
schema_type: AboutPage
toc: true
last_verified: "2026-10-03"
---

# About

## Purpose

This site collects requirements for European Business Wallets and trust infrastructure and traces each one to a law, a standard or an ecosystem specification. It aims to be a reliable place to look things up: what the European Business Wallet is, what the sources say, where they disagree, and what is still open. It is a draft for review; the European Business Wallet is a Commission proposal (COM(2025) 838) and may change.

<div class="about-grid">
<div class="about-card">{% include icon.html name="check-done-02" size="lg" %}<h3>Traceable</h3><p>Every requirement cites a source with version, date and clause. Every number in the business cases cites a source and its basis.</p></div>
<div class="about-card">{% include icon.html name="scales-02" size="lg" %}<h3>Source-bound</h3><p>Only official documents, standards, ecosystem specifications, peer-reviewed papers (business cases only) and the Open Identity Summit 2025 paper are used as sources.</p></div>
<div class="about-card">{% include icon.html name="clipboard-check" size="lg" %}<h3>Reviewed</h3><p>A named person reviews every legal or derived requirement before it counts as agreed. No requirement has been reviewed yet.</p></div>
<div class="about-card">{% include icon.html name="clock-refresh" size="lg" %}<h3>Current</h3><p>Laws, standards and ecosystem specifications are checked every week. Confirmed changes appear on <a href="{{ '/changelog/' | relative_url }}">What changed</a>.</p></div>
</div>

## Who publishes this site

The site is published by Spherity GmbH. It is edited by Carsten Stöcker, who is also an author of the paper *Towards the European Business Wallet* (Open Identity Summit 2025, with T. Hühnlein, D. Hühnlein and S. Schwalm). Contact: [info@spherity.com]({{ '/contact/' | relative_url }}).

**Disclosure.** Spherity takes part in some of the ecosystems described here, for example the WE BUILD pilot and energy data-X, and publishes its own research ([Spherity Research](https://spherity.github.io/spherity-research/)). That research is listed as background reading and is never used as authority for a requirement. Where the publisher has an interest, the page says so.

## How requirements are made

Sources are registered with version, date and URL. Obligations are extracted with the clause, written as technology-neutral requirements, linked to concepts and standards, and reviewed by a named person. The steps, the 13 categories and the provenance classes (law, standard, derived, assumption) are on the [requirements management methodology]({{ '/requirements/methodology/' | relative_url }}) page. The [requirements]({{ '/requirements/' | relative_url }}) are available as [Excel and other downloads]({{ '/downloads/' | relative_url }}).

## Use of AI assistance

Research, drafting, figures and code for this site are prepared with the help of AI tools. A person decides what is published. Facts that could not be verified in a source that was read are marked "to verify", and legal text is analysis, not legal advice. The current draft requirements and concept articles were prepared with AI assistance and have not yet been reviewed by a named person.

## Corrections and feedback

If something is wrong, unclear or missing, tell us in the [discussions](https://github.com/spherity/business-wallet-requirements/discussions) or at [info@spherity.com]({{ '/contact/' | relative_url }}). Confirmed corrections are made in the data, recorded on [What changed]({{ '/changelog/' | relative_url }}) and, for requirements, in the requirement's history.

## Licence and citation

Content is licensed CC BY 4.0 (to be confirmed); figures can be reused with attribution. Please cite as:

> Spherity GmbH. *European Business Wallet Requirements* (draft). {{ site.time | date: "%Y" }}. {{ site.url }}{{ site.baseurl }}/ (accessed with date). A versioned release with a DOI is planned.

## Privacy and accessibility

The site sets no cookies and uses no analytics. At the moment the fonts are loaded from a third-party font service; self-hosting them is planned before the public launch. The pages use semantic headings, text alternatives for figures and keyboard-visible focus; please report barriers.
