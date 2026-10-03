---
title: Use cases
parent: Perspectives
nav_order: 5
permalink: /perspectives/use-cases/
description: "Use cases of the European Business Wallet by sector and perspective (B2B, B2G, G2G, M2M), plus the use cases of the ecosystems Catena-X, WE BUILD, Manufacturing-X, Factory-X, energy data-X and CIRPASS-2."
keywords: [European Business Wallet use cases, EBW use cases, KYC KYB, B2G reporting, data spaces, digital product passport, trusted AI]
schema_type: CollectionPage
toc: true
last_verified: "2026-10-03"
---

# Use cases

What businesses and authorities can do with a European Business Wallet (EBW). Each use case leads to requirements in the [catalogue]({{ '/requirements/' | relative_url }}). *Draft.*

## EBW use cases by sector

Source: the [Spherity Research roadmap](https://spherity.github.io/spherity-research/ebw-roadmap.html) (2026), a Spherity publication and therefore a scenario description, not an official list. Details are added as concept articles and requirements are reviewed.

| Sector | What the EBW enables | Perspective |
|---|---|---|
| Financial services | Reusable KYC/KYB data, strong authentication, automated B2G reporting, simpler onboarding | B2B, B2G |
| Professional services | Firm identity, qualified eSeals, mandate credentials and trusted filings for auditors, law firms, tax advisors and notaries | B2G, B2B |
| Industry 4.0 | Linking machine identities to corporate credentials; provenance, quality and compliance in automated environments | M2M |
| Supply chain and ESG | Digital product passports, supplier declarations and ESG disclosures as verifiable credentials | B2B |
| Data space ecosystems | Trusted gateway for legal-entity onboarding and access control, for example in Gaia-X and Manufacturing-X | B2B, M2M |
| Critical infrastructure | Verified access for legal entities in energy, telecom, water and transport; support for NIS2 security measures | B2G, B2B |
| Trusted AI | Verifiable information about AI developers, providers and operators; mandates for agent delegation; registration in high-risk AI registries | B2G, A2A |
| B2G reporting and registry access | Standardised authentication towards EU portals (for example product, customs, procurement and financial reporting) | B2G |
| G2G integration | Trusted data exchange between authorities, mutual recognition of business attributes, once-only reporting | G2G |

Related concepts: [Concepts]({{ '/concepts/' | relative_url }}).

## Ecosystem use cases

Use cases published by the ecosystems; each ecosystem page lists the requirements it imposes. <span class="vtag v-todo">to verify</span> marks titles that come from a search summary only.

{% for eco in site.data.graph.ecosystems %}
### {{ eco.name }}

{{ eco.domain }}

{% assign ucs = site.data.graph.usecases | where: "ecosystem", eco.id %}
<ul>
{% for uc in ucs %}<li>{{ uc.title }}{% if uc.verification == "unverified" %} <span class="vtag v-todo">to verify</span>{% endif %}</li>
{% endfor %}</ul>
{% endfor %}

See also [Ecosystems and initiatives]({{ '/ecosystem/initiatives/' | relative_url }}) and the [business cases]({{ '/perspectives/business-cases/' | relative_url }}).
