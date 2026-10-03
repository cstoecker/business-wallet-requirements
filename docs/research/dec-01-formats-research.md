# RES-formats: Credential formats and semantic layers for the European Business Wallet (EBW)

Research date: 2026-10-03. No recommendation is made. All quotes are verbatim and 25 words or fewer.
State key: read = fetched and read in the cited part (local copy in /tmp/w); snippet = search snippet only; unverified = not read.
Existing source IDs reused (from _data/graph/sources.yml): SRC-EBW-PROPOSAL, SRC-CIR-2024-2977, SRC-CIR-2024-2979, SRC-CIR-2024-2982, SRC-CIR-2025-1569, SRC-ARF-HLR, SRC-ARF-TRUST, SRC-WEBUILD-ARCH, SRC-WEBUILD-RB, SRC-DATAACT, SRC-CX-0018, SRC-COUNCIL-ST-9684-26, SRC-COUNCIL-ST-7659-26.
NEW sources, not yet in sources.yml (proposed IDs in brackets): [SRC-CIR-2026-1731], [SRC-ETSI-119472-1], [SRC-ETSI-119472-2/-3 only cited via 2026/1731], [SRC-EUDI-TS11], [SRC-ESPR], [SRC-VCDM-2.0], [SRC-VC-DI], [SRC-VC-JOSE-COSE], [SRC-VC-DI-BBS], [SRC-IETF-SDJWT-VC], [SRC-RFC-9901], [SRC-OID4VCI], [SRC-OID4VP], [SRC-HAIP], [SRC-DCP], [SRC-CX-0050], [SRC-IDTA-AAS-P1], [SRC-IDTA-AAS-P4].

## 0. Key findings in one screen (facts only)

1. EU law at the EBW level does not name a credential format. COM(2025) 838 Art 8(3) points to "one of the standards listed in Annex II of Commission Implementing Regulation (EU) 2024/2979" for EBW owner identification data. Annex II was replaced by CIR (EU) 2026/1731 (OJ 22.7.2026). The replacement text applies "clauses 2 to 6 of ETSI TS 119 472-1 V1.2.1 (2026-02)", i.e. the SD-JWT VC (clause 5) and ISO/IEC mdoc (clause 6) realisations. Clause 7 (JSON-LD W3C VC) and clause 8 (X.509 attribute certificate) of that ETSI TS are not in the legal list. This is my reading of the clause range; I did not diff Annex IV against clause 7 in other adaptations.
2. The original OJ text of 2024/2979 Annex II listed "ISO/IEC.18013-5:2021" and "Verifiable Credentials Data Model 1.1" (W3C). Recital 18 of 2026/1731 says the wallets "should also support this format when the new profiles on the W3C VCDM format are available". So W3C VCDM is referenced as future/conditional support, not mandated now.
3. The ARF (v3.0.0 as rendered at eudi.dev/latest) makes mdoc and SD-JWT VC the "common formats" for QEAA and PuB-EAA (ARB_01), and adds W3C VCDM v2.0 only for non-qualified EAA (ARB_01a), with extra conditions (ARB_04).
4. Semantics in the EU framework: attribute catalogue and scheme catalogue (CIR 2025/1569 Arts 7, 8) require "namespace", "identifier", "semantic description", "data type", and publish machine-readable. The format-specific semantic mechanism is the rulebook plus `vct` / `docType` / mdoc namespace. JSON-LD `@context` appears only in the ETSI realisation of clause 7 and in W3C VCDM; it is not in the legal list (see 0.1).
5. AAS has no stated credential or VC specification in the IDTA documents I could reach. Part 1 (V3.0.2) describes `semanticId` (IRDI/IRI, ECLASS/IEC CDD) and an RDF serialisation; Part 4 Security is snippet-level only. AAS is an implementation artefact here, not an EU-mandated format.
6. Machine-readable obligations exist in other EU law (ESPR Art 10(1)(d), Art 11(a); Data Act Art 33(1)); the EBW proposal's "machine-readable" occurrences concern export, lists and the Directory API, not credential semantics.

## A. FACT TABLE

Columns: where mandated/referenced (clause, quote) | status | selective disclosure and unlinkability as stated by the spec | semantics mechanism | verifiability and signature options | version/date/URL | state.

### A1. SD-JWT VC (IETF) with SD-JWT (RFC 9901)

- Mandated/referenced:
  - [SRC-CIR-2026-1731] Annex IV (new Annex II of 2024/2979): "The technical specifications set out in clauses 2 to 6 of ETSI TS 119 472-1 V1.2.1 (2026-02) apply." Clause 5 = "Implementation of EAA based on SD-JWT VC". Same act, Annex I (new Annex of 2024/2977, PID): "clauses 5 (SD-JWT VC format) and 6 (ISO/IEC-mdoc format)".
  - ARF Annex 2.02: PID_02 "A PID Provider SHALL issue any PID in both the format specified in ISO/IEC 18013-5 ... and the format specified in SD-JWT VC." ISSU_02: wallets "SHALL ensure that their Wallet Solution supports the attestation formats specified in ISO/IEC 18013-5 ... and in SD-JWT-based Verifiable Credentials (SD-JWT VC)". ARB_01 (QEAA/PuB-EAA) lists mdoc and SD-JWT VC as the two common formats. ARB_01b: SD-JWT VC attestations "SHALL ensure that these attestations comply with the 'IETF SD-JWT VC Profile' specified in HAIP Section 6.1."
  - EBW proposal COM(2025) 838: not named; Art 8(3) refers to 2024/2979 Annex II (see A0).
  - WE BUILD: cs-01 and cs-02 conformance specs assume SD-JWT-VC issuance and presentation; rb-ebwoid defines only an SD-JWT VC encoding (`vct` "uri:eu.ebw.oid.1"), "No mdoc encoding is defined in this version".
- Status: mandatory (as one of the two legally listed realisations; the legal text says wallet providers support attestations "in compliance with the list of standards" under 2024/2979 Art 8 for all listed standards). Not exclusive: mdoc is the other.
- Selective disclosure / unlinkability:
  - RFC 9901 abstract: "a mechanism for the selective disclosure of individual elements of a JSON data structure". Section 10.1 on unlinkability: it only conceals unrevealed claim values and "does not meet the security properties for anonymous credentials"; colluding issuer and verifier can recognise the same credential; batch issuance helps verifier/verifier and presentation unlinkability but "cannot work for Issuer/Verifier unlinkability". It says this applies to "all salted hash-based approaches, including mDL/mDoc".
  - SD-JWT VC draft-19: "The use of selective disclosure in SD-JWT VCs is optional." Unlinkability: refers to RFC 9901 10.1.
  - ARF: PID_21 all claims individually selectively disclosable (for PID); ARB_30 rulebook must state per claim whether SD is MUST/MAY/MUST NOT; batch methods ISSU_43 to ISSU_51 for unlinkability across relying parties.
- Semantics mechanism: `vct` claim = type identifier ("Collision-Resistant Name"); the spec says "does not define any vct values; instead it is expected that ecosystems ... define such values including the semantics of the respective claims". Section 5 optional Type Metadata (display, claim metadata, `extends`, claim selective-disclosure metadata). SD-JWT VC itself: "does not define the claims ... or their semantics" (RFC 9901 scope as quoted by SD-JWT VC 1.2). No `@context`. ARF ARB_06b: claim names must be IANA/public/private names per RFC 7519; ARB_31: Type Metadata "SHOULD" be defined; ARB_05: unique attestation type value. ETSI TS 119 472-1 EAA-5.2.1.2-01..03: `vct` shall be present, point to Type Metadata, include `vct#integrity`.
- Verifiability / signature: JWS (JOSE); key binding via KB-JWT; issuer trust via x5c/x5u per ETSI/CIR; status via Token Status List (2026/1731 cites "draft-ietf-oauth-status-list-20"); ETSI profile uses JAdES for QEAA/PuB-EAA (clauses 5.6.x, not read in detail).
- Version/date/URL: draft-ietf-oauth-sd-jwt-vc-19, 2026-08-31, "Waiting for AD Go-Ahead" (IESG), intended Proposed Standard, https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/ ; ETSI TS 119 472-1 cites draft-13. RFC 9901 (Nov 2025) https://www.rfc-editor.org/rfc/rfc9901.html . Not yet an RFC (as read on 2026-10-03).
- State: read (draft-19 text, RFC 9901 10.1, ETSI TS 119 472-1 clause 5 headings and requirements 5.2.1).

### A2. ISO/IEC 18013-5 mdoc (with ISO/IEC 23220-2 data elements per ETSI)

- Mandated/referenced: 2024/2979 Annex II original: "ISO/IEC.18013-5:2021"; 2024/2977 Annex original: "the format specified in ISO/IEC 18013-5:2021"; 2024/2982 Annex: "ISO/IEC 18013-5:2021" and "ISO/IEC TS 18013-7:2024" (protocols, original text); 2026/1731 replaces these with ETSI TS 119 472-1 clause 6 (mdoc), ETSI TS 119 472-2 and "Annex C to ISO/IEC 18013-7:2025". ARB_02: if proximity/offline presentation is needed the rulebook "SHALL specify that the attestations must be issued in the ISO/IEC 18013-5-compliant mdoc format."
- Status: mandatory (one of the two legally listed realisations).
- Selective disclosure / unlinkability: per ISO text not readable (paywalled/403). Snippet only (iso.org search result): selective disclosure via data-element requests, "age over X" attributes. RFC 9901 10.1 (quoted above) states mDL/mDoc uses a salted-hash approach with the same unlinkability limits. ARF Topic 53 (ZKP) ZKP_06 says a ZKP scheme "SHOULD be able to generate proofs for already issued PIDs and attestations in the formats specified in ISO/IEC 18013-5 or SD-JWT VC."
- Semantics mechanism: `docType` (attestation type) and attribute namespaces. ARF ARB_06a: "An attribute namespace SHALL fully define the identifier, the syntax, and the semantics of each attribute within that namespace." PID namespace "eu.europa.ec.eudi.pid.1". ETSI 119 472-1 6.2.1.2: "There is no need to define any data element for indicating the context because the data elements namespaces appear within the ISO/IEC-mdoc". No linked-data mapping (WE BUILD blueprint ch.5: "For mDoc and SD-JWT-VC, the meaning of data fields must instead be defined in attestation rulebooks.").
- Verifiability / signature: COSE_Sign1 over MSO (Mobile Security Object); ETSI profile "CB-AdES" per 2026/1731 Annex I text; status via MSO status list/revocation list (2026/1731 Annex IV adaptations).
- Version/date/URL: ISO/IEC 18013-5:2021 https://www.iso.org/standard/69084.html (page behind Cloudflare 403 in this session; abstract content unverified beyond snippet); ISO/IEC TS 18013-7:2024 snippet; ISO/IEC 18013-7:2025 only as cited in 2026/1731.
- State: ISO text unverified/snippet; EU, ARF, ETSI and RFC 9901 statements read.

### A3. W3C VCDM 2.0 (JSON-LD), securing by Data Integrity or JOSE/COSE

- Mandated/referenced:
  - Original 2024/2979 Annex II: "'Verifiable Credentials Data Model 1.1', W3C Recommendation, 3 March 2022" (listed alongside mdoc) and 2024/2977 Annex PID: "Person identification data shall be issued in two formats" (mdoc and VCDM 1.1). Both superseded by 2026/1731 (see A1/A2). VCDM 1.1 is no longer in the replaced PID text I read.
  - 2026/1731 recital (18): "the European Digital Identity Wallets should also support this format when the new profiles on the W3C VCDM format are available." That is the only legal mention found in the amending act.
  - ARF ARB_01a: non-qualified EAA may use "The format specified in W3C Verifiable Credentials Data Model, see W3C VCDM v2.0". ARB_04: if VCDM v2.0 is used, the rulebook "SHALL ensure the Rulebook references one or more documents specifying in detail how a Relying Party can request attributes ... and how a User can selectively disclose" and those documents must be approved by an EU standardisation body or the Cooperation Group. ISSU_12 note: a non-qualified EAA provider "may choose to issue attestations in the format specified in W3C VCDM v2.0 ... it will support only those Wallet Solutions that have implemented this attestation format."
  - ETSI TS 119 472-1 V1.2.1 clause 7 "JSON-LD W3C-VC" is a defined realisation but is outside the legal "clauses 2 to 6" list in 2026/1731.
  - OpenID4VCI 1.0 Appendix A.1 and TS11 list `jwt_vc_json`, `jwt_vc_json-ld`, `ldp_vc` as formats a scheme can declare.
  - WE BUILD rulebooks: rb-gln encodes a GS1 JSON-LD VCDM 2.0 credential and an SD-JWT wrapping of VCDM; rb-ebwoid "W3C VCDM is named as a profiled format; no encoding is defined in this version".
- Status: referenced (conditional/future in law; optional for non-qualified EAA in ARF). Not mandatory for EBW identification data on the legal text read.
- Selective disclosure / unlinkability (spec's own words): VCDM 2.0 glossary: "selective disclosure: The ability of a holder to make fine-grained decisions about what information to share." and "unlinkable disclosure: A type of selective disclosure where presentations cannot be correlated between verifiers." Section 5.7: the model "supports being secured using zero-knowledge proofs"; "Blinded signatures allow for unlinkable disclosure". VCDM does not itself mandate SD. Data Integrity 1.0 section 6.1: "not all use cases require or even permit unlinkability" (regulatory/safety examples). Data Integrity BBS cryptosuites abstract: "BBS signatures to provide selective disclosure and unlinkable derived proofs" (status: Candidate Recommendation Draft 10 September 2026, not a Recommendation). VC-JOSE-COSE section 3.2: SD-JWT as securing mechanism for VCDM.
- Semantics mechanism: `@context` (first value MUST be "https://www.w3.org/ns/credentials/v2"; "Application developers MUST understand every JSON-LD context used"), `type`, optional `credentialSchema`; "software systems identify terminology by using URLs for each term". ETSI 119 472-1 clause 7: `credentialSchema` types "JsonSchemaCredential", "CddlSchemaCredential", "ShaclSchemaCredential" (EAA-7.2.1.3-03); new properties under "https://uri.etsi.org/019472010101#" (EAA-7.2.1.2-04). Per the VCDM, JSON-LD compacted form is required for application/vc, and the model can be processed with or without a JSON-LD processor ("whether or not they use a JSON-LD 1.1 processor").
- Verifiability / signature: two standardised options, "this specification does not mandate any particular securing mechanism": VC Data Integrity 1.0 (embedded proof; cryptosuites e.g. eddsa-jcs-2022, ecdsa-rdfc-2019 in examples) and VC-JOSE-COSE (enveloping proof, incl. SD-JWT). ETSI clause 7.6: JOSE (JAdES-B-B) and SD-JWT, or embedded proofs per Data Integrity.
- Version/date/URL: VCDM 2.0 W3C Recommendation 15 May 2025 https://www.w3.org/TR/vc-data-model-2.0/ ; Data Integrity 1.0 Rec 15 May 2025 https://www.w3.org/TR/vc-data-integrity/ ; VC-JOSE-COSE Rec 15 May 2025 https://www.w3.org/TR/vc-jose-cose/ ; DI BBS CRD 10 Sep 2026 https://www.w3.org/TR/vc-di-bbs/ . VCDM 1.1: 2022-03-03 (cited by CIRs; I did not separately read the 1.1 text, the URL returned 2.0).
- State: read.

### A4. AAS submodels as VC payload (IDTA)

- Mandated/referenced: not in any EU act read; not in the ARF; not in the EBW proposal. No IDTA specification on verifiable credentials was found in the IDTA downloads page (Part 1, 2, 3a, 5 listed there; Part 4 Security found via search). AAS used as VC payload is therefore: not mentioned (EU/ARF/IDTA). I did not find an IDTA, Catena-X or WE BUILD document stating AAS-as-VC.
- Status: not mentioned. AAS is an implementation artefact of industrial ecosystems, not a credential format.
- Selective disclosure / unlinkability: not stated in sources. Part 4 (snippet only, IDTA news page): ABAC access control "claims from a signed access token can be used as attributes"; "disclosure of selected attributes only" is described as access-rule capability, not a credential property.
- Semantics mechanism (Part 1 V3.0.2, March 2025, read): `semanticId` "IRDI, IRI (URI)" for submodels and elements: "A so-called semanticId should be defined for this submodel as well as the submodel element." Concept descriptions in external repositories "such as ECLASS or IEC CDD"; IEC 61360 data specification (Part 3a, not read). Clause 7.5 RDF serialisation: RDF "is the recommended standard of the W3C"; "Connecting distributed data sources through the web ... is referred to by the term 'Linked Data'".
- Verifiability / signature: not stated in Part 1 beyond the above; Part 4 unread (snippet).
- Version/date/URL: IDTA-01001-3-0-2 (March 2025) https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-01001-3-0-2_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf ; Part 4: https://industrialdigitaltwin.org/en/content-hub/aasspecifications/specification-of-the-asset-administration-shell-part-4-security-idta-number-01004 (snippet).
- State: Part 1 read (searched for terms); Parts 2, 3, 4 not read.

### A5. Other formats found

| Format | Where | Status | Notes | State |
|---|---|---|---|---|
| X.509 Attribute Certificate (RFC 5755) | ETSI TS 119 472-1 clause 8; scope item 3(d) | defined in ETSI TS; outside legal "clauses 2 to 6" of 2026/1731 | Realisation of the EAA data model | read (scope and TOC) |
| W3C VCDM 1.1 (JWT/StatusList2021) | DCP v1.0 profile `vc11-sl2021/jwt`; CX-0050 JSON schema uses `issuanceDate`, `expirationDate` (VCDM 1.1 field names) | ecosystem (data space) | Not an EU legal format any more (see A3) | read |
| W3C VCDM 2.0 with JOSE and BitstringStatusList | DCP v1.0 profile `vc20-bssl/jwt` | ecosystem | "Heterogeneous sets of credentials MUST be enclosed in multiple presentations" | read |
| `jwt_vc_json`, `jwt_vc_json-ld`, `ldp_vc` | OpenID4VCI 1.0 App. A.1; TS11 `supportedFormats` | referenced in protocol and catalogue spec | OID4VCI note: Data Integrity VCs "MAY NOT necessarily use JSON-LD" | read |
| PAdES (mandatory), XAdES, JAdES, CAdES, ASiC | 2024/2979 Annex IV (documents, signatures and seals) | mandatory/optional per list | Concerns signing documents, not attestations. Annex IV amended by 2026/1731 Annex VI (PAdES version, CSC API replaced by ETSI TS 119 432). EBW Annex also has "mandatory format" / "optional format" for signature creation. | read |
| "Open format" for EBW data export | COM(2025) 838 Annex pt on data portability (as summarised in the legislative financial statement 4.2): "Open format"; Council ST 9684/26 Annex pt 10: "in at least an open format" | mandatory (proposal) | Format not named | read (statement and Council Annex) |
| CBOR/CDDL, JSON Schema | ARF/TS11, ETSI 119 472-1 7.2.1.3 | metadata schema syntaxes | TS11: schemas "SHALL be provided in JSON format" | read |

### A0. EBW proposal and Council text on formats (for completeness)

- COM(2025) 838, Art 8(3): "European Business Wallet owner identification data shall be issued in a format compliant with one of the standards listed in Annex II of Commission Implementing Regulation (EU) 2024/2979". Same wording in Council ST 9684/26 (2 June 2026) and ST 7659/26 (22 May 2026); I only grep-read these two, they contain no additional format provisions in the passages found.
- Art 8(6): "That scheme shall be listed in the catalogue of schemes for the attestation of attributes referred to in Article 8 of Implementing Regulation (EU) 2025/1569." Art 8(5): minimum attributes = official name and the unique identifier (EUID, Art 9).
- Art 5(1)(b): wallets enable "selectively disclose European Business Wallet owner identification data and attributes contained in electronic attestations of attributes". Art 5(1)(g): issued attestation can be "linked to other relevant attestations forming part of a chain". Recital 27: linked attestations "cryptographically linked ... in a manner that allows the verification of the authenticity and integrity of each individual attestation".
- Art 5(5) and Art 6: Commission to establish by implementing acts "a list of reference standards" and specifications. Recital 28: standards "to take into account relevant technical solutions and standards used by existing ICT systems by economic operators".
- Recital 28 mentions "new use cases, such as agentic AI" as something implementing acts should allow.
- The Annex to the proposal (referred to as "the Annex" in Arts 5(4), 7, 10) is not contained in the Eerste Kamer PDF copy as a separate annex section; only its content is visible via the legislative financial statement and Council text. Whether the Commission-proposal Annex has a selective-disclosure or format point beyond the above was not verified in the proposal itself.

## B. EUDI implementing acts and ARF on attestation schemas, catalogue and metadata

### B1. Legal layer (CIR (EU) 2025/1569, read in OJ text, Articles 7 and 8)

- Catalogue of attributes (Art 7): request must contain "a namespace for the identifier of the attributes", "an identifier of the attribute, unique within the namespace, and the version of the attribute", "semantic description of the attribute", "the data type of the attribute", and the verification point (Art 7(5)(d)-(h)). Art 7(8): published "in both machine-readable and human-readable forms", sealed by the Commission. Art 7(10): "The Commission shall issue a unique identifier to each registered attribute." Art 7(9): Commission "shall publish the technical specifications".
- Catalogue of schemes (Art 8): request contains scheme name, owner, "status and version", legal/standards references, "the format or formats of electronic attestation of attributes within the scope of the scheme" (8(3)(e)), "one or more namespaces, attribute identifiers, semantic descriptions and data types of each attribute" (8(3)(f)), trust model and revocation (8(3)(g)), requirements on providers (8(3)(h)), QEAA/PuB-EAA statement (8(3)(i)). Art 8(4): "schemes ... shall only contain attributes that are identifiable based on unique identifiers"; request signed with QES/seal. Art 8(6): catalogue "shall be machine-readable and human-readable" and in a format guaranteeing integrity and authenticity.
- Recital on catalogue content (recital number not verified): catalogue "should provide at least a minimum set of information, such as a semantic description of the attribute, the namespace of its identifier, and the data type"; versioning so issued attestations "are not affected by changes".
- Art 3 and Annex II (2025/1569): attestations "in a format according to one of the standards listed in Annex II of Commission Implementing Regulation (EU) 2024/2979".
- 2024/2979 Recital 10: wallets "should support predetermined types of data formats and selective disclosure"; "In addition, wallets may support other formats and functionalities to facilitate specific use cases." (this wording is in the original 2024/2979; 2026/1731 amended articles and annexes, I did not diff recitals).
- 2024/2979 Art 8 (original): "Wallet providers shall ensure that wallet solutions support the usage of person identification data and electronic attestations of attributes issued in compliance with the list of standards set out in Annex II." 2024/2977 Art 4(1) as amended by 2026/1731: attestations "shall comply with at least one of the standards set out in Annex II of Implementing Regulation (EU) 2024/2979". (The original 2024/2977 text read "Annex I", an apparent cross-reference slip corrected by 2026/1731.)
- 2024/2982 (articles on presentation, numbers not verified): selective disclosure support: "Wallet providers shall ensure that wallet solutions support the selective disclosure of attributes of personal identification data and of electronic attestations of attributes." Unlinkability: "enable privacy preserving techniques which ensure unlinkability where the electronic attestations of attributes do not require the identification of the wallet user" (2024/2982, article number not verified; 2024/2977 has a PID-provider counterpart, "Providers of person identification data shall enable privacy preserving techniques which ensure unlinkability", article number not verified).
- Wallet scope: these acts are written for EUDI Wallets (natural/legal persons as wallet users). The EBW proposal imports them by reference only for owner identification data (Art 8(3), 8(6)). Whether EBW attestations other than EBWOID are bound to the same Annex II list: Art 5 only requires the same core functions and "list of reference standards" via future implementing acts. Not stated in sources for the general EBW attestation case.

### B2. ETSI TS 119 472-1 V1.2.1 (2026-02), now the legal profile for EAA (via 2026/1731)

- Clause 4 defines encoding-independent semantic areas: EAA type (4.2.1.2), context (4.2.1.3), schema (4.2.1.4), category (4.2.2), identifier, issuer identifier, status, key binding, signature.
- EAA-4.2.1.3-01: "If the components of the EAA have URLs as names, the EAA shall include one or more context components." (conditional).
- EAA-4.2.1.4-02: "An EAA may incorporate a sequence of one or more references allowing to retrieve the EAA schema." Optional.
- Category: QEAA includes URN "urn:etsi:esi:eaa:eu:qualified"; PuB-EAA "urn:etsi:esi:eaa:eu:pub". Rationale (NOTE): eIDAS Annex V(a) requires an indication "in a form suitable for automated processing".
- Realisation-specific: SD-JWT VC (type = `vct` + Type Metadata, context in Type Metadata, 5.2.1.3); mdoc (no context element needed, namespaces); JSON-LD W3C VC (`@context`, `type` array of at least two strings, `credentialSchema`).
- Reference [i.6] in the ETSI TS is "EUDI Wallet TS11" (catalogue formats and API).

### B3. EUDI Technical Specification 11 (catalogue of attributes and attestations), v1.0.1 2026-01-30 (read, raw GitHub)

- Attribute class: `identifier` URI; `semanticDataSpecification` optional URI into the OOTS Semantic Repository ("structured, standardised, and media type-agnostic definition describing the attribute's data elements, semantics, and relationships"); `distributions` with `mediaType` `application/json-schema`.
- SchemaMeta: `supportedFormats` values "`dc+sd-jwt`, `mso_mdoc`, `jwt_vc_json`, `jwt_vc_json-ld` and `ldp_vc`"; per-format schema URI; `rulebookURI` (human-readable rulebook "SHALL define all non-machine readable aspects"); `trustedAuthorities`; SemVer versioning.
- Format-specific schema type: SD-JWT VC -> VCT; mdoc -> DocType per ISO 23220-2; W3C VC -> OpenID4VCI A.1 options.
- API: OpenAPI-compatible management of attestation schemas (GET/PUT/DELETE /schemas).
- Discrepancy: TS11 says "According to Article 2 (3) of [CIR for EAAs] the catalogue of attributes SHALL contain at least a JSON schema". The OJ text of 2025/1569 I read has no occurrence of "JSON" and its Art 2 contains definitions only. The basis for that statement is not visible in the OJ text.
- CAT_* requirements in ARF Annex 2.02 Topic 25 are shown as "Empty" except CAT_04 (verification point usage); the catalogue is now legal text (2025/1569) plus TS11.

### B4. ARF Annex 2.02 (v3.0.0 per SRC-ARF-HLR), Topic 12 Attestation Rulebooks (read)

- ARB_05: attestation type value "SHALL be unique within the scope of the EUDI Wallet ecosystem." (`docType` in mdoc, `vct` in SD-JWT VC).
- ARB_06: attribute definition "SHALL first describe the semantics of each attribute in an encoding-independent manner and SHALL subsequently for each attribute specify an ISO/IEC 18013-5-compliant format, an SD-JWT VC-compliant format, or both".
- ARB_07 (SHOULD): reuse attributes from the catalogue of attributes or existing schemes. ARB_09: mandatory/optional/conditional per attribute. ARB_22: rulebook specifies "all technical details necessary to ensure interoperability, security, and privacy". ARB_29: follow rulebook template. ARB_33: scheme registration references the rulebook; note: "an attestation scheme is machine-readable, whereas an Attestation Rulebook is human-readable."
- ARB_34: rulebook states whether device-bound. ARB_25: attribute `attestation_legal_category`. ARB_28: optional `cryptographically_bound_to` (links attestations; relates to "chain" in EBW recital 27).
- Registration (Topic 27): registries hold "the attestation type(s) that the provider intends to issue" (Reg_01a note). Wallets must support all attestations of registered schemes whose format is supported (ISSU_33b).
- Linked-data support: grep of Annex 2.02 for "JSON-LD", "linked data", "RDF", "ontology" returned no hit. The only semantic-web-like element is OOTS Semantic Repository reference in TS11 and the W3C VCDM option (ARB_01a/04).

### B5. WE BUILD (SRC-WEBUILD-ARCH, upstream clone main at 2026-09-25 b47c1ba; SRC-WEBUILD-RB rulebooks 2026-10-01 208b9bc, read)

- Blueprint ch.5 (blueprint/05-data-and-semantics.md): semantic model in three layers (terminology SKOS, vocabulary OWL, attestation mapping). "The terminology and vocabulary layers are independent of attestation formats, while the mapping layer depends on the format used." "Currently, only W3C VCDM 2.0 supports machine-readable semantic mappings directly within credentials."
- adr/document-formats.md ("Specify PID and eAA formats", advice 2025-11-11 Ronald Koenig, Spherity: OK): WP4 Architecture specifies formats; Semantics group ensures interoperability "if the specified digital document type supports semantic mapping, such as in Verifiable Credentials Data Model v2.0"; for mdoc "extra translation may be needed ... the translation is the responsibility of the scheme owners". The ADR itself says concrete formats "should be recorded soon after".
- ADR "Preferred EUBW attestation format": NOT FOUND. I cloned the public upstream webuild-consortium/architecture (all 34 branch heads fetched) and grepped for "preferred ... attestation format"; no match. The Spherity fork (spherity/webuild-consortium-architecture) was not reachable in this session (GitHub MCP access denied for that repo). If it exists only in a fork branch or an unmerged PR, it is unread.
- adr/build-document-vs-attestation.md: "Attestations SHALL NOT be used as a substitute for business document exchange"; full business documents go through (Q)ERDS; reference attestation per EBW recital 27; the reference attestation schema/flow is listed as an open specification gap.
- Rulebooks (eudi-wallet-rulebooks-and-schemas, fork-independent public repo): per-attestation data schemas in `data-schemas/sd-jwt` and `data-schemas/mdoc`; counts of rulebooks mentioning formats (README grep, not a semantic count): SD-JWT 39, mdoc 33, VCDM 20 of the rulebook READMEs. rb-ebwoid: SD-JWT VC only, mdoc "out of scope", W3C VCDM "named, not specified". rb-gln: GS1 Web Vocabulary terms, JSON-LD paths, VCDM 2.0 context, `credentialSchema` JsonSchema, BitstringStatusList, plus SD-JWT embedding of the VCDM payload "following RFC 9901 Appendix A.4" (the rulebook text claims this; I did not verify RFC 9901 App. A.4). rb-taxid: SD-JWT VC primary, mdoc, W3C VCDM "not yet defined".

## C. Machine-readable and AI-processable semantics in official sources

| Source | Article / location | What it says (quote ≤25 words) | Bearing |
|---|---|---|---|
| ESPR (EU) 2024/1781 | Art 10(1)(d) | DPP data "based on open standards, developed with an interoperable format, and shall be, as appropriate, machine-readable, structured, searchable, and transferable" | DPP data requirement; applies to product data, not to wallet credentials |
| ESPR | Art 11(a) | DPP "fully interoperable ... in relation to the technical, semantic and organisational aspects of end-to-end communication and data transfer" | semantic interoperability across DPPs |
| ESPR | Art 10(1)(a),(c); Annex III | persistent unique product identifier; data carrier per ISO/IEC 15459 series | identifier standards |
| Data Act (EU) 2023/2854 | Art 33(1)(a) | dataset content "sufficiently described, where applicable, in a machine-readable format, to allow the recipient to find, access and use the data" | applies to "Participants in data spaces that offer data" |
| Data Act | Art 33(1)(b) | "data structures, data formats, vocabularies, classification schemes, taxonomies and code lists, where available, shall be described in a publicly available and consistent manner" | vocabulary publication duty |
| Data Act | Art 33(1)(c) | access means "sufficiently described to enable automatic access and transmission of data between parties" | machine-to-machine |
| Data Act | Art 3(1) | product data "including the relevant metadata necessary to interpret and use those data" in "structured, commonly used and machine-readable format" | metadata for interpretation |
| Data Act | Art 33(2),(3),(5) | delegated acts, harmonised standards, common specifications (presumption of conformity) | Commission can specify later |
| EBW proposal COM(2025) 838 | Art 5(1)(l) | export "in a structured, commonly used and machine-readable format" | portability only |
| EBW proposal | Art 6(1)(d) | interaction "automatically without manual intervention or through direct user action" | machine interaction required |
| EBW proposal | Art 8(2), Art 12(3), Art 10(1)(a) | lists of authentic sources and EBW providers "in a machine-readable format"; Directory "machine-readable interface exposed through an API" | registries |
| EBW proposal | Art 6(2)(b) | role-attribute mappings "verifiable, auditable, revocable and traceable"; authorisation logic "interoperable across Member States" | authorisation semantics |
| EBW proposal | Recital 28 | "new technologies that would enable new use cases, such as agentic AI" | only AI mention; no AI-specific data requirement found |
| EBW proposal | Legislative financial statement 4.2 | shared understanding measure: format per 2024/2979 Annex II; "annexes define the high-level requirements that will be then instantiated in specifications and standards in the upcoming implementing act" | semantics deferred to implementing acts |
| CIR 2025/1569 | Arts 7(8), 8(6) | catalogues "machine-readable and human-readable" | EUDI semantic catalogue |
| eIDAS Annex V(a)/VII(a) (via ETSI quote) | indication "in a form suitable for automated processing" | machine-processable category flag |
| W3C VCDM 2.0 | Introduction, A.11 | credentials "cryptographically secure, privacy respecting, and machine verifiable"; non-normative note on "machine-based actors" that "might legitimately hold verifiable credentials" | only AI-related statement in spec set; informative |
| ETSI TS 119 472-1 | 4.2.1.4, 7.2.1.3 | schema references incl. `ShaclSchemaCredential` (SHACL) | RDF-shape validation option only in JSON-LD realisation |
| IDTA AAS Part 1 | 4.3, 7.5 | `semanticId` and RDF/"Linked Data" serialisation; "automated reasoners" | industrial semantics, not a legal duty |

No provision found in the read sources that requires AI-specific processing or requires linked-data/RDF for credentials. Regulation (EU) 2024/1689 (AI Act) and the Interoperable Europe Act (EU) 2024/903 were not read for this question.

## D. DECISION CRITERIA (derived from sources; no ranking)

For each criterion: source basis, then facts per format. "NSS" = not stated in sources.

### D1. Legal listing for EBW owner identification data and EAA (compliance floor)
Basis: COM(2025) 838 Art 8(3); CIR 2026/1731 Annex IV (new Annex II to 2024/2979); CIR 2025/1569 Annex II.
- SD-JWT VC: listed (ETSI TS 119 472-1 cl. 5). mdoc: listed (cl. 6). W3C VCDM 2.0: not in the "clauses 2 to 6" list; recital 18 conditional wish for future profiles. AAS-as-VC: NSS.

### D2. ARF permissibility by attestation class
Basis: ARB_01, ARB_01a, ARB_04, ARB_02, ARB_03.
- SD-JWT VC and mdoc: allowed for QEAA, PuB-EAA, non-qualified EAA. W3C VCDM v2.0: only non-qualified EAA, plus approved RP-request and SD documents (ARB_04). mdoc is the only format for offline/proximity presentation if needed (ARB_02). AAS: NSS.

### D3. Selective disclosure (EBW Art 5(1)(b); 2024/2982 selective disclosure obligation)
Basis: EBW Art 5(1)(b); 2024/2982; ARB_30.
- SD-JWT VC: selective disclosure of any claim, optional per spec, rulebook decides (ARB_30). mdoc: element-level disclosure (per ISO snippet and RFC 9901 statement); ISO text unverified. W3C VCDM 2.0: data model does not mandate; achieved through SD-JWT, BBS (CRD) or ZKP "securing mechanisms"; ARB_04 requires a referenced approved document. AAS: NSS.

### D4. Unlinkability and anti-correlation (2024/2977, 2024/2982 text; ARF batch methods)
Basis: legal text "ensure unlinkability where the electronic attestations of attributes do not require the identification of the wallet user"; ARF ISSU_43 to ISSU_51, ZKP_01..ZKP_09; RFC 9901 10.1.
- SD-JWT VC and mdoc: salted-hash; presentation and verifier/verifier unlinkability via batch issuance; issuer/verifier unlinkability not achieved with colluding parties (RFC 9901 10.1). W3C VCDM: unlinkable disclosure defined as a goal; achieved only with blinded-signature suites (BBS, CRD 2026-09-10) or ZKP; Data Integrity says some use cases "required" linkability (e.g. hazardous materials). ZKP in ARF: SHOULD work on existing mdoc/SD-JWT VC. AAS: NSS. Note for B2B: whether business credentials need unlinkability is NSS in EBW text (the unlinkability wording refers to wallet user identification).

### D5. Semantic expressiveness and machine-readable mapping
Basis: CIR 2025/1569 Arts 7 and 8 (semantic description, namespace, data type); ARB_06; WE BUILD ch.5; ETSI 119 472-1 cl.4 and 7.
- SD-JWT VC: type URI plus optional Type Metadata; claim names under RFC 7519 rules; no standardised link to external vocabularies in the spec (NSS beyond Type Metadata `extends`, display, claim metadata). mdoc: docType + namespace; semantics in the rulebook; no linked-data mapping (WE BUILD). W3C VCDM 2.0: `@context`/`type` map terms to URLs; ETSI adds `credentialSchema` types incl. SHACL; "only W3C VCDM 2.0 supports machine-readable semantic mappings directly within credentials" (WE BUILD blueprint, ecosystem statement). AAS: `semanticId` (IRDI/IRI), ECLASS/IEC CDD, RDF serialisation (IDTA Part 1).

### D6. Registered schema and attribute identity (catalogue, versioning)
Basis: CIR 2025/1569 Arts 7(5), 7(10), 8(3); TS11; ARB_05, ARB_33.
- All EUDI formats: attribute namespace, identifier, version, data type; scheme lists formats. TS11 maps scheme per format (VCT / DocType / W3C options) and requires JSON schema distribution. AAS: submodel templates have IDs/semanticIds in IDTA repositories; relation to EUDI catalogue NSS.

### D7. Linked-data and cross-ecosystem interoperability (Catena-X, DCP, GS1, IDTA)
Basis: DCP v1.0 profiles; CX-0018, CX-0050; OID4VCI/OID4VP; rb-gln.
- DCP v1.0 (stable) profiles only W3C VCDM: `vc20-bssl/jwt` (VCDM 2.0, BitstringStatusList, JOSE) and `vc11-sl2021/jwt` (VCDM 1.1); DCP messages use JSON-LD contexts (DCP `dcp.jsonld`). CX-0018: participants hold VCs "according to the CX-0050 standard"; CX-0050 v2.2.1: JSON Schema for VC (VCDM 1.1-style fields, `@context`), types Membership, BPN, Framework Agreement, Dismantler. Proof format of CX credentials: not visible in read text. SD-JWT VC and mdoc in DCP/CX: not stated in sources read. OID4VCI/OID4VP/HAIP: HAIP profiles SD-JWT VC (`dc+sd-jwt`) and mdoc (`mso_mdoc`) only; OID4VP supports "any Credential format", examples for VCDM, mdoc, SD-JWT VC. EUDI protocol law (2026/1731 Annex XII) references HAIP profile and ISO 18013-7 Annex C. Eclipse Dataspace Protocol (DSP) 2025-1 page: fetched index only; no credential-format statement read.

### D8. Verifiability and signature options (qualified status)
Basis: eIDAS Annex V/VII via ETSI; ETSI 119 472-1 JAdES clauses; EBW Art 8(3)(a)-(c).
- SD-JWT VC: JWS/JAdES, X.509 trust; mdoc: COSE, X.509; W3C VCDM: Data Integrity (embedded) or JOSE/COSE (enveloped), "does not mandate any particular securing mechanism"; legal QEAA/PuB-EAA signature requirements for W3C realisation are in ETSI clause 7.6 (outside legal list). Whether Data Integrity proofs can satisfy qualified seal requirements: NSS in sources read. AAS: NSS.

### D9. Optional verifiability of non-wallet data (data spaces, DPP)
Basis: EBW Art 5(1)(a) (non-qualified EAA allowed), ARB_01a/ARB_24, ESPR Art 10, Data Act Art 33.
- EBW supports "qualified and non-qualified" attestations (Art 5(1)(h), Art 6(1)(a)). Non-qualified EAA may use any ARF-listed format, W3C VCDM only here (ARB_01a). ESPR/Data Act require machine-readable open standards, not signatures (Art 10(1)(d); Art 33(1)). Verifiability of DPP data via VC: NSS in ESPR text read.

### D10. Revocation and status
Basis: ARF VCR_01b, VCR_02; 2026/1731 (Token Status List draft-20); DCP profile; ETSI cl. 4.2.11.
- SD-JWT VC: either validity of 24 hours or less or Attestation Status List (Token Status List). mdoc: MSO status list or revocation list. W3C VC: BitstringStatusList in DCP and rb-gln; not in EU legal list. AAS: NSS.

### D11. Technical readiness and standards maturity
Basis: dates above.
- SD-JWT VC: IETF draft-19 awaiting IESG, referenced in law via ETSI TS; ETSI cites draft-13 (version lag). RFC 9901 (SD-JWT) is an RFC. mdoc: ISO/IEC 18013-5:2021 published; 18013-7 2024/2025. VCDM 2.0, DI 1.0, VC-JOSE-COSE: W3C Recommendations (2025-05-15); BBS: Candidate Recommendation Draft (2026-09-10). AAS Part 1: V3.0.2 (IDTA specification, IEC 63278 series referenced).

### D12. Proximity/offline and protocol coverage
Basis: ARB_02; HAIP; 2026/1731 Annex XII.
- mdoc: ISO 18013-5 (proximity) and 18013-7 Annex C (API); SD-JWT VC: OpenID4VP via HAIP, needs internet per ARF note; W3C VCDM: OID4VP examples, not part of the HAIP profile list. EBW Art 6(1)(d) requires automated interaction; proximity need for EBW: NSS.

### D13. Separation of attestations and documents
Basis: WE BUILD adr/build-document-vs-attestation.md (consortium decision, not law); EBW recital 27.
- Format-neutral. Large business documents are to be exchanged via (Q)ERDS; attestation formats carry identity, status, authorisation claims and hash references. Basis is an ecosystem ADR.

## E. Open questions and what could not be read

1. ISO/IEC 18013-5 and 18013-7 texts: paywalled; iso.org returned a Cloudflare 403. All ISO statements marked above rely on EU/ARF/ETSI/IETF text or search snippets. ISO/IEC 23220-2 and ISO/IEC 23220-7: not read.
2. EBW proposal Annex: the Eerste Kamer PDF as extracted showed no stand-alone annex text; Council ST 9684/26 contains an Annex (points 1 to 11 seen: e.g. pt 10 "in at least an open format"), read only by grep. Council ST 7659/26 only grep-read. Whether the Council or Parliament positions change Art 8(3) beyond the intermediary-platform wording in Art 8(2): not verified.
3. CIR 2026/1731: confirmed by me only for Annex IV/Annex I/Annex XII headings and passages above (Annex IV = clauses 2 to 6 of ETSI TS 119 472-1, with adaptations). Applicability dates: Article 3(4) applies from 11 August 2028; other application dates not extracted. Consolidated versions of 2024/2977, 2024/2979, 2024/2982 not read.
4. ETSI TS 119 472-1 V1.2.1 read mainly clauses 1, 4.2, 5.2.1, 6.2.1, 7.1 to 7.2, 7.6.4/7.6.5 (grep and sections); clause 5.6 and clause 7 selective disclosure details not read in full. ETSI TS 119 472-2, 119 472-3, 119 412-6, 119 478: only as cited.
5. ARF: eudi.dev rendering of Annex 2.02 only (consistent with SRC-ARF-HLR, version "3.0.0 as rendered at /latest/"). Discussion papers (Topic G ZKP, Topic O attributes), the ARF main chapters (formats, catalogue discussion), the Attestation Rulebook Template and the PID Rulebook: not read in full. No "Business Wallet" or "legal person" semantic chapter in the ARF was checked.
6. "Preferred EUBW attestation format" ADR in WE BUILD: not found in upstream; Spherity fork and Ronald Koenig's branch not reachable (repo access denied for spherity/webuild-consortium-architecture). Only the Koenig advice line in adr/document-formats.md (2025-11-11, "OK") was seen. Pull requests and unmerged discussions were not queried.
7. IDTA: Part 1 V3.0.2 searched by term only; Part 2 (API), Part 3a (IEC 61360), Part 4 (Security) not read (Part 4 snippet only); no IDTA specification on verifiable credentials found. AAS "as VC payload" has no source. CX-0050 states only JSON Schema structure in the text I extracted; proof format and exact `@context` values were not visible. Catena-X CX-0018 v4.2.1/preview read in part (credential section 2.3, 2.4); the SRC-CX-0018 entry says v4.3.0 (preview), page title read now says v4.2.1; check which is current.
8. Eclipse Dataspace Protocol (DSP) 2025-1: only the index page fetched; DCP v1.0.1 profiles read from the GitHub repo (commit b80ad76, 2026-08-05).
9. W3C VCDM 1.1 text not read separately (the URL served 2.0). VC JSON Schema, Bitstring Status List, VC render method, W3C DC API: not read. W3C VC Barcodes etc.: not read.
10. TS11 vs OJ discrepancy on "JSON schema" in 2025/1569 (B3) is unresolved; a later or draft version of the CIR may be the source.
11. AI Act, Interoperable Europe Act, ViDA/e-invoicing semantic requirements (EN 16931), eFTI (ISO/ semantic data model): not read for this task.
12. Not stated in any source read: a requirement that EBW credentials carry JSON-LD, RDF or ontology references; an EU-level mapping between the EUDI attribute catalogue and the OOTS Semantic Repository beyond the optional `semanticDataSpecification` URI in TS11; a cross-format guarantee of semantic equivalence between an mdoc namespace and an SD-JWT VC claim set other than the rulebook ("encoding-independent" description, ARB_06).

Local working copies (not part of deliverable): /tmp/w (EBW pdf text ebw.txt, cir*.txt, e472.txt, arf_hlr.txt, ts11.md, wb/, eudi-wallet-rulebooks-and-schemas/, dcp/).
