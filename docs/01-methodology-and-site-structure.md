# 01 — Methodology and Site Structure

Status: **DRAFT for stakeholder review** · Owner: Carsten Stöcker · Date: 2026-10-03

Purpose of the site: a **public, citable, version-controlled requirements baseline** for European Business Wallets (EBW) and the surrounding trust infrastructure, in which **every requirement can be traced back to a formal source** (law, standard, specification) and **forward to an architecture building block, a conformance check and an industry use case**.

> Confidence legend used throughout: ✅ verified in this session · 🔎 to verify in research phase.

---

## 1. Design principles

1. **Traceability first.** A requirement without a source is an *assumption* and is labelled as such. A source obligation without a requirement is a *gap* and shows up in a coverage report.
2. **Normative vs. informative is explicit.** Legal text, standards and our own derived requirements are never mixed visually. Every statement carries a provenance class (see §3.4).
3. **Data is the product, pages are views.** The source of truth is structured data (YAML/JSON-LD) in Git. Jekyll pages, matrices and the graph are generated from it.
4. **Status-aware.** EBW is a Commission *proposal* (COM(2025) 838, 19 Nov 2025 ✅, procedure 2025/0358(COD) ✅); text, article numbers and dates may change in trilogue. Every legal reference is pinned to a **document version + date**; a diff view shows what changed between versions.
5. **Plane-based architecture, technology-neutral requirements.** Requirements say *what*; architecture alternatives say *how*. Requirements never name a product.
6. **Many audiences, one model.** Executives, legal/compliance, architects, domain experts (AAS/DPP/pharma/automotive) and implementers each get an entry path through the same underlying graph.
7. **Open by default**, contribution through pull requests/issues, with a light governance process (§7).
8. **Official sources only in the traceability chain and knowledge graph.** Only (a) official legal and policy documents (EU legislation, proposals, Council/Parliament/Commission documents, implementing acts, the EUDI ARF), (b) published standards and technical specifications of recognised bodies (ETSI/CEN, ISO/IEC, W3C, IETF, OpenID Foundation, Eclipse DSP/DCP, …), plus ecosystem and consortium specifications: **IDTA** specifications, **Catena-X** standards, **Gaia-X** framework documents and the **WE BUILD** consortium architecture blueprint, ADRs and attestation rulebooks (each tagged as *ecosystem specification*, ranking below law and formal standards). From IDTA/AAS, Catena-X and IDSA/Eclipse we take only **high-level, technology-neutral requirements** (e.g. DSP/DCP for data-space connector integration), never specific implementations. AAS is an implementation and is out of scope as a requirements source; it is assessed instead as a candidate implementation artefact (see §4, alternative 7). Finally: (c) the peer-reviewed paper *Towards the European Business Wallet* (T. Hühnlein, D. Hühnlein, S. Schwalm, C. Stöcker; Open Identity Summit 2025, DOI 10.18420/oid2025_09) may appear as sources, obligations or edges. Blog posts, Medium articles, position papers, vendor material and repositories are **not** graph sources. They may appear only in the non-normative reading list under `/research/` and never as the basis of a requirement's provenance.

---

## 2. Requirements classification (the taxonomy)

You asked whether there are categories beyond Functional / Non-functional / Certification / Governance. Yes. Proposed top-level taxonomy (ISO/IEC/IEEE 29148 + ISO/IEC 25010 + Volere + eIDAS/ARF practice):

| Code | Category | Covers | Typical source |
|---|---|---|---|
| **FUN** | Functional | Wallet functions: identify, authenticate, store/present attestations, sign/seal, mandate management, ERDS/notifications, directory lookup, issuance, revocation | EBW proposal, ARF, OID4VC |
| **NFR** | Non-functional (quality) | Security, privacy, availability, performance, scalability, usability, accessibility, auditability, portability, sustainability (per ISO 25010 + 25012 data quality) | ISO 25010, ETSI EN 319 401, NIS2 |
| **INT** | Interoperability & semantic | Protocols, data models, credential formats, schemas, vocabularies, cross-border and cross-domain mapping (e.g. LPID ↔ AAS ↔ DPP) | ARF, W3C, OpenID, IDTA, CEN |
| **TRU** | Trust & assurance | Levels of assurance, trust anchors, trust lists, QTSP status, issuer/verifier registration, revocation, key custody (QSCD) | eIDAS, ETSI TS 119 4xx/5xx |
| **CER** | Certification & conformity | Certification schemes, conformity assessment bodies, testing, evidence, surveillance, re-certification | CIR 2024/2981 ✅(as cited by Spherity roadmap), CSA/EUCC, ISO 17065 |
| **GOV** | Governance | Roles, liability, rulebooks, change control, onboarding of ecosystem participants, dispute handling, supervisory interaction | Regulation, scheme rulebooks, Gaia-X/Catena-X/IDSA |
| **LEG** | Legal & compliance (derived) | Obligations on wallet providers, owners, relying parties: GDPR, NIS2, DORA, CRA, AI Act, sector law | EU regulations |
| **DAT** | Data-space & data-sovereignty | Usage policies (ODRL), contract negotiation, connector–wallet binding, DSP/DCP profiles | Eclipse DSP/DCP, IDSA, DSSC |
| **OPS** | Operational & service | SLAs, support, incident handling, key ceremonies, lifecycle (onboard/offboard), business continuity | ISO 27001/27701, ETSI EN 319 401 |
| **DOM** | Domain-specific | Overlays per industry (DPP/ESPR, battery, automotive, GxP, financial, public procurement, agentic/physical AI) | Sector law and standards |
| **BIZ** | Business & adoption | Cost, onboarding friction, SME accessibility, commercial models, migration from existing eID/e-seal/PKI | Official impact assessments and the EBW proposal's own analysis; the OID 2025 paper |
| **CON** | Constraints & assumptions | Mandated technology choices, legal limits, time constraints, explicit assumptions | Any |
| **TRN** | Transition & migration | Coexistence with legacy (EDI, PKI/X.509 seals, Peppol, AS4), phased roll-out per roadmap | EBW roadmap |

Each requirement also carries **orthogonal facets** (not categories), so filtering stays powerful:

- **Perspective** (B2B / B2G / G2B / B2C / C2B / G2G / B2E / M2M-A2A — see above)
- **Obligation type** (authenticate, authorise, report, register, deliver, sign/seal, …)
- **Plane** (trust / control / data / governance / assurance — see §4)
- **Actor** (EBW owner, wallet provider, QTSP, issuer of attestations, relying party/verifier, authorised representative, natural person/consumer (EUDIW holder), competent authority/registry operator, supervisory body, conformity assessment body, data space operator, agent/machine)
- **Lifecycle phase** (onboarding, issuance, holding, presentation, revocation, offboarding)
- **Priority** (MUST/SHOULD/MAY per RFC 2119, and *legally mandatory* vs *ecosystem-recommended*)
- **Maturity** (draft / proposed / agreed / verified)
- **Domain tag(s)** (DPP, AAS, automotive, pharma/GxP, data space, agentic AI, …)
- **Verification method** (inspection, test, analysis, audit, certification — ISO 29148 / classic IATD)

### Interaction perspectives (B2B, B2G, B2C) — a first-class dimension

Every requirement, obligation and scenario is tagged with the **relationship** it occurs in. These three perspectives are also top-level navigation on the site (`/perspectives/`), because stakeholders think in these terms and the legal sources differ sharply between them.

| Perspective | Direction | Core question | Wallet functions in play |
|---|---|---|---|
| **B2B** | EBW owner ↔ EBW owner | Can I trust a counterparty, its authorised representatives and its data, and prove what was agreed? | Mutual identification (LPID), mandate/representation checks, sign/seal contracts and documents, exchange of attestations (certificates, supplier qualifications), DPP/AAS data access, data-space onboarding and contract negotiation (DSP/DCP), machine/agent delegation, B2B delivery with legal effect (ERDS/eDelivery) |
| **B2G** (and G2B) | EBW owner ↔ public body | Can I authenticate and act legally towards authorities, and can authorities rely on and answer me? | See table below |
| **B2C** (and C2B) | EBW ↔ EUDI Wallet of a natural person | Can a person verify who the business is, and can the business act through and towards people with the right authority? | See table below |

Further relationships kept in scope as tags: **G2G** (public body to public body), **B2E** (organisation ↔ employee/representative; the bridge to the EUDI Wallet), **M2M/A2A** (machine and agent delegation chains).

#### B2G: authentication, authorisation, reporting and registries

B2G is split into four *obligation types*, each with its own requirement family:

| Obligation type | Meaning | Examples (🔎 = verify scope/dates in research phase) |
|---|---|---|
| **Authenticate** | Prove the legal person and its representative to a portal or authority | National and EU portals (company/tax/customs accounts), EU Login, Once-Only Technical System (OOTS), Single Digital Gateway procedures, business register access, public procurement platforms (eForms/e-Certis) |
| **Authorise** | Prove the right to act: power of representation, role, delegation, sub-delegation, scope and validity | Mandates for filing on behalf of a company, authorised representative or processor/agent, group-level and cross-border representation, delegation to service providers and AI agents |
| **Report / notify** | Submit structured, signed/sealed, timestamped reports with proof of delivery and receipt | NIS2 registration and incident reporting (early warning / notification / final report); CRA vulnerability and incident reporting via the single reporting platform 🔎; DORA incident reporting; GDPR breach notification; AI Act serious-incident reporting; MDR vigilance; pharmacovigilance; MiFIT 🔎 *(please confirm: MiFID II/MiFIR transaction and reference-data reporting?)*; AMLR/KYB filings; CSRD/ESAP sustainability reporting; customs and VAT/e-invoicing (ViDA) data submissions; CBAM declarations |
| **Register / publish** | Create and maintain entries in public registries, linked to the legal person | **DPP registry** (ESPR); **EPRL** (European Product Registry for Energy Labelling); **AI Act EU database** for high-risk systems; EUDAMED (medical devices); SCIP (waste framework); REACH-IT/ECHA; Battery passport registry 🔎; EUID/BRIS business registers; EMVS/DSCSA-type verification repositories; EU trusted lists and, under the EBW, the **common directory** and **registration of wallet owners/providers** |

For every B2G obligation the site models: *competent authority*, *legal basis (clause)*, *trigger*, *deadline*, *content/schema*, *channel (portal/API/eDelivery)*, *required assurance level*, *required evidence (signature/seal/timestamp)*, *receipt/acknowledgement*, *retention*, and *who may act (mandate)*. This feeds a **Reporting & Registry Obligations Atlas** (`/legal/reporting-registry/`) and requirement families such as: *the wallet shall support mandate-bound submissions*, *shall bind a seal to a report payload*, *shall obtain and store legally relevant acknowledgements*, *shall support deadline-driven multi-stage reporting*, *shall allow registry entries to reference the owner's LPID and mandated operators*, *shall support authority-side authentication of the wallet owner (G2B direction: authorities issue notices, receipts and attestations to the wallet)*.

Open question to resolve early: the line between what the **EBW** (identity, mandates, sealing, delivery) must provide and what remains in **sector reporting channels** (e.g. national NIS2 portals, ENISA platform, EUDAMED); the EBW's role is likely authentication, authorisation and evidence, not the report schema itself.

#### B2C: EBW ↔ EUDI Wallet (EUDIW)

| Use-case family | Direction | Example requirement themes |
|---|---|---|
| **Consumer verifies the business** | EUDIW user ← EBW | Presentation of LPID and trust signals to a consumer; display of verified business identity (who am I dealing with), authenticity of a DPP, repair/warranty information; privacy-friendly verification without tracking |
| **Business verifies the consumer** | EBW (as relying party) → EUDIW | Relying-party registration and access certificates, minimal attribute requests (e.g. age, residence, payment authorisation/SCA), consent and purpose binding, GDPR data minimisation for the business |
| **Business issues to the consumer** | EBW (as attestation issuer) → EUDIW | Warranty, receipt, product ownership, loyalty, certificates of origin or conformity, digital product ownership transfer, DPP-linked consumer attestations |
| **Representative acts for the business (B2E bridge)** | EUDIW (person) → EBW | Natural person authenticates with EUDIW and proves a mandate/role to act for the company; EBW verifies the link person ↔ legal person; signing with the person's QES/QSealC under company mandate; revocation on employee exit; separation of private and professional identity |
| **Consumer ↔ business transactions with legal effect** | both | Contract signature, notifications to consumers via qualified delivery, consumer rights (withdrawal, complaints), accessibility |

Key design tensions to analyse: privacy of the natural person (unlinkability) versus accountability of the representative; wallet-to-wallet protocols (OpenID4VP/ISO 18013-7 proximity and remote flows) and their fit for B2C scenarios; assurance level alignment; consumer-law and accessibility constraints; and whether EBW and EUDIW share issuance/verification stacks or only interoperate via protocols and trust lists.

### Obligation-type facet

Orthogonal to category and perspective: **authenticate · authorise · report/notify · register/publish · disclose · retain/archive · deliver/receive · sign/seal · verify**. It makes the Atlas queryable (e.g. all *report* obligations on *B2G* in the *pharma* domain).

### Requirement writing rules

- Atomic, one obligation per requirement; EARS-style templates (*"When <trigger>, the <system> shall <response>"*).
- ID scheme: `EBW-<CAT>-<NNN>`, immutable once published; deprecation instead of deletion.
- Each requirement has: statement, rationale, source link(s), plane, actors, verification criterion, status, owner, version history.

---

## 3. Traceability model (the heart of the site)

### 3.1 Chain

```
Formal source (clause)            e.g. EBW Art. X(n), eIDAS Art. 5a, ESPR Art. Y
   │ interpreted-as
   ▼
Obligation (atomic, normative)    "EBW provider shall …"            [who owes what to whom]
   │ derives
   ▼
Requirement (EBW-CAT-NNN)         our technology-neutral statement
   │ realised-by
   ▼
Capability / Building block       e.g. "Presentation verifier", "Mandate registry client"
   │ specified-by                      │ implemented-in (architecture alternative A/B/C…)
   ▼                                   ▼
Standard / profile clause         W3C VCDM 2.0, OID4VP, ETSI TS 119 xxx, DSP/DCP, IDTA 02xxx
   │ verified-by
   ▼
Conformance check / evidence      test case, audit criterion, certification scheme element
   ▲ exercised-in
   │
Industry scenario / use case      DPP exchange, GxP batch release, supplier onboarding, agent mandate
```

### 3.2 Relation vocabulary (edges in the graph)

`derivedFrom`, `interpretedAs`, `refines`, `conflictsWith`, `dependsOn`, `satisfiedBy`, `specifiedBy`, `verifiedBy`, `appliesToDomain`, `supersedes`, `mapsTo` (cross-standard), `assumes`.

### 3.3 Coverage metrics (published on the site, regenerated per build)

- % of obligations covered by ≥1 requirement
- % of requirements with ≥1 source (orphan check)
- % of requirements with a verification criterion
- % of requirements mapped to ≥1 standard clause / architecture building block
- Per-domain and per-plane heatmaps
- "Changed since last legal text version" list

### 3.4 Provenance classes

| Class | Meaning | Visual |
|---|---|---|
| **L** | Directly mandated by law/regulation | solid badge |
| **S** | Mandated/profiled by a standard or technical specification | solid badge |
| **D** | Derived by us (interpretation of L/S for a domain) | outlined badge |
| **A** | Assumption / ecosystem recommendation / stakeholder input (never cites a non-official source as authority) | dashed badge |

Legal interpretation is labelled **"analysis, not legal advice"**, with the author and review date.

---

## 4. Logical architecture: planes

Proposed reference model (to be validated in workshops with IDTA, Data Space, DSSC and ARF experts). The first three were your suggestion; two are added because the requirements demand them.

| Plane | Question it answers | Examples of building blocks |
|---|---|---|
| **Trust plane** | *Who/what can I trust and why?* | Legal person identification (LPID), attestations (QEAA/EAA), trust lists, QTSPs, registries, revocation/status, key custody (QSCD/HSM), mandates/powers of representation, issuer & verifier registration |
| **Control plane** | *Who may do what, under which policy?* | Wallet orchestration, policy decision/enforcement (ODRL/Cedar/Rego), authorisation & delegation (human, machine, AI agent), consent, contract negotiation (DSP), onboarding, lifecycle |
| **Data plane** | *How does data and evidence actually move?* | Credential issuance/presentation (OID4VCI/OID4VP/DIDComm), ERDS/eDelivery, AAS/DPP endpoints, data-space transfer, signing/sealing, notifications |
| **Governance plane** *(added)* | *Under which rules does the ecosystem operate?* | Rulebooks, certification schemes, accreditation, liability, change control, supervisory interfaces |
| **Assurance & evidence plane** *(added)* | *Can I prove compliance afterwards?* | Audit logs, qualified timestamps/e-ledger, evidence packs, conformity test suites, transparency logs |

Cross-cutting: **Security**, **Privacy**, **Semantics** (shared vocabularies — the glue between LPID, AAS, DPP, Catena-X, Gaia-X).

### Architecture alternatives to document (each as an ADR with a decision matrix scored against the requirement set)

1. **Hosted/QTSP wallet** (multi-tenant, provider-run, remote signing)
2. **Enterprise-embedded wallet** (customer-run, integrated with ERP/IAM/PKI)
3. **Hybrid** (customer-held credentials + remote QSCD/HSM + provider-run mandate/ERDS services)
4. **Data-space connector-integrated** (wallet as DCP credential service for DSP connectors)
5. **Agent/machine wallet pattern** (delegated sub-wallets for AAS endpoints, devices, AI agents — incl. Know-Your-Agent, mandate chains)
6. **Verifiable data registry choices**: trust-list-based vs. DID-method-based (did:web, did:webvh, did:ethr, …) vs. ledger-anchored (e.g. qualified electronic ledger) — for status, discovery and anchoring.

7. **AAS as an implementation artefact** (assessment, not a requirements source): would the Asset Administration Shell be a sensible carrier or binding for wallet-related artefacts (legal-person identity, attestations, mandates, DPP access rights) on assets and machines? The ADR assesses fit, gaps and risks against the requirement set, with and without AAS (DPP with and without AAS). Possible outcomes: adopt as a profile, map only, or reject.

Evaluation criteria: legal conformity, assurance level, sovereignty, interoperability, cost/SME fit, operational complexity, crypto-agility (incl. post-quantum), vendor lock-in.

---

## 5. Knowledge graph design

- **Source of truth:** `_data/` YAML (one file per entity type) + `ontology/` (SKOS concept schemes for taxonomy/glossary; OWL/RDFS vocabulary for relations; SHACL shapes for validation). Reuse existing vocabularies where possible: Dublin Core/DCAT, ELI (European Legislation Identifier) and FRBR for legal sources, ODRL for policies, PROV-O for provenance, SKOS for terms, schema.org for pages.
- **Entity types:** `LegalSource`, `Clause`, `Obligation`, `Requirement`, `Capability`, `BuildingBlock`, `ArchitectureOption`, `Standard`, `StandardClause`, `Actor`, `Plane`, `Domain`, `UseCase`, `Ecosystem`, `ConformanceCheck`, `Publication` (restricted to the OID 2025 paper), `Term`.
- **Build pipeline** (GitHub Actions, because custom Jekyll plugins are not supported on the default GitHub Pages build):
  1. Validate data (JSON-Schema + SHACL; broken links, orphans, duplicate IDs fail the build).
  2. Generate: per-entity Markdown stubs, traceability matrices, coverage report, JSON-LD export (`/graph.jsonld`), CSV/Excel export.
  3. Jekyll build → deploy to Pages.
- **Visualisation:** client-side graph explorer (Cytoscape.js), filter by plane/domain/category/provenance; each page has a "neighbourhood" mini-graph. Static fallback tables for accessibility and print.
- **Machine-readable by design:** the same graph is published as JSON-LD so partners (IDTA, data spaces, tooling) and AI agents can consume it. A SPARQL-free approach is deliberate (static hosting); revisit if a query endpoint is needed.

---

## 6. Proposed site map and left-hand navigation (Jekyll)

### 6.1 Left-hand sidebar: 8 top-level entries (decided 2026-10-03)

Requirements come first, ahead of perspectives. Standards, Certification and Governance are grouped under "Ecosystem" together with the ecosystem/initiative pages.

| # | Sidebar entry | Contains |
|---|---|---|
| 1 | **Start here** | Landing page, status of the EBW legislation, paths for executives, legal/compliance, architects, domain experts, implementers |
| 2 | **Requirements** | Catalogue by category; **Requirements management methodology** (§6.3); one page per requirement |
| 3 | **Perspectives** | B2B, B2G, B2C (EBW ↔ EUDI Wallet), G2B/G2G, M2M/A2A |
| 4 | **Legal & compliance** | EBW proposal, eIDAS 2.0, horizontal law, product law, sector law, Reporting & Registry Atlas |
| 5 | **Domains** | DPP with and without AAS, data spaces, automotive, pharma/GxP, industrial/agentic/physical AI, finance, public sector |
| 6 | **Architecture** | Planes, building blocks, alternatives (ADRs, incl. AAS as implementation artefact), reference flows |
| 7 | **Traceability & graph** | Matrices, coverage dashboard, gap list, interactive knowledge graph, JSON-LD download |
| 8 | **Ecosystem** | **Ecosystems & initiatives** (§6.2), Standards radar, Certification, Governance |

Update 2026-10-03: *Concepts* (29 concept articles) and the *Figure gallery* sit under Start here; the header carries search, Discussions, Contact and GitHub; Discussions is also an external sidebar item; every page has a draft-status banner and a footer. See docs/05-navigation-and-deployment.md. The site is branded with the Spherity design system (docs/04 and docs/03 for details).

Utility links (header/footer, not in the numbered sidebar): Roadmap, Glossary, Research (non-normative reading list), Contribute, Changelog, About/Disclaimer.

### 6.2 Ecosystems & initiatives subpage

Location: **Ecosystem → Ecosystems & initiatives** (`/ecosystem/initiatives/`), one page per initiative: **Catena-X, WE BUILD, Manufacturing-X, Factory-X, energy data-X, CIRPASS-2**. Every page has the same template: *what it is and who governs it · what it does (technology-neutral) · use cases · high-level requirements on identity/trust/wallets (each with standard/document ID and link) · relation to EBW/eIDAS · sources with version/date*. Implementation details (specific products) are context only and never requirements. Only high-level requirements enter the requirement catalogue (principle 8).

In the knowledge graph each initiative is an `Ecosystem` entity with edges `hasUseCase` → `UseCase`, `imposes` → `Requirement` (provenance S, tagged *ecosystem specification*), `specifiedBy` → `Standard`, and `relatesTo` → `LegalSource` (e.g. EBW proposal, ESPR).

### 6.3 Requirements management methodology subpage

Location: **Requirements → Requirements management methodology** (`/requirements/methodology/`). It explains the lifecycle (collect → extract → derive → link → review → publish), the taxonomy and facets, ID and status rules, provenance classes, the source rule (principle 8), traceability and coverage metrics, change control and versioning. It is generated from, and must stay consistent with, §1–§3 and §7 of this document.

### 6.4 Page tree

```
/                              Landing: purpose, status of EBW legislation, entry paths, coverage dashboard
/start/                        Start-here paths per stakeholder
/requirements/                 Catalogue (filter by category, plane, actor, domain, provenance, status)
    methodology/               Requirements management methodology
    functional/  non-functional/  interoperability/  trust/  certification/
    governance/  legal/  data-space/  operational/  domain/  business/  constraints/  transition/
    <EBW-CAT-NNN>/             One page per requirement incl. trace links, history, discussion link
/perspectives/                 Interaction perspectives (cross-cut every other section)
    b2b/  b2g/ (authenticate · authorise · report · register)  b2c/ (EBW ↔ EUDI Wallet)  g2b-g2g/  m2m-a2a/
/legal/                        Legal & compliance atlas
    reporting-registry/  ebw/  eidas/  horizontal/  product/  sector/
/domains/                      dpp/ (with and without AAS)  data-spaces/  automotive/  pharma-gxp/
                               industrial-ai/  agentic-ai/  physical-ai/  finance-trade/  public-sector/
/architecture/                 planes/  building-blocks/  alternatives/ (ADRs + scoring)  reference-flows/
/traceability/                 Matrices, coverage dashboard, gap list
/graph/                        Interactive knowledge graph + JSON-LD download
/ecosystem/
    initiatives/               catena-x/  we-build/  manufacturing-x/  factory-x/  energy-data-x/  cirpass-2/
    standards/                 Standards & specs radar with maturity and mapping
    certification/             Conformance profiles, test-suite catalogue, evidence templates
    governance/                Roles, rulebook requirements, change process, RACI
/research/  /roadmap/  /glossary/  /contribute/  /changelog/  /about/  /disclaimer/
```

Page template essentials: provenance badge, status banner ("based on proposal COM(2025) 838 — may change"), "last verified" date, permalink + citation block (BibTeX/CSL), "view in graph", "edit on GitHub".

### Tech choices (to be confirmed)

- **Jekyll** with a clean, accessible theme (candidate bases: Just the Docs for navigation/search; or a lean custom layout with Spherity branding). Lunr/Pagefind search. Mermaid for sequence diagrams. Cytoscape.js for the graph.
- **Languages:** English primary; German summaries for the Bitkom/IDTA/DACH audience as phase-2 option.
- **Licensing:** CC BY 4.0 for text; Apache-2.0/MIT for code; clarify handling of third-party standard text (link and paraphrase only — ETSI/ISO text is copyrighted).

---

## 7. Governance of the site itself

- Roles: **Editors** (maintain taxonomy and quality), **Domain stewards** (IDTA/AAS, DPP, data space, pharma, automotive, AI), **Legal reviewers**, **Contributors**.
- Change flow: issue → proposal (PR with data diff) → review by steward + legal reviewer (for L/D classes) → merge → versioned release (SemVer for the requirements baseline: `v0.x` drafts, `v1.0` after first stakeholder review).
- Quality gates in CI: schema validation, orphan/coverage thresholds, link check, spelling, accessibility check (axe/pa11y).
- Every release produces a tagged, citable snapshot (Zenodo DOI via GitHub integration).

---

## 8. Methodology references

- ISO/IEC/IEEE 29148 (requirements engineering); ISO/IEC 25010 & 25012 (quality models); EARS; Volere
- ISO/IEC/IEEE 42010 (architecture description) for viewpoints/planes; ADR practice (MADR) for alternatives
- Legal engineering practice: obligation extraction in the style of LegalRuleML/Akoma Ntoso/ELI; clause-level citation
- EU ARF (EUDI), ETSI/CEN ESI series, DSSC blueprint, Gaia-X Trust Framework, Catena-X standards, IDTA specifications
- SEBoK for traceability patterns; INCOSE guide for writing requirements
