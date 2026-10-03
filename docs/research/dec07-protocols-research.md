# RES-dec07-protocols: protocols and interfaces (K08, K12)

Scope: facts from primary sources only; no recommendation. Date of work: 2026-10-03. Decision question (DEC-07): which issuance, presentation, data space and delivery protocols must a business wallet implement, and how do they fit together?
Source IDs reuse `_data/graph/sources.yml`; sources not yet registered are marked (new) and listed in `/tmp/cand/I4-new_sources.yml`. Read states: read = the cited passage was read in the full text of the original; partly-read = the cited section was read, the rest of the document was not; snippet = read only through a search hit or a reference in another document; unverified = not read.
Local texts used: EBW proposal /tmp/claude-0/s/838.txt; Council ST 9684/26 /tmp/w/ST-9684-2026-INIT.txt (Annex read in full); CIR 2024/2982, 2025/1944 /tmp/cand/eu; CIR 2026/1731 /tmp/w/cir1731.txt (OJ L, 22.7.2026); OpenID4VCI 1.0 (final, 16 Sep 2025), OpenID4VP 1.0 (final, 9 Jul 2025), HAIP 1.0 (final, 24 Dec 2025) in /tmp/w; ETSI TS 119 472-2 V1.2.1 (2026-03), TS 119 472-3 V1.1.1 (2026-03), EN 319 522-1 V1.2.1, EN 319 522-4-1 V1.2.1, EN 319 522-4-3 V1.1.1 downloaded from etsi.org; OASIS AS4 Profile 1.0 (2013) html; Eclipse DCP (/tmp/w/dcp, git b80ad76, 2026-08-05) and DSP release 2025-1 (/tmp/cand/i4/dsp, git 8c20a5b); Catena-X CX-0018 (preview).
Caveat 1: COM(2025) 838 is a proposal; the Commission Annex is not in the local copy (text ends at the financial statement); the Council Annex (points 1 to 17) was read instead. The outcome of the Council meeting of 9 June 2026 was not read.
Caveat 2: ISO/IEC 18013-5 and 18013-7 are paywalled and were not read. Statements about them come from CIR 2024/2982, CIR 2026/1731, ETSI TS 119 472-2 and HAIP.
Caveat 3: CIR 2026/1731 cites TS 119 472-2 V1.2.1 and 119 472-3 V1.1.1; a V1.3.1 of 119 472-2 exists on the ETSI server and was not used for quotes.

## (A) FACTS FROM SOURCES

### A1 EBW proposal and Council text: what the text asks for
- A1.1 Common protocols. Providers shall ensure support for "common protocols and interfaces" for issuance, request and validation, sharing and presenting, automatic interaction, onboarding, wallet-to-wallet interaction, relying-party authentication, wallet validation, registered delivery, digital addresses, wallet unit attestations and critical assets | SRC-EBW-PROPOSAL Art 6(1)(a) to (l) | read.
- A1.2 Issuance. "for the issuance of European Business Wallet owner identification data, qualified and non-qualified electronic attestations of attributes" and certificates, to European Business Wallets | Art 6(1)(a) | read.
- A1.3 Presentation. "for European Business Wallet-relying parties to request and validate European Business Wallet owner identification data and electronic attestations of attributes" | Art 6(1)(b); sharing and presenting selectively disclosed data | 6(1)(c) | read.
- A1.4 Automation. "to allow interaction with the European Business Wallets automatically without manual intervention or through direct user action" | Art 6(1)(d) | read.
- A1.5 Between wallet types. "for interaction between European Business Wallets, and between European Business Wallets and European Digital Identity Wallets" | Art 6(1)(f) | read.
- A1.6 Verification of the wallet. Protocols "for European Business Wallet-relying parties to verify the authenticity and validity of European Business Wallets, where the verification of the authenticity and validity is required" | Art 6(1)(h) | read.
- A1.7 Registered delivery and directory. "for the provision of the qualified electronic registered delivery service referred to in Article 5(1), point (i), including an interface to the European Digital Directory" and "at least one unique digital address" per owner | Art 6(1)(i), 6(1)(j) | read.
- A1.8 Standalone delivery for personal wallet users. Providers "shall enable the provision of the qualified electronic registered delivery service ... as a standalone service to users of European Digital Identity Wallets" | Art 5(3) | read.
- A1.9 Standards are left to implementing acts. The Commission "shall, by means of implementing acts, establish a list of reference standards and where necessary, establish specifications and procedures for the technical features" | Art 6(5) | read. The same for core functionalities in Art 5(5) | read.
- A1.10 Directory interfaces. The Directory is a web application with "a machine-readable interface exposed through an API for automated system-to-system communication" and a portal | Art 10(1) | read; implementing acts set "standards and technical specifications for the unique digital addresses" | Art 10(6) | read. Protocol and API are not specified in the articles read.
- A1.11 Council Annex 11 on the delivery channel. Wallets shall "integrate and support the use of a specific qualified electronic registered delivery service in accordance with Articles 43 and 44"; the Commission shall "designate the protocol"; the service must rest on "open, publicly available and royalty-free standards", provide "end-to-end encryption", and have "continuous availability, redundancy and fallback mechanisms"; "Interoperability ... shall be mandatory" | SRC-COUNCIL-ST-9684-26 Annex point 11 | read.
- A1.12 Council Annex 13 to 17 on interfaces. Wallet units "authorise requests and, where applicable, authenticate those made through European Digital Identity Wallets relying-party access certificates or European Digital Identity Wallet unit attestations"; "Authentication of the relying party shall be required where attestations are intended for a restricted audience" | Annex 13(1) | read. Units "are able to authenticate relying parties" when requesting issuance | Annex 14(1) | read. Protocols for presentation follow "the standards defined in the implementing acts" | Annex 15(1) | read. Owner identification data "cryptographically bound to the European Business Wallet unit" | Annex 16(2) | read. Attestation providers "shall identify themselves to European Business Wallet units" | Annex 17(2) | read.
- A1.13 Formats. Owner identification data shall be "issued in a format compliant with one of the standards listed in Annex II of Commission Implementing Regulation (EU) 2024/2979" | SRC-COUNCIL-ST-9684-26 Art 9(3) | read.
- A1.14 Interaction with EUDI Wallets in the core functions. Providers shall enable owners to "request and share ... in a secured way between European Business Wallets and European Digital Identity Wallets and with European Business Wallet-relying parties" | SRC-EBW-PROPOSAL Art 5(1)(c) | read.

### A2 CIR 2024/2982 as amended by CIR 2026/1731 (EUDI Wallet protocols)
- A2.1 Original rule. Wallets support presentation protocols "in accordance with the standards set out in the Annex" and the Annex listed two standards: "ISO/IEC 18013-5:2021" and "ISO/IEC TS 18013-7:2024" | SRC-CIR-2024-2982 Art 5(1), Annex | read.
- A2.2 Amendment of 15 July 2026. "The Annex is deleted." and replaced by Annex I (issuance) and Annex II (presentation) | SRC-CIR-2026-1731 Art 4 (amending 2024/2982) | read.
- A2.3 Issuance specification now cited. "The technical specification ETSI TS 119 472-3 V1.1.1 (2026-03) shall apply with the following adaptations" | SRC-CIR-2026-1731 Annex XI (new Annex I of 2024/2982) | read.
- A2.4 Presentation specifications now cited. "The technical specification in Annex C to ISO/IEC 18013-7:2025 shall apply." and clauses 4.1, 4.2, 5 and 6 of ETSI TS 119 472-2 V1.2.1 (2026-03) with adaptations | SRC-CIR-2026-1731 Annex XII (new Annex II) | read.
- A2.5 Two profiles in TS 119 472-2. The ISO/IEC-mdoc profile (ISO/IEC 18013-5 for non-API-mediated, Annex C of ISO/IEC 18013-7 for API-mediated transmission) and the OpenID4VC-HAIP profile "for both API-mediated and non-API mediated transmission mechanisms" | SRC-CIR-2026-1731 Annex XII scope text; SRC-ETSI-119472-2 (new) clause 1 | read.
- A2.6 Registered-relying-party checks. "The EUDI Wallet shall validate the wallet-relying party registration certificate received in the request" before presenting any requested PID or attestation to the user for approval | SRC-CIR-2026-1731 Annex XII clause 4.4 WRP-VALIDATION-01 | read. Over-asking: wallet "shall compare the attestations and attributes requested ... with the registered attestations" and warn before disclosure | WRP-OVERASKING-01, -02 | read.
- A2.7 Access certificate checks stay in the wallet. Wallets authenticate and validate access certificates "without delegating execution of these processes to an operating system browser or other intermediary application" | SRC-CIR-2026-1731 Art 4(2)(a) amending Art 3(1) | read. Article 3(4) (registration certificate) "shall apply from 11 August 2028" | Art 4(5) | read.
- A2.8 Issuers must be authenticated. Wallet units request issuance "only from parties having an authentic and valid wallet-relying party access certificate" | SRC-CIR-2024-2982 Art 4(2) | read.
- A2.9 Privacy in the same regulation. Wallets "enable privacy preserving techniques which ensure unlinkability" where attestations do not require identification; Article 5(4) selective disclosure; erasure requests (Art 6) and reports to data protection authorities (Art 7) | SRC-CIR-2024-2982 Art 3(10), 5(4), 6, 7 | read.
- A2.10 ARF position. "at least two different protocols can be used within the EUDI Wallet ecosystem, namely the ones specified in ISO/IEC 18013-5 and OpenID4VP" | SRC-ARF-TRUST 6.6.3.2 | read.
- A2.11 Mediating API. "The EUDI Wallet shall support a mediating API that supports both protocols defined in clause 5.2 of [11] and in Annex C of [16]." A note excuses non-conformity where the operating system or browser does not provide the features | SRC-CIR-2026-1731 Annex XII EAAP-API-GEN-01 | read.

### A3 ETSI TS 119 472-3 and 119 472-2 (EU profiles)
- A3.1 Issuance base. The wallet implements "the profile of the protocol defined in OpenID4VCI [2] specified by the requirements defined for the Wallet in OpenID4VC-HAIP [1], clause 4" | SRC-ETSI-119472-3 (new) GEN-REQ-4.1-01 | read. Issuers do the same for the issuer role | GEN-REQ-4.1-02 | read.
- A3.2 Flows. The wallet supports the Authorisation Code Flow and the Pre-Authorised Code Flow; providers implement at least one; "PID Providers implementing the Pre-Authorised Code Flow shall perform user authorisation with the physical presence." | GEN-REQ-4.1-03 to -05 | read. A note says online issuance at LoA high "is discarded for the Pre-Authorised Code Flow".
- A3.3 Invocation. "The custom URL scheme "eu-eaa-offer://" shall be used to invoke the EUDI Wallet." | GEN-REQ-4.1-06 | read.
- A3.4 Signed metadata with the access certificate. "The Issuer Metadata shall be a signed metadata according to clause 12.2.3 of OpenID4VCI" and "The signing certificate ... shall be the access certificate of the PID/EAA Provider." | ISS-MDATA-4.2.1-01, -02 | read. The registration certificate is carried in `issuer_info` | ISS-MDATA-REG_CERT-4.2.3-04 as amended by CIR 2026/1731 Annex XI | read.
- A3.5 Presentation profile. "The Authorization Request shall use the Client Identifier Prefix x509_hash." and "The RO JWT body shall contain the verifier_info parameter." with the registration certificate as an element | SRC-ETSI-119472-2 OIDFVP-HAIP-COMMON-REQ-01, -RO-01, -RO-13 to -16 | read.
- A3.6 Response encryption. "The EUDI Wallet shall encrypt the authorization response." | OIDFVP-HAIP-COMMON-RESP-01 | read.
- A3.7 Cross-device. "The EUDI Wallet shall support the cross-device flow using only the API-mediated mechanism." Wallets support at least the custom URL scheme eu-eaap:// for the authorization endpoint; the request carries the `request_uri` parameter | OIDFVP-HAIP-SUPPORT-03, -REDIRECTS-03, -04 | read. A note says API-mediated support "could change in the future depending on the evolution of W3C DC API".
- A3.8 Mediating API disclosure. "The EUDI Wallet shall by default disclose the presence of all stored EAAs' type to the mediating API" but not attributes or values | OIDFVP-HAIP-ADD-API-01 | read.
- A3.9 Other formats. The documents also cover X.509 attribute certificate EAAs and JSON-LD W3C VC presentation (clause numbers JSON_LD_EAA) | SRC-ETSI-119472-3 scope item 11 and SRC-ETSI-119472-2 JSON_LD_EAA requirements | partly-read.

### A4 OpenID4VC specifications (final)
- A4.1 Issuance flow variations. Authorization Code or Pre-Authorized Code; wallet-initiated or issuer-initiated; same-device or cross-device offer; "Immediate or Deferred" | SRC-OID4VCI-1.0 (new) 3.3.3 | read.
- A4.2 Batch. "the batch of issued Credentials sent in response MUST share the same Credential Format and Credential Dataset, but SHOULD contain different Cryptographic Data" | 3.3.2 | read.
- A4.3 Notification. "Support for this endpoint is OPTIONAL." and no guarantee a notification arrives | 11 | read.
- A4.4 Signed metadata and wallet trust. "the Wallet MUST establish trust in the signer of the metadata"; mechanisms are out of scope | 12.2.3 | read. Wallet attestation and key attestation are mechanisms for issuer trust in the wallet | 13.3 | read.
- A4.5 Client identifier prefixes (OpenID4VP). Values defined: pre-registered, redirect_uri, openid_federation, verifier_attestation, decentralized_identifier, x509_san_dns and x509_hash | SRC-OID4VP-1.0 (new) wallet metadata and 5.9.3 | read. "Requests using the redirect_uri Client Identifier Prefix cannot be signed" | 5.9.3 | read.
- A4.6 Query language. DCQL with credential queries, credential sets, claims queries and trusted authorities; "Verifiers MUST validate the VP Token" including holder binding, and "the VP Token MUST be rejected" if overall checks fail | 6 and 8.6 | read.
- A4.7 Response modes. direct_post and direct_post.jwt (encrypted responses) and the Digital Credentials API in an appendix | 8.2, 8.3, Appendix A | read.
- A4.8 Transaction data. "The transaction data mechanism enables a binding between the user's identification/authentication and the user's authorization" and a wallet that does not support it "MUST return an error" | 8.4 | read.
- A4.9 Consent assumption. "Wallets SHOULD obtain explicit, informed consent from the End-User before releasing any Verifiable Credential or Presentation to a Verifier" | 15.1 | read. The specification text is built around an end user; no passage addresses unattended machine-to-machine presentation.

### A5 HAIP 1.0 (final)
- A5.1 Scope and limits. HAIP "fulfils some, but not all, of the requirements to meet the "High" Level of Assurance (LoA) as defined in the eIDAS Regulation"; trust management is out of scope; "Ecosystems SHOULD clearly indicate which of these formats" are required | SRC-HAIP-1.0 (new) 1, 3.4, 4 | read.
- A5.2 Issuance security. Authorization code flow; FAPI 2.0 provisions; PKCE S256, PAR; "Sender-constrained access token: MUST support DPoP as defined in [RFC9449]" | HAIP 4 | read.
- A5.3 Wallet attestation privacy. "Wallet Attestations MUST NOT be reused across different Issuers." and "MUST NOT introduce a unique identifier specific to a single Wallet instance" | HAIP 4.4.1 | read.
- A5.4 Presentation. "For signed requests, the Verifier MUST use, and the Wallet MUST accept the Client Identifier Prefix x509_hash"; DCQL; response encryption with ECDH-ES on P-256 and A128GCM/A256GCM; Redirects use signed requests via `request_uri` and `direct_post.jwt`; the DC API flow uses `dc_api.jwt` | HAIP 5, 5.1, 5.2 | read.
- A5.5 Formats and status. SD-JWT VC and ISO mdoc; "Each Credential MUST have its own unique, unpredictable status list index"; X.509 key resolution mandatory for SD-JWT VC issuer keys | HAIP 6.1 | read.
- A5.6 Cryptography. ES256 (P-256, SHA-256) and SHA-256 must be supported by all | HAIP 7, 8 | read.
- A5.7 Pre-final references. HAIP names "SD-JWT-based Verifiable Credentials (SD-JWT VC) draft -13" and "Token Status List draft -14" as specifications that are not yet final | HAIP 9.4 | read.
- A5.8 Extension points left to ecosystems: which flows, which formats, signed issuer metadata or not, how a credential offer is delivered, which key and wallet attestation format, which X.509 profile | HAIP 9.3 | read.

### A6 Qualified electronic registered delivery
- A6.1 Legal frame. Data sent through a qualified service "shall enjoy the presumption of the integrity of the data, the sending of that data by the identified sender, its receipt by the identified addressee" | SRC-EIDAS-CONSOL Art 43(2) | read; requirements incl. sealing by "signature or an advanced electronic seal of a qualified trust service provider" | Art 44(1)(d) | read.
- A6.2 Standards in force. CIR 2025/1944 Annex I applies "ETSI EN 319 521 V1.1.1 (2019-02)" with adaptations; Annex II (interoperability) applies EN 319 522-1, -2, -3 (V1.2.1, 2024-01), -4-1 (V1.2.1), -4-2 and -4-3 (V1.1.1) | SRC-CIR-2025-1944 Annexes I and II | read. EN 319 521 itself was not read.
- A6.3 Architecture. EN 319 522-1 defines a black-box model, a 4-corner model and an extended model with interfaces ERDS MSI (submission), MERI (retrieval), RI (relay) and MEPI (push to the user agent); the common service interface covers "message routing, trust management, capability management, governance functions"; an ERDS "can rely on external, trusted parties for authentication" | SRC-ETSI-EN-319522-1 (new) 3.1 and 4 | read.
- A6.4 Directory component. "ERDS User directory: this component is used to translate the unique identification of a recipient ... into a delivery endpoint." | EN 319 522-1 4.2.1 | read.
- A6.5 AS4 binding. EN 319 522-4-1 "defines the binding of the ERD messages ... to the specific transmission protocol AS4"; "ERDS shall only use the push message exchange pattern."; "All AS4 messages exchanged between the ERDS shall be signed and encrypted by the sending ERDS."; encryption "AES-GCM128 shall be used"; "Signed Receipts shall be used" | SRC-ETSI-EN-319522-4-1 (new) 5.2, 5.3 | read. A second binding for registered electronic mail "points to a different document" (EN 319 532-3, not read) | clause 4 | read.
- A6.6 AS4 profile. The OASIS AS4 profile of ebMS 3.0 trims ebMS "into a more simplified and AS2-like specification" and defines ebHandler, Light Client and Minimal Client conformance profiles | SRC-OASIS-AS4 (new) abstract | read.
- A6.7 Discovery. Receiver identification is bound to OASIS BDXL and capability discovery to OASIS SMP; trust evaluation to a trusted list or a domain PKI | SRC-ETSI-EN-319522-4-3 (new) clause 4 | read.
- A6.8 Standards check against Council Annex 11. EN 319 522-4-1 encrypts messages between ERDS; Council Annex 11(2)(d) asks for "end-to-end encryption to guarantee confidentiality". The text read does not say whether message-level encryption between two providers satisfies that wording; not resolved in any source read.
- A6.9 Not read: EN 319 522-2 (semantic content), -3 (formats) and -4-2 (evidence and identification bindings) beyond their scope clauses; EN 319 532 (registered electronic mail).

### A7 Data space protocols: Eclipse DSP and DCP, Catena-X profile
- A7.1 DSP scope. DSP specifies how datasets are advertised via catalogs, how policies and agreements are expressed and negotiated, and how datasets are accessed using transfer process protocols; "This document does not apply to the Data Transfer Protocol." | SRC-DSP (new) scope.md | read.
- A7.2 DSP versions and HTTPS binding. Release 2025-1 (latest tag 2025-1-err2). A connector "MUST provide a version metadata endpoint" under `/.well-known/dspace-version` | common.protocol.md | read.
- A7.3 DCP purpose. DCP is an overlay to DSP for "conveying organizational identities and establishing trust in a way that preserves privacy"; it covers self-issued identity tokens, a presentation protocol and an issuance protocol | SRC-DCP README | read.
- A7.4 Machine-to-machine consent. "presentation protocols that rely on end-user (i.e., human) consent are not applicable" | SRC-DCP trust.model.md | read.
- A7.5 Profiles. Two profiles: `vc20-bssl/jwt` (VC Data Model 2.0, BitstringStatusList, JOSE enveloped proofs) and `vc11-sl2021/jwt` (VC Data Model 1.1, StatusList2021); "the same data model version and proof mechanism MUST be used for both credentials and presentations" | SRC-DCP dcp.profiles.md | read.
- A7.6 Identifiers and endpoints. Participant identifier "MUST be a DID"; the DID document carries a service entry of type `CredentialService`; the verifier queries the credential service with a presentation query message | SRC-DCP base.protocol.md; verifiable.presentation.protocol.md | read.
- A7.7 Catena-X profile. "A Participant Agent MUST use the DID as the Participant identifier."; transfer type profiles HttpData-PULL and AmazonS3-PUSH | SRC-CX-0018 2.1.1, 2.2 | read (preview).
- A7.8 Relation to EBW text. The proposal and Council text read mention neither DSP nor DCP; they require protocols for automatic interaction (A1.4). Any link between EBW and data space protocols is not stated in the sources read.

### A8 ISO/IEC 18013-5 and 18013-7 (not read)
- A8.1 Named as the proximity and API-mediated presentation standards in CIR 2024/2982 and CIR 2026/1731 (A2.1, A2.4); ISO mdoc is a credential format profiled by HAIP (A5.5); the ARF names it next to OpenID4VP (A2.10) | snippet.

### A9 Requirement set status (checked against `_requirements/`, 477 entries)
- A9.1 Existing entries cover the proposal's Article 6(1) topics at headline level (INT-002, INT-003, INT-008, INT-009; FUN-014 automated and manual interaction), the EUDI Wallet access certificate rules (TRU-032, -033, -043 to -046), and agent protocols (INT-021 to INT-029). INT-001 records OpenID4VCI 1.0 and OpenID4VP 1.0 only for the WE BUILD pilot.
- A9.2 Gaps found: the protocol clauses of CIR 2026/1731 and ETSI TS 119 472-2/-3 (signed issuer metadata, x509_hash, response encryption, physical presence rule), ERDS interoperability bindings (AS4, BDXL/SMP), the DCP homogeneity and identifier rules, and OID4VP transaction data. See `/tmp/cand/I4-trust-protocols-privacy.yml`.

## (B) NEUTRAL DECISION CRITERIA
[S] = stated or implied by a source; [D] = project driver, to be confirmed by stakeholders.
- B1 [S] Interoperability with EUDI Wallets (Art 6(1)(f), 5(1)(c); CIR 2026/1731): same issuance and presentation profiles on both sides.
- B2 [S] Support for automated interaction without manual intervention (Art 6(1)(d)) against protocol texts that assume an end user (A4.9, A7.4).
- B3 [S] Mandated or cited standards: what the law fixes today (ETSI TS 119 472-2/-3, ISO/IEC 18013-7 Annex C; EN 319 522 series) versus what the proposal leaves to implementing acts (A1.9, A1.11).
- B4 [S] Open, royalty-free standards for the delivery channel (Council Annex 11(2)(c)); openness of OpenID specifications and ETSI documents.
- B5 [S] Security profile for high assurance (HAIP, DPoP, signed requests, encrypted responses) and its stated limits (A5.1).
- B6 [S] Privacy properties of the protocol layer: unlinkable wallet attestations, unique status indices, minimum disclosure to mediating APIs (A3.8, A5.3, A5.5).
- B7 [S] Maturity of referenced drafts: SD-JWT VC and Token Status List were drafts when HAIP was published (A5.7).
- B8 [S] Dependence on operating system or browser features (Digital Credentials API, mediating API; A2.11, A3.7).
- B9 [S] Delivery interoperability across providers (4-corner model, AS4 push, signed receipts, directory and capability discovery; A6.3 to A6.7).
- B10 [S] Data space compatibility: DID-based identifiers, credential service endpoints, homogeneous credential profiles (A7.5, A7.6).
- B11 [S] Authentication of counterparties inside the protocol (access certificates, registration certificates; A2.6, A2.7, A3.4, A3.5).
- B12 [D] Number of protocol stacks a provider must implement, operate and test.
- B13 [D] Conformance and certification effort (conformance tests exist for OpenID4VCI/4VP per HAIP 10.1; none read for AS4 binding or DCP beyond the technology compatibility kit named in the DCP README).
- B14 [D] Version and change management: CIR 2026/1731 pins ETSI versions of March 2026; ETSI has already published a newer 119 472-2 (V1.3.1).
- B15 [D] Fit with legacy channels in B2B (EDI, AS4 access points, e-invoicing networks): no source read states a requirement.

## (C) OPTIONS: what the sources enable, restrict, leave open (no recommendation)

### Option (a) One EU-aligned profile stack
OpenID4VCI and OpenID4VP in the HAIP profile of ETSI TS 119 472-2/-3 for issuance and presentation, ISO mdoc paths where needed, and AS4-based qualified registered delivery per EN 319 522-4-1 and -4-3.
- Enables: direct interoperability with EUDI Wallets and EU relying parties (B1); the specifications are final and cited in force for the EUDI Wallet (A2.3, A2.4); conformance tests exist for the OpenID specs; delivery standards are already named in CIR 2025/1944 (A6.2).
- Restricts: the profile assumes an end user for consent and error handling (A4.9); the OS-dependent API-mediated flow is mandatory for cross-device (A3.7); HAIP excludes trust management and states it does not alone reach LoA high (A5.1); the business wallet's own implementing acts may differ from the EUDI Wallet profile (A1.9).
- Leaves open: unattended machine-to-machine presentation; how a business wallet is identified in the request (access certificate, registration certificate or other, A1.12); how EBW-to-EBW interaction (Art 6(1)(f)) differs from EBW-to-EUDI Wallet interaction.

### Option (b) EU stack plus data space overlay
Option (a) plus DSP and DCP (and ecosystem profiles such as Catena-X CX-0018) for catalogue, negotiation, transfer and machine identity.
- Enables: connector-to-connector automation with DID-based identity and machine consent (A7.1, A7.4, A7.6); multiple trust anchors (see RES-dec04); existing data space deployments (A7.7).
- Restricts: DCP profiles use W3C VC 1.1/2.0 with JOSE proofs and DIDs, not the SD-JWT VC and mdoc formats of the EU profile (A7.5 versus A5.5), so credentials may need to be issued twice or translated; DSP leaves authorisation semantics open (A7.2); no EBW source read refers to either protocol (A7.8).
- Leaves open: whether data space membership credentials can be issued by an EBW provider; how the wallet connector binds to the business wallet (concept `CON-WALLET-CONNECTOR`); how DSP/DCP and OID4VP flows share one holder key and one status mechanism.

### Option (c) Broader OpenID4VC profile set with an ecosystem profile registry
OpenID4VCI/4VP used with more options than HAIP allows (client identifier prefixes such as decentralized_identifier or openid_federation, DID-based verifiers), and a registry of supported profiles per ecosystem.
- Enables: reuse of the same protocol family for data spaces and agent use cases (A4.5, A4.6); fits ecosystems that already use DIDs (A7.6); HAIP itself allows ecosystems to choose extensions (A5.8).
- Restricts: departs from the EU profile where the profile fixes x509_hash and encrypted responses (A3.5, A3.6); each added prefix needs a trust mechanism and wallets must support the matching processing rules (A4.5); no EU legal text read endorses the additional options.
- Leaves open: how a counterparty learns which profile a business wallet supports (HAIP assumes "mechanisms in place" without defining them, HAIP 3.1); how profile negotiation affects LoA and certification.

## (D) OPEN QUESTIONS AND WHAT I COULD NOT READ
- D1 The Commission Annex and the implementing acts under Art 5(5), 6(5), 10(6) are not available; which protocol is "designated" for the delivery channel (Council Annex 11(2)(a)) is not known.
- D2 ISO/IEC 18013-5 and 18013-7 were not read; any statement about their content in this note is second-hand.
- D3 EN 319 521 V1.1.1, EN 319 522-2, -3 and -4-2 were not read beyond scope clauses; CEF eDelivery AS4 profiles and the OASIS BDXL/SMP specifications themselves were not read.
- D4 Whether message-level encryption between providers meets Council Annex 11(2)(d) "end-to-end" wording (A6.8).
- D5 How the business wallet is addressed in OpenID4VP (client identifier for a business wallet relying party) is not stated; the proposal speaks of European Business Wallet-relying parties (Art 6(1)(b)), and the access certificate regime of CIR 2024/2980 covers wallet relying parties of EUDI Wallets only.
- D6 W3C Digital Credentials API and IETF SD-JWT VC and Token Status List drafts were not read directly; HAIP names the draft versions (A5.7).
- D7 DCP was read at repository state of 2026-08-05; DSP at release 2025-1. Later releases were not checked.
- D8 Catena-X wallet requirements (CX-0149) were not read (stub page).

## (E) REQUIREMENT CANDIDATES FOUND
In `/tmp/cand/I4-trust-protocols-privacy.yml`: issuer-metadata-signed-with-access-certificate, presentation-request-certificate-hash-identifier, presentation-response-encrypted, pre-authorised-flow-physical-presence, access-certificate-validation-not-delegated, wallet-attestation-not-instance-identifying, mediating-api-discloses-types-only, transaction-data-carried-in-presentation, erds-evidence-archived, erds-relay-signed-and-encrypted, erds-relay-push-pattern, dcp-credential-homogeneity, dataspace-participant-identifier-did (and erds-capability-discovery-binding, listed under RES-dec04). The EUDI Wallet profile items are labelled as such; whether they apply to the business wallet is the DEC-07 question.
