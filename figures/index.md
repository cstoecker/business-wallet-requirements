---
title: Figure gallery
parent: Start here
nav_order: 3
permalink: /figures/
description: "All conceptual figures of the European Business Wallet Requirements site with captions, descriptions and download links (SVG and PNG, CC BY 4.0)."
keywords: [European Business Wallet figures, concept model, trust plane diagram, requirements lifecycle diagram]
schema_type: CollectionPage
last_verified: "2026-10-03"
---

# Figure gallery

Every figure has its own page with a description, alternative text, the articles that use it and downloads (SVG and PNG, CC BY 4.0). Figure conventions are described in the [concept article standard](https://github.com/spherity/business-wallet-requirements/blob/main/docs/03-concept-articles.md).

<div class="fig-gallery">
{% for f in site.figures %}
<a href="{{ f.url | relative_url }}"><img src="{{ f.image_png | relative_url }}" alt="{{ f.alt | escape }}" width="{{ f.width }}" height="{{ f.height }}" loading="lazy"><strong>{{ f.title }}</strong><br>{{ f.caption }}</a>
{% endfor %}
</div>
