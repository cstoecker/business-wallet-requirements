---
title: Ecosystems & initiatives
parent: Ecosystem
nav_order: 1
has_children: true
permalink: /ecosystem/initiatives/
---

# Ecosystems & initiatives

European and national initiatives that use, or will use, wallets, credentials and trust infrastructure. For each one this section explains **what it does**, its **use cases** and the **high-level requirements** it places on identity, trust and wallets. Each initiative is an `Ecosystem` entity in the [knowledge graph](../../traceability/), linked to its use cases, requirement statements and sources.

**Scope rule.** Only high-level, technology-neutral requirements are taken from these initiatives. Specific implementations (for example AAS, specific connectors or products) are not requirements; AAS is assessed separately as an implementation artefact in the [architecture alternatives](../../architecture/). Sources are limited to official documents and ecosystem specifications; statements that could not be verified in a source that was read are marked 🔎.

| Initiative | Domain | Status (retrieved 2026-10-03) |
|---|---|---|
{% for e in site.data.graph.ecosystems %}| [{{ e.name }}]({{ e.id | remove: "ECO-" | downcase }}/) | {{ e.domain }} | {{ e.status }} |
{% endfor %}
The six initiatives relate differently to the European Business Wallet: only Catena-X and WE BUILD state a direct relation in the sources read; for the others no official statement was found.
