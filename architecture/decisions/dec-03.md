---
title: "DEC-03 Key custody and wallet architecture"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 3
permalink: /architecture/decisions/dec-03/
description: "Where do the keys of an organisation live: on a device it holds, in a back-end run by the wallet provider, in a hardware security module it runs itself, or with a qualified trust service provider that seals and signs remotely? Facts from the sources, decision criteria, four options and the conditions under which each holds."
keywords: [key custody, wallet secure cryptographic device, WSCD, WSCA, hardware security module, remote sealing, remote signing, wallet unit attestation, QTSP, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-03 Key custody and wallet architecture

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838) with an Annex; the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. The EUDI Wallet rules (eIDAS Article 5a, Regulations 2024/2979 and 2024/2981, the ARF) concern a wallet of a natural person and bind the EBW only where the EBW text refers to them. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

Where do the keys of an organisation live, and what does that mean for control, assurance and exit? Four placements are conceivable, and they can be combined:

- **(1)** on a **device the owner holds** (local or external secure device, for example a smart card, token or secure element);
- **(2)** in a **back-end operated by the wallet provider** (the cryptographic device as a remote hardware security module, HSM);
- **(3)** in an **HSM operated by the organisation itself** (on premises or in its own cloud account);
- **(4)** with a **qualified trust service provider (QTSP)** that creates seals and signatures remotely on behalf of the owner, orchestrated by the wallet.

The decision touches cluster K04 (wallet unit attestation and key protection) and, through it, assurance, revocation and exit. Wallet unit lifecycle and status are treated in DEC-06; this page repeats from it only the points that bear on keys.

## What the requirement set says

K04 has 60 tagged requirements, 18 of them with priority P1. The P1 requirements that drive this decision are:

{% include cluster-drivers.html cluster="K04" %}

Gaps in the set (facts found in the research, not yet written as requirements): the requirement that the back-end uses a wallet secure cryptographic application and device (Annex point 3(1)), the Council deletion of the assurance-level clauses for critical operations, the provider's conformity regime without a device certificate (Article 11), and the choice between local, external and remote qualified devices (Annex point 8). One register item is stale: EBW-TRU-029 cites Regulation 2024/2979 Article 3(2), which Regulation 2026/1731 Article 2(1) deletes; it needs review.

## Facts from the sources

Each fact has a source and was read in the original text unless marked. "Commission proposal" is COM(2025) 838, "Commission Annex" is its Annex (Cellar copy), "Council text" is ST 9684/26, "in-force law" is eIDAS as consolidated and the implementing regulations named.

**What the EBW texts define and require.**
- Commission proposal, Article 3(25): the wallet unit is "a unique configuration" provided to a specific owner that includes front-end, back-end, wallet secure cryptographic applications (WSCA) and wallet secure cryptographic devices (WSCD). The WSCD is "a tamper-resistant device that provides an environment that is linked to and used by the wallet secure cryptographic application" (Article 3(29)). The back-end is "the server-side components, including software, services, and infrastructure" (Article 3(43)).
- Council text: Article 3(25) lists only front-end and back-end; Article 3(26) lists front-end and back-end; Article 3(28) and (29) are marked "deleted".
- Commission Annex point 3(1) and Council Annex point 3(1), same wording: the back-end "shall use at least one Wallet secure cryptographic application and Wallets secure cryptographic device to manage critical assets".
- Commission proposal Article 6(1)(l) and Commission Annex points 3(3), 4(1)(b) and 4(1)(g): critical operations meet the requirements for electronic identification means at assurance level substantial. Council text: Annex 3(3), 4(1)(b) and 4(1)(g) read "deleted", Article 6(1)(l) is absent from the Council Article 6(1) list, and Council Annex point 4(1) addresses "secure cryptographic applications and devices" jointly.
- Commission proposal Article 6(1)(k): the unit attestation contains "public keys and corresponding private keys protected by a wallet secure cryptographic device". Council text Article 6(1)(k) is shortened; Council Annex point 5(1) keeps the key-protection wording.
- Onboarding: Commission proposal Article 6(1)(e) names assurance "substantial" or "high" for the representative's eID; Council text names "high". Council Annex point 1 keeps "substantial" for user access to the unit, and access is granted only after successful authentication of the user.
- Signing and sealing: the core function is to "sign by means of qualified electronic signatures and seal by means of qualified electronic seals, as applicable" (Commission proposal Article 5(1)(d)). Commission Annex point 8 and Council Annex point 8 (same wording): certificates are linked to qualified devices "either local, external, or remote" in relation to the unit, and the solution can interface with "local, external, or remotely managed" devices.
- Signature creation applications may be provided by the wallet provider, a trust service provider or a relying party; they may be integrated into or external to the back-end, and if integrated and relying on a remote qualified device they "shall support the application programming interface" set out in implementing acts (Council Annex point 9(1), 9(3); Commission Annex point 9). No named standard appears in the EBW texts.
- The unit presents its unit attestation "to European Business Wallet relying parties or European Business Wallet units that request it" (Annex point 13(4), Council wording; the Commission Annex has the same point).
- Conformity of the provider: Commission proposal Article 11(2)(e) asks for a declaration of conformity, and qualified trust service providers are not reviewed (Article 11(3)). Council text Article 11(2aa) asks applicants to demonstrate conformity with Articles 5, 6, 7 and the Annex "through a self-assessment report", with a risk assessment and reuse of valid eIDAS reports. No EBW text requires a certificate for the WSCA, the WSCD or the solution.
- Security duties: Article 19a of Regulation (EU) 910/2014 (not for qualified trust service providers), NIS2 and supplier standards (Commission proposal Article 7(3) to (5)). The Council text adds an update of the self-assessment every 24 months, or immediately after a significant incident or a substantial change to "cryptographic components" (Article 7(6b)).
- Providers must be established in the Union, have their principal place of business and main operations there, and "shall not be subject to control by a third country or by a third-country entity" (Commission proposal Article 7(2)).
- Exit: owners can export data on termination of service or revocation of the provider's notification (Article 5(1)(l)); the provider ensures "transfer or deletion" of owner data on instruction (Article 7(6)(f)). The Council text adds import for "data portability across European Business Wallet providers" (point (la)) and Annex point 10 "secure export, import and portability" "in at least an open format"; the Commission Annex point 10 ties portability to assurance level substantial. None of these texts says whether private keys can be exported or must be re-created.
- Logs are accessible to the provider "where it is necessary for the provision of European Business Wallets services" (Council Annex point 7(5)). Neither EBW text contains the explicit prior-consent condition that Regulation 2024/2979 Article 9(5) sets for EUDI Wallet logs.
- Wallet validity can be revoked where the provider is not on the list (Commission proposal Article 6(2)(f)); supervisors can revoke the inclusion of a non-compliant provider (Article 13(5)(k)) and implementing acts may suspend it (Article 13(12)). The texts do not say how keys held by that provider pass to another provider.
- Absence: the words custody, hosted, HSM and hardware security module do not occur in the proposal or the Council text (searched). No provision states where the keys of an owner must be held.

**Signatory, seal creator and remote qualified devices (in-force law, eIDAS).**
- A signatory is "a natural person who creates an electronic signature"; the creator of a seal is "a legal person who creates an electronic seal" (Article 3(9), 3(24)).
- A remote qualified creation device is managed by a qualified trust service provider "on behalf of a signatory", and for seals "on behalf of a seal creator" (Article 3(23a), 3(23b)). Creation data are generated, managed or duplicated for back-up "only on behalf of the signatory, at the request of the signatory, and by a qualified trust service provider" (Article 29(1a)); Article 39a applies Article 29a to seals.
- Back-up copies are allowed only at the same security level and in the minimum number needed for continuity (Article 29a(1)(b)). The provider complies with the certification report of the specific device (Article 29a(1)(c)); certification and cross-border recognition are in Articles 30 and 24a(2) and (3).
- Advanced seals use data that the creator "can, with a high level of confidence under its control, use" (Article 36(1)(c)). Qualified seal certificates indicate where the creation data are in a qualified device (Annex III, point (j)). EUDI Wallets support qualified signing and sealing by means of qualified devices (Article 5a(5)(a)(xi)) and are provided at assurance level high (Article 5a(11)).
- Commission Implementing Decision 2016/650 lists ISO/IEC 15408, ISO/IEC 18045 and EN 419 211 for devices in a user-managed environment; for devices managed by a QTSP it requires comparable security levels, notified to the Commission, until a list of standards exists.

**Standards for remote signing and sealing.**
- ETSI TS 119 431-1 (read) covers providers of a remote qualified device: "The service consists of a server signing application and a QSCD / SCDev." It incorporates EN 419 241-1 by reference and applies the requirements "mutatis mutandis to electronic seals" (clauses 1 and 4.1). It has three policies (lightweight, normalised, EU policy v2, clause 4.3.2 and Annex A). Under the EU policy v2 the signing key "shall be generated in a QSCD"; the signature activation module "should be certified to be conformant to EN 419241-2"; identity-based activation ends "at most 30 minutes after the end of the identity verification process".
- For a legal-person signer, identity proofing follows EN 419241-1 at level substantial or higher, and activation by identity needs "an explicit action (not just a checkbox)" of the identified natural person who "is allowed to sign in the name of the legal person" (SIG-6.3.1-16, LNK-6.2.2-02B); the EU policy v2 applies control in place of sole control for a legal person (SIG-A.6-07A).
- Key life cycle: "If the public key certificate is revoked, the corresponding signing key shall be destroyed"; the provider destroys a key when the signer requests it; back-up "shall not exceed the minimum needed" (DEL-6.3.2-01, -02, GEN-6.3.3-04). The provider should check that the certificate is valid before using the key (SIG-6.3.1-08).
- CSC API v2.0.0.2 (read in part) covers architectures where the key is "in the cloud"; architectures where the key is in the signer's hand are not covered as a particular case. It supports sole control levels SCAL1 and SCAL2; for SCAL2 the activation data are linked to the documents and a two-factor authorisation is needed (clauses 1, 6.1, 8.2). For seals it describes automated processes and three strategies to avoid human interaction per signature, and a multi-signature authorisation "SHALL explicitly specify the total number of signatures to be authorized" (clauses 8.5 and 9).
- ETSI TS 119 431-2 and ETSI TS 119 432: the register lists both as snippet <span class="vtag v-todo">to verify</span>. The research read the scope, clause 6.4.3 and Annex A.8 to A.10 of TS 119 432 and the scope and annexes B and C of TS 119 431-2, not the full texts. TS 119 432 is "limited to remote server signing"; local signing, with the key on the signer's device, is a possible solution whose protocols "are not covered". In clause 6.4.3 the wallet "coordinates AdES signature creation through a SCASC, that may be part of the EUDIW or of the EUDIW backend", and the request travels as OpenID4VP transaction data.
- Regulation 2026/1731 replaces the Cloud Signature Consortium reference in Annex IV of Regulation 2024/2979 with "ETSI TS 119 432 v1.3.1 (2026-03) clauses 6.4.3, A.6, A.7 and A.8". The EBW Annex point 9(3) points to "implementing acts".
- ARF Topic 16 (read): QES_01 allows a qualified device "either local, external, or remotely managed"; QES_23 requires wallet providers and QTSPs to comply with SCAL 2 of EN 419 241-1. ARF Discussion Topic AB (the register lists it as snippet, <span class="vtag v-todo">to verify</span>; the research read section 4.2 in part): "Although the liability on signature creation compliance is on the QTSP, the Wallet Unit shall follow applicable requirements to enable compliance of the involved QTSP." It is a discussion paper, not normative.

**EUDI Wallet architecture for keys (for comparison, not binding on the EBW).**
- The ARF allows four WSCD architectures: remote WSCD (a "remote HSM"), local external, local internal and local native. A remote WSCD is "typically" an HSM on a secure server, used where the device lacks secure hardware or the provider wants no dependency on it; the provider must ensure "only the legitimate Wallet Instance can access the remote HSM", for example with "a split-key architecture" (ARF main text, sections 4.5.1 and 4.5.2). One WSCD may be part of several wallet units, for example a remote HSM, and a wallet instance can be a web application or a server (section 4.3.2).
- ARF Topic 40: the provider "SHALL NOT access the contents of a Wallet Instance" (WIAM_12a) and must implement strict controls where contents sit in a provider service (WIAM_12c); the note says the unit "cannot fully prevent" such access. The ARF assumes "a User device is a personal device".
- ARF key rules: the provider activates a unit only if its WSCA/WSCD is certified for assurance level high (WIAM_08); "A WSCA SHALL NOT enable export of private keys from a WSCD" (WUA_16a). Regulation 2024/2979 Article 4(1) requires at least one WSCD for critical assets; Article 11(1) allows local, external or remote qualified devices; Article 11(3) gives natural persons free qualified signing "at least for non-professional purposes".
- Regulation 2024/2981: certification covers the provision and operation of wallet solutions; the WSCD is assessed against assurance level high, with vulnerability assessment at AVA_VAN.5 unless justified; where verification of the WSCD stays inconclusive and no compensating requirements are possible, no certificate is issued (Article 8(2), Annex IV points 2(2) to 2(6)). Cancelling a certificate "might have severe consequences such as the revocation of all deployed wallet units" (recital, Article 12).
- Regulation 2026/1731: the unit attestation comprises one or more wallet instance attestations and one or more key attestations, signed JWTs; the key attestation carries 'key_storage' and 'user_authentication' with value 'iso_18045_high' where a WSCD is mentioned; the instance attestation expires less than 24 hours after the provider's integrity check; Regulation 2024/2979 Article 3(2) is deleted. Wallet providers use only the cryptographic mechanisms of its Annex Ia; the EBW texts do not refer to it.
- In the EUDI Wallet the unit attestation goes only to a PID provider or attestation provider during issuance, "not to a Relying Party" (ARF Topic 9, WUA_07 and WUA_24). The EBW Annex point 13(4) differs (see above).
- Provider revocation and suspension: Article 5e of eIDAS and Regulation 2025/847 require suspension and withdrawal of EUDI Wallets after a breach, with evaluation of wallet unit attestation revocation within 24 hours; revoked attestations "cannot revert to a valid state" (Regulation 2025/847 Article 4 and Article 8). The risk register of Regulation 2024/2981 names the threat "An attacker can prevent suspension or revocation of a wallet" (Annex I, TR79, read in part).

**WE BUILD (ecosystem specification, not law).**
- The WE BUILD architecture decision on wallet unit attestation and lifecycle (status Proposed, 11 February 2026) says the EBW "operates within a cloud or on-premise environment", requires "A valid WUA" for a unit to operate, and does not consider the wallet instance attestation "for the first iteration". The holder authorisation handshake rulebook has relying parties check that the holder's unit attestation is not revoked. The blueprint leaves the WSCA/WSCD architecture "to be specified by the Architecture and Wallets groups" and names "Theft of a YubiKey" as a revocation example (read in part).

**Overlap with DEC-06.** Key life cycle follows certificate status (TS 119 431-1 DEL-6.3.2-01, SIG-6.3.1-08), and wallet unit revocation (ARF Topic 38) and the split into wallet instance and key attestation (Regulation 2026/1731) are treated there. The EBW texts speak of one "wallet unit attestation"; whether implementing acts follow the split is open.

## Decision criteria

Criteria marked **source** are stated in a source; **driver** means an architecture or business driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| C1 | Control of the keys by the owner (sole control, or control for a legal person) | source: eIDAS Article 36(1)(c); TS 119 431-1 clause 4.1 and SIG-A.6-07A; CSC SCAL2 |
| C2 | Assurance level of key protection (substantial or high; certified WSCD) | source: Commission Annex 3(3), 4(1)(g) against Council deletion; Regulation 2024/2981 for EUDI Wallets; driver: level needed by business use cases |
| C3 | Qualified status of signatures and seals (qualified device, remote only through a QTSP) | source: eIDAS Article 29(1a), 29a, 39a; Article 5(1)(d) |
| C4 | Natural person signs, legal person seals; who may trigger use of the key | source: eIDAS Article 3(9), 3(24); TS 119 431-1 SIG-6.3.1-16; driver: internal approval rules |
| C5 | Availability and continuity (back-up, redundancy, recovery after loss) | source: eIDAS Article 29a(1)(b); TS 119 431-1 GEN-6.3.3-04; driver: availability targets |
| C6 | Dependence on the provider and exit (portability, re-creation of keys, transfer on provider failure) | source: Article 5(1)(l), 7(6)(f), Council (la) and Annex 10; ARF WUA_16a; driver: switching cost |
| C7 | Provider and insider risk (provider access to keys, logs, content) | source: ARF WIAM_12a to 12c; Council Annex 7(5); driver: threat model for hosted keys |
| C8 | Evidence and conformity burden for the provider | source: Article 11, Council Article 11(2aa), eIDAS Article 29a and 30; driver: cost of evaluation |
| C9 | Verifiability of the unit by counterparties | source: Annex 13(4); Regulation 2026/1731 Annex Ib; WE BUILD decision; driver: what relying parties check |
| C10 | Interoperability of signing interfaces | source: Regulation 2026/1731 Annex VI; TS 119 432; Annex 9(3) |
| C11 | Union establishment and freedom from third-country control of the key-holding provider | source: Article 7(2) |
| C12 | Cost and scalability for many units and small owners | driver |
| C13 | Cryptographic agility and post-quantum migration of the key store | source (partial): Regulation 2026/1731 Annex Ia for EUDI Wallets; requirements EBW-NFR-021 and EBW-NFR-044; driver: timing |
| C14 | Multi-user access to keys under owner authorisation, with audit | source: Article 5(1)(j), Annex 12(2)(c); driver: segregation rules |

## Options

The four patterns are not mutually exclusive. A wallet may combine them, for example a provider-hosted wallet key with a QTSP-managed qualified seal key.

### (1) Keys on a device the owner holds

**What the sources enable.** The ARF lists local external, internal and native WSCDs as allowed for the EUDI Wallet. The QES texts accept a "local" or "external" qualified device (Annex point 8, ARF QES_01). The owner keeps physical possession, which matches the control wording of eIDAS Article 36(1)(c).

**What they restrict.** Annex point 3(1) places the WSCA and WSCD use at the back-end, and no source says how a device held only by the owner fits. The ARF assumes a personal device, and no EBW text says how several users share one device. WUA_16a excludes key export, so a lost device means new keys. TS 119 432 does not cover protocols for a key on the signer's device, and the CSC API does not cover it as a particular case.

**What they leave open.** How a device is assigned to an owner and to which users; how an owner withdraws access to a physical device when an authorised user leaves; how the unit attestation is built for an EBW with a local device, given that the Council text drops the device from the unit definition.

### (2) Keys in a back-end operated by the wallet provider

**What the sources enable.** The EBW definitions place a back-end in the unit and require it to use a WSCA and WSCD. The ARF describes the remote HSM as typical where device hardware is missing and for web wallets and servers, and one WSCD may serve several units with isolation between them. The WE BUILD decision assumes "a cloud or on-premise environment".

**What they restrict.** Limits on provider access are strict controls, not technical impossibility (WIAM_12c and its note). The provider must be established in the Union and free of third-country control (Article 7(2)). Under the Council text it evidences conformity by self-assessment, not certification. Keys are not exportable in the ARF rules (WUA_16a), so exit would mean re-creating keys and re-issuing bound attestations, which no EBW text describes. Qualified signatures or seals cannot be created with keys held by a provider that is not a QTSP running a qualified remote device service (Article 29(1a)).

**What they leave open.** The assurance level of the HSM (substantial in the Commission text, not stated in the Council text); whether a certified WSCD is required at all for the EBW; how the owner proves control to counterparties; recovery after provider failure or removal from the list.

### (3) Keys in an HSM operated by the organisation itself

**What the sources enable.** The WE BUILD decision names "on-premise" operation. The ARF notes that wallet providers, PID providers and trusted list providers typically use a certified HSM (ARF main text, chapter 7). An owner can be the entity with the strongest control over the key (Article 36(1)(c)).

**What they restrict.** The EBW provider must be a notified provider on the list, established in the Union, so an owner-run HSM would have to be integrated as the WSCD of a provider's solution. For qualified seals the remote operator must be a QTSP (Article 29(1a)). The sole control levels of EN 419 241 are applied to the QTSP service in the standards read, not to an owner-run store. The unit attestation describes the components of the unit or allows their authentication and validation (Article 3(24) of the proposal), and no source describes how a component run by the owner would be covered.

**What they leave open.** Whether an owner-operated HSM counts as WSCD in the sense of Article 3(29); who is liable and who evidences certification; how the provider verifies the owner-operated component for the unit attestation; the minimum evaluation level.

### (4) Remote qualified sealing and signing by a QTSP, orchestrated by the wallet

**What the sources enable.** eIDAS defines the remote qualified device as a trust service on behalf of the creator. Annex points 8 and 9 allow remote qualified devices and a signature creation application from a trust service provider. TS 119 431-1 gives policy requirements, and TS 119 432 gives a wallet-orchestrated flow (read in part). The ARF requires SCAL 2 for remote QES in the EUDI Wallet, and Regulation 2026/1731 fixes the interface reference for the EUDI Wallet.

**What they restrict.** Keys are generated and managed only on behalf of the creator, at its request, by the QTSP; back-up is limited to the minimum. Identity-based activation needs an explicit action by the identified natural person. An EBW has no device certification requirement of its own, so the qualified path brings its evidence through the QTSP's conformity regime. The key is destroyed when the certificate is revoked.

**What they leave open.** How a legal-person seal is activated by several authorised users in the wallet (the standards read give the rule for one identified natural person per activation); whether sole control levels for seals are defined where the text says control (EN 419 241-1 not read); transfer of keys or re-issuance of certificates when changing QTSP; the relation between the QTSP's key and the wallet's own WSCD keys.

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | (1) owner device | (2) provider back-end | (3) owner HSM | (4) QTSP remote |
|---|---|---|---|---|
| C1 Owner control | Physical possession; sharing among users not stated | Strict controls on provider access, not impossibility (WIAM_12c) | Strongest in principle; integration not stated | Sole control or control levels apply to the QTSP service |
| C2 Assurance of key protection | Not stated for the EBW; ARF high for EUDI Wallet | Substantial in Commission Annex, not stated in Council text | Not stated | Qualified device certification (Article 30) |
| C3 Qualified status | Local or external qualified device accepted (Annex 8) | Qualified only with a QTSP service (Article 29(1a)) | QTSP needed for remote qualified seals | Yes, by definition |
| C4 Who triggers use | Not stated | Not stated | Not stated | Explicit action of an identified natural person (SIG-6.3.1-16) |
| C5 Continuity | Lost device means new keys (WUA_16a) | Not stated for the EBW | Not stated | Back-up at minimum and same level (Article 29a(1)(b)) |
| C6 Exit | Not stated | Export of keys not stated; data transfer or deletion (Article 7(6)(f)) | Not stated | Change of QTSP not stated |
| C7 Provider risk | Not stated | Provider can read logs where necessary (Council Annex 7(5)) | Reduced provider role; not stated | QTSP under certification and supervision |
| C8 Conformity burden | Not stated | Self-assessment in Council text (Article 11(2aa)) | Not stated | QTSP conformity regime |
| C9 Verifiability | Not stated | Unit attestation shown to relying parties (Annex 13(4)) | Not stated | Certificate and trusted list |
| C10 Interfaces | Not covered by TS 119 432 or CSC API | Annex 9(3), implementing acts | Not stated | TS 119 432 for the EUDI Wallet; EBW names no standard |
| C11 Union establishment | Not stated | Required (Article 7(2)) | Not stated | QTSP rules of eIDAS |
| C14 Multi-user access | Not stated | Owner authorises users (Article 5(1)(j)) | Not stated | Several-user activation for a seal not stated |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Four observations follow from the facts.

1. **The EBW texts do not fix where keys are held.** They require a back-end that uses a WSCA and WSCD (Annex point 3(1)) and allow local, external or remote qualified devices (Annex point 8). Options (2) and (4) fit the wording most directly; options (1) and (3) depend on how a provider integrates a device or HSM it does not run, which no source describes.
2. **Qualified seals and signatures require a QTSP when the key is remote.** Under Article 29(1a) a provider that is not a QTSP cannot hold the qualified key. A pattern with a provider-hosted wallet key for unit operations and a QTSP-managed key for qualified seals follows the structure of the sources, including the split between the wallet's own keys and the certificate of the QTSP.
3. **Exit is the weakest documented point.** The EBW texts specify export, transfer and deletion of owner data, and the ARF excludes private key export for the EUDI Wallet. No source says how keys or key attestations move between providers. Until this is settled, any placement with a provider carries re-creation of keys and re-issuance of bound attestations as the working assumption.
4. **The assurance level for key protection is not settled.** The Commission text names substantial; the Council text removes the clause. The EUDI Wallet rules name high and certification, but they bind the EBW only where referred to.

**Conditions under which this reading holds.** The final text keeps the WSCA/WSCD requirement for the back-end (Annex point 3(1)) and the local, external or remote qualified devices (Annex point 8); eIDAS Articles 29(1a) and 29a stay as they are; qualified providers offer remote sealing for legal persons with several authorised users.

**What would change it.** The Council outcome of 9 June 2026 and the adopted text; an implementing act on the signature creation interface (Annex point 9(3)); a statement on whether an owner-run HSM counts as WSCD; rules on key transfer between providers; a decision to apply the EUDI Wallet certification scheme (Regulation 2024/2981) to the EBW; EN 419 241-1 and -2 once read.

## Gaps and next steps

- Obtain the outcome of the Council meeting on 9 June 2026, then re-check Articles 3, 5, 6, 7 and 11 and Annex points 3, 4, 8, 9 and 10.
- Read what could not be read: EN 419 241-1 and -2 (paid CEN standards, connection refused), EN 419 221-5, EN 419 211, ETSI TS 119 461, TS 119 101, EN 319 411-2, CSC API 2.2, ARF Technical Specification 3, and the full call sequence of TS 119 432. Regulation 2015/1502 was not read for this note. The Parliament report (A10-0240/2026) and the EDPS opinion 5/2026 were not read.
- Review requirement EBW-TRU-029 (cites a deleted article); write the missing requirements (see "What the requirement set says") and review them with a named reviewer.
- Ask the Commission or a supervisory body whether an owner-operated or customer-managed HSM can be the WSCD, how keys move between providers, how a multi-user wallet maps users to keys, and how liability is allocated between provider, owner and QTSP. No source in the EBW texts says.
- Confirm the business drivers (C2, C5, C12, C13, C14) with stakeholders; they are assumptions until then.

## References

SRC-EBW-PROPOSAL, SRC-EBW-ANNEX-CELLAR, SRC-COUNCIL-ST-9684-26, SRC-EIDAS-CONSOL, SRC-CID-2016-650, SRC-CIR-2024-2979, SRC-CIR-2024-2981, SRC-CIR-2025-847, SRC-CIR-2026-1731, SRC-ETSI-TS-119431-1, SRC-ETSI-TS-119431-2, SRC-ETSI-TS-119432, SRC-CSC-API-V2, SRC-ARF-HLR, SRC-ARF-MAIN, SRC-ARF-DT-AB, SRC-WEBUILD-ARCH, SRC-WEBUILD-RB. Full entries with version, date and URL are in the source register.
