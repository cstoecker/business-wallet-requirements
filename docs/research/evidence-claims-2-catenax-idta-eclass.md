# RES-evidence-claims-2: Catena-X, IDTA AAS, ECLASS, open semantics, Manufacturing-X, IPCEI-AI, Gaia-X

Date 2026-10-04. Primary sources only. Method note: most web pages were read through a summarising fetch tool (marked "part"); PDFs for IDTA Part 1 V3.0.2, Part 4 V3.1, the Digital Nameplate, the IDTA ECLASS guideline, ECLASS Terms of Use v4.3 and the Manufacturing-X study were downloaded and searched as text. Source IDs are proposed in RES-evidence-claims-2-new_sources.yml; IDs without that file are already in sources.yml.
Claims from docs/16 "Claims that need support" covered here: Catena-X credential share and catalogue content; ECLASS and IDTA semantic id licence terms. Not covered (other items of the list): EPCIS 2.0, VC 2.0 outside Europe, JSON-LD performance, Article 22 GDPR.

## 1. Catena-X

| Fact | Source | Read | To verify |
|---|---|---|---|
| CX-0149 v2.1.0 (preview; stable Titan v2.0.0): wallet manages VCs, identified by a DID; MUST use did:web; DID document per CX-0049; implements DCP v1.0; three mandatory credential scopes MembershipCredential, DataExchangeGovernanceCredential, BpnCredential; follows "VC Data Model v1.1" and StatusList2021 | SRC-CX-0149 | part (summary) | Exact wording of the VCDM 1.1 sentence (earlier note read the page in full) |
| CX-0049 v2.3.0: DID document MUST comply with DID v1.0 and DCP v1.0; contains a CredentialService endpoint, optional DataService endpoint; credential types are defined in CX-0050 | SRC-CX-0049 | part | Whether did:web is mandated here (summary says no; CX-0149 says yes, earlier note says CX-0049 has no did:web rule) |
| CX-0050 v2.2.1 (preview): defines four credential types Membership, BPN, Framework Agreement, Dismantler; JSON Schema 2020-12; issued by core service providers (CSP-B); the page does not state the VC data model version and does not address attaching credentials to assets or catalogue entries | SRC-CX-0050 | part | Changelog summary showed v2.1.0 for CX-0050; page says v2.2.1. Confirm which is preview |
| CX-0018 v4.3.0 (preview; stable v4.2): participants hold VCs per CX-0050; a Participant Agent MUST use the DID as participant identifier; DCP used between connector and wallet; catalogue request token scope needs Membership, BPN and Framework Agreement credentials; policy mapping via CX-0152 (leftOperand = credential name). SAMM, Semantic Hub, DCAT not addressed in CX-0018 | SRC-CX-0018 | part | Quoted wording; clause numbers |
| Data catalogue entries or data assets do not carry credentials in the standards read. Credentials are presented by the consumer (token scope, DCP) and checked against ODRL-style policy constraints on the asset (CX-0152). | SRC-CX-0018, SRC-CX-0152, SRC-CX-0050 | part | Our reading, not a source statement. Check CX-0152 constraint list in full |
| Share of Catena-X data exchange that uses credentials | not found | n/a | Not stated in any standard. Needs Catena-X Association statement; otherwise drop |
| CX-0002 Digital Twins v2.4.0 (preview and stable): requires AAS 3.x (Part 1 V3.2, Part 2 V3.2); semanticIds must reference Aspect Models conformant to CX-0003; references CX-0149 and CX-0050 for security without mandating them for basic Digital Twin Registry operations | SRC-CX-0002 (new) | part | Clause numbers |
| CX-0003 v1.3.0: mandates SAMM 2.2.0; Semantic Hub holds released Aspect Models, synchronised with public GitHub; semantic ids are URNs `urn:samm:io.catenax.<name>:<version>#<Aspect>`; legacy `urn:bamm:` MUST NOT be used; copyright Catena-X e.V., all rights reserved; uses open source ESMF tools | SRC-CX-0003 (new) | part | Changelog summary said v2.2.0 for CX-0003, page says v1.3.0 (likely SAMM version in changelog). Licence of the models themselves (Eclipse Tractus-X repo) not read |
| CX-0143 Digital Product Passport v1.2.0: DPP implemented as SAMM Aspect Models (snippet only); battery passport and transmission passport are realisations | SRC-CX-0143 (new) | snippet | Fetch the page; look for any credential or signature requirement. Changelog says battery passport info removed in v1.2.0; battery semantic ids `urn:samm.io.admin-shell.idta.batterypass.` per CX-0003 |
| CX-0044 ECLASS v1.0.2 (stable): ECLASS is the preferred dictionary; "An ECLASS license is needed to describe commercial products"; testing and development of Catena-X models free of cost; IRDI ICD for ECLASS is 0173 | SRC-CX-0044 (new) | part | Not in preview index list read; check status in next release |
| Release status: CX-Neptune is Preview, CX-Titan is Current (stable); earlier note records go-live announced 24 Nov 2026 | SRC-CX-CHANGELOG, overview page | part | Go-live date was not found on the changelog page in this pass; rely on cx-cross-jurisdiction note and re-check |
| CX-0167 absent in stable; CX-0006 and CX-0009 fast-track | cx-cross-jurisdiction note | (from repo note) | Not re-read here |

## 2. IDTA AAS

| Fact | Source | Read | To verify |
|---|---|---|---|
| Part 1 V3.0.2 (March 2025): semanticId on Submodel, SubmodelElement, Qualifier etc. has type "IRDI, IRI (URI)" ("The semantic ID might refer to an external semantic model defining the semantics of the submodel") | SRC-IDTA-AAS-P1 table, 4.3, 5.3 | part (searched text) | Page numbers. Current is V3.2 (CX-0002); V3.3 online edition exists |
| Two global identifier types: IRDI (ISO 29002-5, ISO/IEC 6523, ISO/IEC 11179-6) and IRI (RFC 3987/3986 URI, URL), plus custom ids. An IRI is expressly allowed for assets, shells and "not standardized, but globally unique" properties | SRC-IDTA-AAS-P1 4.3.3 | part | |
| ConceptDescription id: mandatory, IRDI, IRI or Custom; if a copy from an external dictionary like ECLASS or IEC CDD "it may use the same global ID as it is used in the external dictionary". Semantic matching default is exact string identity; versions of ECLASS IRDIs are backward compatible; cross-dictionary equivalence example 0112/2///61360_4#AAE530 (IEC CDD) = 0173-1#02-AAI048#004 (ECLASS) | SRC-IDTA-AAS-P1 4.4.1 | part | Matching strategy is a hint ("first hints"), not a rule |
| ECLASS id can be sent as IRDI `0173-1#02-AAC895#008` or IRI `https://api.eclass-cdp.com/0173-1-02-AAC895-008` | SRC-IDTA-ECLASS-GUIDE v1.0 Oct 2024 | part | |
| Part 1 defines an RDF serialisation (clause 7.5: RDF recommended; "requires a clear scheme of its RDF representation"; RDF schema/OWL .ttl files in repo aas-specs, folder schemas\rdf; mapping rules in Readme); XML, JSON and RDF mappings moved into GitHub repositories since V3.0 | SRC-IDTA-AAS-P1 1.1, 7.5 | part | Repo name aas-specs (admin-shell-io) and current path (my direct fetch of aas-specs-metamodel/schemas returned 404). No JSON-LD serialisation named in Part 1 (not found) |
| JSON-LD for the DPP: "In EN 18220 it is specified that JSON shall be used for syntactic interoperability. In addition to JSON also XML and JSON-LD may be used based on http content negotiation" (DPP annex of Part 1 V3.2) | SRC-IDTA-AAS-P1-V32 (new) | part | Applies to DPP annex, not the metamodel as such |
| Part 4 Security V3.1: access tokens as signed JWT bearer tokens (RFC 7519, RFC 9068 claims); VCs appear as an option: Figure 13 shows a Dataspace Protocol flow where the consumer presents a Verifiable Presentation, claims "usually follow the Verifiable Credential Data Model embedded in a jwt"; lists X.509 and "Decentralized Identifiers (DID) and Verifiable Credentials (VC)" as examples of secure identity infrastructures; the AAS server may trust an Identity Provider key "available ... by a verifiable credential"; dataspace policy defines trusted tokens | SRC-IDTA-AAS-P4 | part (text searched) | The VC is an access credential about the consumer. It is not a VC around a submodel |
| Part 4 signing: chapter "Accountability for AAS Content and Digital Signatures": digitally signing AAS payloads applies especially when information from a 3rd party is relayed; examples are a signed PDF/XML file as submodel element value or detached signatures in a Property; "Signing of Identifiables is defined in the REST API specification ... Currently plain JWS (JSON Web Signature) is used ..., which MAY be extended to additional formats e.g. JAdES. In addition AASX packages can be signed." | SRC-IDTA-AAS-P4 | part | Part 2 text defining the signing was not read. So: signed submodels exist via JWS; no W3C VC around AAS content found in Parts 1 or 4 |
| VC as AAS payload / AAS as VC format: no IDTA statement found | | | confirms RES dec-01 finding (NSS) |
| IDTA 02099-1 DPP Part 1 Metadata V1.0.1 (July 2026), conforms to EN 18223:2026; nine properties (digitalProductPassportId, uniqueProductIdentifier, granularity, dppSchemaVersion, dppStatus, lastUpdate, economicOperatorId, facilityId, contentSpecificationIds); semantic ids are IRIs e.g. https://admin-shell.io/idta/cds/granularity/1; no VC or signature content (EN 18246 data authentication named; EN 18239 access rights "not yet released" per the V3.2 annex) | SRC-IDTA-DPP-02099-1 (new) | part | Whether EN 18246 is released by today |
| Digital Nameplate IDTA 02006 V3.0.1 (Oct 2025): submodel semanticId IRI `https://admin-shell.io/idta/nameplate/3/0/Nameplate`; properties described by IEC CDD (semantic ids) with ECLASS IRDIs as supplemental semantic ids | SRC-IDTA-DIGITAL-NAMEPLATE (new) | part | Version history in the pdf (V3.0.1) |
| Carbon Footprint IDTA 02023 V1.0 (25 March 2025); Digital Battery Passport IDTA 02035 parts 1 to 7 (nameplate, handover, PCF, technical data, condition, material composition, circularity) | SRC-IDTA-CARBON-FOOTPRINT (new) | snippet | Open the PDFs before citing any content |
| Part 2 API: query language, registry, semanticId lookup | SRC-IDTA-AAS-P2 (new) | snippet | Not read |

## 3. ECLASS and IEC CDD licence

| Fact | Source | Read | To verify |
|---|---|---|---|
| ECLASS Standard: every structural element has an IRDI (ISO 29002-5). "To use the ECLASS Standard (or parts of it) you need a license" (Terms of Use page). Single licence = one release, Concordance licence = all releases; both with ECLASS BASIC and ADVANCED; fees by company size; members of ECLASS e.V. use all licences without additional cost | SRC-ECLASS-LICENSES, SRC-ECLASS-TOU page | read | Price figures not opened (SRC-ECLASS-PRICES) |
| Free without licence (Terms v4.3 cl. 4.1): (a) use in standardisation documents "e.g. AutomationML, IDTA, EANCOM, OPC UA companion specification" in which structural elements are displayed; (b) indirect obtainment: receiving ECLASS data from a business partner's product data, storing and using it unaltered in own processes and passing it on unaltered, only for the described products or that business relationship; no modification or appending of further ECLASS content (4.1.3). Research and teaching free (4.3.1); development and testing by contact with ECLASS head office (4.3.2) | SRC-ECLASS-TOU | part (cl. 1 to 4 read) | Version 4.3 is dated 2022; check for newer terms. Does a semanticId reference inside an AAS count as "work result" under 4.1.2? Legal reading needed, our reading only |
| Licence needed (cl. 4.2, 3): to describe own products with ECLASS, enrich product data with further structural elements, use as internal classification. Webservice: certificate required, billed per IRDI; free for ordinary members and Concordance licensees | SRC-ECLASS-TOU, SRC-ECLASS-WEBSERVICE | part | |
| Terms obligation: name "ECLASS" must be used with release number, e.g. "ECLASS 11.0" (5.1) | SRC-ECLASS-TOU | part | |
| Catena-X says: "An ECLASS license is needed to describe commercial products"; testing and development free | SRC-CX-0044 | part | Quote repeats ECLASS wording (search snippet) |
| IDTA own statement on semantic ids: identifiers are IRDI or IRI; the Digital Nameplate has IEC CDD as primary and ECLASS as supplemental; IDTA submodel semantic ids use its own IRIs (admin-shell.io/idta/...). A licence statement for those IRIs: not found | SRC-IDTA-AAS-P1, DIGITAL-NAMEPLATE | part | Licence of IDTA templates (the PDFs had no "licen" hit in the nameplate) not found; check the submodel-templates repo LICENSE |
| IEC CDD licence terms | not found | n/a | cdd.iec.ch returned 403 to automated fetch. Only the tc3.iec.ch page on IRDI format (RAI#DI#VI, ISO TS 29002-5) was read. A search summary mentioned an IEC/ISO licence agreement and free access, from non-primary text: do not use |

## 4. Open alternatives

| Fact | Source | Read | To verify |
|---|---|---|---|
| schema.org vocabulary: Creative Commons Attribution-ShareAlike 3.0; W3C RF patent policy; sponsors may change at any time | SRC-SCHEMA-ORG-TERMS | part | Software licence (Apache 2.0) only referenced |
| GS1 Web Vocabulary: extension of schema.org (gs1:Product equivalent to schema:Product); Apache 2.0; JSON-LD and Turtle; ratified version at ref.gs1.org/voc | GitHub gs1/WebVoc README (development site; a GS1 repository), SRC-GS1-WEBVOC | part (README) | ref.gs1.org did not render; version and licence of the ratified site unverified |
| UNTP: all main artefacts issued as W3C VCDM 2.0 credentials with the UNTP JSON-LD context; issuers identified by DID; DPP spec v0.8.0 "work in progress, suitable for pre-production pilot"; v1.0 expected; UN/CEFACT standards "free to use under CC BY 4.0" | SRC-UNTP-SPEC | part | Version mismatch: vocabulary site shows 0.7.0 contexts. The repo spec-untp showed GPL-3.0 on LICENSE (curl of main/LICENSE) while docs say CC BY 4.0; clarify code vs spec |
| UNTP spec list: DPP, DFR, DTE, Conformity Credential, Conformity Vocabulary Catalog, Identity Resolver, Digital Identity Anchor, Digital Corporate Record, VC profile, Decentralised Access Control, Core Vocabulary | SRC-UNTP-SPEC | part | |
| QUDT: CC BY 4.0; release 2.1; RDF and JSON | SRC-QUDT | part | Latest version number |
| W3C Recommendations: SHACL 20 July 2017; OWL 2 Second Edition 11 Dec 2012; RDF Schema 1.1 25 Feb 2014 | SRC-W3C-SHACL, -OWL2, -RDFS | part | |
| SAMM: meta model specified in RDF/Turtle with SHACL validation rules; Eclipse ESMF; releases 2.0.0, 2.1.0, 2.2.0 | SRC-SAMM | part | Licence of spec not found (MPL-2.0 stated for UI code only) |

## 5. Manufacturing-X

| Fact | Source | Read | To verify |
|---|---|---|---|
| Plattform Industrie 4.0 and BMWK pages are blocked to automated access (Radware challenge); not read | | not read | Open in a browser |
| Existing register entries: SRC-MX-WP (Whitepaper 2022-11), SRC-MX-TALK15 | sources.yml | (existing) | |
| Data Space Study (ZVEI, VDMA, Fraunhofer, 2023): federated data spaces, Catena-X with EDC and semantic models, AAS "encompasses the concept of semanticIDs, which makes it possible to reference ECLASS or IEC CDD models or any other kind of model"; AAS security uses X.509 certificate chains; no VC or DID statement found by search | SRC-MX-DATASPACE-STUDY | part (text searched) | Industry study, not an official programme text; say so in the talk |

## 6. IPCEI-AI

| Fact | Source | Read | To verify |
|---|---|---|---|
| Commission news item 16 Sep 2026 (updated 17 Sep): 19 Member States (AT, BE, HR, EE, FI, FR, DE, HU, IE, IT, LV, LU, NL, PL, RO, SK, SI, ES, SE), coordinated by Germany, "design" and pre-notification under State aid rules; covers "the entire AI stack", "decentralised and commonly accessible AI services", "AI and compute management technologies", digital sovereignty | SRC-EC-IPCEI-AI | read (via summary) | Item is a short announcement |
| Agents or data specification in IPCEI-AI | not found | | No mention of agents, data or interoperability in the official item. Press (non-primary) says data provision is part of the lifecycle; do not cite |
| Name: "IPCEI AI" (Commission wording, also written IPCEI-AI) | SRC-EC-IPCEI-AI | read | |

## 7. Gaia-X

| Fact | Source | Read | To verify |
|---|---|---|---|
| Gaia-X ICAM 24.07: "A Gaia-X Credential is a Verifiable Credential following W3C Verifiable Credential Data Model 2.0 using the Gaia-X Ontology" from the Gaia-X Registry; VP bundles VCs; example uses issuer did:web, secured as VC-JWT (VC-JOSE-COSE) | SRC-GAIAX-ICAM-24.07 | part | Later release (25.xx) not checked |
| Trust Framework technical prelude (main): attributes follow the VC Data Model; a JSON-LD context maps terms to full URIs "for interoperability" and RDF compliance; context at w3id.org/gaia-x/core/ | SRC-GAIAX-TF-PRELUDE | part | main branch is not a release |
| SHACL shapes for credential validation (registry) | search snippet of Gaia-X docs | snippet | Open the ICAM or Trust Framework page, find the SHACL clause |
| Existing register entry SRC-GAIAX-COMPLIANCE-24.04 (compliance document; pages on VC/JSON-LD not read) | sources.yml | (existing) | The "latest" URL still serves 24.04-prerelease |

## Open points to hand back
1. Catena-X credential share: not found. Suggest label "our reading" or remove.
2. ECLASS: an IDTA submodel reference needs no licence in standardisation documents (4.1.1) and indirect obtainment is limited (4.1.2); describing own products needs a licence. Needs a lawyer before the talk claims "free".
3. IEC CDD licence: not found.
4. IDTA: RDF serialisation yes (Part 1 7.5); JSON-LD only in the DPP annex; VC around submodels not found; signed JWS exists in Part 2/4.
5. Version conflicts to check: CX-0050 (2.1.0 vs 2.2.1), CX-0003 (1.3.0 vs 2.2.0), UNTP vocabulary 0.7.0 vs spec 0.8.0.
