---
title: "DEC-07 Protocols and interfaces"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 7
permalink: /architecture/decisions/dec-07/
description: "Which issuance, presentation, data space and registered delivery protocols must a business wallet implement, and how do they fit together? Facts from the sources, decision criteria, three options and the conditions under which each holds."
keywords: [OpenID4VCI, OpenID4VP, HAIP, ETSI TS 119 472, ISO mdoc, AS4, ERDS, registered delivery, Eclipse DSP, Eclipse DCP, Catena-X, protocols, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-07 Protocols and interfaces

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. The Commission Annex of the proposal is not in the copy read. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

Which issuance, presentation, data space and delivery protocols must a business wallet implement, and how do they fit together? Four groups are in play: protocols to issue attestations to the wallet, protocols to present them to relying parties and to other wallets, protocols for qualified electronic registered delivery, and protocols for data spaces. Agent protocols are treated in [DEC-10]({{ '/architecture/decisions/dec-10/' | relative_url }}), and credential formats in [DEC-01]({{ '/architecture/decisions/dec-01/' | relative_url }}); neither is repeated here. The decision touches clusters K08 (protocols and interfaces) and K12 (registered delivery and notifications).

## What the requirement set says

The requirements that shape the choice of protocols:

{% include cluster-drivers.html cluster="K08" %}

{% include cluster-drivers.html cluster="K12" %}

Gaps in the set (facts found in the research, not yet written as requirements): the protocol clauses of CIR 2026/1731 and of ETSI TS 119 472-2 and -3 (signed issuer metadata, the x509_hash client identifier prefix, encrypted responses, the physical presence rule for the Pre-Authorised Code Flow), the interoperability bindings for registered delivery (AS4, BDXL and SMP), the DCP rules on credential homogeneity and participant identifiers, and OpenID4VP transaction data. Existing entries cover the Article 6(1) topics only at headline level; INT-001 records OpenID4VCI 1.0 and OpenID4VP 1.0 only for the WE BUILD pilot.

## Facts from the sources

Each fact has a source. Read states are those of the source register: items marked <span class="vtag v-todo">to verify</span> were not read in the original or were read only as a reference in another document.

**What the EBW texts ask for.**
- Providers shall ensure support for "common protocols and interfaces" for issuance, request and validation, sharing and presenting, automatic interaction, onboarding, wallet-to-wallet interaction, relying-party authentication, wallet validation, registered delivery, digital addresses, wallet unit attestations and critical assets (SRC-EBW-PROPOSAL Article 6(1)(a) to (l)).
- Issuance covers owner identification data, qualified and non-qualified electronic attestations of attributes and certificates (Article 6(1)(a)). Relying parties request and validate owner identification data and attestations (Article 6(1)(b)); selectively disclosed data is shared and presented (Article 6(1)(c)).
- Protocols must allow interaction "automatically without manual intervention or through direct user action" (Article 6(1)(d)), between European Business Wallets and between them and European Digital Identity Wallets (Article 6(1)(f)), and let relying parties verify the authenticity and validity of a wallet "where the verification ... is required" (Article 6(1)(h)). Owners can request and share in a secured way between both wallet types and with relying parties (Article 5(1)(c)).
- Standards are left to implementing acts: the Commission "shall, by means of implementing acts, establish a list of reference standards and where necessary, establish specifications and procedures for the technical features" (Article 6(5)); the same holds for core functionalities (Article 5(5)).
- Registered delivery: protocols for the qualified service "including an interface to the European Digital Directory" and "at least one unique digital address" per owner (Article 6(1)(i), (j)). Providers must offer the service as a standalone service to users of European Digital Identity Wallets (Article 5(3)). The Directory has "a machine-readable interface exposed through an API for automated system-to-system communication" and a portal (Article 10(1)); the articles read specify neither protocol nor API, and implementing acts set the standards for digital addresses (Article 10(6)).
- The Council text (SRC-COUNCIL-ST-9684-26, Annex point 11) requires wallets to "integrate and support the use of a specific qualified electronic registered delivery service in accordance with Articles 43 and 44". The Commission shall "designate the protocol". The service must rest on "open, publicly available and royalty-free standards", provide "end-to-end encryption" and have "continuous availability, redundancy and fallback mechanisms"; interoperability "shall be mandatory".
- The Council Annex adds interface duties for wallet units: they authorise requests and, where applicable, authenticate those made through European Digital Identity Wallet relying-party access certificates or wallet unit attestations, and authentication of the relying party is required where attestations are intended for a restricted audience (Annex 13(1)); they authenticate relying parties when requesting issuance (Annex 14(1)); presentation protocols follow "the standards defined in the implementing acts" (Annex 15(1)); owner identification data is cryptographically bound to the wallet unit (Annex 16(2)); attestation providers identify themselves to wallet units (Annex 17(2)). Owner identification data is issued in a format compliant with a standard listed in Annex II of Commission Implementing Regulation (EU) 2024/2979 (Council text, Article 9(3)).

**What is already fixed for the EUDI Wallet.**
- CIR 2024/2982 Article 5(1) and its Annex originally named two standards for presentation, ISO/IEC 18013-5:2021 and ISO/IEC TS 18013-7:2024 (SRC-CIR-2024-2982). CIR 2026/1731 of 15 July 2026 deletes that Annex and replaces it with Annex I (issuance) and Annex II (presentation) (SRC-CIR-2026-1731 Article 4).
- New Annex I applies ETSI TS 119 472-3 V1.1.1 (2026-03) with adaptations. New Annex II applies Annex C of ISO/IEC 18013-7:2025 and clauses 4.1, 4.2, 5 and 6 of ETSI TS 119 472-2 V1.2.1 (2026-03) with adaptations. TS 119 472-2 has two profiles: ISO/IEC mdoc (ISO/IEC 18013-5 for non-API-mediated, Annex C of ISO/IEC 18013-7 for API-mediated transmission) and OpenID4VC-HAIP for both mechanisms (SRC-ETSI-119472-2, clause 1). The ARF states that "at least two different protocols can be used within the EUDI Wallet ecosystem", ISO/IEC 18013-5 and OpenID4VP (SRC-ARF-TRUST 6.6.3.2).
- ISO/IEC 18013-5 and 18013-7 are paywalled and were not read; statements about them come from CIR 2024/2982, CIR 2026/1731, ETSI TS 119 472-2 and HAIP <span class="vtag v-todo">to verify</span>.
- Wallets request issuance only from parties with "an authentic and valid wallet-relying party access certificate" (CIR 2024/2982 Article 4(2)). The wallet validates the registration certificate received in a request before presenting any requested attestation for approval, and warns before disclosure when more is requested than registered (CIR 2026/1731 Annex XII, WRP-VALIDATION-01, WRP-OVERASKING-01, -02). Access certificate checks are not delegated to an operating system browser or another intermediary application (Article 4(2)(a), amending Article 3(1)); Article 3(4) on the registration certificate applies from 11 August 2028 (Article 4(5)).
- The wallet supports a mediating API for both protocols; a note excuses non-conformity where the operating system or browser does not provide the features (EAAP-API-GEN-01). Privacy rules in the same regulation: unlinkability where attestations need no identification (Article 3(10)), selective disclosure (Article 5(4)), erasure requests and reports to data protection authorities (Articles 6 and 7).
- Scope caveat: these texts regulate the EUDI Wallet. Whether they apply to the business wallet is the question of this decision. The access certificate regime of CIR 2024/2980 covers wallet relying parties of EUDI Wallets only; how a business wallet relying party is identified in a request is not stated in the sources read.

**Issuance and presentation profiles (ETSI, OpenID, HAIP).**
- ETSI TS 119 472-3: the wallet and the issuer implement the profile of OpenID4VCI specified by HAIP clause 4. The wallet supports the Authorisation Code Flow and the Pre-Authorised Code Flow; providers implement at least one; PID Providers using the Pre-Authorised Code Flow perform user authorisation with the physical presence. The custom URL scheme `eu-eaa-offer://` invokes the wallet. Issuer metadata is signed with the access certificate of the provider, and the registration certificate is carried in `issuer_info` (SRC-ETSI-119472-3, GEN-REQ-4.1-01 to -06, ISS-MDATA-4.2.1-01, -02).
- ETSI TS 119 472-2: the authorization request uses the client identifier prefix `x509_hash`; the request object carries `verifier_info` with the registration certificate; the wallet encrypts the authorization response; cross-device flow uses only the API-mediated mechanism, with `eu-eaap://` as custom URL scheme; the wallet by default discloses only the presence of stored attestation types to the mediating API, not attributes or values. A note says the API-mediated support could change with the evolution of the W3C Digital Credentials API. The documents also cover X.509 attribute certificate attestations and JSON-LD W3C VC presentation (partly read) (SRC-ETSI-119472-2, OIDFVP-HAIP-COMMON-REQ-01, -RESP-01, -SUPPORT-03, -ADD-API-01).
- OpenID4VCI 1.0 (final, 16 September 2025): Authorization Code or Pre-Authorized Code, wallet-initiated or issuer-initiated, same-device or cross-device offer, immediate or deferred issuance; batch credentials share format and dataset but should carry different cryptographic data; the notification endpoint is optional; for signed metadata the wallet must establish trust in the signer, and the mechanisms are out of scope (SRC-OID4VCI-1.0 3.3.2, 3.3.3, 11, 12.2.3, 13.3).
- OpenID4VP 1.0 (final, 9 July 2025): defined client identifier prefixes are pre-registered, redirect_uri, openid_federation, verifier_attestation, decentralized_identifier, x509_san_dns and x509_hash; requests with redirect_uri cannot be signed; the query language is DCQL; verifiers must validate the VP Token and reject it if checks fail; response modes are direct_post, direct_post.jwt and the Digital Credentials API; transaction data binds user authentication to user authorization, and a wallet that does not support it must return an error. The specification says wallets should obtain explicit, informed consent from the end user; it is built around an end user, and no passage read addresses unattended machine-to-machine presentation (SRC-OID4VP-1.0 5.9.3, 6, 8.2 to 8.4, 8.6, 15.1).
- HAIP 1.0 (final, 24 December 2025): fulfils "some, but not all" of the requirements for level of assurance high, and trust management is out of scope. It requires FAPI 2.0 provisions, PKCE S256, PAR and DPoP for issuance; wallet attestations must not be reused across issuers and must not carry an identifier specific to one wallet instance; signed requests use `x509_hash`; responses are encrypted (ECDH-ES on P-256); formats are SD-JWT VC and ISO mdoc, each credential with its own unique, unpredictable status list index; ES256 and SHA-256 are mandatory. HAIP names SD-JWT VC draft -13 and Token Status List draft -14 as not yet final, and leaves to ecosystems the choice of flows, formats, signed issuer metadata, offer delivery, key and wallet attestation format and X.509 profile (SRC-HAIP-1.0 sections 1, 3.4, 4, 4.4.1, 5, 6.1, 7, 8, 9.3, 9.4).
- ETSI has published a V1.3.1 of TS 119 472-2 on its server; CIR 2026/1731 cites V1.2.1, and V1.3.1 was not used. The W3C Digital Credentials API and the IETF drafts for SD-JWT VC and Token Status List were not read directly <span class="vtag v-todo">to verify</span>.

**Qualified electronic registered delivery.**
- Legal frame: data sent through a qualified service enjoys the presumption of integrity, of sending by the identified sender and of receipt by the identified addressee (SRC-EIDAS-CONSOL Article 43(2)); requirements include sealing by a qualified trust service provider (Article 44(1)(d)).
- CIR 2025/1944 applies ETSI EN 319 521 V1.1.1 (2019-02) with adaptations in Annex I, and EN 319 522-1, -2, -3 (V1.2.1), -4-1 (V1.2.1), -4-2 and -4-3 (V1.1.1) for interoperability in Annex II (SRC-CIR-2025-1944). EN 319 521 itself was not read <span class="vtag v-todo">to verify</span>.
- EN 319 522-1 defines a black-box model, a 4-corner model and an extended model with the interfaces ERDS MSI (submission), MERI (retrieval), RI (relay) and MEPI (push to the user agent); its common service interface covers message routing, trust management, capability management and governance functions; an ERDS can rely on external trusted parties for authentication. The user directory component translates the unique identification of a recipient into a delivery endpoint (SRC-ETSI-EN-319522-1 clauses 3.1, 4, 4.2.1).
- EN 319 522-4-1 binds the messages to AS4: only the push message exchange pattern; all AS4 messages between providers are signed and encrypted by the sending provider; AES-GCM128 encryption; signed receipts. A second binding, for registered electronic mail, points to EN 319 532-3, which was not read <span class="vtag v-todo">to verify</span> (SRC-ETSI-EN-319522-4-1 clauses 4, 5.2, 5.3). The OASIS AS4 profile of ebMS 3.0 simplifies ebMS and defines the ebHandler, Light Client and Minimal Client conformance profiles (SRC-OASIS-AS4).
- EN 319 522-4-3 binds receiver identification to OASIS BDXL and capability discovery to OASIS SMP, with trust evaluation by a trusted list or a domain PKI (SRC-ETSI-EN-319522-4-3 clause 4). The BDXL and SMP specifications and the CEF eDelivery AS4 profiles were not read <span class="vtag v-todo">to verify</span>.
- Council Annex 11(2)(d) asks for "end-to-end encryption"; EN 319 522-4-1 encrypts messages between providers. The text read does not say whether message-level encryption between two providers satisfies that wording, and no source read resolves it.
- Beyond their scope clauses, EN 319 522-2, -3 and -4-2 and EN 319 532 were not read <span class="vtag v-todo">to verify</span>.

**Data space protocols.**
- Eclipse Dataspace Protocol (DSP, release 2025-1) specifies how datasets are advertised via catalogs, how policies and agreements are expressed and negotiated, and how datasets are accessed through transfer process protocols; it does not apply to the Data Transfer Protocol. A connector must provide a version metadata endpoint under `/.well-known/dspace-version` (SRC-DSP).
- Eclipse Decentralized Claims Protocol (DCP) is an overlay to DSP for conveying organisational identities and establishing trust while preserving privacy: self-issued identity tokens, a presentation protocol and an issuance protocol. "Presentation protocols that rely on end-user (i.e., human) consent are not applicable." Two profiles exist, `vc20-bssl/jwt` (VC Data Model 2.0, Bitstring Status List, JOSE enveloped proofs) and `vc11-sl2021/jwt` (VC Data Model 1.1, StatusList2021), and the same data model version and proof mechanism must be used for credentials and presentations. The participant identifier must be a DID; the DID document carries a `CredentialService` entry (SRC-DCP). DCP was read at repository state of 2026-08-05, DSP at release 2025-1; later releases were not checked.
- The Catena-X profile CX-0018 (preview) requires the DID as participant identifier and defines the transfer type profiles HttpData-PULL and AmazonS3-PUSH (SRC-CX-0018 2.1.1, 2.2). The Catena-X wallet requirements (CX-0149) were not read, the page being a stub <span class="vtag v-todo">to verify</span>.
- The EBW proposal and the Council text read mention neither DSP nor DCP. Any link between the EBW and data space protocols is not stated in the sources read.

**What the EBW texts say nothing about.** The texts read do not name a protocol for issuance, presentation or registered delivery (they defer to implementing acts), do not state which protocol is designated for the delivery channel, do not say how a business wallet is addressed as a relying party in OpenID4VP, and do not mention data space protocols, EDI, AS4 access points or e-invoicing networks.

## Decision criteria

Criteria marked **source** are stated or implied by a source; **driver** means a project driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| P1 | Interoperability with EUDI Wallets: same issuance and presentation profiles on both sides | source: Article 6(1)(f), 5(1)(c); CIR 2026/1731 |
| P2 | Automated interaction without manual intervention, against protocol texts that assume an end user | source: Article 6(1)(d); OpenID4VP 15.1; DCP trust model |
| P3 | Standards fixed in law today against standards left to implementing acts | source: CIR 2026/1731, CIR 2025/1944; Article 6(5); Council Annex 11 |
| P4 | Open, royalty-free standards for the delivery channel; openness of the specifications | source: Council Annex 11(2)(c) |
| P5 | Security profile for high assurance and its stated limits | source: HAIP 1, 4, 5 |
| P6 | Privacy of the protocol layer: unlinkable wallet attestations, unique status indices, minimum disclosure to mediating APIs | source: HAIP 4.4.1, 6.1; TS 119 472-2 |
| P7 | Maturity of referenced drafts | source: HAIP 9.4 |
| P8 | Dependence on operating system or browser features | source: EAAP-API-GEN-01; TS 119 472-2 |
| P9 | Delivery interoperability across providers: 4-corner model, AS4 push, signed receipts, directory and capability discovery | source: EN 319 522 series; CIR 2025/1944 |
| P10 | Data space compatibility: DID-based identifiers, credential service endpoints, homogeneous credential profiles | source: DCP, CX-0018 |
| P11 | Authentication of counterparties inside the protocol: access and registration certificates | source: CIR 2026/1731; TS 119 472-2, -3; Council Annex 13 to 17 |
| P12 | Number of protocol stacks a provider must implement, operate and test | driver |
| P13 | Conformance and certification effort | driver; conformance tests exist for OpenID4VCI and OpenID4VP (HAIP 10.1); none read for the AS4 binding, and for DCP only the technology compatibility kit named in its README |
| P14 | Version and change management | driver; CIR 2026/1731 pins ETSI versions of March 2026 and a newer TS 119 472-2 exists |
| P15 | Fit with legacy B2B channels (EDI, AS4 access points, e-invoicing networks) | driver; no source read states a requirement |

## Options

### (a) One EU-aligned profile stack

OpenID4VCI and OpenID4VP in the HAIP profile of ETSI TS 119 472-2 and -3 for issuance and presentation, ISO mdoc paths where needed, and AS4-based qualified registered delivery per EN 319 522-4-1 and -4-3.

**Enables.** Direct interoperability with EUDI Wallets and EU relying parties (P1); specifications that are final and cited in force for the EUDI Wallet (CIR 2026/1731 Annexes XI and XII); conformance tests for the OpenID specifications; delivery standards already named in CIR 2025/1944.

**Restricts.** The profile assumes an end user for consent and error handling (OpenID4VP 15.1); the operating-system-dependent API-mediated flow is mandatory for cross-device (TS 119 472-2); HAIP excludes trust management and does not alone reach level of assurance high; the implementing acts for the business wallet may differ from the EUDI Wallet profile (Article 6(5)).

**Leaves open.** Unattended machine-to-machine presentation; how a business wallet is identified in a request (access certificate, registration certificate or other); how interaction between two business wallets (Article 6(1)(f)) differs from interaction with an EUDI Wallet.

### (b) EU stack plus data space overlay

Option (a) plus DSP and DCP, and ecosystem profiles such as Catena-X CX-0018, for catalogue, negotiation, transfer and machine identity.

**Enables.** Connector-to-connector automation with DID-based identity and machine consent (DSP scope, DCP trust model); multiple trust anchors (see the research note on trust, RES-dec04); existing data space deployments (CX-0018).

**Restricts.** DCP profiles use W3C VC 1.1 or 2.0 with JOSE proofs and DIDs, not the SD-JWT VC and mdoc formats of the EU profile, so credentials may need to be issued twice or translated (formats are treated in [DEC-01]({{ '/architecture/decisions/dec-01/' | relative_url }})); DSP leaves authorisation semantics open; no EBW source read refers to either protocol.

**Leaves open.** Whether data space membership credentials can be issued by an EBW provider; how the wallet connector binds to the business wallet (concept CON-WALLET-CONNECTOR); how DSP, DCP and OpenID4VP flows share one holder key and one status mechanism.

### (c) Broader OpenID4VC profile set with an ecosystem profile registry

OpenID4VCI and OpenID4VP used with more options than HAIP allows (client identifier prefixes such as decentralized_identifier or openid_federation, DID-based verifiers), and a registry of supported profiles per ecosystem.

**Enables.** Reuse of one protocol family for data spaces and agent use cases (agent protocols: [DEC-10]({{ '/architecture/decisions/dec-10/' | relative_url }})); a fit with ecosystems that already use DIDs; HAIP itself leaves extension points to ecosystems (HAIP 9.3).

**Restricts.** Departs from the EU profile where it fixes `x509_hash` and encrypted responses; each added prefix needs a trust mechanism and matching processing rules in wallets (OpenID4VP 5.9.3); no EU legal text read endorses the additional options.

**Leaves open.** How a counterparty learns which profile a business wallet supports (HAIP assumes mechanisms in place without defining them, HAIP 3.1); how profile negotiation affects level of assurance and certification.

Registered delivery is carried by the AS4 binding in options (a) and (b). In option (c) the sources read give no alternative delivery protocol; the choice stays with the protocol the Commission designates (Council Annex 11).

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | (a) EU profile stack | (b) plus data space overlay | (c) broader OpenID4VC set |
|---|---|---|---|
| P1 EUDI Wallet interoperability | Same profiles as the EUDI Wallet | As (a) for the EU part | Departs where the EU profile is fixed |
| P2 Automated interaction | Profile assumes an end user; unattended use not stated | DCP states machine consent for presentation | Not stated |
| P3 Standards in law today | Cited in force for the EUDI Wallet; delivery standards named in CIR 2025/1944 | DSP and DCP not named in any EBW text | No EU legal text endorses the extra options |
| P5 Security for high assurance | HAIP profile with DPoP, signed requests, encrypted responses; does not alone reach level high | DCP security not assessed in the sources read | Each added prefix needs its own trust mechanism |
| P6 Privacy of the protocol layer | Rules on wallet attestations, status indices and mediating API disclosure | DCP privacy statement; combination with the EU rules not stated | Not stated |
| P7 Maturity | SD-JWT VC and Token Status List were drafts when HAIP was published | Profiles on W3C VC 1.1 and 2.0; DCP read at a repository state | Not stated |
| P8 OS and browser dependence | API-mediated flow mandatory for cross-device | Not stated | Not stated |
| P9 Delivery interoperability | 4-corner model, AS4 push, signed receipts, BDXL and SMP | As (a) | Not stated |
| P10 Data space compatibility | Not covered | DID identifier, credential service, homogeneous profiles | DID-based verifiers possible |
| P11 Counterparty authentication | Access and registration certificates; business wallet case not stated | As (a) plus DID-based identity | New prefixes need trust mechanisms |
| P12 Number of stacks | OpenID family, ISO mdoc paths and AS4 | Adds DSP and DCP | One protocol family; profile registry added |
| P13 Conformance effort | OpenID conformance tests exist; none read for AS4 | None read beyond the DCP compatibility kit | Not stated |
| P14 Change management | Pinned ETSI versions; a newer TS 119 472-2 exists | DCP and DSP releases not checked beyond those read | Not stated |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Four observations follow from the facts.

1. **For issuance and presentation, option (a) is the reference point.** It is the only combination that the law cites in force for the EUDI Wallet, and the proposal ties the business wallet to the EUDI Wallet in Articles 5(1)(c) and 6(1)(f). The profile assumes an end user, and the sources read do not say how a business wallet is identified as a relying party, so (a) is a floor for interoperability, not a complete answer for automated interaction.
2. **Automated interaction is the unresolved part.** Article 6(1)(d) asks for it, OpenID4VP and the ETSI profiles are written around an end user, and DCP states that human-consent presentation does not apply. The sources read do not connect the two. Option (b) addresses machine identity for data spaces but brings W3C VC profiles that differ from the EU formats.
3. **Registered delivery follows a separate path.** The standards in CIR 2025/1944 point to AS4 with BDXL and SMP discovery. The protocol the Commission designates under Council Annex 11 is not known, and the end-to-end encryption wording is not resolved.
4. **Option (c) departs from the profile the law cites.** It may fit ecosystems that use DIDs, but no source read endorses it, and it would need a stated trust mechanism per added prefix.

**Conditions under which this reading holds.** The implementing acts under Articles 5(5) and 6(5) adopt the EUDI Wallet profiles for the business wallet or a close variant; the Commission designates a delivery protocol compatible with the EN 319 522 series; the HAIP and ETSI profiles do not change materially before application.

**What would change it.** The Commission Annex and the implementing acts under Articles 5(5), 6(5) and 10(6); the designated delivery protocol; a statement in a source on how a business wallet relying party is identified in OpenID4VP; an EBW text or implementing act naming a data space protocol; the outcome of the Council meeting of 9 June 2026; adoption of a newer TS 119 472-2 in a Commission act.

## Gaps and next steps

- Obtain the Commission Annex of COM(2025) 838 and the outcome of the Council meeting of 9 June 2026; then re-check Articles 5, 6 and 10 and Council Annex 11.
- Read ISO/IEC 18013-5 and 18013-7 through an authorised copy; read EN 319 521, EN 319 522-2, -3 and -4-2, EN 319 532, the CEF eDelivery AS4 profiles and the OASIS BDXL and SMP specifications; read the W3C Digital Credentials API and the IETF drafts directly; read Catena-X CX-0149 and later DSP and DCP releases.
- Clarify whether message-level encryption between providers meets the "end-to-end" wording of Council Annex 11(2)(d).
- Clarify how a business wallet relying party is addressed in OpenID4VP, given that CIR 2024/2980 covers wallet relying parties of EUDI Wallets only.
- Write the missing requirements (see "What the requirement set says") and review them with a named reviewer.
- Confirm the drivers P12 to P15 with stakeholders; they are assumptions until then.

## References

SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26, SRC-CIR-2024-2982, SRC-CIR-2026-1731, SRC-CIR-2025-1944, SRC-ARF-TRUST, SRC-ETSI-119472-2, SRC-ETSI-119472-3, SRC-OID4VCI-1.0, SRC-OID4VP-1.0, SRC-HAIP-1.0, SRC-EIDAS-CONSOL, SRC-ETSI-EN-319522-1, SRC-ETSI-EN-319522-4-1, SRC-ETSI-EN-319522-4-3, SRC-OASIS-AS4, SRC-DSP, SRC-DCP, SRC-CX-0018. Full entries with version, date and URL are in the source register.
