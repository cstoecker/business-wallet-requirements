---
title: "DEC-04 Trust framework and discovery"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 4
permalink: /architecture/decisions/dec-04/
description: "Which trust lists, lists of trusted entities and ecosystem trust anchors does a relying party use, and how does it find the right one? Facts from the sources, decision criteria, three options and the conditions under which each holds."
keywords: [trust list, trusted list, list of trusted entities, trust anchor, discovery, OpenID Federation, data space, Gaia-X, Catena-X, third countries, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-04 Trust framework and discovery

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. The Annex of the Commission text was not in the copy read; the Council Annex was read instead. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

A relying party receives a credential, a signature, a seal or a presentation. It has to decide which signers and issuers it accepts. Three setups are conceivable:

- **(a)** it trusts only entries reachable from **EU lists**: the EU list of trusted lists, the Commission lists for wallet roles and the Commission list of business wallet providers;
- **(b)** it keeps **separate lists or anchors per ecosystem** (EU qualified, EU wallet roles, data space, sector, global) and selects the domain per credential or counterparty;
- **(c)** it uses a **bridged or federated trust layer** that maps ecosystem anchors to common entries and resolves trust through a resolver or a federation chain.

The decision also covers how the relying party finds the applicable list, and how third-country and ecosystem anchors enter. What a trust list is and how it is validated is explained in the concept article {% include concept-ref.html id="CON-TRUST-LIST" %} and is not repeated here. This page adds discovery, several trust domains, third-country anchors and ecosystem anchors.

## What the requirement set says

The cluster K05 (trust framework and discovery) carries this decision. The requirements that decide between the options are:

{% include cluster-drivers.html cluster="K05" %}

The research note found candidate requirements that are not yet written as requirements: availability of 99,9 % for trusted lists, a distribution point that resolves to the latest list, authentication of a pointed-to list before use, trust evaluation from the list for registered electronic delivery (ERDS), capability discovery binding for ERDS, a rulebook statement of the anchor mechanism for non-qualified attestations, and recognition of several governance authorities. Existing entries already cover the Article 22 lists and the wallet ecosystem lists. The candidates are for the next requirement pass.

## Facts from the sources

Each fact has a source and was read in the original text unless marked.

**EBW proposal and Council text.** The two texts are kept apart here.
- The Commission proposal says the trust framework "should build upon the structures established under Regulation (EU) No 910/2014" (recital 16). Providers must be included in "the list established pursuant to Article 12(5)" (Article 7(1)); that reference is dangling, because Article 12 of the copy read has paragraphs 1 to 3 only and the list is in Article 12(3). The Commission is to maintain on its website, in a machine-readable format, a list of providers (Article 12(3)). The text does not say the list is signed or sealed and names no location or signing key. By contrast, information on validation mechanisms is published "in electronically signed or sealed form suitable for automated processing" (Article 6(3)). A wallet can be revoked when its provider is not on the list (Article 6(2)(f)).
- The Council text adds timing: inclusion and removal "within two working days" (Article 12(3)), changes the title from notified to authorised providers, and has a recital on temporary suspension from the list of trusted providers. Its Annex requires the wallet unit attestation to be issued under a certificate listed in the trusted list referred to in Regulation (EU) 2024/2980.
- The European Digital Directory is "the trusted source of information" for owners, with an API (Commission Article 10(1)); access is limited to owners, their authorised representatives and providers, and the Council text adds Member State authorities (Article 10(4)). The articles read do not say the Directory carries keys, certificates or trust anchors; its content is identity and address data. This is a lookup, not a trust list.
- Third-country frameworks: the Commission may establish by implementing act that third-country wallets or frameworks offer equivalent assurance, if interoperable with the trust framework of Regulation (EU) 910/2014, and publishes a list of them (Article 17). The Council text adds an assessment of independence from the control of high-risk governments. Providers established in the Union are not to be subject to control by a third country (Article 7(2)); providers may serve operators in a third country that hold owner identification data and a unique identifier (Article 18(1)).

**eIDAS and the wallet ecosystem lists.**
- Third countries and international organisations "shall in particular establish, maintain and publish a trusted list of recognised trust service providers"; recognition itself is by implementing act or agreement (SRC-EIDAS-CONSOL, Article 14).
- Relying party registers are published by Member States in signed or sealed form suitable for automated processing, with a common mechanism for identifying and authenticating relying parties (Article 5b(5) and (7)).
- The Commission publishes the wallet lists without registration or authentication, in signed form and on a human-readable website, together with the URL, the certificates that verify the lists and the mechanisms to validate changes (SRC-CIR-2024-2980, Article 5(3) and (4)). The ARF requires the Commission to publish the locations of the lists in the Official Journal (SRC-ARF-HLR, Topic 31, TLPub_06, TLPub_07). Wallet units and other actors accept PID provider trust anchors because of notification and publication (PPNot_05).
- CIR 2026/1731 deletes Article 3(2) of CIR 2024/2979 and states that wallet unit attestations must be validated by a certificate listed under Annex II of CIR 2024/2980 (SRC-CIR-2026-1731, Article 2; SRC-CIR-2024-2979).
- Non-qualified attestation providers are not notified, and "their trust anchors are not included in a LoTE by the Commission"; the relying party "must know how to obtain the trust anchor" (SRC-ARF-TRUST 6.3.2.4). "No centralised service discovery mechanism for PID or attestation issuance is foreseen", and a wallet provider may configure a pre-defined list of providers (6.6.2.2). The relying party distinguishes anchors per attestation class (6.6.3.6). Trust in list providers is "primarily rooted in authority and in procedural measures" (6.1). Wallet providers receive no access or registration certificates (6.2.2).
- ETSI TS 119 602 has profiles for lists of PID providers, wallet providers, providers of access certificates, providers of registration certificates, public sector bodies issuing attestations, and registrars and registers. It has no profile for business wallet providers or for their access certificates (SRC-ETSI-119602).

**Discovery mechanisms in the specifications.**
- A trusted list carries a URI pointer to another list with a digital identity of the issuer of the pointed-to list; for EU lists the field points to the Commission list of links, for non-EU schemes it is optional (SRC-ETSI-119612, clause 5.3.13). TS 119 602 has the same mechanism, states that one identity "shall allow successful authentication of the pointed-to list before its use", allows distribution points that provide identical copies, and has a tag that lets a web-searching tool recognise a list (clauses 6.3.9, 6.3.13, 6.3.16).
- Providers may add an extension to certificates and tokens that locates their list; it should not be marked critical and must resolve to the latest applicable list or a scheme that points to it (TS 119 612, clause 6.3). Lists are to be available 24 hours a day, 7 days a week, with at least 99,9 % availability over one year (clause 6.4).
- The EU list of trusted lists is at ec.europa.eu/tools/lotl/eu-lotl.xml; its location and signing certificates are authenticated by an Official Journal publication and can change by a pivot list; EU lists have a legal constitutive value (ETSI TS 119 615, V1.4.1, clause 4.1.1, read; not yet in the source register). The live instance read has sequence number 395, issue date 2026-09-24, next update 2027-03-17 and 43 pointers, including Iceland, Liechtenstein, Norway and an entry for the UK. The content of the UK list and the status of its services were not analysed.
- For registered electronic delivery, the recipient identification service is bound to OASIS BDXL (DNS) and capability discovery to OASIS SMP. Trust may be bilateral, through the EU trusted list, a domain trusted list or a domain PKI; for the EU list, the relying party checks that the digital identity matches and that the status is "granted" (ETSI EN 319 522-4-3, read; not yet in the source register).
- OpenID4VP lets a query name accepted authorities: `aki`, `etsi_tl` (a list that can reference other lists) or `openid_federation`. Verifiers "must verify that the issuer of a received presentation is trusted on their own", and online resolution "can leak information that could be used to profile the usage of the Credentials" (OpenID4VP 1.0, sections 6.1, 6.1.1, 15.10, read; not yet in the source register). HAIP leaves trust establishment out of scope and requires support for `aki`; the ISO VICAL text was not read. The EU wallet profile (ETSI TS 119 472-2) says the Authority Key Identifier shall use the "etsi_tl" mechanism and mixes the names of two query types; the intended type was not clarified in the text read. Signed issuer metadata needs trust in the signer, with the mechanisms out of scope; in the EU profile the signer is the access certificate of the provider (OpenID4VCI 1.0; ETSI TS 119 472-3; read, not yet registered).

**OpenID Federation 1.0 (final, 17 February 2026).** Entity statements are signed JWTs forming a chain from an entity to a trust anchor. The mechanism does not rely on Web PKI, and anchor keys are distributed "in some secure out-of-band way not described in this document". A party needs the identifier of the other party and a list of anchors with their keys. Anchors and intermediates may list their subordinates, and a resolve endpoint lets a trusted third party do the chain evaluation. If several valid chains exist, the party decides which to use. Trust marks state conformance to criteria set by an accreditation authority. The specification "does not define a revocation process"; chains carry an expiry and must be refreshed. No EU law text read (proposal, Council text, CIR 2024/2979, 2024/2980, 2024/2982, 2026/1731) mandates or mentions OpenID Federation for the wallet ecosystem. Profiles of OpenID Federation for wallets were not searched. The specification was read, but is not yet in the source register.

**Data space and ecosystem anchors.**
- Eclipse DCP: the Dataspace Protocol is "independent of the identity and trust system used"; DCP "allows for multiple trust anchors in a dataspace". Holders and verifiers expect a secure list of trusted issuer DIDs, but "how this list is provided is out of scope"; verifiers "can recognize several Dataspace Governance Authorities". The governance authority handles participant registration and designation of trust credential issuers. The participant identifier must be a DID (SRC-DCP, git main of 2026-08-05, which states v1.0). Catalogs that support issuance advertise it at `/.well-known/dspace-trust`. The Dataspace Protocol release 2025-1 says the semantics of authorisation tokens are not part of that specification (read; not yet in the source register).
- Gaia-X: trust anchors are conformity assessment bodies or technical means accredited by the Gaia-X Association, "not necessarily Root Certificate Authorities as commonly understood". Claims must be signed with material traceable to a trust service provider; non-EU anchors named are South Korea, the United Arab Emirates and India, with the full list in the Gaia-X Registry. Notaries use EORI, LEI, local registers and VAT sources. The compliance service forwards a presentation to a clearing house instance. The page read is the 24.04 prerelease compliance document, and whether a newer release exists was not established. The list and operators of clearing house instances and their technical documentation were not read (the pages fetched were stubs or 404). The document is not yet in the source register.
- Catena-X: a core service provider validates the company, creates the business partner number, does identity proofing and issues the Membership, BPN and Framework Agreement credentials (SRC-CX-0006, preview, go-live announced for 24 November 2026). The Membership Credential is issued by the core service provider or an assigned issuer (SRC-CX-0050). A BPN-DID resolution service maps the business partner number to a DID and checks that the credential is signed by a trusted issuer (SRC-CX-0167, partly read, the sections quoted were read). The participant identifier is the DID (SRC-CX-0018). In the pages read, no passage defines how a participant obtains the list of trusted issuers. The wallet standard CX-0149 was not read (the copy fetched was a stub).
- Global root: GLEIF is the "root of trust" of the vLEI chain, from GLEIF through qualified vLEI issuers to legal entities and persons (SRC-GLEIF-VLEI; SRC-GLEIF-EGF-PRIMARY, v4.0 document v1.2). ISO 17442-3 is named as the standard; its text was not read.
- WE BUILD pilot: the Commission is shown as compiling, signing and publishing the lists for wallet providers, PID providers, access certificate providers and registration certificate providers; Member State providers publish national lists for non-qualified and qualified attestation providers; validation follows ETSI TS 119 615. The authorisation model is "allow all" at ecosystem level, tightened by list extensions and registration data, in a draft pilot convention (SRC-WEBUILD-ARCH).

**What the sources do not say.** No source read defines a legal or technical list of trusted entities for business wallet providers or for access certificates of business wallet relying parties, other than the Commission list in Article 12 and the reference to the lists under CIR 2024/2980. No source read defines how a relying party chooses between several trust domains for the same credential; OpenID4VP lets the verifier name accepted authorities and DCP lets it recognise several governance authorities, and neither prescribes a decision rule. No source read defines equivalence between an ecosystem anchor and an EU list entry, except that Gaia-X names eIDAS trust service providers as one allowed anchor class.

## Decision criteria

Criteria marked **source** are stated or implied in a source; **driver** means a business or architecture driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| C1 | Legal effect of the anchor | **source**: EU trusted list status has legal constitutive value for qualified services (TS 119 615); ecosystem anchors carry contractual effect only |
| C2 | Authenticity of the list itself (signed or sealed, location and keys anchored outside the list) | **source**: CIR 2024/2980 Article 5; TS 119 615 |
| C3 | Machine readability and open access without registration | **source**: CIR 2024/2980 Article 5(3); ARF TLPub_04 |
| C4 | Status and history, and speed of withdrawal | **source**: concept article; ARF GenNot_05 (status Invalid); OpenID Federation chain expiry |
| C5 | Coverage of issuer classes (qualified, public sector, other attestation providers, ecosystem members) | **source**: ARF 6.3.2.4 |
| C6 | Support for several trust domains at once and per-credential policy | **source**: ARF 6.6.3.6; OpenID4VP `trusted_authorities`; DCP |
| C7 | Privacy of trust resolution (online lookups that reveal which credential is used) | **source**: OpenID4VP section 15.10 |
| C8 | Availability and caching (99,9 % list availability, offline validation with cached data) | **source**: TS 119 612 clause 6.4; ARF 6.6.3.2 |
| C9 | Third-country recognition path | **source**: proposal Article 17; eIDAS Article 14; Gaia-X registry |
| C10 | Governance of the anchor (who admits and removes members, EU establishment, independence from third-country control) | **source**: proposal Articles 7(2) and 17, Council Article 17(3); EN 319 522-4-3 |
| C11 | Discovery path from the credential or service to the applicable list | **source**: TS 119 612 clause 6.3; EN 319 522-4-3; OpenID4VP; the issuer discovery gap in ARF 6.6.2.2 |
| C12 | Number of parsers and signature profiles a relying party has to run (XML trusted lists with XAdES, JSON lists with JAdES, JWT entity statements, DID documents) | **driver** |
| C13 | Operational dependence on a single operator (Commission, clearing houses, one core service provider) and exit path | **driver** |
| C14 | Effort and cost for small relying parties to maintain anchor stores per attestation class | **driver**; ARF 6.6.3.6 requires a regular process |
| C15 | Liability and recourse when a list entry is wrong or late | **driver** |

## Options

### (a) EU lists as the single root

**What the sources enable.** Qualified services carry legal constitutive value, and the authentication of the list of lists is anchored in the Official Journal with a pivot list. Publication is open and signed, and the same rule set applies as for the EUDI Wallet. EEA states and a UK entry already appear in the live list of lists. The ERDS trust evaluation is defined for the EU list.

**What they restrict.** Non-qualified and ecosystem issuers have no entry. TS 119 602 has no profile for business wallet provider lists. The Article 12 list of the proposal has no stated signature, location or key. Third-country anchors enter only through implementing acts or agreements.

**What they leave open.** How a relying party learns of a new EU list location (the Official Journal publication and the pivot list are defined for the list of lists only), whether the Article 12 list will be published as a signed list of trusted entities, and how long a withdrawal takes to appear (TS 119 612 gives no timing beyond list validity, and the Council text sets two working days for the provider list).

### (b) Separate lists per ecosystem, selected per credential

**What the sources enable.** DCP and OpenID4VP support exactly this: multiple anchors, accepted authorities per credential query, several governance authorities. Catena-X and Gaia-X already run their own anchors, and the ARF already separates anchors per attestation class.

**What they restrict.** The specifications give no decision rule between domains. Ecosystem lists are out of scope of DCP and not specified in the Catena-X pages read. Each domain brings its own format and revocation behaviour. Wallets in the EU ecosystem have no discovery service for issuers.

**What they leave open.** How a business wallet advertises accepted domains to counterparties without revealing its credential portfolio, how a domain lists non-EU participants, and who audits ecosystem operators.

### (c) Bridged or federated trust layer

**What the sources enable.** OpenID Federation offers anchors, intermediates, trust marks, member enumeration and resolution as a service. Gaia-X already admits eIDAS trust service providers as anchors and uses notaries over registers. The OpenID4VP query type `openid_federation` exists.

**What they restrict.** No EU legal text read mentions OpenID Federation. The federation specification defines no revocation process and leaves anchor key distribution out of band. Delegated resolution adds a trusted third party and an online lookup. Equivalence between ecosystem and EU anchors is not defined.

**What they leave open.** The legal status of a federation anchor next to an eIDAS list, governance and liability of a bridge operator, and whether resolved results may be cached for offline presentation.

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | (a) EU lists | (b) per ecosystem | (c) federated layer |
|---|---|---|---|
| C1 Legal effect | Constitutive value for qualified services | Contractual effect only | Not stated; no EU text read mentions it |
| C2 Authenticity of the list | Signed lists; location and keys anchored in the Official Journal (list of lists); Article 12 list: not stated | Differs per domain; DCP leaves the list out of scope | Signed entity statements; anchor keys out of band |
| C3 Open access | Without registration (CIR 2024/2980 Article 5(3)) | Not stated for DCP and Catena-X lists | Not stated |
| C4 Status and withdrawal | Status values; Invalid status in notification; Council: two working days for the provider list | Not stated in the pages read | No revocation process; chain expiry |
| C5 Issuer classes | No entry for non-qualified and ecosystem issuers | Ecosystem members covered by their own anchor | Not stated |
| C6 Several domains | Anchors per attestation class (ARF) | Supported by OpenID4VP and DCP; no decision rule | Several valid chains possible; party decides |
| C7 Privacy of resolution | Lists are downloaded; online resolution not required | Not stated | Resolution through a third party is an online lookup |
| C9 Third countries | Implementing act or agreement | Gaia-X names non-EU anchors; Catena-X: not stated | Not stated |
| C11 Discovery | Pointers, extensions and the list of lists; no issuer discovery in the ARF | Catalog advertising (DCP); no issuer discovery for EU wallets | Resolution and enumeration endpoints |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Three observations follow from the facts.

1. **Option (a) alone does not cover the issuer classes in the requirement set.** The ARF and the sources leave non-qualified attestation providers and ecosystem members off the Commission lists, and no source defines the list of business wallet providers as a signed list with a stated location and key. (a) is the basis where legal effect is needed (C1) and where qualified services are involved.
2. **Option (b) is where the specifications are already written, but it leaves the choice between domains to the relying party.** OpenID4VP and DCP support several anchors per credential, and the sources give no decision rule (C6). This makes a stated policy per credential class necessary, not a single list.
3. **Option (c) rests on text the sources do not yet contain.** No EU legal text read mentions OpenID Federation, the specification has no revocation process, and equivalence between ecosystem and EU anchors is not defined. It can be treated as an option to test, not as a basis.

A working reading follows: **EU lists as the root for qualified services and wallet roles, ecosystem anchors admitted per credential class by relying-party policy, and a federated layer only as an optional resolver where a use case needs it.**

**Conditions under which this reading holds.** The adopted text keeps the Article 12 list and its link to the existing trust structures (recital 16); the Article 12 list is published in a signed, machine-readable form with a stated location and key; relying parties are willing to maintain anchor stores per attestation class, as the ARF requires.

**What would change it.** An adopted text that defines a trusted list or a list of trusted entities for business wallet providers or their access certificates (then (a) covers more); an EU or OpenID Foundation profile of OpenID Federation for wallets; a definition of equivalence between ecosystem anchors and EU list entries; a Commission decision under Article 17; the content of the Commission Annex; a clarified allocation of liability for wrong list entries.

## Gaps and next steps

- Obtain the Annex of COM(2025) 838 and the outcome of the Council meeting on 9 June 2026, then re-check Articles 10, 12 and 17 and the dangling reference to Article 12(5). <span class="vtag v-todo">to verify</span>
- Check whether CIR 2024/2980, as amended by CIR 2026/1731, will be extended to business wallet roles; this was not checked beyond the Council Annex reference. <span class="vtag v-todo">to verify</span>
- Read ISO/IEC 18013-5 and 18013-7 (VICAL and IACA lists), which were paywalled; statements on VICAL come from HAIP only.
- Read Catena-X CX-0149 and the Gaia-X clearing house documentation, and check for a Gaia-X release newer than the 24.04 prerelease.
- Search for OpenID Federation profiles for wallets.
- Analyse what the UK entry of the EU list of lists means legally today; read case law and national rules on the legal effect of trusted lists; check the amendment status of Implementing Decision (EU) 2015/1505.
- Register the sources marked "not yet in the source register" (ETSI TS 119 615, the live EU list of trusted lists, ETSI EN 319 522-4-3, ETSI TS 119 472-2 and 119 472-3, OpenID4VP 1.0, OpenID4VCI 1.0, HAIP 1.0, OpenID Federation 1.0, the Dataspace Protocol, the Gaia-X compliance document) before citing them in requirements.
- Per the research note, TS 119 612 V2.4.1 and TS 119 602 V1.1.1 are the latest versions in the ETSI delivery directory fetched on 2026-10-03.
- Write the missing requirements (see "What the requirement set says") and review them with a named reviewer.
- Confirm the business drivers (C12 to C15) with stakeholders; they are assumptions until then.

## References

SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26, SRC-EIDAS-CONSOL, SRC-CIR-2024-2979, SRC-CIR-2024-2980, SRC-CIR-2026-1731, SRC-ARF-HLR, SRC-ARF-TRUST, SRC-ETSI-119602, SRC-ETSI-119612, SRC-DCP, SRC-CX-0006, SRC-CX-0050, SRC-CX-0167, SRC-CX-0018, SRC-GLEIF-VLEI, SRC-GLEIF-EGF-PRIMARY, SRC-WEBUILD-ARCH. Full entries with version, date and URL are in the source register.
