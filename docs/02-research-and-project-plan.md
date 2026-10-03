# 02 — Research and Project Plan

Status: **DRAFT** · Date: 2026-10-03 · Companion to `01-methodology-and-site-structure.md`

## 1. Objective and deliverables

Deliver a public Jekyll site (see doc 01) with a **requirements baseline v1.0** for European Business Wallets and trust infrastructure, traceable to law and standards, with industry-domain overlays and architecture alternatives.

| # | Deliverable | Phase |
|---|---|---|
| D1 | Methodology + site structure (doc 01) | 0 ✅ draft |
| D2 | Research & project plan (this doc) | 0 ✅ draft |
| D3 | Source register (all legal sources, standards, publications; with version/date/URL/licence) | 1 |
| D4 | Obligation register extracted from EBW proposal + eIDAS 2.0 + implementing acts | 2 |
| D5 | Jekyll skeleton + data schema + CI pipeline + graph explorer (empty-but-working) | 2 |
| D6 | Requirement catalogue v0.5 (core: FUN/TRU/INT/NFR/CER/GOV) | 3 |
| D7 | Domain overlays (DPP±AAS, data spaces, automotive, pharma/GxP, AI) | 4 |
| D7a | Perspective packs: B2B, B2G (authenticate/authorise/report/register), B2C (EBW↔EUDIW) incl. Reporting & Registry Obligations Atlas | 3–4 |
| D8 | Architecture planes, building blocks, alternatives ADRs + scoring | 4–5 |
| D9 | Traceability matrices + coverage dashboard | 3–5 |
| D10 | Stakeholder review round (IDTA, data space, Industry 4.0 / industrial / agentic / physical AI) → v1.0 | 6 |

## 2. Research streams

### R1 — Core regulation (EBW and eIDAS)
- **EBW proposal** COM(2025) 838 ✅ (EUR-Lex 52025PC0838; procedure 2025/0358(COD)). Article-by-article obligation extraction; definitions; roles (EBW owner, provider, authorised representative); functions (identification data, EAAs, sign/seal, documents & legally valid notifications, mandate management, common directory); acceptance duties for public bodies.
- **Legislative status:** Council working documents ✅ found (ST 7659/26 of 22 May 2026, ST 9684/26 of 2 June 2026 — 🔎 read for compromise changes); Parliament committee reports/amendments; trilogue timeline (Spherity roadmap projects Q4 2026 agreement ✅ as scenario only).
- **eIDAS 2.0** Reg. (EU) 2024/1183 amending 910/2014; implementing acts incl. CIR 2024/2977–2982 (🔎 confirm exact set, esp. certification 2024/2981 ✅ cited); EUDI **ARF** (GitHub `eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework`) incl. EBW updates.
- **Position papers** (DIGITALEUROPE, CNUE/Notaries, Bitkom, iGrant.io, Yivi, others): read for context only. **Not** registered as graph sources (see source rule below).
- **Legal-person identity ecosystem:** LPID, EUID/BRIS, e-CODEX, Once-Only Technical System, Peppol/eDelivery AS4, ERDS (eIDAS Regulation Ch. III Sec. 7), company-law digitalisation directives.

**Source rule (decided 2026-10-03):** the source register, obligation register and knowledge graph contain **only** official sources (EU legal and policy documents, ARF, standards and specifications of recognised bodies, and ecosystem specifications from IDTA, Catena-X, Gaia-X and the WE BUILD consortium: blueprint, ADRs, rulebooks) **plus** the paper *Towards the European Business Wallet* (OID 2025, DOI 10.18420/oid2025_09). Everything else in R2 is background reading, kept in a separate non-normative reading list.

### R2 — Author & network publications (background reading only; not graph sources, except the OID 2025 paper)
- **Carsten Stöcker (cstoecker):** GitHub public repos ✅ found: `Trusted-AI-from-a-Supply-Chain-Perspective` (KYA, AI BOM, Data Cards, TEVV, AISP, PoA, A2A — Catena-X Trusted AI WG), `chem-x`, `Project-Julius`; private `dpp-systems-staging` (not accessible/not to be used publicly without permission). Full read of public repos required — **access to these repos must be added to the session** (currently scoped to this repo only).
- **Spherity org** ✅: `spherity-research` (EBW roadmap, DPP, trust infrastructure, PQC, qualified electronic ledger, trusted AI, zero-trust), `building-passport-viewer`, `trusted-hint-registry` (ERC-7506), `ethr-revocation-registry`, `oid-public` (JSON-LD specs), `shared-context` (private knowledge graph — ask owner whether reusable).
- **Medium / Spherity blog:** found ✅ "EUBW and Legal Person Identity", "Legal & Operational EBW Roadmap", "Implementing Digital Product Passports using decentralized identity standards". Medium returned 403 to automated fetch → **need you to export or paste the list** (or allow a different fetch route).
- **Academic:** "Towards the European Business Wallet" (Hühnlein, Hühnlein, Schwalm, Stöcker; Open Identity Summit 2025, DOI 10.18420/oid2025_09 ✅); Springer chapter "Von Identifikatoren zu Wallets" ✅; ResearchGate DPP papers ✅ (DID/VC-based DPP management; AAS-based DPP as Gaia-X service).
- **Detlef Hühnlein (ecsec):** Open Identity Summit/GI proceedings, EUDI wallet/HEI-EDU work ✅ found, legal-person identity and LPID standardisation; check Google Scholar/dblp/ResearchGate. Also **Steffen Schwalm** (ETSI/CEN contributions).
- **Other voices to cover:** DSSC, IDSA, Catena-X, Gaia-X, Eclipse Tractus-X/EDC, ECLASS, Plattform Industrie 4.0, IDTA working groups, GS1 (Digital Link, EPCIS, GS1 verifiable credentials), UN/CEFACT (UNTP), OpenID Foundation, DIF, W3C VC WG, ToIP, ESSIF/EBSI (🔎 status).

### R3 — Standards & technical specifications
| Area | To analyse |
|---|---|
| **W3C** | VC Data Model 2.0, Data Integrity, VC JOSE/COSE, Bitstring Status List, DID Core, did:web/webvh status, DID Resolution, WebAuthn, Verifiable Credentials for Controlled Identifiers/ Digital Credentials API 🔎 |
| **OpenID / IETF** | OpenID4VCI, OpenID4VP, SIOPv2, HAIP (high-assurance profile), SD-JWT, SD-JWT VC, OAuth 2.0 attestation-based client auth, JOSE/COSE, Token Status List, DPoP |
| **ISO/IEC** | 18013-5/-7 (mdoc), 23220 series, 29003, 27001/27701, 17065/17021 (conformity), 15459 (identifiers), 22123 cloud 🔎 |
| **ETSI/CEN** | ESI series: TS 119 461 (identity proofing), 119 471/472 (EAA, incl. 119 472 ✅ cited), 119 475 (relying-party attributes), 119 411/412 (policy, certificate profiles incl. legal person), 119 612 (trusted lists), 119 602 (list of trusted entities), 119 182/119 312, EN 319 401, EN 319 521/522 (ERDS), EN 319 403-1; CEN/TC 224, CEN/TC 307 DPP (🔎 numbers) |
| **Data spaces** | Eclipse **DSP** (Dataspace Protocol), **DCP** (Decentralized Claims Protocol), EDC, Tractus-X, IDSA Rulebook, Gaia-X Trust Framework/Digital Clearing House, DSSC Blueprint, iSHARE, ODRL |
| **Industry 4.0** | IDTA AAS metamodel (IDTA-01001), AAS API (01002), DPP submodels (IDTA 02099-x ✅ found), security (IDTA-01004?) 🔎, Verifiable Credentials in AAS (IDTA discussion), OPC UA, eCl@ss, IEC 63278, IEC 62443, VDI/VDE 2193 |
| **Supply chain/product** | GS1 Digital Link/EPCIS, UNTP, CIRPASS, Battery Pass, Catena-X standards (CX-0xxx incl. Trusted AI) |

### R4 — Horizontal & sectoral regulation (compliance requirement sources)
Priority A (full obligation extraction):
- **EBW, eIDAS 2.0 + IAs**, **GDPR** (+ EDPB wallet/blockchain guidance), **NIS2**, **Cyber Resilience Act**, **Data Act** (switching, smart contracts, interoperability), **AI Act** (high-risk, GPAI, agents, Art. 4 literacy, logging), **ESPR / DPP** (delegated acts, registry, data carrier, access rights per actor, Art. 10+ 🔎), **Battery Regulation 2023/1542** (battery passport).
Priority B (domain overlays; extract wallet-relevant obligations only):
- **Automotive:** UNECE R155/R156, ISO/SAE 21434, ISO 26262 (context), Catena-X, EU type-approval, ELV Regulation (proposal), Data Act/vehicle data, supplier due-diligence (CSDDD, Batteries).
- **Pharma/GxP/health:** EU GMP Annex 11 (computerised systems) and draft Annex 22 (AI) 🔎, FDA 21 CFR Part 11, ALCOA+ data integrity, EU FMD / DSCSA serialisation & verification, MDR/IVDR UDI/EUDAMED, EHDS, GDP, PIC/S PI 041.
- **Finance/trade:** DORA, AMLR/AMLA (KYB/UBO), PSD3/PSR, ViDA/e-invoicing (EN 16931), eIDAS in customs (EU Customs Reform/Data Hub), MiCA (out of scope unless tokens).
- **Public sector:** Single Digital Gateway / OOTS, public procurement (eForms), Interoperable Europe Act.
- **Sustainability:** CSRD/ESRS, CSDDD, CBAM (data and attestations flow through wallets).
- **AI-specific:** AI Act, NIST AI RMF, ISO/IEC 42001, Catena-X Trusted AI; agent identity/mandates (KYA, A2A, MCP auth) — emerging, mark maturity low.
- 🔎 Verify current status/dates of each (esp. proposals and delegated acts) before extraction; record version and date in the source register.

### R5 — Domain perspectives (workshops + literature)
For each domain: actors, trust relationships, 3–5 scenarios, wallet interactions, gaps vs EBW scope.
- **DPP with AAS (IDTA)** and **DPP without AAS** (GS1/UNTP/DID-VC) — the intersection of AAS submodels with LPID/EAA/mandates (who may read which DPP part: authority/customer/recycler/supplier).
- **Data spaces** (Catena-X, Manufacturing-X, Gaia-X, DSSC, Mobility Data Space): wallet ↔ DCP credential service ↔ DSP connector; participant onboarding; usage-policy credentials.
- **Industry 4.0 / industrial AI / agentic AI / physical AI:** machine identity vs. organisation identity, delegation chains (organisation → system → agent → device), accountability and audit, safety/liability.
- **Automotive** and **pharma/GxP** deep dives (above).

### R7 — Interaction perspectives: B2B, B2G, B2C (added 2026-10-03)

**B2G — authenticate, authorise, report, register** (feeds the Reporting & Registry Obligations Atlas)
- *Authenticate/authorise towards portals:* EU Login, national company/tax/customs/business-account portals (per Member State, start with DE, FR, NL, ES, IT, plus 🔎 others), OOTS and Single Digital Gateway, public procurement (eForms/e-Certis), business registers (EUID/BRIS), powers of representation and delegation models, eIDAS node and EBW acceptance duties for public bodies.
- *Reporting obligations* (per item: authority, clause, trigger, deadline, schema, channel, assurance level, evidence, acknowledgement): NIS2 (registration, incident reporting stages), CRA (reporting via the single reporting platform, 🔎 start date), DORA, GDPR Art. 33/34, AI Act (serious incidents, post-market monitoring), MDR/IVDR vigilance, pharmacovigilance (EudraVigilance), MiFIT 🔎 *(confirm intended scope: MiFID II/MiFIR transaction and reference-data reporting?)*, AMLR/KYB, CSRD/ESAP, customs (UCC, ICS2, EU Customs Data Hub), VAT/ViDA e-invoicing, CBAM.
- *Registries:* DPP registry (ESPR), EPRL (Reg. (EU) 2017/1369 and 2019/2013 etc. 🔎), AI Act EU database for high-risk systems, EUDAMED, SCIP, REACH-IT/ECHA, battery passport/registry 🔎, EBW common directory, EU trusted lists, national registries.
- *Question to answer per item:* what must the **EBW** supply (identity, mandate, seal, timestamp, delivery proof, receipt) versus what stays in the sector channel; where does the EBW **replace** existing credentials (e.g. company certificates, eIDAS-based organisation certificates) and what is the migration path.

**B2B**
- Counterparty onboarding (KYB, supplier qualification), mandate checking at transaction time, contract/document sealing, B2B ERDS/eDelivery and Peppol coexistence, data-space onboarding and contract negotiation (DSP/DCP), DPP/AAS data access rights between economic operators, machine and agent delegation chains.

**B2C (EBW ↔ EUDIW)**
- ARF treatment of relying parties, access certificates and registration; attestation issuance to EUDIW by businesses (EAA/QEAA); representative (B2E) flow: EUDIW user proves mandate to act for an EBW owner; wallet-to-wallet protocols (OpenID4VP, ISO 18013-5/-7); consumer law, accessibility (EAA directive/EN 301 549), GDPR data minimisation, DPP consumer access, right to repair, warranty/receipt attestations, payment SCA/PSD3 interplay 🔎.
- Analyse unlinkability and accountability trade-offs, and whether EBW and EUDIW share stacks or only interoperate.

### R6 — Architecture research
- Reference model: five planes (doc 01 §4). Validate vs. ARF component model, DSSC blueprint, ISO/IEC 42010 viewpoints, Gaia-X architecture, Catena-X, IDS-RAM.
- Alternatives ADRs (hosted / embedded / hybrid / data-space-integrated / agent pattern / registry options).
- Cross-cutting: key management & QSCD, remote signing, crypto-agility & **post-quantum** (Spherity research topic), privacy (selective disclosure, unlinkability for legal persons — differs from natural persons), revocation & status at scale, offline/B2B batch use, mandate/power-of-representation modelling.
- Reference implementations to survey (read-only): EUDI reference wallet repos, Eclipse EDC/DCP, Veramo, walt.id, Credo, Sphereon, Spherity stack.

## 3. Method of work per stream

1. **Collect** → record in source register (`_data/sources.yml`): ID, title, issuer, type, version, date, URL, licence, status, retrieved-on.
2. **Extract** → obligations (clause-level) in `_data/obligations.yml` with who/what/whom/condition/deadline.
3. **Derive** → requirements with category, plane, actors, facets, verification criterion.
4. **Link** → standards, building blocks, domains, scenarios.
5. **Review** → steward + legal reviewer; mark provenance class.
6. **Publish** → CI build, coverage dashboard, changelog.

Tooling for scale: structured extraction assisted by LLM agents with **mandatory human review** for every L/D-class item; every extracted obligation stores the verbatim source quote + clause pointer so reviewers can check in seconds. No requirement derived by an agent is published without a named human reviewer.

## 4. Project plan (indicative; effort in working days, duration for one lead + AI-assisted research; adjust to team size)

| Phase | Content | Duration | Exit criterion |
|---|---|---|---|
| **0 — Frame** | Doc 01/02, decisions in §6, repo set-up decisions | wk 0–1 | Stakeholder go on structure & taxonomy |
| **1 — Source register** | R1–R4 collection; access to author repos/Medium; bibliography | wk 1–3 | ≥90% of priority-A sources registered with version/date |
| **2 — Foundations** | Jekyll skeleton, schemas (JSON-Schema + SHACL), CI, templates, graph explorer MVP; EBW obligation extraction (full) | wk 2–5 | Site builds on Pages; EBW obligations 100% extracted & reviewed |
| **3 — Core requirements** | FUN, TRU, INT, NFR, CER, GOV from EBW + eIDAS + ARF + core standards | wk 4–9 | v0.5 catalogue; ≥95% EBW obligations covered; matrices live |
| **3b — Perspective packs** | B2B, B2G (four obligation types), B2C/EUDIW; Reporting & Registry Obligations Atlas v0 | wk 6–11 | Each perspective has scenarios, ≥10 reviewed requirements, and atlas entries for NIS2, DPP, EPRL, AI Act DB |
| **4 — Domain overlays & compliance** | DPP/ESPR(+AAS), data spaces (DSP/DCP), automotive, pharma/GxP, AI/agentic/physical; horizontal law (GDPR, NIS2, CRA, Data Act, AI Act) | wk 8–14 | Overlay per domain with ≥10 reviewed requirements and scenarios |
| **5 — Architecture** | Planes, building blocks, ADRs, scoring matrix, reference flows | wk 10–16 | Alternatives scored against v0.9 requirements |
| **6 — Validate & release** | Workshops (IDTA, data space, I4.0, AI), public review, fixes, v1.0, DOI | wk 15–20 | v1.0 tagged; review comments resolved or logged |
| **7 — Sustain** | Trilogue tracking, version-diff updates, new domains, German summaries | ongoing | Monthly legal-status update |

Milestones: **M1** structure approved · **M2** site live (skeleton) · **M3** EBW obligations complete · **M4** v0.5 · **M5** domain overlays · **M6** architecture ADRs · **M7** v1.0.

Critical path: legislative text moves (trilogue) → re-baseline obligations. Mitigation: pin versions, provide diff view, keep requirements tied to obligation IDs so changes propagate.

## 5. Stakeholder engagement plan

| Group | Role in project | Engagement |
|---|---|---|
| IDTA (AAS, DPP WGs) | Validate AAS↔LPID/EAA mapping, DPP access-right requirements | Working session after Phase 2; review of DOM-DPP overlay |
| Data space community (DSSC, IDSA, Catena-X, Eclipse DSP/DCP) | Validate DAT requirements and DCP/DSP profiling | Review round Phase 4 |
| Industry 4.0 / Industrial AI / Agentic / Physical AI | Machine/agent identity and delegation requirements | Workshop Phase 4 |
| Standards experts (ETSI/CEN, OpenID, W3C, DIF) | Standards mapping accuracy | Targeted review Phase 3/5 |
| Authorities & registry operators (national portal owners, ENISA, DG GROW/CNECT, EMA) 🔎 | Validate B2G flows, reporting channels, EBW acceptance | Interviews Phase 3b/4 |
| Consumer/B2C (consumer organisations, EUDIW ARF team, retail/e-commerce) | Validate B2C and EBW↔EUDIW flows | Review Phase 3b/6 |
| Legal/compliance (Bitkom, notaries, law firms, authorities) | Legal interpretation check | Reviewer role Phase 2–6 |
| Sector (automotive, pharma/GxP, finance) | Domain overlays | 1–2 expert interviews each |

## 6. Decisions needed from you (blocking items first)

1. ~~Where does the work live?~~ **Resolved:** fork at `cstoecker/business-wallet-requirements`; branch `claude/friendly-brown-gplwfl`; Spherity repo gets a PR later.
2. ~~Access to source material~~ **Resolved:** `spherity/spherity-research`, `webuild-consortium-architecture` and `webuild-attestation-rulebooks-catalog` cloned read-only as background; three Medium articles supplied as PDFs. Open: where the author's own WE BUILD contributions live (repo/branch/PR).
3. ~~Publication stance~~ **Resolved:** public from day one; neutral look (no vendor branding).
4. ~~Languages~~ **Resolved:** English only.
5. **Licence:** CC BY 4.0 for content — still to confirm.
6. ~~Scope boundary~~ **Resolved:** European Business Wallet **plus** the EUDI wallet interface, interactions and workflows (first-class, not a footnote).
7. ~~MiFIT~~ **Resolved:** MiFID II/MiFIR (given as an example only).
8. ~~Sources in traceability/graph~~ **Resolved:** official sources, ecosystem specifications (IDTA, Catena-X, Gaia-X, WE BUILD) and the OID 2025 paper only (source rule in R1).
9. **Effort/resourcing:** one lead with AI-assisted research, or also named domain stewards (reviewers owning IDTA/AAS, DPP, data space, pharma, automotive, legal)? Drives the timeline above.

## 7. Risks

| Risk | Mitigation |
|---|---|
| EBW text changes during trilogue | Version pinning, diff view, obligation-ID based traceability |
| Legal misinterpretation | Provenance classes, "not legal advice", legal reviewer gate |
| Standards copyright (ETSI/ISO text) | Link + paraphrase; no verbatim copying beyond short quotes |
| Scope explosion (many domains) | Core first, overlays with fixed template and minimum size |
| LLM-extraction errors | Verbatim quote + human reviewer mandatory; spot-check sampling |
| Perception of vendor bias | Technology-neutral requirements, neutral architecture scoring, open contribution |
| Emerging areas (agentic/physical AI) immature | Maturity facet; flag as assumptions (class A) |

## 8. Proposed next steps (once you approve doc 01/02)

1. Resolve decisions 1–3 above.
2. Create the working branch/fork, scaffold the Jekyll site (Phase 2 skeleton) with the taxonomy and schemas.
3. Start Phase 1: source register + EBW obligation extraction in parallel research agents.
