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

## How decisions are derived

1. **Requirements are tagged with clusters.** A cluster is an architecture concern such as credential data model, wallet subject model, key custody or agent interoperability. Each requirement gets one to three clusters, the primary one first. The cluster list is a fixed starting set that follows the architecture planes and the quality concerns; it grows only when a requirement fits none (for example the AI-first cluster that was added when agent protocols and mandates came into scope).
2. **A cluster becomes a decision when two things hold.** It carries several architecture-shaping (P1) requirements, and at least two plausible options differ on criteria that matter. Otherwise it stays a set of constraints, as with governance and conformity, where the sources leave little design freedom.
3. **A decision page has a fixed form.** Question, the requirements that drive it, facts from the sources, criteria (marked *source* or *driver*), options with what the sources enable, restrict and leave open, an assessment against the criteria, a preliminary reading with its conditions, and what would change it. The weights of the criteria are set by stakeholders, not by the page.
4. **Patterns come from options.** When an option recurs across decisions, it is recorded as a reusable pattern (for example a format-independent semantic layer with bindings, or authority in the organisation's wallet with person-bound acts in the personal wallet). A pattern lists the requirements it satisfies and the decisions it appears in.
5. **Decisions depend on each other.** Credential formats (DEC-01), the employee wallet model (DEC-02) and agent mandates (DEC-10) share the mandate and semantics questions; the pages say where one decision constrains another.
6. **Status.** *Planned* (question defined), *draft* (analysis written, open), *proposed* (preliminary reading put to the deciders), *decided* (decision, date, decider and consequences recorded, then the requirements it implies are written or updated), *superseded*.
