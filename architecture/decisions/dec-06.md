---
title: "DEC-06 Credential lifecycle and revocation"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 6
permalink: /architecture/decisions/dec-06/
description: "How validity, status and revocation are handled for credentials, wallet units and authorisations in the European Business Wallet: facts from the sources, decision criteria, five options for latency and privacy, and the conditions under which each holds."
keywords: [revocation, validity status, token status list, short-lived credentials, suspension, wallet unit attestation, instance attestation, key attestation, authorisation, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-06 Credential lifecycle and revocation

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. The detailed status rules in the implementing acts and the ARF bind EUDI Wallets, PID providers and qualified or public-sector attestation providers; the EBW texts give no status mechanism of their own beyond the points listed below and point to implementing acts. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

How are validity, status and revocation handled for credentials, wallet units and authorisations, with which latency and which privacy properties? A business wallet holds attestations issued to the organisation, authorisations given to users, and a wallet unit that has its own attestation. Each can end for a different reason (request, compromise, leaver, dissolution, provider event), and a relying party has to learn about it without the issuer or an outsider being able to follow who checks what.

The decision touches cluster K07 (credential lifecycle) and, through it, key custody (DEC-03), mandates, privacy and audit.

## What the requirement set says

The requirements that decide between the options are:

{% include cluster-drivers.html cluster="K07" %}

Gaps in the set (facts found in the research, not yet written as requirements): the revocation grounds and the 24-hour notice for unit attestations in the Annex (point 6), the right of representatives to request revocation of the unit attestation (Article 7(6)(c)), the real-time validation of roles and mandates (Article 6(2)(b)), and the rules of Implementing Regulation (EU) 2026/1731 that chain the status of a PID to the wallet instance attestation and the key attestation. They are candidates for the next requirement pass.

## Facts from the sources

Each fact has a source and was read in the original text unless marked. Sources are marked "read in part" where only named clauses were read.

**Finding: the unit attestation is split in the EUDI Wallet rules, not yet in the EBW texts.**
- Implementing Regulation (EU) 2026/1731 replaces Article 6(1) of Implementing Regulation (EU) 2024/2979 and adds Annex Ib: a wallet unit attestation "shall comprise one or more wallet instance attestations and one or more key attestations". Both are signed JWTs; the wallet provider issues a separate key attestation for the secure cryptographic device and for each keystore. Article 3(2) of 2024/2979 is deleted by Article 2(1) of 2026/1731 (SRC-CIR-2026-1731 Art 2(1), 2(4), Annex Ib points 1 and 2(a) to (c), read).
- The instance attestation is short-lived: its expiry "shall be less than 24 hours" after the provider's integrity check (TR-WIA-2.1). Instance and key attestations carry `client_status` and `key_storage_status` with a status list reference and an `exp` "until which the wallet provider will maintain the revocation status"; the provider "shall use Token Status Lists" for both (R_GEN-1) (SRC-CIR-2026-1731 Annex Ib point 2(c) to (e), read).
- The EBW texts still speak of one "wallet unit attestation": Annex point 6 (Commission annex and Council text), Article 7(6)(c) and Article 6(1)(k). Whether implementing acts for the EBW will follow the split is open (SRC-EBW-ANNEX-CELLAR Annex point 6; SRC-EBW-PROPOSAL Art 6(1)(k), 7(6)(c); SRC-COUNCIL-ST-9684-26 Annex point 6, read; see also the key custody page DEC-03, which records the same split).
- Consequence for the register: EBW-TRU-029 cites Article 3(2) of 2024/2979, deleted by 2026/1731 Article 2(1). EBW-TRU-035 (PID provider verifies the unit attestation) and EBW-TRU-030 and -031 (Article 7 of 2024/2979) should be checked against the replaced Article 6 and Annex Ib <span class="vtag v-todo">to verify</span>.

**What the EBW texts say about validity, revocation and authorisations.**
- Revocation of the wallet: providers must "ensure that the validity of the European Business Wallets can be revoked" upon explicit request of the owner, compromise of security, permanent or temporary cessation of the owner's activity, or where the provider is "not included in the list" (SRC-EBW-PROPOSAL Art 6(2)(f); SRC-COUNCIL-ST-9684-26 Art 6(2)(f), same four grounds).
- Validation: providers "provide validation mechanisms, in order to ensure that the authenticity and validity of European Business Wallets can be verified", notify the mechanism to the Commission, which publishes it in signed form; relying parties get protocols to verify authenticity and validity (SRC-EBW-PROPOSAL Art 6(2)(d), (g), 6(3), 6(1)(h)).
- Unit attestation (Annex point 6): providers publish a policy "specifying the conditions and the timeframe for the revocation of Wallets unit attestations", inform affected users "no later than 24 hours from the revocation" with reason and consequences, and "make publicly available the validity status of the European Business Wallet unit attestation", describing its location in the attestation. Commission and Council wording of points 6(1) to 6(3) is the same. Unlike Article 7(4) of 2024/2979, the EBW text does not say "in a privacy preserving manner" (SRC-EBW-ANNEX-CELLAR Annex point 6; SRC-COUNCIL-ST-9684-26 Annex point 6).
- Right to request revocation: providers inform representatives (Council text: owners and authorised users) of "the right to request revocation of their wallet unit attestation" (SRC-EBW-PROPOSAL Art 7(6)(c); SRC-COUNCIL-ST-9684-26 Art 7(6)(c)).
- Authorisations: the owner can "manage and revoke such authorisations" (Article 5(1)(j)), and the same for authorisations of relying parties (Article 5(1)(k)). Role mappings are "verifiable, auditable, revocable and traceable to their legitimate issuers"; "conflicts of roles, over-delegation, or expired authorisations are automatically detected and prevented in real time" (Article 6(2)(b)). The Council Annex point 12(2)(b) says access "is controlled by real-time validation of roles and mandates", and point 12(1)(c) bases decisions on "the scope, validity and constraints of any mandate, delegation, or power of attorney" (SRC-EBW-PROPOSAL Art 5(1)(j), (k), 6(2)(b); SRC-COUNCIL-ST-9684-26 Annex point 12).
- Owner identification data may be issued as a qualified attestation of attributes, as an attestation by a public sector body, or by the Commission (Article 8(3)). The Council recital 33 states that "Qualified electronic attestations of attributes can be easily updated or revoked." The proposal sets no validity period and no revocation trigger for it.
- Provider-level events: providers notify owners "in the event of suspension, revocation or voluntary termination" of services and of removal from the list (Article 7(6)(f)); supervisory bodies "revoke the inclusion" of non-compliant providers (Article 13(5)(k)); implementing acts may provide for "temporarily suspending the provider from the list" (Article 13(12)); supervisors report list changes to the Commission "within 24 hours" (Article 12(1)). The Council text updates the self-assessment immediately where "a function affecting the security, validity, authenticity or portability of the European Business Wallet is suspended, revoked or materially modified" (Article 7(6b)(c)). The EBW texts do not say what happens to the status of attestations or authorisations in units of a delisted provider.
- Directory: any modification or revocation of directory information goes to the Commission "without undue delay and in any event within one working day" (SRC-EBW-PROPOSAL Art 10(5)).
- Article 5a(9) of eIDAS (EUDI Wallet) names revocation upon explicit request, compromise, and "upon the death of the user or cease of activity of the legal person"; the EBW text names cessation of activity of the owner instead (SRC-EIDAS-CONSOL Art 5a(9)).
- The EBW texts give no status mechanism for owner identification data, for attestations issued to businesses, or for authorisations beyond Articles 5(1)(j), 6(2)(b), 6(2)(f) and Annex point 6. Implementing acts under Articles 5(5), 6(5) and 8(7) are pending. Whether the EUDI Wallet instruments (Implementing Regulations 2024/2977, 2025/1569, 2026/1731) apply to EBW credentials is not stated in the EBW texts, except through Article 8(3) (format standards of Annex II of 2024/2979).

**Qualified certificates, seals and attestations (eIDAS).**
- A qualified trust service provider that revokes a qualified certificate must "publish the revocation status of the certificate in a timely manner, and in any event within 24 hours after the receipt of the request"; the revocation "shall become effective immediately upon its publication". Paragraphs 3 and 4 apply to qualified attestations of attributes (Article 24(3), (4), (4a)). Validity information is available "at least on a per certificate basis at any time and beyond the validity period", automated. Annex III(i) and Annex V(i) require the certificate or attestation to carry the location of the status service.
- Revoked qualified certificates and attestations, and public-sector attestations, lose validity "from the moment of its revocation" and the status "shall not in any circumstances be reverted" (Articles 28(4), 38(4), 45d(4); Article 45f(4) omits the words "in any circumstances").
- Suspension exists for qualified certificates only, and only where Member States "may lay down national rules on temporary suspension"; the suspension status "shall be visible" from the status service (Articles 28(5), 38(5)). No suspension rule appears for qualified attestations of attributes (Article 45d).
- EUDI Wallet breach (Article 5e of eIDAS and Implementing Regulation (EU) 2025/847): suspension "without undue delay"; revocation of validity after three months without remedy; within 24 hours the Member State evaluates whether revoking the wallet unit attestations of the units affected is necessary; after three months the withdrawal within 72 hours revokes them, and they "cannot revert to a valid state" (SRC-EIDAS-CONSOL Art 5e; SRC-CIR-2025-847 Art 4, 8).
- Member States provide free-of-charge validation mechanisms for EUDI Wallets (Article 5a(8)). The framework must not allow any party, after issuance, "to obtain data that allows transactions or user behaviour to be tracked" unless the user authorises it (Article 5a(16)(a)) (SRC-EIDAS-CONSOL).

**Implementing acts on status of PID, attestations and wallet units.**
- PID (Implementing Regulation (EU) 2024/2977 Article 5): public policy for validity status; only the provider can revoke; the user is informed "within 24 hours of the revocation" through a secure channel; revocation on user request, on revocation of the wallet unit attestation, and in other cases in the policy; revocations "cannot be reverted"; a revoked PID "shall remain accessible for as long as required by Union law or national law"; validity status is published "in a privacy preserving manner" with its location in the PID; "privacy preserving techniques which ensure unlinkability". Implementing Regulation 2026/1731 Article 1(3) rewords 5(4)(b) to refer to the revoked wallet unit attestation of the unit to which the PID was issued (SRC-CIR-2024-2977 Art 5; SRC-CIR-2026-1731 Art 1(3)).
- Qualified and public-sector attestations (Implementing Regulation (EU) 2025/1569 Article 4): written public policies on status management including "measures for ensuring the availability of the validity status information"; the provider is "the only" entity able to revoke; for attestations "issued with a validity period of more than 24 hours" revocation at least on explicit request of the person or subject, on known compromise, and in other cases required by law or policy; "revocation techniques and management methods that are privacy preserving and hindering linkability or traceability"; status made available "in a manner that ensures the integrity and authenticity". Recital 5 says attestations "should be able to be revoked, or alternative measures should be implemented to compensate for the risks related to non-revocability" (SRC-CIR-2025-1569 Art 4).
- Wallet unit attestation (Implementing Regulation 2024/2979 Articles 6 and 7): the wallet provider is "the only" entity able to revoke; public policy on "the conditions and the timeframe"; users informed "within 24 hours"; status public "in a privacy preserving manner". Recital 9 names an alternative: "to limit the lifetime of the wallet unit attestation as an alternative to the use of revocation identifiers" (SRC-CIR-2024-2979 Art 6(3), Art 7, recital 9).
- Attestation formats (Implementing Regulation 2026/1731, Annex IV): a status element "shall only indicate whether the attestation is revoked or not revoked and shall not support any other status values, such as suspension" for PID, qualified and public-sector attestations (EAA-4.2.11.1-06); revoked means "permanently revoked" (-06.1); "Where short-lived electronic attestations of attributes with a validity period of 24 hours or less are issued, revocation shall not be required" (EAA-4.2.13-03).
- mdoc: the Mobile Security Object carries either an attestation status list (a bit per index, Token Status List "in CWT format") or an attestation revocation list (identifier list); the provider uses "one of" these methods; "Verification of the MSO revocation list is optional for the wallet-relying party", and a relying party that checks "shall support both" mechanisms (EAA-6.2.10.1-01 to -17).
- SD-JWT VC: the status member "may contain the status_list member as specified in clause 6.2 of IETF draft-ietf-oauth-status-list-20" (EAA-5.2.10.1-06). For the PID, `nbf` and `exp` express the technical validity period; the attribute table also has an administrative expiry date and an issuance date (read in part) (SRC-CIR-2026-1731 Annex IV, Annex I).
- Chaining to the wallet unit (Annex Ib): a wallet unit can always present attestations whose status periods are "at least 31 days in the future" (LC_GEN-1); PID technical validity "shall end before both" status periods (LC_GEN-3); a PID provider with validity above 24 hours "shall check the revocation status of both the wallet instance attestation and the key attestation received during issuance at least once every 24 hours" and revokes if either is revoked (LC_GEN-4); status lists should "relate to at least 10 000 attestations" where possible (R_WIA-5); revoking a unit means revoking all index values in its instance attestations (R_WIA-4); a type-shared key status index may be revoked "only" for a vulnerability in the device type (R_KA-4). Revoking a wallet unit attestation ends display of the trust mark (Article 14a(8)) (SRC-CIR-2026-1731 Annex Ib point 2(c) to (e), Art 2(9)).

**ARF (v3.0.0).**
- Methods per format: PID, QEAA and PuB-EAA in mdoc are short-lived (24 hours or less) or use an attestation status list or attestation revocation list; in SD-JWT VC they are short-lived or use a status list ("No suitable specification of Attestation Revocation Lists in JSON format is available"). For non-qualified EAAs "the relevant Rulebook SHALL specify whether that type of EAA must be revocable" (SRC-ARF-HLR Topic 7, VCR_01, VCR_01b, VCR_02, VCR_11, VCR_11a).
- The provider "SHALL be the only party" executing revocation (it may outsource the operation) and "SHALL NOT reverse the revocation". Triggers: compromise, user request (PID shall, attestation should), revoked wallet unit (PID shall, attestation may), death, and changed attribute values when the credential is valid for at least 24 hours (VCR_03 to VCR_09).
- Relying parties "SHOULD verify the revocation status" or perform a risk analysis, which decides acceptance where no reliable status information exists (not revocable, offline with expired cache); they "SHOULD NOT request the relevant Attestation Status List or Attestation Revocation List each time an attestation is presented"; no authentication of the relying party before download (VCR_13 to VCR_16).
- Privacy of lists: the index is assigned randomly "to prevent this index from becoming a correlator"; each list holds enough entries "to ensure herd privacy", decoys allowed (VCR_17, VCR_18). The wallet instance "SHOULD regularly check the revocation status" of its credentials and of itself and notify the user (VCR_19).
- Wallet unit revocation (Topic 38): revocation of the wallet instance (status list index) or of a secure device or keystore; triggers are user request after authentication, request of a PID provider upon death of the person, and a security breach found by the provider's regular check; the user is informed within 24 hours through a channel "independent of the Wallet Unit"; PID providers "immediately revoke" PIDs on a revoked unit, attestation providers "MAY" (WURevocation_09 to _19) (SRC-ARF-HLR Topic 38).
- States (main chapter 4.6.3 to 4.6.7): a wallet unit is installed, operational, valid or revoked; "Revocation cannot be undone."; "Wallet Units can only be revoked", while the wallet solution can be suspended, restored or withdrawn; registrations of PID providers, attestation providers and relying parties can be suspended and unsuspended; a PID or attestation expires or is revoked as independent transitions (SRC-ARF-MAIN).
- Representation attestations: the issuer "SHALL ensure that either the attestations are short-lived" or that all entities entitled by law to request revocation are able to do so (RP_02). The ARF has no legal-person wallet (Topic 28 empty) and no rule for a natural person representing a legal person (SRC-ARF-HLR Topic 29).
- The ARF explains the 24-hour figure as originating from ETSI EN 319 411-1 requirement REV-6.2.4-03A, "the process of revocation must take at most 24 hours"; EN 319 411-1 itself was not read (SRC-ARF-HLR VCR_01 note).

**Token Status List (IETF draft -21; Implementing Regulation 2026/1731 cites -20, also read).**
- Statuses: 0x00 VALID, 0x01 INVALID, 0x02 SUSPENDED ("temporarily invalid"); values 0x03 and 0x0C to 0x0F are application specific; lists use 1, 2, 4 or 8 bits per entry.
- Freshness: the token carries `exp` (absolute) and `ttl` ("the maximum amount of time, in seconds, that the Status List Token can be cached"); a relying party may cache for the ttl, or check at issue time plus ttl "for critical use cases", or after `exp` if there is no ttl. The draft leaves the interval to ecosystems.
- Privacy: "The herd privacy is depending on the number of entities within the Status List called its size." An issuer can track by generating one list per token or a unique URI; relying parties that store the URI and index can profile validity, for example "profiling the suspension of an employee credential"; outsiders can infer counts and revocation rates. Mitigations named: random indices, decoys, several lists, no historical resolution, batch issuance of one-time-use tokens, re-issuance with a fresh list entry, and an external status provider ("the Issuer has no means to identify the Relying Party"). "Batch revocation of a batch of Referenced Tokens might reveal that they are all members of the same batch."
- Ecosystems using more than VALID and INVALID "should consider the possible leakage of data and profiling possibilities before doing so and evaluate if revocation and re-issuance might be a better fit".
- Aggregation URI, a status issuer that differs from the token issuer, and delivery through content delivery networks ("greater scalability") are described, read in part (SRC-IETF-TSL sections 4.1, 5.1, 7.1, 9, 12.1 to 12.8, 13.2 to 13.7).

**Key life cycle and remote signing.**
- ETSI TS 119 431-1: "If the public key certificate is revoked, the corresponding signing key shall be destroyed."; the service "should ensure that the public key certificate is valid before using the corresponding signing key", valid meaning "not expired not revoked not suspended" (SRC-ETSI-TS-119431-1 DEL-6.3.2-01, SIG-6.3.1-08).
- Certification bodies suspend "without undue delay" after a confirmed breach and cancel if it is not remedied; the recital says: "The cancellation of a certificate of conformity might have severe consequences such as the revocation of all deployed wallet units." The risk register lists "A public attestation/relying party revocation list can contain information about the user's usage of their attestation" (TR37) and "An attacker can prevent suspension or revocation of a wallet" (TR79), read in part (SRC-CIR-2024-2981 Art 12, recital, Annex I).

**WE BUILD.**
- The architecture decision record on the wallet unit lifecycle (status Proposed, 11 February 2026) lists the unit states uninstalled, installed, operational and valid, says "Revocation of WUA immediately suspends infrastructural legitimacy." and that revocation of the EBWOID suspends identity validity "while preserving structural trust". It adds: "Where EBWOID is short-lived, the dependency between WUA revocation and EBWOID validity must be further specified in the implementing acts" (SRC-WEBUILD-ARCH adr/wallet-unit-lifecycle-management.md).
- The blueprint lists triggers for PID, EBWOID and units: explicit request ("A change in ownership of a company could be a reason for authorized representatives to revoke the EBWOID"), data change, regulatory change, loss or theft, provider revocation, abusive use, inactivity, service-term violation and end of life ("Termination or dissolution of the legal entity/business activity such as liquidation of a company"). Provider duties: publish a policy, only the issuer revokes, notify within 24 hours, revocation irreversible (SRC-WEBUILD-ARCH blueprint/06-trust-and-security.md).
- The EBWOID rulebook says "EBWOID SHALL include `exp`. Validity longer than 24 hours is permitted; therefore, revocation MUST be supported."; the SD-JWT VC EBWOID includes a `status` claim of type status list with purpose revocation when validity exceeds 24 hours; relying parties "Treat any indeterminate status as non-valid per risk policy."; chapter 6 carries a TODO for the revocation task (SRC-WEBUILD-RB rb-ebwoid/README.md sections 3.2.1, 6).
- The employee and contact-person rulebooks require a status claim when validity exceeds 24 hours; the employee rulebook adds "A revoked or suspended attestation must be treated as invalid for credential-validity purposes by all RPs." and requires an "active IETF Token Status List". The rulebook sample status object uses the members `status_list_credential`, `status_list_index` and `status_purpose`, which differ from the `idx` and `uri` members of the IETF draft `status_list` claim. The base rulebook has each side check the unit attestation of the other at presentation: "WUA not revoked, RP EBW unit components valid and authenticated" (SRC-WEBUILD-RB rb-employee/README.md section 6, rb-contact-person/README.md, rb-base/holder-authorization-handshake.md).

## Decision criteria

Criteria marked **source** are stated in a source; **driver** means an architecture or business driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| C1 | Latency from revocation decision to relying party knowledge | source: 24 hours for publication (eIDAS Article 24(3)), notice (Implementing Regulations 2024/2979 Article 7(3), 2024/2977 Article 5(3)) and instance attestation freshness (2026/1731); no source states a latency for non-qualified EAAs or authorisations; driver: business tolerance |
| C2 | Freshness against availability (cache time, offline relying parties) | source: ARF VCR_14, VCR_15; draft `ttl` and `exp`; driver: per use case |
| C3 | Privacy and unlinkability of status checks (herd size, random index, issuer observability, relying party profiling) | source: eIDAS Article 5a(16); 2025/1569 Article 4(4); ARF VCR_16 to VCR_18; draft section 12 |
| C4 | Who may revoke and on which triggers (issuer only, owner, user, provider, supervisor) | source: 2024/2977 Article 5(2); 2025/1569 Article 4(2) and (3); EBW Article 5(1)(j); driver: owner-side triggers for credentials issued to a business (leaver, dissolution) |
| C5 | Irreversible revocation versus suspension and reinstatement | source: eIDAS Articles 28(4), 28(5), 45d(4); 2026/1731 EAA-4.2.11.1-06; draft status 0x02; driver: need for temporary suspension (employee leave, investigation) |
| C6 | Short-lived credentials versus status checking (issuer availability, re-issuance load, offline use) | source: ARF VCR_01, EAA-4.2.13-03; driver: cost and availability of issuance |
| C7 | Cascade of status from wallet unit to PID, owner identification data and attestations | source: 2024/2977 Article 5(4)(b); LC_GEN-3 and -4; WE BUILD decision record; driver: cascade to mandates and non-qualified attestations |
| C8 | Scale of the status infrastructure (list size, hosting, third-party status provider) | source (partial): draft sections 13.4 to 13.6; R_WIA-5; driver: number of credentials per owner |
| C9 | Interoperability of status formats (mdoc, SD-JWT VC, JWT and CWT, W3C credentials) | source: 2026/1731 Annex IV; ARF VCR_11, VCR_11a; the W3C status specification was not read |
| C10 | Real-time validity of authorisations and mandates inside the wallet | source: EBW Article 6(2)(b); Council Annex 12(2)(b); driver: target time |
| C11 | Notification of holder, owner and users after revocation | source: 24 hours (2024/2979 Article 7(3)); ARF WURevocation_14 and _16 |
| C12 | Evidence and retention of revoked credentials | source: 2024/2977 Article 5(6); driver: audit needs |
| C13 | Mass events (provider suspension, delisting, certificate cancellation, algorithm change) | source: eIDAS Article 5e; 2025/847; 2024/2981 recital; EBW Articles 6(2)(f), 7(6)(f) |
| C14 | Liability for acts relying on stale status | driver; no source read allocates it |

## Options

The patterns can be combined by credential type. The sources do not rank them.

### Option 1: short-lived credentials (24 hours or less), no status check

**What the sources enable.** Implementing Regulation 2026/1731 (EAA-4.2.13-03) and ARF VCR_01 allow it for PID, qualified and public-sector attestations. The draft lists re-issuance as a privacy mitigation, and without a status list the issuer cannot observe checks.

**What they restrict.** The issuer must be online and willing to re-issue at least daily per credential. The ARF explains the 24-hour threshold as the maximum duration of the revocation process, so a credential valid for less than that may expire before revocation completes. The EBWOID rulebook allows validity above 24 hours and then requires revocation.

**What they leave open.** How re-issuance interacts with issuer-side authentication of the business wallet; whether the status of a wallet unit still needs checking at each re-issuance (LC_GEN-4 addresses a PID with longer validity only); offline use.

### Option 2: status list (revocation only) for longer-lived credentials

**What the sources enable.** Token Status List is the named mechanism for the wallet instance and key attestations and for SD-JWT VC credentials, and for mdoc as the attestation status list. Herd privacy comes from list size, random indices and caching, and a third party may host lists.

**What they restrict.** Only revoked or not revoked for PID, qualified and public-sector attestations; revocation is irreversible. The status URI and index are traceable data. Relying party verification is "optional" in the mdoc profile and a "SHOULD" in the ARF. An owner with few credentials produces small lists (R_WIA-5 says "where possible" at least 10 000 attestations).

**What they leave open.** List sizes and decoys for businesses with few credentials; cache time values per use case (the draft gives none); the status format for non-qualified EAAs issued by businesses, which ARF VCR_02 leaves to the rulebook.

### Option 3: identifier-based revocation list (mdoc only)

**What the sources enable.** It is the second mdoc mechanism; the identifier is unique per Mobile Security Object, and relying parties that check must support both options.

**What they restrict.** Only for mdoc ("No suitable specification of Attestation Revocation Lists in JSON format is available"). The list grows with revoked entries only.

**What they leave open.** Observability of the revocation rate by outsiders (the draft treats this for status lists; no source analyses it for identifier lists).

### Option 4: status values beyond revoked, including suspension

**What the sources enable.** The draft defines SUSPENDED; eIDAS allows national temporary suspension of qualified certificates with visible status; the WE BUILD employee rulebook speaks of "revoked or suspended"; the ARF registration states of providers and relying parties can be suspended.

**What they restrict.** Implementing Regulation 2026/1731 forbids status values other than revoked for PID, qualified and public-sector attestations. The ARF has no suspension of wallet units. The draft warns of leakage and profiling and suggests considering revocation with re-issuance instead.

**What they leave open.** Whether non-qualified EAAs and EBW authorisations may carry a suspended state (Article 5(1)(j) speaks only of revoking authorisations); the legal effect of a suspension for a business (no source).

### Option 5: online per-credential validation by the issuer or a validation service

**What the sources enable.** eIDAS requires status "on a per certificate basis at any time" for qualified certificates; the EBW text speaks of validation mechanisms for the wallet and of real-time validation of roles and mandates inside the wallet.

**What they restrict.** The sources describe lists as the approach that stops the issuer from learning which credential is checked, and require status information "in a privacy preserving manner". The risk register notes that lists can reveal usage (TR37).

**What they leave open.** Whether a direct query service is acceptable for business credentials where unlinkability to a natural person is not at stake; relying party burden and availability.

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | 1 short-lived | 2 status list | 3 identifier list | 4 beyond revoked | 5 online validation |
|---|---|---|---|---|---|
| C1 Latency | Bounded by credential life (24 hours or less); no revocation step | 24-hour figures apply to qualified items; others not stated | As 2 | Not stated | Per-request status; latency not stated |
| C2 Freshness and availability | Issuer must be online for re-issuance | Draft `ttl` and `exp`; ARF caching rule; values not stated | As 2 | Not stated | Relying party depends on the service; not stated |
| C3 Privacy | No issuer observability of checks | Herd privacy by size, random index; URI and index traceable | Identifier unique per MSO; analysis not stated | Draft warns of leakage and profiling | Issuer can learn which credential is checked (L5.3, L4.3) |
| C4 Who revokes | Not needed; issuer decides on re-issuance | Issuer only (ARF VCR_03) | As 2 | Not stated for businesses | Not stated |
| C5 Irreversibility | Not stated | Irreversible for PID and attestations | Irreversible (VCR_04) | Forbidden for PID, qualified and public-sector attestations; open for others | Not stated |
| C6 Short life against status | This option | Longer life with checking | As 2 | Not stated | Not stated |
| C9 Format interoperability | All formats | mdoc and SD-JWT VC | mdoc only | Draft values; legal profile revoked only | Not stated |
| C10 Real-time authorisations | Not stated | Not stated | Not stated | Not stated | EBW text names real-time validation; mechanism not stated |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Four observations follow from the facts.

1. **Credential classes need different answers, and the EBW texts answer none of them.** For PID-like and qualified or public-sector attestations the legal profile already narrows the choice to short life or a status list with revoked or not revoked only (options 1 to 3). For non-qualified attestations issued to businesses and for authorisations, the sources leave format, trigger and latency to rulebooks and to implementing acts that are pending.
2. **A status list with a short-lived instance attestation is the pattern the sources describe most completely.** It carries the cascade from wallet unit to PID (C7), the 24-hour figures (C1) and the privacy mitigations (C3). Its weak point for a business is list size (C8): few credentials per owner means small lists unless issuers pool them.
3. **Suspension (option 4) cannot be assumed.** It is excluded for PID, qualified and public-sector attestations and discouraged by the draft; whether it is possible for business attestations and authorisations is open. Leaver and investigation cases may need revocation with re-issuance.
4. **The split of the unit attestation changes what a cascade means.** If EBW implementing acts follow Implementing Regulation 2026/1731, the cascade has two inputs (instance attestation and key attestation), not one wallet unit attestation.

**Conditions under which this reading holds.** The EBW implementing acts reuse the status mechanisms of the EUDI Wallet instruments, or rulebooks adopt Token Status List for business attestations; Article 5(1)(j) and Article 6(2)(b) survive in the final text; the 24-hour figures are accepted as targets for business credentials, which no source states.

**What would change it.** An adopted EBW text with its own status mechanism or a different treatment of the unit attestation; a source that gives a maximum revocation time for non-qualified attestations or for authorisations; a rule on the status of attestations in units of a delisted provider; a W3C status specification adopted by the rulebooks; a change of the normative reference of Implementing Regulation 2026/1731 from draft -20 to a later version <span class="vtag v-todo">to verify</span>; the rules of Directive (EU) 2025/25 on validity and revocation of mandates, which were not read.

## Gaps and next steps

- Obtain the outcome of the Council meeting of 9 June 2026, and re-check Articles 5, 6, 7 and Annex point 6.
- Read what was not read: ETSI EN 319 411-1 (the REV-6.2.4-03A requirement is known through the ARF note and the requirement register), ETSI TS 119 471 and TS 119 472-1 beyond the extracts in the implementing act, OID4VCI Appendix D and E, ISO/IEC 18013-5 second edition, the W3C Verifiable Credentials status specifications (Bitstring Status List), the CRL and OCSP profiles (RFC 5280, RFC 6960), ARF Technical Specification 3 (a pointer page only), Implementing Regulation (EU) 2015/1502, Directive (EU) 2025/25 and its rules on mandates, Parliament report A10-0240/2026 and EDPS opinion 5/2026.
- Settle who may revoke credentials issued to a business wallet when an authorised user leaves (owner, issuer or user), and how a relying party learns that a mandate attestation ended (ARF RP_02 offers short life or revocation by those entitled).
- Check the draft -21 against the version -20 cited in Implementing Regulation 2026/1731, which differ in dates and some sections <span class="vtag v-todo">to verify</span>.
- Review the stale register items EBW-TRU-029, -030, -031 and -035 against the replaced Article 6 and Annex Ib <span class="vtag v-todo">to verify</span>.
- Write the missing requirements (see "What the requirement set says") and review them with a named reviewer; confirm the business drivers (C1, C2, C4, C5, C6, C10, C12, C14) with stakeholders, since they are assumptions until then.

## References

SRC-EBW-PROPOSAL, SRC-EBW-ANNEX-CELLAR, SRC-COUNCIL-ST-9684-26, SRC-EIDAS-CONSOL, SRC-CIR-2024-2977, SRC-CIR-2024-2979, SRC-CIR-2024-2981, SRC-CIR-2025-1569, SRC-CIR-2025-847, SRC-CIR-2026-1731, SRC-ARF-HLR, SRC-ARF-MAIN, SRC-IETF-TSL, SRC-ETSI-TS-119431-1, SRC-WEBUILD-ARCH, SRC-WEBUILD-RB. Full entries with version, date and URL are in the source register.
