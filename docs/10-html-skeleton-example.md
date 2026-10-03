# 10 — HTML skeleton of a concept article (generated example)

Generated from `concepts/trust-plane.md` (layout `concept`, theme Just the Docs, Spherity tokens). Shortened; the real output carries the full theme markup around it.

```html
<!doctype html>
<html lang="en">
<head>
  <title>Trust plane | European Business Wallet Requirements</title>
  <meta name="description" content="The trust plane answers who or what a relying party can trust and why: ...">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">  <!-- noindex while status is planned or proposed -->
  <link rel="canonical" href="https://spherity.github.io/business-wallet-requirements/concepts/trust-plane/">
  <link rel="alternate" type="text/plain" href=".../llms.txt" title="llms.txt">
  <link rel="sitemap" type="application/xml" href=".../sitemap.xml">
  <meta property="og:type" content="article"> <meta property="og:title"> <meta property="og:description">
  <meta property="og:url"> <meta property="og:image" content=".../assets/figures/trust-plane-concept-model.png">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@graph": [
    { "@type": "Organization", "@id": ".../#publisher", "name": "Spherity GmbH" },
    { "@type": "WebSite", "@id": ".../#website" },
    { "@type": "TechArticle", "@id": ".../concepts/trust-plane/#page", "headline": "Trust plane", "dateModified": "2026-10-03",
      "keywords": "...", "about": [ ... ], "hasPart": [ {"@id": ".../figures/trust-plane-concept-model/#image"}, ... ] },
    { "@type": "BreadcrumbList", "itemListElement": [ Home, Start here, Concepts, Trust plane ] },
    { "@type": "DefinedTerm", "name": "Trust plane", "inDefinedTermSet": { "@type": "DefinedTermSet", "@id": ".../concepts/#termset" } },
    { "@type": "FAQPage", "mainEntity": [ ... three visible questions ... ] },
    { "@type": "ImageObject", "@id": ".../figures/trust-plane-concept-model/#image", "caption": "...", "license": "CC BY 4.0" },
    { "@type": "ImageObject", "@id": ".../figures/trust-plane-flow/#image" } ] }
  </script>
</head>
<body>
  <header> <!-- logo, search, Discussions, Contact, GitHub; status banner "Draft for review ..." --> </header>
  <nav aria-label="Main"> <!-- 8 entries; Concepts expanded; Discussions external link --> </nav>
  <main id="main-content">
    <nav aria-label="Breadcrumb"> Start here / Concepts / Trust plane </nav>
    <span class="badge badge-draft">draft</span>
    <h1>Trust plane</h1>
    <div class="concept-meta"> <!-- ID, group, summary, related concepts as links, requirement categories, last verified, provenance --> </div>
    <h2>Summary</h2> <p>...</p>
    <h2>Definition</h2> <div class="concept-def"><span class="term">Trust plane.</span> ... </div>
    <h2>Why it matters</h2>
    <h2>How it works</h2>
    <figure class="fig" id="fig-trust-plane-concept-model">
      <a href="/figures/trust-plane-concept-model/"><img src="...svg" alt="Concept model of the trust plane ..." width="1200" height="640" loading="lazy"></a>
      <figcaption><span class="fig-no">Figure 1.</span> ... <a>Figure page and description</a> · <a>SVG</a> · CC BY 4.0</figcaption>
    </figure>
    <h2>Interaction flow</h2> <!-- Figure 2 -->
    <h2>Roles and responsibilities</h2> <table>...</table>
    <h2>Related concepts</h2> <h2>Requirements and obligations</h2> <h2>Standards and specifications</h2>
    <h2>Design choices and alternatives</h2> <h2>Examples</h2> <h2>Open questions and limitations</h2>
    <h2>Terms introduced</h2> <h2>References</h2> <h2>Change log</h2>
    <section class="faq"><h2>Frequently asked questions</h2> <details><summary>...</summary><p>...</p></details> ... </section>
    <footer class="site-footer-extra"> licence, Contact, Discussions, GitHub, Figures, llms.txt, Sitemap, Imprint, Privacy </footer>
  </main>
</body>
</html>
```

Every element above is produced by the layout, includes and front matter; an author writes only Markdown plus front matter (`description`, `keywords`, `about`, `figures`, `faq`).
