---
title: Concepts
parent: Start here
nav_order: 2
has_children: true
permalink: /concepts/
description: "Plain-language, referenced articles on the basic concepts behind European Business Wallets: control, data and trust planes, trust lists, levels of assurance, B2G reporting and registries, agent mandates, data-space integration and more."
keywords: [European Business Wallet concepts, trust plane, control plane, data plane, trust list, levels of assurance, B2G reporting, agent mandate, DSP, DCP]
schema_type: CollectionPage
last_verified: "2026-10-03"
figures: [concept-model-planes]
---

# Concepts

Each concept is an article with the same sections: summary, definition, why it matters, how it works (with figures), roles, related concepts, requirements, standards, design choices, examples, open questions, terms and references. Articles reference each other, so you can start anywhere. Concepts are also entities in the [knowledge graph](../traceability/).

{% include figure.html id="concept-model-planes" no=1 %}

{% assign groups = site.data.graph.concepts | group_by: "group" %}
{% for g in groups %}
## {{ g.name }}

| Concept | In one sentence | Status |
|---|---|---|
{% for c in g.items %}| [{{ c.title }}]({{ '/concepts/' | append: c.slug | append: '/' | relative_url }}) | {{ c.summary }} | {{ c.status }} |
{% endfor %}
{% endfor %}

Status *planned* means the article is in preparation; *proposed* means we suggest adding it. See the [concept article standard](https://github.com/spherity/business-wallet-requirements/blob/main/docs/03-concept-articles.md).
