---
title: What changed
parent: Start here
nav_order: 4
permalink: /changelog/
description: "Public change log of the European Business Wallet Requirements site: new or changed laws, standards and ecosystem specifications that affect requirements, and changes to the site itself."
keywords: [European Business Wallet changes, eIDAS updates, standards updates, change log]
schema_type: CollectionPage
last_verified: "2026-10-03"
---

# What changed

Law and standards move. Each week the site checks the watched sources (see [how the weekly watch works](https://github.com/spherity/business-wallet-requirements/blob/main/docs/11-weekly-watch.md)); confirmed changes are listed here after human review. Feed: [RSS]({{ '/feed.xml' | relative_url }}).

| Date | Type | Change | Summary |
|---|---|---|---|
{% for e in site.data.changelog %}| {{ e.date }} | {{ e.type }} | {{ e.title }} | {{ e.summary }} |
{% endfor %}
