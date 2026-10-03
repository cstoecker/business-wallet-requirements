---
title: Methodology
parent: Requirements
nav_order: 1
permalink: /requirements/methodology/
description: "How a statement in a law, standard or ecosystem specification becomes a traceable, reviewed requirement: sources, lifecycle, categories, facets, provenance classes, traceability and change control."
---

# Requirements management methodology

How a statement in a law, standard or ecosystem specification becomes a traceable, reviewed requirement on this site. *Status: draft. Analysis, not legal advice.*

## 1. Principles

1. **Traceability first.** A requirement without a source is an *assumption* and is labelled so. A source obligation without a requirement is a *gap* and appears in the coverage report.
2. **Normative and informative are never mixed.** Every statement carries a provenance class.
3. **Data is the product, pages are views.** Structured data in Git (`_data/`) is the source of truth; pages, matrices and the graph are generated from it.
4. **Status-aware.** The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); every legal reference is pinned to a document version and date, and changes are tracked as a diff.
5. **Technology-neutral requirements.** Requirements say *what*; architecture alternatives say *how*. No product names.
6. **Human review.** No legal or derived requirement is published without a named human reviewer.

## 2. Sources: what may enter

| Class | Examples | Rank |
|---|---|---|
| **official** | EU legislation, proposals, Council/Parliament/Commission documents, implementing acts, the EUDI ARF | highest |
| **standard** | ETSI/CEN, ISO/IEC, W3C, IETF, OpenID Foundation, Eclipse DSP/DCP | high |
| **ecosystem-specification** | IDTA, Catena-X, Gaia-X, WE BUILD (blueprint, ADRs, rulebooks), Manufacturing-X, Factory-X, energy data-X, CIRPASS-2 | below law and formal standards |
| **academic** | peer-reviewed journal papers and working papers of recognised institutions (NBER, CEPR, OECD, World Bank, IMF), used for business-case claims only, never as the basis of a requirement | context for claims |
| **paper** | *Towards the European Business Wallet* (Open Identity Summit 2025, DOI 10.18420/oid2025_09) | context for derivation |

From IDTA/AAS, Catena-X and IDSA only **high-level, technology-neutral requirements** are taken, never implementations; AAS is assessed as an implementation artefact in the architecture section. Blog posts, Medium articles, position papers, vendor material and repositories are **not** graph sources; they appear only in the non-normative reading list. Every source is recorded in the source register (`_data/graph/sources.yml`) with issuer, version, date, URL and a verification state (`read`, `snippet`, `unverified`).

## 3. Lifecycle

1. **Collect:** register the source with version, date and URL.
2. **Extract:** record atomic obligations with the verbatim quote, the clause pointer and who owes what to whom.
3. **Derive:** write one technology-neutral requirement per obligation in EARS style ("When *trigger*, the *system* shall *response*"), with ID `EBW-<CAT>-<NNN>` (immutable once published, deprecated instead of deleted).
4. **Link:** connect to building blocks, standard clauses, conformance checks and scenarios.
5. **Review:** domain steward plus, for law-derived content, a legal reviewer.
6. **Publish:** CI validates, builds and deploys; the coverage dashboard updates.

Ecosystem requirement statements (see [Ecosystems & initiatives]({{ '/ecosystem/initiatives/' | relative_url }})) enter at step 2 as `candidate` statements and are derived into EBW requirements in step 3.

## 4. Categories

| Code | Category | Covers |
|---|---|---|
| FUN | Functional | identify, authenticate, store and present attestations, sign and seal, mandates, delivery and notifications, directory lookup, issuance, revocation |
| NFR | Non-functional | security, privacy, availability, performance, usability, accessibility, auditability, portability, sustainability |
| INT | Interoperability and semantics | protocols, data models, credential formats, vocabularies, cross-domain mapping |
| TRU | Trust and assurance | levels of assurance, trust anchors, trust lists, qualified trust services, registration, revocation, key custody |
| CER | Certification and conformity | schemes, conformity assessment, testing, evidence, surveillance |
| GOV | Governance | roles, liability, rulebooks, change control, onboarding, disputes, supervision |
| LEG | Legal and compliance (derived) | obligations from GDPR, NIS2, DORA, CRA, AI Act, sector law |
| DAT | Data space and sovereignty | usage policies, contract negotiation, connector-wallet binding, DSP/DCP profiles |
| OPS | Operational and service | SLAs, support, incidents, key ceremonies, lifecycle, continuity |
| DOM | Domain-specific | overlays per industry |
| BIZ | Business and adoption | cost, onboarding friction, SME access, migration |
| CON | Constraints and assumptions | mandated technology, legal limits, explicit assumptions |
| TRN | Transition and migration | coexistence with legacy, phased roll-out |

## 5. Facets

Orthogonal to the category, so the catalogue can be filtered: **perspective** (B2B, B2G, B2C, G2B, B2E, M2M/A2A), **obligation type** (authenticate, authorise, report/notify, register/publish, disclose, retain, deliver/receive, sign/seal, verify), **plane** (trust, control, data, governance, assurance and evidence), **actor**, **lifecycle phase**, **priority** (MUST/SHOULD/MAY, and legally mandatory versus recommended), **maturity**, **domain tag**, **verification method** (inspection, test, analysis, audit, certification).

## 6. Provenance classes

| Class | Meaning |
|---|---|
| **L** | directly mandated by law or regulation |
| **S** | mandated or profiled by a standard or specification, including ecosystem specifications |
| **D** | derived by us from L or S for a domain |
| **A** | assumption or recommendation; never cites a non-official source as authority |

## 7. Traceability

Formal source (clause) → obligation → requirement → capability or building block → standard or profile clause → conformance check or evidence ← industry scenario. Relations in the graph: `derivedFrom`, `interpretedAs`, `refines`, `conflictsWith`, `dependsOn`, `satisfiedBy`, `specifiedBy`, `verifiedBy`, `appliesToDomain`, `supersedes`, `mapsTo`, `assumes`, plus for ecosystems `hasUseCase`, `imposes` and `relatesTo`.

Coverage metrics regenerated on every build: share of obligations covered by a requirement, requirements with a source (orphan check), with a verification criterion, mapped to a standard clause or building block, per-domain and per-plane heatmaps, and changes since the last legal text version.

## 8. Change control and versioning

Issue, proposal (pull request with data diff), review by steward and legal reviewer, merge, versioned release (SemVer for the baseline: `v0.x` drafts, `v1.0` after the first stakeholder review) and a citable snapshot with a DOI. CI gates: schema validation, orphan and coverage thresholds, link check, accessibility check.

## 9. Confidence markers

<span class="vtag v-ok">verified</span> verified in a source that was read. <span class="vtag v-todo">to verify</span> to verify. Unverified facts are never presented as verified.
