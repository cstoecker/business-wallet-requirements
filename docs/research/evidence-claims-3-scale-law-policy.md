# RES-evidence-claims-3: support for claims in docs/16 ("Claims that need support before the talk")

Date of work: 2026-10-04. Primary sources only. Columns: fact | source | read in full / part / not read | to verify. Quotes under 25 words. "not found" = no primary source located. Facts marked "our reading" are analysis, not source text. New source IDs are in `/tmp/review/RES-evidence-claims-3-new_sources.yml`. No repo files edited.

Scope covered: docs/16 claims "Performance of JSON-LD processing at scale" and "Legal limits for risk scoring (GDPR Art 22, AI Act)"; plus policy languages, vocabularies, agent cards (support for DEC-12 and the evidence-graph talk).

## 1. JSON-LD 1.1, RDFC-1.0, VC DM 2.0

| Fact | Source | Read | To verify |
|---|---|---|---|
| RDFC-1.0 is a W3C Recommendation of 21 May 2024. Errata exist (page says "Errata exists"). | SRC-RDF-CANON-1.0 (new) header | part | Content of errata |
| Complexity: "Most RDF datasets can be canonicalized fairly quickly"; datasets with blank nodes lacking global identifiers raise the graph isomorphism problem, "believed to be difficult to solve quickly in the worst case". "existing real world data is rarely, if ever, modeled in a way that manifests as the worst case". | SRC-RDF-CANON-1.0 intro | part | No O()-bound is stated in the text read |
| Normative DoS defence: "Implementations MUST defend against potential denial-of-service attacks by raising suitable exceptions and terminating early" (4.4.3). Non-normative note: limit calls to Hash N-Degree Quads; "more than a couple of iterations ... per blank node would be unusual". | SRC-RDF-CANON-1.0 4.4.3 | part | |
| 7.1 Dataset Poisoning (non-normative): attackers can build datasets that take "large amounts of computing time"; mitigations: configurable timeout, iteration limit, schema validation before canonicalisation. | SRC-RDF-CANON-1.0 7.1 | part | |
| Hash algorithm is parameterisable (7.2); default SHA-256 per spec (default not re-quoted). | SRC-RDF-CANON-1.0 7.2 | part | |
| Implementation report (24 Feb 2026) lists 11 test subjects (Java, Python, C++, JavaScript, Rust, Elixir, TypeScript, Ruby). It is a conformance report. No timing or throughput data found. | SRC-RDF-CANON-REPORT (new) | part | Per-implementation pass counts not extracted |
| Data Integrity 1.0: canonicalisers "are required to detect these sorts of bad inputs and halt processing"; test suite includes poisoned datasets. Cryptosuites using transformations "are required to mitigate" such attacks. Also offers JCS suites (eddsa-jcs-2022, ecdsa-jcs-2019) that avoid RDF canonicalisation. | SRC-VC-DI-1.0 5.6, 5.7 | part | |
| Remote contexts (JSON-LD 1.1): "Remote context documents should be cached to prevent overloading the location of the remote context"; a documentLoader can statically cache well-known contexts; retrieval "may provide a signal of application behavior". | SRC-JSONLD-1.1 (documentLoader section) | part | |
| JSON-LD security (IANA section): contexts over HTTP "run the risk of being altered"; apps depending on remote context for mission critical purposes should "vet and cache" it; documents "may expand considerably ... might consume all of the recipient's resources". | SRC-JSONLD-1.1 appendix C | part | |
| JSON-LD privacy (section 12): fetching contexts exposes the processor and allows fingerprinting and MITM; publishers should cache or use a local version. Future SRI support is only a note (issue 86). | SRC-JSONLD-1.1 s12, s11 | part | |
| API: a processor-defined limit on the number of remote-context entries; exceeding it is a "context overflow" error. | SRC-JSONLD-1.1-API (new), grep | snippet | Read full algorithm |
| VC DM 2.0 (Rec 15 May 2025): base context `https://www.w3.org/ns/credentials/v2` is "a permanently cacheable static document"; extension contexts should be highly available via bundling, CDNs with long caching, or content-addressed URLs. | SRC-VCDM-2.0 s4.3 area, App B.1 | part | |
| VC DM 2.0: type-specific processing is allowed if context values are in expected order, "contents of the context files match known good cryptographic hashes", and domain experts approved them; static contexts with JSON Schema is "one acceptable approach". | SRC-VCDM-2.0 App B / processing | part | |
| VC DM 2.0: if JSON-LD expansion or RDF conversion of a credential results in an error, the credential "MUST result in a verification failure". Related resources can be protected by `digestSRI` / `digestMultibase`. | SRC-VCDM-2.0 App B.1, 5.3 | part | |
| VC DM 2.0 privacy: verifiers fetching external resources can signal to the issuer; Oblivious HTTP is named as one mitigation. | SRC-VCDM-2.0 8.7-style section | part | Exact section number |
| Performance data (throughput, latency, scaling) for JSON-LD processing or RDFC in W3C specs or reports: not found. Academic benchmark papers: not searched or retrieved, so none cited. Talk claim "Performance of JSON-LD processing at scale" therefore has no primary support; usable statements are the complexity and DoS texts above. | n/a | n/a | Search academic literature (label as academic) or run own benchmark |

## 2. Status lists and batch verification

| Fact | Source | Read | To verify |
|---|---|---|---|
| Bitstring Status List v1.0 is a W3C Recommendation, 15 May 2025. | SRC-VC-BSL-1.0 (registered) | part | |
| Default list size 131,072 entries = 16 KB uncompressed; "a few hundred bytes" when a handful are revoked; minimum list length 131,072 for group privacy. Example: 100,000 credentials about 12,500 bytes worst case. | SRC-VC-BSL-1.0 s1 | part | |
| `statusSize` default 1 bit; `ttl` in milliseconds before refresh "SHOULD be attempted"; issuers SHOULD publish so lists can be cached without tracking retrievers; verifiers SHOULD cache and use proxies or Oblivious HTTP. | SRC-VC-BSL-1.0 2.1, 2.2, 3.x, 6.3, 6.4 | part | |
| IETF Token Status List: draft-ietf-oauth-status-list-21, 21 June 2026, Active Internet-Draft (datatracker record last updated 2026-08-13, no RFC number found). Covers JWT, SD-JWT, CWT, mdoc. Not yet an RFC. | SRC-IETF-OAUTH-STATUS-LIST (registered), datatracker | part | Re-check RFC status before the talk |
| TSL structure: `bits` of 1, 2, 4 or 8 per token; array DEFLATE-compressed (zlib), base64url in JWT; `exp` and `ttl` (seconds) claims; optional Status List Aggregation URI for fetching, caching and "offline validation of the status ... for a period of time". | SRC-IETF-OAUTH-STATUS-LIST 4.1, 5, 9 | part | |
| TSL Appendix B sizes (compressed array, without signature/metadata), bits=1: 100k entries: 81 B (0.01% revoked), 1.4 KB (1%), 12.2 KB (50%); 1M entries: 442 B, 13.7 KB, 122.1 KB; 10M entries: 3.8 KB at 0.01%, about 1.2 MB at 50%. Worst case near 50% and random. | SRC-IETF-OAUTH-STATUS-LIST App B Table 1 | part (table first rows) | Rows for 100M entries not extracted |
| TSL privacy: one-time-use batches of Referenced Tokens recommended against collusion; random indices, decoys, several lists. | SRC-IETF-OAUTH-STATUS-LIST 12.5 | part | |
| Batch verification: the specs describe batches of one-time-use credentials (issuance side) and caching of lists. No spec text read defines "batch verification" of many presentations in one operation. | n/a | n/a | not found |
| Streaming / event-based status: neither BSL nor TSL defines push or streaming; both are pull with cache lifetimes. TSL recommends checking at iat+ttl for critical use. Real-time/event verification: not found in either. | SRC-VC-BSL-1.0, TSL 13.7 | part | |

## 3. Legal limits for scoring and automated decisions

| Fact | Source | Read | To verify |
|---|---|---|---|
| GDPR Art 22(1): right "not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects ... or similarly significantly affects" the data subject. | SRC-GDPR Art 22 (re-fetched, OJ text) | full article | |
| Art 22(2) exceptions: (a) necessary for contract, (b) authorised by Union or Member State law with safeguards, (c) explicit consent. 22(3): at least "right to obtain human intervention", express a point of view, contest. 22(4): no special-category data unless Art 9(2)(a) or (g). | SRC-GDPR Art 22 | full article | |
| Art 4(4) 'profiling' = automated processing of personal data to evaluate personal aspects "relating to a natural person", incl. economic situation, reliability, behaviour. | SRC-GDPR Art 4(4) | part | |
| Recital 71: examples "automatic refusal of an online credit application or e-recruiting practices"; allows law-authorised profiling incl. fraud and tax-evasion monitoring; safeguards include specific information, human intervention, explanation of the decision; controller should use appropriate mathematical or statistical procedures and prevent discriminatory effects. | SRC-GDPR recital 71 | full recital | |
| Recital 72: profiling "is subject to the rules of this Regulation governing the processing of personal data"; the Board may issue guidance. | SRC-GDPR recital 72 | full recital | |
| Recital 14: GDPR "does not cover the processing of personal data which concerns legal persons". So B2B scoring of a legal person is outside GDPR as such; personal data of natural persons attached to it (sole traders, directors, UBOs, contacts) remain in scope (our reading). | SRC-GDPR recital 14 | part | Legal review for sole traders |
| Fines: Art 83(5) up to EUR 20,000,000 or 4% of worldwide turnover (infringement of data subjects' rights, Arts 12-22 per 83(5)(b)). | SRC-GDPR Art 83 | part (para 5 head read; point (b) not re-quoted) | Confirm point (b) wording |
| CJEU C-634/21 (SCHUFA, 7 Dec 2023): automated establishment of a probability value of ability to meet payment commitments "constitutes 'automated individual decision-making'" where a third party "draws strongly on that probability value" to establish, implement or terminate a contract. | SRC-CJEU-C-634-21 operative part | part | Applies to natural persons; later case law (2024-2026) not searched |
| AI Act Reg (EU) 2024/1689, consolidated text of 27 July 2026: Art 6(2) Annex III systems are high-risk; 6(3) derogation if no significant risk (narrow procedural task, improve prior human activity, detect patterns without replacing review, preparatory task); but "always high-risk where the AI system performs profiling of natural persons". Art 6(4) provider documents non-high-risk assessment. | SRC-AIACT-CONSOL-2026-07 (registered) Art 6 | full article | |
| Annex III point 5(b): AI systems "to evaluate the creditworthiness of natural persons or establish their credit score", excluding fraud detection. Point 5(c): risk assessment and pricing for life and health insurance of natural persons. Point 5(a): public-authority eligibility for essential benefits. Point 5(d): emergency calls. | SRC-AIACT-CONSOL-2026-07 Annex III | full annex III | |
| Annex III point 4: (a) recruitment or selection of natural persons; (b) decisions on terms of work-related relationships, promotion, termination, task allocation by behaviour, monitoring and evaluation of performance. Point 2: safety components in management of critical digital infrastructure, road traffic, water, gas, heating, electricity. | SRC-AIACT-CONSOL-2026-07 Annex III | full | |
| Recital 58: credit scoring of natural persons is high-risk because it determines "access to financial resources or essential services such as housing, electricity, and telecommunication services". | SRC-AIACT-ORIG (new) recital 58 | part | |
| Scope of B2B risk scoring of legal persons: Annex III points 4 and 5(b), and 6(3) profiling, are all worded for natural persons. Reading the text: pure scoring of a company (legal person) is not within points 4 or 5(b). Not found: any provision classifying B2B scoring of legal persons as high-risk. Art 5(1)(c) social scoring also refers to "natural persons or groups of persons". Risk remains where output concerns sole traders or individuals behind a company (our reading, legal review needed). | SRC-AIACT-CONSOL-2026-07 Annex III, Art 5(1)(c) | part | Commission guidelines under Art 6(5) (due 2 Feb 2026): not located or read |
| Art 14 human oversight: design so systems "can be effectively overseen by natural persons"; persons must be able to be aware of automation bias, interpret output, "disregard, override or reverse" it, and stop the system. | SRC-AIACT-CONSOL-2026-07 Art 14 | full article | |
| Art 26 deployers: use per instructions, assign oversight to competent natural persons, ensure input data relevant and representative where under their control, monitor, keep logs at least six months, inform workers (26(7)), 26(11): deployers of Annex III systems deciding or assisting decisions "related to natural persons shall inform the natural persons". | SRC-AIACT-CONSOL-2026-07 Art 26 | full article | |
| Art 27 FRIA: required for deployers of Annex III 5(b) and (c) systems and for public bodies. Art 86: right to explanation of decisions on the basis of Annex III system output. | SRC-AIACT-CONSOL-2026-07 Arts 27, 86 | part | |
| Reg (EU) 2026/1744 (Digital Omnibus on AI, 8 July 2026, OJ 24.7.2026) amends Arts 2, 3, 5, 10, 25, 27, 57, 58, 60, 75, 77, 96, 97, 99, 111, 113 and Annex I. It does not amend Art 6, 14, 26 or Annex III (no such amendment found in the text). Art 27(4)-(5) changed (DPIA cross-references, AI Office template). | SRC-REG-2026-1744 (registered) | part (amendment list) | Check Art 3 and Art 5 amendment details if the talk uses them |
| Application dates (as amended by 2026/1744): Annex III high-risk obligations (Chapter III Sections 1-3) from 2 December 2027; Annex I products from 2 August 2028. | SRC-AIACT-CONSOL-2026-07 Art 113 | full article | |
| DORA (Reg 2022/2554) Art 28: financial entities must manage ICT third-party risk, keep a register of information, and before contracting "identify and assess all relevant risks" incl. concentration risk (28(4)(c)). Art 31(2): ESAs designate critical ICT third-party providers on criteria (systemic impact, number of G-SIIs/O-SIIs). DORA does not define scoring of ICT providers or a score format. Relevant only to financial entities and their ICT providers (our reading). | SRC-DORA Arts 28, 31 | part | Delegated acts on criteria not read |
| Data Act (Reg 2023/2854) Art 33: participants in data spaces must describe datasets, use restrictions, licences, data quality, vocabularies and access means "in a machine-readable format". No provision on risk scoring found. Not applicable to scoring. | SRC-DATAACT Art 33 | part | |
| AML, sanctions screening: out of scope; not examined. | n/a | not read | |
| GDPR/EDPB guidance on Art 22 (WP251 rev.01): not read in this pass. | n/a | not read | If the talk needs the EDPB reading |

## 4. Policy languages

| Fact | Source | Read | To verify |
|---|---|---|---|
| ODRL Information Model 2.2 and ODRL Vocabulary & Expression 2.2: both W3C Recommendations of 15 February 2018. | SRC-ODRL-IM-2.2, SRC-ODRL-VOCAB-2.2 (registered) | part / snippet | Later ODRL versions: none found |
| Profiles (IM s3): "An ODRL Profile MUST be defined to provide vocabulary terms ... for ODRL policies requiring additional semantics"; policy conforming to a profile MUST carry the `profile` IRI; a processor that does not recognise the profile "MUST stop processing". | SRC-ODRL-IM-2.2 s3.1-3.2 | part | |
| Conflicts: `conflict` values perm, prohibit, invalid; if not set, default "invalid" (policy void on any conflict). | SRC-ODRL-IM-2.2 s2.10 | part | |
| ODRL defines an "ODRL Evaluator" and requires evaluators to support logical operands, but defines no PDP/PEP architecture and no enforcement semantics in the sections read (our reading). | SRC-ODRL-IM-2.2 | part | |
| DSP Release 2025-1 (Eclipse Dataspace Working Group, formerly IDSA) "considered to be stable". Scope: "specifies how data usage requirements are expressed as Policies (reusing terminology from ODRL)"; datasets via DCAT 3 terminology; "does not apply to the Data Transfer Protocol". | SRC-DSP (registered), scope.md | part | |
| DSP: Dataset MUST have at least one `hasPolicy` containing an Offer; Agreement MUST have `target`, `assigner`, `assignee`, `timestamp`; uses ODRL compact-policy inferencing rules. DSP does not define constraint left operands or policy evaluation in the files read. Correction to RES-dec12 A1.16: the quote "The semantics of such tokens are not part of this specification" concerns authorization tokens in HTTP headers, not policy semantics. | SRC-DSP common.protocol.md, catalog.protocol.md, contract.negotiation.protocol.md | part | Re-check dec12 A1.16 wording |
| DSP: presenting proofs for catalog requests "is outside the scope of the Dataspace Protocol". | SRC-DSP catalog.protocol.md | part | |
| XACML 3.0: OASIS Standard, 22 January 2013. PDP "evaluates applicable policy and renders an authorization decision"; PEP "MUST abide by the authorization decision" (as in RES-dec12 A1.14). | SRC-XACML-3.0 (new) | snippet | Later OASIS errata not checked |
| OpenID AuthZEN Authorization API 1.0: Final, 11 January 2026; lets PDPs and PEPs exchange requests and decisions "without requiring knowledge of each other's inner workings"; defines no policy language. Only standards-body PDP/PEP interface found. | SRC-AUTHZEN-1.0 (new) | part | |
| OPA: no standard. CNCF Graduated project (accepted 29 Mar 2018, Graduated 29 Jan 2021); project maturity is not standardisation. | SRC-CNCF-OPA (new) | read | |
| Cedar: no standard. CNCF Sandbox project, accepted 8 October 2025. No standards-body specification found. | SRC-CNCF-CEDAR (new) | read | Check for any IETF or OASIS draft |

## 5. PROV-O, DCAT 3, SHACL, OWL, RDFS: status and dates

| Fact | Source | Read | To verify |
|---|---|---|---|
| PROV-O: W3C Recommendation, 30 April 2013. | SRC-PROV-O | snippet | |
| DCAT 3 (Data Catalog Vocabulary v3): W3C Recommendation, 22 August 2024. Replaces DCAT 2 Rec of 4 February 2020 (change history J). DSP reuses DCAT 3 terminology. | SRC-DCAT-3 | snippet | |
| SHACL: W3C Recommendation, 20 July 2017 (still the latest Recommendation). SHACL 1.2 Core is a Working Draft of 18 September 2026, not a Recommendation. | SRC-SHACL, SRC-SHACL-1.2-CORE | snippet | Other SHACL 1.2 parts not checked |
| RDF 1.1 Concepts Rec 25 Feb 2014; RDFS 1.1 Rec 25 Feb 2014; OWL 2 Primer 2nd ed. Rec 11 Dec 2012; JSON-LD 1.1 Rec 16 Jul 2020. | respective TR pages | snippet | |

## 6. Open world versus closed world (one clause each)

| Fact | Source | Read | To verify |
|---|---|---|---|
| OWL: absent facts "may simply be missing (but possibly true), following the open-world assumption"; and OWL "does not make the assumption that different names are names for different individuals" (no unique name assumption). | SRC-OWL2-PRIMER | part | |
| RDFS: no statement on open or closed world found in the RDFS 1.1 text. (VC DM 5.2 and DCAT 3 refer to the "open world assumption" for RDF data.) | SRC-RDFS-1.1 (not registered; dec12 list), SRC-VCDM-2.0, SRC-DCAT-3 | part | |
| SHACL: validates a data graph against shapes and reports conformance (`sh:conforms`); the Recommendation text does not use the terms open or closed world. Calling it closed-world validation is our reading. | SRC-SHACL | part | |

## 7. Agent cards and agent authorization

| Fact | Source | Read | To verify |
|---|---|---|---|
| A2A specification latest released version 1.0.0 (Linux Foundation project). Agent Card is "a self-describing manifest". Required fields: name, description, supportedInterfaces, version, capabilities, defaultInputModes, defaultOutputModes, skills. Optional: provider, documentationUrl, securitySchemes, securityRequirements, signatures, iconUrl. | SRC-A2A / SRC-A2A-SPEC-1.0 4.4.1 | part | |
| AgentSkill fields: id, name, description, tags (required); examples, inputModes, outputModes. Skills are "largely a descriptive concept" (self-declared; no verification mechanism for skills in spec). | SRC-A2A 4.4.1, 4.4.5 | part | |
| Security schemes: APIKey, HTTPAuth, OAuth2, OpenIdConnect, MutualTls. | SRC-A2A 4.5 | headings | |
| Signing: card MAY be signed with JWS (RFC 7515); content canonicalised with JCS (RFC 8785) excluding `signatures`; protected header MUST include `alg`, `typ`, `kid`, MAY include `jku`. Clients SHOULD verify at least one signature, "MAY maintain a trusted key store"; revoked or expired keys MUST NOT be used. | SRC-A2A 8.4 | part | |
| What is verifiable (our reading from the text): integrity and that the signer holds the key; no binding of the key to a legal entity (no X.509/LEI/EBW link), no verification of skill claims. TLS check of the server identity is "SHOULD". | SRC-A2A 8.4, 7 | part | Check if any A2A extension binds to eIDAS/EBW |
| A2A: authorization scope in task state AUTH_REQUIRED is not defined by the protocol ("does not define the scope, representation, validity, or revocation semantics"). | SRC-A2A 7.6.4 | part | |
| MCP Authorization (protocol revision 2026-07-28, latest): authorization is OPTIONAL; for HTTP transports it SHOULD conform; STDIO SHOULD NOT and takes credentials from the environment. MCP server is an OAuth 2.1 resource server; servers MUST implement RFC 9728 Protected Resource Metadata; clients MUST implement RFC 8707 Resource Indicators; servers MUST validate token audience; no token passthrough; Client ID Metadata Documents SHOULD be supported; Dynamic Client Registration deprecated. | SRC-MCP-AUTH (registered) | part (sections 1-8 grep and read) | Confirm DCR deprecation wording |
| W3C AI Agent Protocol Community Group: W3C Community Group (proposed 2025-05-08, 276 participants on page); drafts are a white paper (Agent Network Protocol) and protocol/use-case documents of 2025-08-19; "W3C's hosting of this group does not imply endorsement". Not on the W3C standards track. Agent Identity draft: DID-method-agnostic, HTTP Message Signatures (RFC 9421) with DID URL as keyid; "a separate authorization decision" follows. | SRC-W3C-AIAP-CG (new), SRC-W3C-AIAP-ID (registered) | part | Draft dates not stated in the page text |

## Gaps (not found)

- Primary performance data for JSON-LD processing and RDFC at scale: not found (specs give complexity and DoS texts only).
- Any text classifying B2B risk scoring of legal persons as high-risk or Art 22 decision: not found; relevant texts are limited to natural persons.
- Commission Art 6 high-risk guidelines (due 2 Feb 2026), EDPB Art 22 guidance: not read.
- Streaming or event verification and batch verification of presentations in status-list specs: not found.
- Cedar or OPA standards-body specification: not found (no standard).
