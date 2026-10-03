---
title: "DEC-01 Credential data model, semantics and formats"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 1
permalink: /architecture/decisions/dec-01/
description: "Which credential formats and which semantic layer should a business wallet support? Facts on SD-JWT VC, ISO mdoc, W3C VCDM 2.0 with JSON-LD and the Asset Administration Shell, decision criteria, options and the conditions under which each holds."
keywords: [credential format, SD-JWT VC, mdoc, W3C Verifiable Credentials, JSON-LD, linked data, Asset Administration Shell, semantic interoperability, selective disclosure, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-01 Credential data model, semantics and formats

*Analysis for decision, not a decision. Analysis, not legal advice. Statements marked "not stated" mean that no source read says it; they do not mean the opposite is true.*

## Question

Which credential formats and which semantic layer should a business wallet support, so that credentials are **interoperable** across Member States and ecosystems, **semantically rich** enough for linked data and machine or AI processing, protected by **selective disclosure** where needed, and **verifiable** where the use case requires it? The decision is usually framed as JSON-LD (W3C VCDM), SD-JWT VC, mdoc or Asset Administration Shell (AAS) submodels. The sources show that these options sit on different layers, which changes the question.

## What the requirement set says

No requirement in the draft set names a credential format. The legal texts are format-neutral at the level of obligations and point to lists of standards in implementing acts. The set contains these architecture-shaping requirements for cluster K01 (credential data model and formats) and K16 (AI use):

{% include cluster-drivers.html cluster="K01" %}

{% include cluster-drivers.html cluster="K16" %}

The consequence for the decision: the **formats are a compliance floor set by implementing acts**, while **semantic richness, linked data and AI processing are not required by any source read**. They are drivers that a stakeholder has to state and weigh. Section "Gaps" lists the requirements that are missing.

## Facts from the sources

### What law and specifications fix for the business wallet

- The proposal does not name a format. Article 8(3) says owner identification data "shall be issued in a format compliant with one of the standards listed in Annex II" of Implementing Regulation (EU) 2024/2979. Article 8(6) requires the attestation scheme to be listed in the catalogue of schemes under Regulation (EU) 2025/1569.
- Implementing Regulation (EU) 2026/1731 (OJ of 22 July 2026) replaces that annex. It applies "clauses 2 to 6 of ETSI TS 119 472-1 V1.2.1 (2026-02)": the SD-JWT VC realisation (clause 5) and the ISO mdoc realisation (clause 6). The JSON-LD W3C VC realisation (clause 7) and the X.509 attribute certificate (clause 8) are outside that range; this is the research reading of the clause range and should be confirmed. The earlier text listed ISO/IEC 18013-5 and W3C VCDM 1.1. Recital 18 of 2026/1731 says wallets "should also support" the W3C format "when the new profiles on the W3C VCDM format are available".
- The ARF treats mdoc and SD-JWT VC as the common formats for qualified and public-sector attestations (ARB_01), allows W3C VCDM v2.0 only for non-qualified attestations (ARB_01a) with an approved document on requests and selective disclosure (ARB_04), and names mdoc as the only format for offline or proximity presentation (ARB_02). The research found no JSON-LD, RDF or ontology term in the annex.
- AAS as a credential payload is not mentioned in any EU act, in the ARF or in the IDTA documents reached.

### Semantics in the EU framework

- Regulation (EU) 2025/1569 (Articles 7 and 8) requires catalogue entries with namespace, identifier, version, semantic description and data type, published in machine-readable and human-readable form. Schemes state their formats. The EUDI technical specification 11 lists the supported formats of a scheme as `dc+sd-jwt`, `mso_mdoc`, `jwt_vc_json`, `jwt_vc_json-ld` and `ldp_vc`, with an optional link to the semantic repository of the Once-Only system. TS11 says the catalogue holds a JSON schema "according to Article 2(3)", which the published text of 2025/1569 does not contain; the discrepancy is unresolved.
- Within each format the semantic mechanism is different: `vct` plus optional Type Metadata (SD-JWT VC), `docType` plus attribute namespace (mdoc), `@context` plus `credentialSchema` (JSON-LD VC). ETSI TS 119 472-1 allows SHACL schemas, but only in the JSON-LD clause.
- The ARF requires a rulebook to describe attribute semantics "in an encoding-independent manner" first and then per format (ARB_06). The WE BUILD blueprint describes three layers: terminology (SKOS), vocabulary (OWL) and an attestation mapping that depends on the format. It states that "only W3C VCDM 2.0 supports machine-readable semantic mappings directly within credentials". For mdoc and SD-JWT VC the meaning is defined in rulebooks.

### Selective disclosure and unlinkability, as the specifications say

- **SD-JWT** (RFC 9901, section 10.1) conceals unrevealed claim values but "does not meet the security properties for anonymous credentials". Colluding issuer and verifier can recognise a credential; batch issuance helps against verifier-to-verifier correlation, not issuer-to-verifier. The RFC says the same limits apply to salted-hash approaches including mdoc. Selective disclosure in SD-JWT VC is optional.
- **W3C VCDM 2.0** defines selective and unlinkable disclosure as goals and "supports being secured using zero-knowledge proofs". It does not mandate them. Data Integrity notes that some use cases do not permit unlinkability. The BBS cryptosuite for unlinkable derived proofs was a Candidate Recommendation Draft (10 September 2026), not a Recommendation.
- The EU wording on unlinkability concerns not identifying the wallet user. Whether business credentials need it is not stated in the sources.

### Verifiability, maturity and protocols

- SD-JWT VC is an IETF draft (draft 19, awaiting IESG go-ahead on 31 August 2026); ETSI cites draft 13. RFC 9901 (SD-JWT) is published. VCDM 2.0, Data Integrity 1.0 and VC-JOSE-COSE are W3C Recommendations (15 May 2025). ISO/IEC 18013-5 is published; its text was not readable (paywalled).
- Verifiability options: SD-JWT VC uses JWS with X.509 trust, mdoc uses COSE; VCDM "does not mandate any particular securing mechanism" and offers Data Integrity (embedded proofs) or JOSE/COSE (enveloped proofs, including SD-JWT). Whether Data Integrity proofs can satisfy qualified seal requirements is not stated in the sources read.
- Protocols: HAIP 1.0 (OpenID) profiles only SD-JWT VC and mdoc. The Eclipse Decentralized Claims Protocol v1.0 profiles only W3C VCDM (2.0 with JOSE and Bitstring Status List, and 1.1). The Catena-X credential standard CX-0050 is a JSON schema in the VCDM 1.1 style; its proof format was not visible. WE BUILD rulebooks use SD-JWT VC for the EBWOID, a GS1 JSON-LD payload for the global location number, and say W3C VCDM is "named, not specified".

### AAS

AAS Part 1 (V3.0.2) provides `semanticId` (IRDI or IRI, with ECLASS and IEC CDD as external concept repositories) and an RDF serialisation described as linked data. Parts 2, 3a and 4 were not read, and no IDTA specification on verifiable credentials was found. AAS is therefore an **implementation artefact for industrial data**, not a credential format in any source.

### Machine-readable and AI-processable data in other law

ESPR Article 10(1)(d) requires digital product passport data on "open standards ... interoperable format ... machine-readable, structured, searchable" and Article 11(a) semantic interoperability. Data Act Article 33(1) requires data-space participants to describe datasets and vocabularies machine-readably and publicly. In the EBW proposal, "machine-readable" concerns export, lists and the Directory interface, not credential semantics. The only mention of AI is recital 28 ("agentic AI"). W3C VCDM 2.0 has a non-normative note on machine actors holding credentials. The AI Act and the Interoperable Europe Act were not read for this question.

## Decision criteria

| # | Criterion | Basis |
|---|---|---|
| F1 | Legal listing for EBW owner identification data and attestations (compliance floor) | source: proposal Article 8(3); Regulation 2026/1731; 2025/1569 |
| F2 | ARF permissibility by attestation class (qualified, public-sector, non-qualified, proximity) | source: ARF ARB_01, 01a, 02, 04 |
| F3 | Selective disclosure | source: proposal Article 5(1)(b); Regulation 2024/2982 |
| F4 | Unlinkability against issuer, verifier and colluding parties | source (partial): wording concerns wallet users; business need is a driver |
| F5 | Semantic expressiveness and machine-readable mapping of claims | source (partial): catalogue entries (2025/1569); further richness is a driver |
| F6 | Registered schemas, versioning and identity of attributes | source: 2025/1569 Articles 7 and 8; TS11 |
| F7 | Interoperability with ecosystems (Catena-X, data spaces, GS1, IDTA) | source (partial): DCP and CX-0050 profiles; business need is a driver |
| F8 | Verifiability and signature options, including qualified status | source: eIDAS Annexes V and VII via ETSI TS 119 472-1 |
| F9 | Optional verifiability for non-wallet data (product data, data spaces) | driver; related: ESPR Article 10, Data Act Article 33 |
| F10 | Revocation and status mechanism | source: ARF VCR_01b, VCR_02; Regulation 2026/1731 |
| F11 | Maturity and stability of the specification | source: dates above |
| F12 | Offline and proximity presentation | source: ARF ARB_02; the EBW need is not stated |
| F13 | Processing by AI systems (vocabulary access, schema validation, provenance of claims) | driver; no source requires it |

## Comparison by format

How far the sources support each format per criterion. "Not stated" is not a negative.

| Criterion | SD-JWT VC | ISO mdoc | W3C VCDM 2.0 (JSON-LD) | AAS submodel as payload |
|---|---|---|---|---|
| F1 Legal listing (2026/1731) | Listed (ETSI clause 5) | Listed (clause 6) | Not in the clause range; recital 18 conditional wish | Not mentioned |
| F2 ARF classes | Qualified, public-sector, non-qualified | Qualified, public-sector, non-qualified; only format for proximity | Non-qualified only, with approved selective-disclosure document | Not mentioned |
| F3 Selective disclosure | Optional per spec; rulebook sets it per claim | Element-level (ISO text not read) | Not mandated; via SD-JWT, BBS or zero-knowledge proofs | Not stated |
| F4 Unlinkability | Limits per RFC 9901 10.1; batch issuance helps partly | Same limits per RFC 9901 | Goal of the model; needs blinded signatures or zero-knowledge proofs (BBS draft) | Not stated |
| F5 Semantics | Type URI plus optional Type Metadata; no standard link to external vocabularies | docType plus namespace; semantics in rulebook | `@context` maps terms to URLs; SHACL schema option (ETSI) | `semanticId`, ECLASS, IEC CDD, RDF serialisation |
| F6 Catalogue | Supported (TS11, `vct`) | Supported (docType) | Listed formats in TS11 | Relation to the EUDI catalogue not stated |
| F8 Signature | JWS, JAdES in ETSI profile | COSE | Data Integrity or JOSE/COSE; qualified suitability not stated | Not stated |
| F10 Status | Short validity or Token Status List | MSO status or revocation list | Bitstring Status List (DCP, WE BUILD); not in the EU list | Not stated |
| F11 Maturity | IETF draft 19; RFC 9901 published | ISO/IEC 18013-5:2021 | Recommendations (2025); BBS is a draft | IDTA V3.0.2 |
| F12 Proximity | Needs online per ARF note | Yes (18013-5) | Not part of HAIP | Not stated |

## Options

**O1. EUDI baseline only.** Support SD-JWT VC and mdoc as listed in 2026/1731 for all business wallet credentials; define semantics through rulebooks and catalogue entries.
- *Enables:* certainty of compliance, alignment with the ARF and with HAIP protocols, one set of wallet implementations.
- *Restricts:* no directly embedded linked-data mapping; ecosystems using DCP and VCDM (Catena-X, GS1-based credentials) need a separate path.
- *Leaves open:* whether the catalogue's semantic description can carry rich vocabulary mappings.

**O2. W3C VCDM 2.0 with JSON-LD as the primary model for business credentials.**
- *Enables:* direct machine-readable semantic mapping in the credential, SHACL schemas, alignment with DCP and Catena-X profiles, a route to unlinkable disclosure with future cryptosuites.
- *Restricts:* not in the legal list for identification data and qualified attestations (ARF allows it only for non-qualified attestations with additional approved documents); HAIP does not profile it; qualified suitability of Data Integrity proofs is not stated.
- *Leaves open:* the new W3C profiles that recital 18 of 2026/1731 mentions.

**O3. Two layers: EUDI formats as the credential binding, a format-independent semantic layer, and VCDM 2.0 as an optional second binding.** Credentials carry their claims in SD-JWT VC (and mdoc where proximity is needed). A published, versioned semantic model (terminology, vocabulary, attribute mappings) describes every attribute once, as the ARF rulebook approach (ARB_06) and the WE BUILD blueprint already imply, and is bound to each format. Ecosystems that need VCDM get a VCDM binding of the same model.
- *Enables:* compliance floor and semantic richness at once, one meaning per attribute across bindings, AI systems and linked-data tools consume the semantic layer and the verified claim set rather than parsing formats.
- *Restricts:* more work to maintain mappings; semantic equivalence between bindings is not guaranteed by any source (the rulebook is the only mechanism named).
- *Leaves open:* who governs the semantic layer, and which attribute subset needs linked-data mapping.

**O4. AAS submodels as credential payload.**
- *Enables:* reuse of industrial semantics (`semanticId`, ECLASS, IEC CDD).
- *Restricts:* no source specifies an AAS credential binding, and no EU act lists it.
- *Leaves open:* whether to reference AAS data from a credential (link and hash) instead of embedding it. The WE BUILD architecture decision keeps business documents out of attestations and routes them through registered delivery.

## Preliminary reading

*The analysis of this project, not a statement of a source.*

1. **The question is two decisions.** The *credential binding* (SD-JWT VC, mdoc, VCDM) is largely set by implementing acts for identification data and qualified attestations. The *semantic layer* (what an attribute means, how it maps to vocabularies, how machines and AI use it) is free of legal prescription, and that is where the user's goals (semantic richness, linked data, AI processing) can be met without leaving the compliance floor.
2. **Option O3 is the only option in the facts that satisfies both the floor (F1, F2) and the drivers (F5, F7, F13).** O1 gives the floor without the drivers, O2 gives the drivers for non-qualified credentials only, and O4 has no basis in any source. O3 works only if the semantic layer is a first-class artefact with an owner and versioning.
3. **Use a class-based format policy** instead of one format for everything:

| Credential class | Binding | Basis |
|---|---|---|
| EBW owner identification data, EBWOID | SD-JWT VC, mdoc where needed | proposal Article 8(3); 2026/1731 |
| Qualified and public-sector attestations | SD-JWT VC, mdoc | ARF ARB_01 |
| Non-qualified business attestations in EU ecosystems | SD-JWT VC by default; VCDM 2.0 allowed | ARF ARB_01a and ARB_04 |
| Data-space credentials (DCP, Catena-X) | VCDM binding of the same semantic model | DCP profiles |
| Industrial asset and product data (AAS, DPP) | Referenced from a credential by link and hash; semantics through `semanticId` mapping | not a credential format in any source |
| Mandates and authorisations | see DEC-02 | |

4. **Verifiability stays at the credential edge.** Optional verifiability (F9) is met by letting non-qualified credentials be signed but not qualified, and by referencing bulk data instead of embedding it. Nothing in the sources requires signatures on product data.
5. **AI processing** should use the semantic layer and the verified claims. Agents acting with credentials raise logging and human-oversight duties (see requirements LEG-040 to LEG-044, which assume a high-risk classification and are derived, not literal).

**Conditions under which this reading holds.** SD-JWT VC and mdoc stay the legal list for identification data; the semantic description fields of the EUDI catalogue (or the proposal's implementing acts) can reference external vocabularies; a stakeholder confirms that linked-data mapping and AI processing are drivers.

**What would change it.** Final text or implementing acts that add VCDM profiles to the list (recital 18 of 2026/1731); a Recommendation-level cryptosuite for unlinkable disclosure with qualified suitability; DCP adopting SD-JWT VC; publication of SD-JWT VC as an RFC; evidence that business credentials need issuer-verifier unlinkability; an IDTA specification for AAS-based credentials.

## Gaps

Requirements that the research suggests and the set does not yet contain (candidates for the next pass, class to be set after review):

- every attestation type of the business wallet has a format-independent semantic description with identifier, version and data type (follows 2025/1569 Articles 7 and 8);
- semantic descriptions and schemas are published machine-readably and versioned;
- the wallet supports the formats listed for identification data, and the attestation scheme states its formats;
- the wallet states per attribute whether selective disclosure is mandatory, optional or not allowed (ARF ARB_30);
- a mapping rule between bindings of the same attribute (assumption, class A);
- AI systems acting with credentials work from verified claims and documented vocabularies (assumption, class A).

## Evidence gaps and next steps

- Confirm the clause range of 2026/1731 against the Official Journal text and read its application dates; diff ETSI TS 119 472-1 clause 7 against the legal text.
- Read ISO/IEC 18013-5 through an authorised copy; read IDTA Parts 2, 3a and 4.
- Resolve the TS11 versus 2025/1569 discrepancy on the JSON schema.
- Find out whether the Commission annex of the proposal sets a selective-disclosure or format point beyond Article 8(3).
- The WE BUILD architecture decision on the preferred attestation format was not found in the public repository; read it in the Spherity fork if it exists there.
- Ask stakeholders which drivers (F4, F5, F7, F9, F13) are real requirements and weigh them.

## References

SRC-EBW-PROPOSAL, SRC-CIR-2026-1731, SRC-CIR-2025-1569, SRC-CIR-2024-2979, SRC-CIR-2024-2982, SRC-ETSI-119472-1, SRC-EUDI-TS11, SRC-ARF-HLR, SRC-VCDM-2.0, SRC-RFC-9901, SRC-IETF-SDJWT-VC, SRC-IDTA-AAS-P1, SRC-DCP, SRC-CX-0018, SRC-WEBUILD-ARCH, SRC-WEBUILD-RB, SRC-DATAACT. Full entries with version, date and URL are in the source register.
