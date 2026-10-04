# Access-controlled verifiable evidence graph: structure of the stakeholder presentation

Status: structure for discussion, to be broken down into slides next. Audience: Industry 4.0, IPCEI-AI, IDTA, Catena-X and Manufacturing-X stakeholders. Language of the deck: English.

The aim is to choose the technology base from requirements, not from the tool a community already owns. The talk walks from industry needs down to architecture properties, concrete requirements, technology layers and what each ecosystem builds on.

## Core claim to be tested

One pattern recurs in B2G registers, digital product passports, AI agents, data spaces and supply chains: **an access-controlled, verifiable evidence graph under open-world semantics, operated with legal compliance**. Writers and readers authenticate and are authorised (control plane). Evidence is read, checked for integrity, authenticity and issuer authority, and acted on (data plane). Risk scoring and triggered actions close the loop where the two planes converge.

The claim is a hypothesis for the room. Each domain example must show the same five elements or the room should say where it does not hold.

| Element | B2G register (macro) | Digital product passport (micro register) | Agent card (micro register) | Data space catalogue |
|---|---|---|---|---|
| Subject nodes | Companies, products, facilities | Product, batch, component | Agent, organisation, tools | Offering, provider, dataset |
| Evidence nodes | Filings, certificates, authorisations | Declarations, test reports, events | Attestations, mandates, audit records | Credentials, policies, usage records |
| Who may write | Authenticated and authorised filers | Manufacturer, supply chain actors, authorities | Owner, issuers, monitors | Participant, catalogue operator |
| Who may read | By policy: public, authorities, partners | By role: market surveillance, recyclers, customers | Other agents, relying parties | Participants by policy |
| What it triggers | Decisions, approvals, audits | Compliance checks, recalls, market access | Delegation, tool calls, shutdown | Contract, transfer, process start |

## Part A. Why: industry needs and the shared pattern (5 slides)

1. **Evidence is everywhere, trust is not.** Any PDF or API response can be forged. Integrity, authenticity and the authority of the issuer must be checkable by machines.
2. **Four domains, one shape.** The table above, drawn as one diagram: subjects, evidence, writers, readers, triggers.
3. **Macro and micro.** A register is a large graph. A passport or an agent card is a small one with the same access rules. Dynamic micro graphs allow real-time checks, for example behavioural drift of an agent.
4. **Control plane and data plane converge.** Control plane: authenticate, authorise, apply policy. Data plane: look at the data, provenance, trustworthiness, risk score, then decide what to trigger: start an agent, take over data, start a process, call an API.
5. **Why open-world semantics.** New facts and new parties can be added without redesigning a schema; meaning is shared by globally resolvable identifiers; closed models break when a new jurisdiction or sector joins.

## Part B. Top-down derivation (6 slides)

A derivation chain on one slide, then one slide per level. Each level cites what is source-based and what is our reading.

| Level | Content |
|---|---|
| 0 Industry needs | Semantically rich international supply chain data; compliance evidence across jurisdictions; AI agents acting for companies; real-time decisions at volume |
| 1 Capabilities | Authenticate and authorise writers and readers; verify integrity, authenticity, authority; link evidence into a graph; keep legal compliance by design; score risk across trust domains; trigger actions |
| 2 Architecture properties | Selection criteria, see below |
| 3 Concrete requirements | Mapped to the catalogue (clusters K18, K01, K03, K10, K16, K17) and to new requirement families, see below |
| 4 Technology implications | Layers: identifiers, credential model, securing mechanism, semantics, policy, transport, scale |
| 5 Ecosystem implications | What Catena-X, AAS and IDTA, Manufacturing-X and IPCEI-AI keep, add or change |

**Architecture properties as criteria (level 2).**

1. Open-world semantics, with globally resolvable identifiers and shared vocabularies.
2. Global acceptance: specified by bodies with worldwide membership (W3C, IETF, ISO, UN/CEFACT, GS1, OpenID Foundation), implemented outside Europe.
3. Open access: specifications and vocabularies usable without a licence fee (a licensed classification such as ECLASS fails this; it can be mapped, not made the base).
4. Verifiability: integrity, authenticity and authority of the issuer for every statement.
5. Access control and selective disclosure: reading and writing by policy, minimal disclosure.
6. Legal compliance by design: eIDAS, GDPR, sector law, cross-jurisdiction rules expressed as policy and as evidence.
7. Machine and AI processability: low latency, high throughput, streaming, caching, batch verification.
8. Federation: several trust domains and issuers without a central authority.
9. Durability and exit: verifiable after the provider or the certificate is gone; portable between providers.

## Part C. Risk scoring as the consumer of the graph (3 slides)

1. **What scoring needs.** Evidence from several trust domains, each with its issuer, its assurance level and its provenance chain.
2. **Requirements on scoring.** Inputs are verifiable statements, not copies; every score names its evidence and the policy used; scores are replayable; legal limits for automated decisions about people and for high-risk AI are respected.
3. **Presenting once, using everywhere.** Once evidence is in the graph, the same record serves different industries, sectors and jurisdictions by policy and by projection, not by re-collecting data.

Open point: the catalogue has no requirement on risk scoring yet. It is a gap to fill.

## Part D. From abstract to concrete requirements (4 slides)

1. **What the catalogue already covers.** Control plane and data plane requirements (cluster K18, 183 requirements, 45 at P1), mandates (K03), evidence and audit (K10), formats (K01), AI-first (K16), cross-jurisdiction identity (K17).
2. **What it does not cover.** No P1 requirement on a graph model, on open-world semantics, on semantic profiles, on scale, or on risk scoring.
3. **New requirement families to research.** Evidence graph model and linking; resolvable identifiers and vocabularies; write and read authorisation on graph elements; provenance and issuer authority; policy language and enforcement points; cross-jurisdiction legal policy; scoring inputs and explainability; throughput, latency and streaming; update and revocation of graph elements; licence and openness of vocabularies.
4. **Rule for the catalogue.** Each new requirement keeps a source (law, standard, ecosystem specification) or is marked as derived (D) with its derivation. The pattern itself is a derivation (D), not law.

## Part E. Technology implications by layer (5 slides)

One slide per layer with the options considered and the criteria they meet. This is a method slide first; the scoring is filled from sources, not from preference.

| Layer | Candidates to assess |
|---|---|
| Identifiers | Decentralised identifiers, web identifiers, EUID, GLN, LEI, product identifiers (GS1 Digital Link) |
| Credential model | W3C Verifiable Credentials Data Model 2.0 as the common data model |
| Securing mechanism | SD-JWT VC, ISO mdoc, W3C Data Integrity, JOSE and COSE |
| Semantics | JSON-LD and RDF, SHACL for validation, PROV for provenance, DCAT for catalogues, ODRL for policy, sector vocabularies (for example UN Transparency Protocol, GS1) |
| Policy and enforcement | ODRL profiles, policy engines at the control plane |
| Transport | OpenID for Verifiable Credential Issuance and Presentation, Dataspace Protocol, HTTP APIs, event streams |
| Scale | Context caching, canonicalisation cost, batch and streaming verification, status lists, graph stores |

**Tension to show openly.** Implementing Regulation (EU) 2026/1731 lists SD-JWT VC and mdoc for the EUDI Wallet. The JSON-LD realisation of ETSI TS 119 472-1 (clause 7) is outside that list. A global, open-world graph on W3C Verifiable Credentials therefore needs a profile or bridge to the EU legal formats. This must be a decision, not a footnote. Sources: dec-01 and DEC-12 research notes.

## Part F. What it means for the ecosystems (4 slides)

One slide per ecosystem with three lines: what stays, what is added, what changes. Assumed starting points (to verify with each community):

| Ecosystem | Starting point | Questions |
|---|---|---|
| Catena-X | Credentials and decentralised identifiers already used; connector-based data exchange; BPN as ecosystem identifier | Credential-ise catalogue entries and policies; map BPN to EUID and EBWOID; trust anchors beside EU lists |
| AAS and IDTA | Typed submodels with semantic identifiers; shell as implementation artefact; passport work | Semantic identifiers as resolvable identifiers; open vocabulary beside licensed classifications; verifiable submodel elements; shell as one carrier of the graph |
| Manufacturing-X | Federation of sector data spaces | Shared evidence model across sectors; trust domain bridging |
| IPCEI-AI | Agent protocols and agent cards | Agent card as verifiable micro register; behavioural evidence streams; mandates and limits; real-time scale |

## Part G. Method for choosing architecture options (4 slides)

Not "we have a hammer", but a repeatable method:

1. State the industry needs and the capabilities they imply.
2. Fix the architecture properties as criteria and weigh them with the stakeholders (the weights are the first decision).
3. Generate options without owner bias: a single ecosystem standard, EU legal formats only, W3C VC with JSON-LD, hybrid with profiles.
4. Score each option per criterion with evidence (source, version, status), not opinion. Mark unknowns as unknown.
5. Take the intersection: the layers where all serious options agree are the base; the layers where they differ become decisions.
6. Test with sensitivity (what if the weights change) and name tripwires (what would change the decision).
7. Record the decision as a decision page with its assumptions and a review date.

## Part H. Cross-jurisdiction and AI-first scale as hard tests (3 slides)

1. **Cross-jurisdiction.** Germany, EU, and beyond (including partners with no business wallet): legal compliance as policy and evidence; mapping of legal regimes to evidence types; acceptance of third-country evidence and assurance levels.
2. **AI-first scale.** Real-time, high throughput, low latency, mass processing. Questions: verification cost per statement, caching, streaming evidence, dynamic micro graphs for behavioural drift.
3. **Global acceptance check.** For each candidate standard: who specifies it, who implements it, outside Europe, and under which licence.

## Part I. Close (2 slides)

1. **Decisions we ask for.** Confirm the pattern, the nine criteria and their weights, the scope of the evidence graph (EBW only or the wider ecosystem layer).
2. **Next steps.** Research of the new requirement families, scoring of options with sources, DEC-12, concept articles on the control plane, the data plane and the evidence graph.

Total: about 36 slides for a half-day session, or Parts A, B, G and I (about 17 slides) for 90 minutes.

## Claims that need support before the talk

These statements are plausible but not yet backed by sources in the catalogue. Each needs a primary source or a label as our reading.

- UN Transparency Protocol and its use of W3C Verifiable Credentials, decentralised identifiers and JSON-LD vocabularies.
- GS1 EPCIS 2.0 as a supply chain event model that fits "every event is a node".
- The share of Catena-X data exchange that already uses credentials, and what the catalogue entries carry.
- Licence terms of ECLASS and of the IDTA semantic identifiers in use.
- Implementation of W3C Verifiable Credentials 2.0 outside Europe (North America, Asia).
- Performance of JSON-LD processing at scale.
- Legal limits for risk scoring (GDPR Article 22, AI Act) for each use case.
- Scope: the catalogue's scope is the EBW and the EUDI Wallet interfaces and workflows. A universal evidence graph reaches into data spaces and AI. The scope decision belongs to the owner of the site.

## Scope note

The evidence graph pattern widens the scope of the site from the wallet to the ecosystem layer above it. Decide first whether the pattern lives as theme 10 of the stakeholder brief and DEC-12 (recommended, with the new requirement families as cluster K18), or as a separate track.
