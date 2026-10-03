---
title: Architecture decisions
parent: Architecture
nav_order: 1
has_children: true
permalink: /architecture/decisions/
description: "Architecture decisions derived from the clustered requirements for the European Business Wallet: the question, the requirements that drive it, criteria, options and open points."
keywords: [European Business Wallet architecture, architecture decisions, credential format, employee wallet, decision criteria]
schema_type: CollectionPage
last_verified: "2026-10-03"
---

# Architecture decisions

The [clustered requirements]({{ '/requirements/review/' | relative_url }}) force a small number of architecture decisions. Each decision names the question, the requirements that drive it, the criteria, the options and what the sources leave open. *Analysis for decision, not a decision. Where the sources do not settle a point, the page says so.*

How to read a decision page: criteria marked **source** come from a law, standard or specification and carry a reference; criteria marked **driver** are architecture or business drivers that no source states. Drivers are assumptions of this project (provenance class A) until a stakeholder confirms them.

{% for d in site.data.graph.decisions %}
<h2 id="{{ d.id | downcase }}">{{ d.id }}: {{ d.title }}</h2>

{{ d.question }}

{% if d.page %}<p><strong>Status: analysis written.</strong> <a href="{{ d.page | relative_url }}">Read {{ d.id }}</a></p>{% else %}<p><strong>Status: planned.</strong> Question defined, analysis pending.</p>{% endif %}

Clusters:
{%- for c in d.clusters %} {{ c }}{% unless forloop.last %},{% endunless %}{% endfor %}
{% endfor %}
