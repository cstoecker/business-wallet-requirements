---
title: Review list
parent: Requirements
nav_order: 2
permalink: /requirements/review/
description: "Review worklist for the draft requirements: priority, architecture decision cluster, applicability and the proposed review action for every requirement."
keywords: [requirements review, requirements prioritisation, requirements clustering, architecture decisions]
schema_type: CollectionPage
toc: true
last_verified: "2026-10-03"
---

# Review list

The draft requirements were reviewed in a first pass for wording, fidelity to the source, applicability to a European Business Wallet, priority and the architecture decision they bear on. The result is a worklist for the human reviewer. *The review actions are proposals; the requirement texts have not been changed unless the requirement page says so.*

{% assign rv = site.data.review.requirement-review %}{% assign p1 = rv | where: "priority", "P1" | size %}{% assign p2 = rv | where: "priority", "P2" | size %}{% assign p3 = rv | where: "priority", "P3" | size %}

## Summary

| Measure | Count |
|---|---|
| Requirements reviewed | {{ rv.size }} |
| Priority P1 (mandatory and architecture-shaping) | {{ p1 }} |
| Priority P2 (mandatory but local, or derived from a standard) | {{ p2 }} |
| Priority P3 (peripheral, procedural or organisational) | {{ p3 }} |
| Proposed: reword | {{ rv | where: "verdict", "reword" | size }} |
| Proposed: split into several requirements | {{ rv | where: "verdict", "split" | size }} |
| Proposed: merge with another requirement | {{ rv | where: "verdict", "merge-with" | size }} |
| Proposed: move to another category | {{ rv | where: "verdict", "recategorise" | size }} |
| Proposed: drop | {{ rv | where: "verdict", "drop" | size }} |
| No change proposed | {{ rv | where: "verdict", "ok" | size }} |

**Priority.** P1 is a mandatory obligation, or an obligation in the Commission proposal, that shapes the architecture and is hard to change later. P2 is mandatory but local to an implementation, or derived from a standard. P3 is peripheral: procedures of authorities, publication duties and organisational rules.

## Architecture decision clusters

Each requirement is tagged with one to three clusters, the primary one first. A cluster with a decision link feeds an [architecture decision]({{ '/architecture/decisions/' | relative_url }}).

| Cluster | Requirements (any tag) | P1 | Decision |
|---|---|---|---|
{%- for c in site.data.graph.clusters %}
{%- assign cn = 0 -%}{%- assign c1 = 0 -%}
{%- for x in rv %}{% if x.clusters contains c.code %}{% assign cn = cn | plus: 1 %}{% if x.priority == "P1" %}{% assign c1 = c1 | plus: 1 %}{% endif %}{% endif %}{% endfor %}
| **{{ c.code }}** {{ c.name }}. {{ c.summary }} | {{ cn }} | {{ c1 }} | {% if c.decision %}[{{ c.decision }}]({{ '/architecture/decisions/' | relative_url }}#{{ c.decision | downcase }}){% else %}none yet{% endif %} |
{%- endfor %}

## Worklist

Sorted by priority, then by ID. *Cl.* lists the clusters; *Proposal* is the proposed review action.

{% assign prs = "P1,P2,P3" | split: "," %}{% for pr in prs %}
### Priority {{ pr }}

<div class="table-scroll" markdown="0"><table><thead><tr><th>ID</th><th>Title</th><th>Cl.</th><th>Applies to</th><th>Proposal</th><th>Note</th></tr></thead><tbody>
{%- for x in rv %}{% if x.priority == pr %}
{%- assign r = site.requirements | where: "req_id", x.id | first %}
<tr><td><a href="{{ r.url | relative_url }}">{{ x.id }}</a></td><td>{{ r.title }}</td><td>{{ x.clusters | join: ", " }}</td><td>{{ x.applicability }}</td><td>{{ x.verdict }}{% if x.verdict_arg %} {{ x.verdict_arg }}{% endif %}</td><td>{{ x.note | default: x.priority_reason }}</td></tr>
{%- endif %}{% endfor %}
</tbody></table></div>
{% endfor %}
