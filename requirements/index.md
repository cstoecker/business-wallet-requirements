---
title: Requirements
nav_order: 2
has_children: true
permalink: /requirements/
description: "Requirements for European Business Wallets and trust infrastructure, broken down by category and traced to law, standards and ecosystem specifications. Draft requirements with provenance, status, sources and an Excel download."
keywords: [European Business Wallet requirements, requirements catalogue, trust requirements, eIDAS requirements, requirements by category]
schema_type: CollectionPage
last_verified: "2026-10-03"
---

# Requirements

Each requirement is atomic, technology-neutral and traced to a source. They are grouped into 14 categories and can be filtered by category, status, provenance and text. How they are written and reviewed is described in the [requirements management methodology](methodology/).

<div class="status-note" role="note"><strong>Draft.</strong> {{ site.requirements.size }} requirements are derived from sources that were read in the original text. None has been reviewed by a named person yet, and those marked "proposal" follow the Commission proposal COM(2025) 838, which may change. Another {{ site.data.graph.ecosystem-requirements.size }} statements from ecosystems are candidates that still have to be derived.</div>

<p><a class="btn btn-primary" href="{{ '/assets/downloads/ebw-requirements.xlsx' | relative_url }}">Download Excel</a> <a class="btn" href="{{ '/downloads/' | relative_url }}">All downloads</a></p>

## Breakdown by category

<div class="cat-grid">
{% for c in site.data.categories %}
{% assign n = site.requirements | where: "category", c.code | size %}
{% assign k = site.data.graph.ecosystem-requirements | where: "category", c.code | size %}
<a class="cat-card" href="#all" data-cat="{{ c.code }}" aria-label="{{ c.name }}: {{ n }} requirements, {{ k }} candidates">
  <span class="cat-head">{% include icon.html name=c.icon size="lg" %}<span class="cat-code">{{ c.code }}</span></span>
  <strong>{{ c.name }}</strong>
  <span class="cat-scope">{{ c.scope }}</span>
  <span class="cat-count">{{ n }} requirement{% if n != 1 %}s{% endif %} · {{ k }} candidate{% if k != 1 %}s{% endif %}</span>
</a>
{% endfor %}
</div>

## All requirements {#all}

<form class="req-filter" id="req-filter" aria-label="Filter requirements">
  <label>Category
    <select id="f-cat"><option value="">All</option>{% for c in site.data.categories %}<option value="{{ c.code }}">{{ c.code }} {{ c.name }}</option>{% endfor %}</select>
  </label>
  <label>Status
    <select id="f-status"><option value="">All</option><option>draft</option><option>in-review</option><option>agreed</option><option>verified</option><option>obsolete</option></select>
  </label>
  <label>Provenance
    <select id="f-prov"><option value="">All</option><option value="L">L law</option><option value="S">S standard</option><option value="D">D derived</option><option value="A">A assumption</option></select>
  </label>
  <label>Search
    <input id="f-q" type="search" placeholder="Text, ID or source">
  </label>
</form>
<p id="req-count" class="mono" aria-live="polite"></p>

<div class="table-scroll">
<table id="req-table">
<thead><tr><th>ID</th><th>Requirement</th><th>Provenance</th><th>Status</th><th>Legal status</th><th>Sources</th></tr></thead>
<tbody>
{% assign rs = site.requirements | sort: "req_id" %}
{% for r in rs %}
<tr data-cat="{{ r.category }}" data-status="{{ r.status }}" data-prov="{{ r.provenance }}">
<td><a href="{{ r.url | relative_url }}">{{ r.req_id }}</a></td>
<td>{{ r.statement }}</td>
<td>{{ r.provenance }}</td>
<td><span class="badge badge-{{ r.status }}">{{ r.status }}</span></td>
<td>{{ r.legal_status }}</td>
<td>{% for s in r.sources %}{{ s.id }}, {{ s.location }}{% unless forloop.last %}; {% endunless %}{% endfor %}</td>
</tr>
{% endfor %}
</tbody></table>
</div>

<script>
(function () {
  var rows = Array.prototype.slice.call(document.querySelectorAll("#req-table tbody tr"));
  var f = { cat: document.getElementById("f-cat"), status: document.getElementById("f-status"), prov: document.getElementById("f-prov"), q: document.getElementById("f-q") };
  var count = document.getElementById("req-count");
  function apply() {
    var n = 0, q = f.q.value.trim().toLowerCase();
    rows.forEach(function (r) {
      var ok = (!f.cat.value || r.dataset.cat === f.cat.value) && (!f.status.value || r.dataset.status === f.status.value) &&
               (!f.prov.value || r.dataset.prov === f.prov.value) && (!q || r.textContent.toLowerCase().indexOf(q) > -1);
      r.hidden = !ok; if (ok) n++;
    });
    count.textContent = n + " of " + rows.length + " requirements shown";
  }
  Object.keys(f).forEach(function (k) { f[k].addEventListener("input", apply); });
  document.querySelectorAll(".cat-card").forEach(function (c) {
    c.addEventListener("click", function () { f.cat.value = c.dataset.cat; apply(); });
  });
  apply();
})();
</script>
