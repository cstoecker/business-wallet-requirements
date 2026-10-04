---
title: Stakeholder brief
parent: Architecture
nav_order: 2
permalink: /architecture/brief/
description: "Ten architecture themes and the key requirements behind them, prepared for discussion with Industry 4.0, IPCEI-AI and IDTA stakeholders: the question, the selected requirements with source and status, and one question to decide."
keywords: [European Business Wallet, stakeholder brief, Industry 4.0, IPCEI-AI, IDTA, architecture decisions, requirements]
schema_type: CollectionPage
toc: true
last_verified: "2026-10-04"
---

# Stakeholder brief

This page condenses the catalogue into ten themes for a discussion with Industry 4.0, IPCEI-AI and IDTA stakeholders. Each theme has one question, the requirements that constrain the answer most, what the sources leave open, and one question for the session. It is a working paper for discussion. It takes no position on the options and is not legal advice.

<div class="status-note" role="note"><strong>How the selection works.</strong> A script picks priority P1 requirements that concern the business wallet, drops duplicates, takes at most three per theme and adds named conflict items (<code>scripts/build_brief.py</code>). The first selection is a proposal for review. Each item shows its source, its legal status (in force, proposal, standard, ecosystem) and its provenance (L law, S standard, D derived). Derived items are derivations, not law.</div>

{%- assign themes = site.data.brief-themes -%}
{%- assign sel = site.data.brief-selection -%}
{%- assign total = 0 -%}
{%- for s in sel %}{% assign total = total | plus: s.requirements.size %}{% endfor %}

<p>{{ total }} requirements in {{ themes.size }} themes. Decision codes link to the <a href="{{ '/architecture/decisions/' | relative_url }}">decision pages</a> where they exist.</p>

## Overview

<div class="table-scroll"><table>
<thead><tr><th>Theme</th><th>Clusters</th><th>Decision</th><th>Selected</th></tr></thead>
<tbody>
{%- for t in themes %}{% assign s = sel | where: "theme", t.id | first %}
<tr><td><a href="#{{ t.id | downcase }}">{{ t.id }} {{ t.title }}</a></td><td>{{ t.clusters | join: ", " }}</td><td>{{ t.decision }}</td><td>{{ s.requirements.size }}</td></tr>
{%- endfor %}
</tbody></table></div>

Clusters K11 (security) and K13 (governance) apply to all themes as constraints and have no theme of their own.

{% for t in themes %}
{%- assign s = sel | where: "theme", t.id | first -%}
{%- assign dec = site.data.graph.decisions | where: "id", t.decision | first %}
## {{ t.id }} {{ t.title }}
{: #{{ t.id | downcase }} }

<div class="concept-meta"><dl>
<dt>Question</dt><dd>{{ t.question }}</dd>
<dt>Clusters</dt><dd>{{ t.clusters | join: ", " }}</dd>
<dt>Decision</dt><dd>{% if dec.page %}<a href="{{ dec.page | relative_url }}">{{ dec.id }}: {{ dec.title }}</a>{% else %}{{ dec.id }}: {{ dec.title }} <span class="vtag v-todo">{{ dec.status }}</span>{% endif %}{% if t.also %}; see also {{ t.also }}{% endif %}</dd>
<dt>Sources are silent on</dt><dd>{{ t.silent }}</dd>
</dl></div>

**Key requirements**

<div class="table-scroll"><table>
<thead><tr><th>Requirement</th><th>Statement</th><th>Source</th><th>Status</th></tr></thead>
<tbody>
{%- for r in s.requirements %}{% assign src = site.data.graph.sources | where: "id", r.source | first %}
<tr><td><a href="{{ '/requirements/' | append: r.id | downcase | append: '/' | relative_url }}">{{ r.id }}</a></td><td>{{ r.statement }}{% if r.reword %} <span class="vtag v-todo">rewording proposed</span>{% endif %}</td><td>{{ src.title | default: r.source }}, {{ r.location }}</td><td>{{ r.legal_status }}, {{ r.provenance }}{% if r.check and r.check != "yes" %}; {{ r.check }}{% endif %}</td></tr>
{%- endfor %}
</tbody></table></div>

**What each group needs from the answer**

- **Industry 4.0:** {{ t.lens.industry40 }}
- **IPCEI-AI:** {{ t.lens.ipceiai }}
- **IDTA:** {{ t.lens.idta }}

**Question for the session:** {{ t.session_question }}
{% endfor %}

## How to give feedback

Agree, disagree or missing, per theme. Comments on single requirements go through the <a href="{{ '/requirements/review/' | relative_url }}">review page</a>, which feeds the same loop as the review worksheet.
