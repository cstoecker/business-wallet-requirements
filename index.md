---
title: Start here
nav_order: 1
has_children: true
permalink: /
description: "Open, traceable requirements for European Business Wallets and trust infrastructure: what the European Business Wallet is, why it matters, what changed recently and where to start as policy maker, researcher, implementer or business leader."
keywords: [European Business Wallet, EBW, eIDAS 2.0, legal person identity, business wallet requirements, COM(2025) 838]
schema_type: WebPage
last_verified: "2026-10-03"
faq:
  - q: "What is the European Business Wallet?"
    a: "A digital wallet for companies and public bodies proposed by the European Commission on 19 November 2025 (COM(2025) 838). It lets an organisation identify itself, authenticate, sign and seal, hold and exchange verified attestations, and send and receive documents by qualified electronic registered delivery. It builds on the eIDAS framework and is interoperable with the EUDI Wallet of natural persons. It is a proposal and may change."
  - q: "Is the European Business Wallet mandatory for companies?"
    a: "The proposal sets obligations for public sector bodies, including having a wallet with registered delivery (Article 16). What it requires of businesses is to be checked in the article text, which may change in the legislative procedure."
  - q: "How big is the expected economic effect?"
    a: "The Commission states that the wallets could unlock up to EUR 150 billion in savings for businesses each year, assuming broad uptake. Its impact assessment gives a range with a minimum of about EUR 58 billion per year and shows costs next to benefits. See the business cases."
---

# European Business Wallet requirements

Open, traceable requirements for European Business Wallets and trust infrastructure. Every requirement is traced to law, a standard or an ecosystem specification, and every number to an official source. Draft for review; the European Business Wallet is still a Commission proposal.

## What is the European Business Wallet

On 19 November 2025 the European Commission proposed European Business Wallets (COM(2025) 838) as part of the Digital Package. A business wallet is a secure digital tool for economic operators and public sector bodies. Among the core functions in Article 5(1) are transmitting and receiving electronic documents and data through a qualified electronic registered delivery service and authorising relying parties to request attestations. The Commission also describes identification, signing and sealing, and mandate management for representatives; these details are to be checked against the article text. It extends the eIDAS framework from people to organisations and is meant to work with the EUDI Wallet of natural persons. Wallet providers are notified to a supervisory body and listed by the Commission, and a European Digital Directory serves as the trusted source of information on wallet owners.

## Why it matters

- **Scale.** The Commission's impact assessment counts about 32.7 million economic operators in the EU, 94% of them microenterprises, and about 95,800 public sector bodies.
- **Economics.** The Commission states that the wallets could unlock up to EUR 150 billion in savings for businesses each year with broad uptake; its own range for direct benefits starts at about EUR 58 billion, with costs shown separately. See the [business cases](perspectives/business-cases/).
- **Trust.** Reliable identification of organisations and their representatives underlies B2B, B2G and B2C processes: supplier onboarding, reporting to authorities, product passports, data spaces and AI agents that act for a company.
- **Open points.** The legislative text is still moving, standards are being written and several figures are modelled upper bounds. This site keeps the sources, versions and open questions visible.

## Where to start

<div class="path-grid">
<a class="path-card" href="{{ '/legal/' | relative_url }}">{% include icon.html name="scales-02" size="lg" %}<strong>Policy makers</strong><span>What the proposal says, its status and what changed. Start with the legal overview and the business cases.</span></a>
<a class="path-card" href="{{ '/concepts/' | relative_url }}">{% include icon.html name="microscope" size="lg" %}<strong>Researchers</strong><span>Concepts with sources, figures and open questions; the method and the knowledge graph.</span></a>
<a class="path-card" href="{{ '/requirements/' | relative_url }}">{% include icon.html name="code-02" size="lg" %}<strong>Implementers</strong><span>Requirements by category with sources and verification criteria; Excel download; ecosystems and standards.</span></a>
<a class="path-card" href="{{ '/perspectives/business-cases/' | relative_url }}">{% include icon.html name="briefcase-02" size="lg" %}<strong>Business leaders</strong><span>Costs, savings and risks at economy, ecosystem and company level, with every number sourced.</span></a>
</div>

## Recent developments

| Date | Type | Development | Source |
|---|---|---|---|
{% for n in site.data.news limit: 6 %}{% assign s = site.data.graph.sources | where: "id", n.source | first %}| {{ n.date }} | {{ n.type }} | **{{ n.title }}**. {{ n.summary }} | [{{ s.id }}]({{ s.url }}) |
{% endfor %}
Full list of confirmed changes: [What changed]({{ '/changelog/' | relative_url }}) (RSS: [feed]({{ '/feed.xml' | relative_url }})). Checked weekly against official sources and standards.

## Recent publications

| Date | Venue | Title |
|---|---|---|
{% for p in site.data.publications limit: 7 %}| {{ p.date }} | {{ p.venue }} | [{{ p.title }}]({{ p.url }}) |
{% endfor %}
More in [Research and reading]({{ '/research/' | relative_url }}) and at [Spherity Research](https://spherity.github.io/spherity-research/).

## Status of this site

Draft for review: {{ site.requirements.size }} draft requirements, {{ site.data.graph.concepts.size }} concept entries (one article so far), {{ site.data.graph.ecosystems.size }} ecosystems, {{ site.data.graph.claims.size }} traced claims in three business cases. Legal content is analysis, not legal advice. Questions, corrections and sources are welcome in the [discussions](https://github.com/spherity/business-wallet-requirements/discussions) or at [info@spherity.com]({{ '/contact/' | relative_url }}).

{% include faq.html %}
