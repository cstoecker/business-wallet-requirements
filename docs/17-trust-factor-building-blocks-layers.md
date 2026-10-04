# Trust as a production factor, universal building blocks and the layered model

Status: working paper for the stakeholder presentation. It extends `docs/16-evidence-graph-presentation-structure.md`. Statements marked "our reading" are derivations of the authors; sourced statements cite the research notes. Research notes for the economics of trust, the legal map for Germany and the EU and the protocol and format matrix are in progress and replace the placeholders marked "pending".

## 1. Start: trust as a production factor (working definition)

Working definition: **trust is an input that a business needs, in addition to labour, capital and knowledge, to produce and exchange goods and services with parties it does not control.** It is produced, not found: a relying party turns checkable evidence into a decision to rely.

Trust is produced from six inputs, each of which can be checked by a machine:

| Input | Question the relying party asks |
|---|---|
| Identity | Who made this statement, and which legal person is it about? |
| Authority | Was the issuer or actor entitled to make it or to act? |
| Integrity and authenticity | Is it unchanged and really from that source? |
| Provenance | Where does it come from, through which hands? |
| Compliance | Which rule does it satisfy, in which jurisdiction? |
| Freshness | Is it still valid now? |

Output: a decision to rely, to trade, to delegate or to trigger a process, at a risk the relying party can name (risk scoring).

Why this framing matters for the architecture: if trust is a production factor, its cost and quality can be compared across designs. A design that lowers the cost of producing the six inputs for many parties and many sectors is worth more than one that serves a single community. This is the criterion behind "universal" in the building blocks below.

Pending: economics sources (transaction cost, information asymmetry, institutional trust) and quantified claims from impact assessments (research note `RES-trust-factor`). Until verified, the framing is our reading.

## 2. Universal architecture building blocks (derivation)

Derived from the six inputs and the recurring pattern (registers, passports, agent cards, catalogues). Each block answers one input and is independent of the sector.

| Block | Answers | Notes |
|---|---|---|
| B1 Identifier | Identity | Globally unique, resolvable identifiers for subjects, issuers, verifiers; primary and secondary identifiers mapped |
| B2 Statement | Integrity, authenticity | A signed claim with issuer, subject, validity and status: the credential, in some format |
| B3 Vocabulary | Meaning | Published, versioned, resolvable terms; shapes for validation |
| B4 Evidence graph | Provenance | Statements linked into a graph; entries stay verifiable; access controlled |
| B5 Authority statement | Authority | Representation, mandate, delegation as statements with scope, limits, onward delegation |
| B6 Policy decision and enforcement | Compliance | Control plane: authenticate, authorise, apply policy; enforcement at the point of access |
| B7 Trust anchor and registry | Authority of issuers | Trust lists, registries and ecosystem anchors tell who may issue what |
| B8 Status and lifecycle | Freshness | Validity, suspension, revocation, expiry, privacy-preserving status |
| B9 Protocol adapter | Connectivity | Extension modules that carry statements over issuance, presentation, exchange, delivery and agent protocols |
| B10 Scoring | Decision | Risk score from verified statements under a named policy; replayable |
| B11 Audit and attribution | Accountability | Every act attributed to the owner; logs that are themselves evidence |
| B12 Key custody | Signing and sealing | Where the keys live and who controls them |

Rule: a building block is universal if it needs no change when a new sector, jurisdiction or actor type joins.

## 3. Layered model: foundation first

| Layer | Content | Clusters on the requirements site |
|---|---|---|
| L0 Purpose | Trust as production factor, the six inputs | none, framing |
| L1 Foundation (decide first) | B1 identifiers, B2 statement format, B3 vocabulary, B4 graph, B5 authority, B6 control and data plane, B12 keys | K01, K02, K03, K04, K06, K17, K18 |
| L2 Mechanisms on the foundation | Trust frameworks, lifecycle, evidence and audit, protocol adapters and delivery, privacy, security, governance, conformity | K05, K07, K08, K09, K10, K11, K12, K13, K14 |
| L3 Context | Adoption, AI-first use, domains, operations, business case, constraints, transition | K15, K16 and the categories DOM, OPS, BIZ, CON, TRN |

**Why the foundation is decided first (our reading):**

1. **Dependency.** Every mechanism refers to the format, the identifier and the authority model. A trust list, a revocation rule or a log schema cannot be written before it is clear what a statement and an identifier are.
2. **Cost of change.** Signed evidence outlives software. Changing the credential format or the identifier scheme after issuing invalidates or strands existing evidence. Governance rules can be changed; issued credentials cannot be re-signed by the old issuer.
3. **Multiplier.** A common foundation lets every mechanism and every ecosystem be built once and reused. Each additional foundation variant multiplies the mechanisms to be specified, tested and certified.
4. **Enforceability.** Governance and conformity need something concrete to test against. Without a fixed foundation, a rulebook states intentions that no verifier can check.
5. **Legal fit.** Law names formats, identifiers and trust services. The foundation is where law and technology meet, so the choice carries legal risk early.

Governance and trust mechanisms (L2) sit on this base. They define who may issue, who supervises and how disputes are resolved, using the same statements, identifiers and authority model as everything else, so they are themselves evidence in the graph.

## 4. Requirement categories as secondary views

The 14 categories describe the kind of requirement. The topics discussed here (foundation) are the primary organising principle; categories are secondary views.

| Category | Role | Requirements | Of which touch a foundation cluster |
|---|---|---|---|
| FUN functional | Carries foundation behaviour (what the wallet does) | 60 | 53 |
| INT interoperability and semantics | Carries foundation (formats, identifiers, semantics) | 98 | 85 |
| DAT data space and sovereignty | Carries foundation (graph, policy, data plane) | 41 | 35 |
| NFR non-functional | Constrains the foundation (security, performance, availability) | 122 | 82 |
| AIF AI-first | Applies the foundation to agents; collection with cross-references | 68 | 46 |
| TRU trust and assurance | Built on the foundation (anchors, lifecycle, assurance) | 176 | 121 |
| CER certification | Built on the foundation (conformance against a fixed format) | 23 | 16 |
| GOV governance | Built on the foundation (rules about who may do what) | 57 | 29 |
| LEG legal and compliance | Built on the foundation (legal duties mapped to elements) | 80 | 41 |
| OPS operational | Built on the foundation (service operation) | 47 | 22 |
| DOM domain-specific | Context (sector profiles) | 26 | 23 |
| BIZ business and adoption | Context | 8 | 2 |
| CON constraints and assumptions | Context | 9 | 5 |
| TRN transition | Context | 4 | 4 |

Counts are from the review data of 2026-10-04 (a requirement may touch several clusters). Reading: INT, FUN and DAT carry the foundation; TRU, GOV, CER, LEG and OPS are built on it; DOM, BIZ, CON and TRN give context. NFR constrains all layers.

## 5. Credential format and protocol adapters (pending research)

The choice of credential format is one of the key design decisions of L1. Proposed approach: a format-agnostic statement model (B2) with one or more format profiles, and protocol adapters (B9) as extension modules that carry a statement over a given protocol where the format allows it. Pending: the protocol and format matrix (`RES-protocol-format-matrix`): OpenID4VCI and OpenID4VP, Dataspace Protocol and Decentralized Claims Protocol, DIDComm, qualified electronic registered delivery (EN 319 522, AS4), A2A, Agent Network Protocol, MCP.

## 6. Legal compliance layer for Germany and the EU (pending research)

Pending: the legal map (`RES-legal-map`): eIDAS, the EBW proposal and Council text (kept apart from law in force), GDPR, Data Act, ESPR, AI Act, NIS2, CRA, company law, and German law (Vertrauensdienstegesetz, commercial register law, retention rules, supply chain due diligence, supervision). Each duty is mapped to the building block it constrains.
