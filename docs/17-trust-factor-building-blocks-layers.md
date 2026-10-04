# Trust as a production factor, universal building blocks and the layered model

Status: working paper for the stakeholder presentation. It extends `docs/16-evidence-graph-presentation-structure.md`. Statements marked "our reading" are derivations of the authors; sourced statements cite the research notes. Research notes for the economics of trust, the legal map for Germany and the EU and the protocol and format matrix are in progress and replace the placeholders marked "pending".

## 1. Start: trust as a production factor (Spherity Research, Harald and Stöcker, 2026)

This section follows the executive research brief of the authors (SRC-WHY-2026, CC BY 4.0, evidence cut-off 30 August 2026). The brief is the authors' own analysis; its scenario figures are conditional, not forecasts.

**Definition used in the brief.** A production factor in a broader managerial sense is an input that materially affects how productively people, capital, data and technology can be combined. Trust is not a separate national-accounts category but an enabling complement: without sufficient trust, valuable AI systems, data, machines and skills cannot be used fully. Trust becomes a primary production factor in a zero-trust-by-default threat landscape, where offensive AI, deepfakes and fabricated credentials spread at near-zero marginal cost.

**Four mechanisms by which trust enters production.**

1. It reduces transaction and coordination costs by replacing repeated bilateral checks with reusable identity, mandates and evidence.
2. It expands authorised process depth: more steps move from human-assisted preparation to accountable execution across organisations.
3. It raises risk-adjusted productivity by reducing fraud, error, unsafe action, expected loss and incident duration.
4. It creates infrastructure and network effects: accepted credentials, policies and evidence formats are reused by further transactions.

**Trusted execution capital** is the accumulated stock of reusable technical, legal and organisational capabilities that let digital and physical actions be attributed, constrained, evidenced, monitored and corrected. Trust as a production factor at the point of use is supplied by this stock.

**Three layers kept distinct and connected.** AI Governance (legitimate purposes, decision rights, accountability), Trustworthy AI (required system qualities) and Trusted AI (selected claims and controls made machine-verifiable for an actor, action, context and time). A credential proves a claim; it does not prove that an action is authorised now.

**The six-question execution chain** (the brief, section 3.2) is the backbone of this paper:

1. Who or what is acting? Identity and attribution.
2. For whom may it act? Mandate and delegation.
3. Which facts support the action? Verifiable evidence and provenance.
4. What do those facts mean? Shared semantics and validation rules.
5. Is the action permitted now? Current status, policy and runtime authorisation.
6. What happens if execution fails? Monitoring, interruption, recovery and accountability.

**Trust Algorithms** (NIST SP 800-207: the process a policy engine uses to grant or deny access) are extended in the brief to two planes: a control-plane algorithm evaluates identity, mandate, workload posture and policy; an evidence-plane algorithm evaluates provenance, authority, semantic validity, freshness, contradiction and fitness for purpose. An action decision combines both with model state, context, security posture, safety limits and recoverability. Outputs: permit, restrict, escalate or deny.

**Why this matters for the architecture.** If trust is a production factor, the cost and quality of producing it can be compared across designs. A foundation that serves many parties and sectors lowers that cost; one that serves a single community does not. That is the meaning of "universal" in the building blocks below.

Supporting economics (research note `trust-factor-economics`): Coase 1937, Williamson 1979 and 1985, Akerlof 1970, Luhmann 1968 and Fukuyama 1995 are confirmed bibliographically, with the primary texts not opened. No verified text uses the phrase "trust as production factor". The impact assessment SWD(2025) 837 estimates a trust-related value of EUR 16.66 billion from a vendor trust index (correlational). The brief cites Commission modelling of direct annual benefits of EUR 58.4 to 169 billion across assumptions (ex ante; to verify against SWD(2025) 837).

## 2. Universal architecture building blocks (derivation)

Derived from the six-question execution chain and the recurring pattern (registers, passports, agent cards, catalogues). Each block answers one question of the chain and is independent of the sector. The column 'Answers' gives the question number.

| Block | Answers | Notes |
|---|---|---|
| B1 Identifier | Q1 who acts | Globally unique, resolvable identifiers for subjects, issuers, verifiers; primary and secondary identifiers mapped |
| B2 Statement | Q3 facts: integrity, authenticity | A signed claim with issuer, subject, validity and status: the credential, in some format |
| B3 Vocabulary | Q4 meaning | Published, versioned, resolvable terms; shapes for validation |
| B4 Evidence graph | Q3 facts: provenance | Statements linked into a graph; entries stay verifiable; access controlled |
| B5 Authority statement | Q2 for whom | Representation, mandate, delegation as statements with scope, limits, onward delegation |
| B6 Policy decision and enforcement | Q5 permitted now | Control plane: authenticate, authorise, apply policy; enforcement at the point of access |
| B7 Trust anchor and registry | Q2, Q3: who may issue what | Trust lists, registries and ecosystem anchors tell who may issue what |
| B8 Status and lifecycle | Q5 current status | Validity, suspension, revocation, expiry, privacy-preserving status |
| B9 Protocol adapter | Connects all questions across ecosystems | Extension modules that carry statements over issuance, presentation, exchange, delivery and agent protocols |
| B10 Scoring | Q5 evidence-plane Trust Algorithm | Risk score from verified statements under a named policy; replayable |
| B11 Audit and attribution | Q6 failure, accountability | Every act attributed to the owner; logs that are themselves evidence |
| B12 Key custody | Q1, Q2: who controls the signing keys | Where the keys live and who controls them |

Rule: a building block is universal if it needs no change when a new sector, jurisdiction or actor type joins.

## 3. Layered model: foundation first

| Layer | Content | Clusters on the requirements site |
|---|---|---|
| L0 Purpose | Trust as production factor, the six-question chain | none, framing |
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
