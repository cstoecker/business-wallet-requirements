---
title: "Trust list"
layout: concept
concept: CON-TRUST-LIST
parent: Concepts
grand_parent: Start here
description: "A trust list is a signed list of providers and services that a relying party uses as the source of trust anchors. This article explains the EU trusted list under eIDAS and ETSI TS 119 612, the lists of trusted entities for wallet roles under ETSI TS 119 602, and how a relying party validates against them."
permalink: /concepts/trust-list/
schema_type: TechArticle
keywords: [trust list, trusted list, list of trusted lists, list of trusted entities, ETSI TS 119 612, ETSI TS 119 602, trust anchor, service status, qualified trust service provider, European Business Wallet]
about: [Trust list, Trusted list, List of trusted entities, Trust anchor, eIDAS]
last_verified: "2026-10-03"
figures: [trust-list-anatomy, trust-list-validation]
faq:
  - q: "What is a trust list?"
    a: "A trust list is a signed list of providers and the services they offer, with the status of each service. A relying party reads it to learn which signing keys and certificates it may treat as trust anchors. In the EU, Member States publish trusted lists of qualified trust service providers under Article 22 of Regulation (EU) No 910/2014, in the XML format of ETSI TS 119 612."
  - q: "What is the difference between a trusted list and a list of trusted entities?"
    a: "A trusted list under ETSI TS 119 612 covers qualified and other trust services and is published by Member States. A list of trusted entities under ETSI TS 119 602 generalises that model for wallet-related roles such as wallet providers, PID providers and providers of access certificates, and is provided by the Commission in JSON or XML profiles."
  - q: "How does a relying party find the right trusted list?"
    a: "The Commission publishes a list of trusted lists that points to each Member State list and names the certificate that signs it. A relying party authenticates that list first, then the national list. ETSI TS 119 612 describes this procedure in an informative annex."
  - q: "Does the European Business Wallet proposal create a trusted list for business wallet providers?"
    a: "The proposal COM(2025) 838 provides for notification of providers and a machine-readable list of notified providers published by the Commission, and for a European Digital Directory. The articles read do not call this list a trusted list. The proposal is not adopted law and may change."
---

## Summary

A trust list is a signed list that tells a relying party which providers and services it may trust, and with which keys. In the EU, each Member State publishes a trusted list of its qualified trust service providers, and the Commission publishes a list that points to all of them. Wallet-related roles use the related model of lists of trusted entities. A relying party that checks the signature, the status and the certificate chain against such a list does not have to know the provider in advance.

## Definition

{% include concept-definition.html id="CON-TRUST-LIST" %}

What it is not. A trust list is not a decision about what a party may do; that is the control plane. It is also not a registry of all companies: it lists providers and services that have a status under a scheme, such as qualified status. And it is not a trust anchor itself. The list is the signed container; the trust anchors are the digital identities of the listed services.

## Why it matters

A relying party cannot know every provider whose certificate it will meet. The trust list lets it verify a signature or seal from a provider it has never dealt with, because a supervised scheme has put that provider on a signed list. Within the {% include concept-ref.html id="CON-TRUST-PLANE" %}, the trust list is the artefact that carries the result of supervision.

- **B2B.** A company checks a supplier's sealed document against the national trusted list of the issuing provider.
- **B2G.** An authority validates a business's qualified seal and timestamp the same way, in any Member State.
- **Wallets.** A wallet unit or issuer takes the trust anchors of wallet providers, access certificate providers and other roles from lists of trusted entities provided by the Commission (ARF chapter 6).

## How it works

{% include figure.html id="trust-list-anatomy" no=1 %}

**Structure.** In ETSI TS 119 612 a trusted list is an XML document with three parts: scheme information, the list of providers with their services, and a digital signature (clauses 4 and 5.1.1). Scheme information includes the scheme operator, the territory, a sequence number that starts at 1 and increases with each release, the issue date, the next update and pointers to other lists (clause 5.3). A list whose next update lies in the past is discarded as expired, and the next update may not be more than six months after the issue date (clause 5.3.15).

**Services and trust anchors.** Each provider has one or more services. A service has a type identifier, a name, a service digital identity, a current status with its starting time, and a history of earlier statuses (clauses 5.5 and 5.6). The service digital identity is the material a relying party uses as trust anchor in certificate path validation (Annex I, informative). For qualified service types the status is either *granted* or *withdrawn* (clause 5.5.4). A new status time may not be set before the date the list was reissued, so a status cannot be changed retroactively (clause 5.5.5).

**Signature.** The scheme operator signs the list with an XAdES baseline B signature, using a certificate whose subject country and organisation match the scheme territory and operator (clause 5.7.1). A published SHA-256 digest next to the list "shall not be used to authenticate" it (clause 6.1).

**Legal basis.** Each Member State establishes, maintains and publishes trusted lists, signed or sealed in a form suitable for automated processing, and notifies the Commission of the responsible body, the place of publication and the signing certificates. The Commission makes this information available in signed form (eIDAS Article 22(1) to (4)). Commission Implementing Decision (EU) 2015/1505 set the technical specifications and formats and relied on version 2.1.1 of TS 119 612.

**Lists of trusted entities.** ETSI TS 119 602 defines a data model that generalises TS 119 612 and applies to lists of PID providers, wallet providers, providers of wallet relying party access certificates and registration certificates, public sector bodies issuing attestations, and registrars and registers (clause 1 and Annex C). It has XML and JSON bindings; the profiles for PID providers, wallet providers and access certificate providers use JSON with a compact JAdES baseline B signature, while the profile for public sector attestation providers allows XML or JSON. Most of these profiles do not use a service status: an entity is listed while approved and removed when its approval ends. The profile for public sector attestation providers does use a status, with the values *notified* and *withdrawn*. TS 119 602 defines no profile for qualified attestation providers; they appear on the national trusted lists (ARF 6.3.2).

## Interaction flow

{% include figure.html id="trust-list-validation" no=2 %}

1. The relying party locates the Commission list of trusted lists (TS 119 612 Annex H.2).
2. It verifies that list's signature against the digest of the signing certificate published in the Official Journal (Annex A.1).
3. It finds the pointer to the national list and the certificate that signs it.
4. It downloads the national list and verifies the signature with that certificate. If a check fails, authentication of the list fails (Annex A.1).
5. It finds the service by type and digital identity.
6. It checks that the status is granted at the time of the signature or seal and that the list has not expired, then uses the digital identity as trust anchor.

For wallet roles the ARF describes the same idea with lists of trusted entities: a PID provider downloads the Wallet Provider list from the location the Commission publishes, and a relying party regularly downloads the latest versions of all applicable lists to manage its trust anchors (ARF 6.2 and 6.6).

## Roles and responsibilities

| Role | Responsibility | Source |
|---|---|---|
| Scheme operator (Member State body) | establishes, maintains, publishes and signs the national trusted list | eIDAS Article 22; TS 119 612 clause 5.7 |
| Commission | publishes the list of trusted lists and, for wallet roles, the lists of trusted entities | eIDAS Article 22(4); ARF chapter 6 |
| Supervisory body | grants or withdraws the status that the list shows | eIDAS Article 21 |
| Listed provider | offers services under the listed status; links to the list on its website when using the trust mark | eIDAS Article 23 |
| Relying party | authenticates the lists, checks status and expiry, keeps trust anchors per provider type | TS 119 612 Annex A.1; ARF 6.6 |

## Related concepts

- {% include concept-ref.html id="CON-TRUST-PLANE" %} is the plane in which the trust list sits.
- {% include concept-ref.html id="CON-TRUST-LIST-DISCOVERY" %} covers how a relying party finds the list that applies to a credential or sector.
- {% include concept-ref.html id="CON-LOA" %} describes how much confidence a listed status gives.
- {% include concept-ref.html id="CON-QUALIFIED-SERVICES" %} describes the services whose status the lists show.
- {% include concept-ref.html id="CON-MULTI-TRUST" %} describes what changes when several lists and trust domains meet.
- {% include concept-ref.html id="CON-WUA" %} describes the attestation of a wallet unit, which depends on listed wallet providers.
- {% include concept-ref.html id="CON-WALLET-CONNECTOR" %} binds a wallet to a data space connector, which needs a trust decision at the boundary.

## Requirements and obligations

Obligations found in the sources, not yet derived into EBW requirements (each still needs a technology-neutral requirement and a named reviewer). Categories: TRU, GOV.

| Source obligation | Source | Candidate category |
|---|---|---|
| Member States establish, maintain and publish trusted lists in signed form suitable for automated processing | SRC-EIDAS-CONSOL, Article 22(1) and (2) | TRU |
| Member States notify the Commission of the list body, location and signing certificates | SRC-EIDAS-CONSOL, Article 22(3) | GOV |
| The Commission publishes this information in signed, machine-processable form | SRC-EIDAS-CONSOL, Article 22(4) | GOV |
| A trusted list is signed by the scheme operator and expires at its next update | SRC-ETSI-119612, clauses 5.3.15 and 5.7.1 | TRU |
| Lists of trusted entities for wallet roles are signed with a JAdES or XAdES baseline B signature | SRC-ETSI-119602, clause 6.8 and Annexes D to H | TRU |
| The Commission maintains a machine-readable list of notified business wallet providers (proposal) | SRC-EBW-PROPOSAL, Article 12 | GOV |
| The Commission operates a European Digital Directory as trusted source on business wallet owners (proposal) | SRC-EBW-PROPOSAL, Article 10 | FUN |
| Relying parties download the latest lists regularly and keep trust anchors separate per provider type | SRC-ARF-TRUST, chapter 6.6 | TRU |

## Standards and specifications

- **ETSI TS 119 612 V2.4.1 (2025-08), Trusted Lists:** structure, XML format, status values, signature and publication (SRC-ETSI-119612).
- **ETSI TS 119 602 V1.1.1 (2025-11), Lists of trusted entities, data model:** generalised model and profiles for wallet roles (SRC-ETSI-119602).
- **Commission Implementing Decision (EU) 2015/1505:** technical specifications and formats for trusted lists under Article 22(5) (SRC-EC-ID-2015-1505).
- **EUDI ARF v3.0.0, chapter 6 Trust model:** which lists exist for which role and how they are used (SRC-ARF-TRUST).
- **eIDAS consolidated text, Articles 20 to 23:** audit, qualified status, trusted lists and the EU trust mark (SRC-EIDAS-CONSOL).

## Design choices and alternatives

1. **One format or two.** XML trusted lists for qualified services and JSON lists of trusted entities for wallet roles exist side by side. A relying party that handles both needs two parsers and two signature profiles.
2. **Status in the list or by absence.** Qualified services carry an explicit status with history. Most wallet-role lists show only currently approved entities and keep history in earlier list versions. Revocation latency therefore differs, which matters for the {% include concept-ref.html id="CON-LOA" %} a use case needs.
3. **Central or federated lists.** One Commission list of lists for the EU is simple to authenticate. Ecosystems such as data spaces may run their own lists; then {% include concept-ref.html id="CON-TRUST-LIST-DISCOVERY" %} and {% include concept-ref.html id="CON-MULTI-TRUST" %} decide which list applies.

## Examples

- **Qualified seal from another Member State.** A company receives a sealed invoice. The relying party locates the list of lists, verifies it, finds the issuer's national list, verifies that list, finds the service whose digital identity matches the signing certificate, checks that its status was granted when the seal was made, and accepts the seal.
- **Wallet provider removed.** A wallet provider loses its approval. It is removed from the Wallet Provider list or its status is set to invalid; issuers stop trusting its anchors and refuse to issue to its wallet units (ARF 6.2.3).
- **Business wallet provider (proposal).** A provider that wants to offer business wallets is notified to the supervisory body and appears on the Commission's machine-readable list of notified providers (proposal Articles 11 and 12). This is a proposal and may change.

## Open questions and limitations

- <span class="vtag v-todo">to verify</span> Whether Regulation (EU) 2024/1183 changed the wording of Article 22(3) and (4) was not checked; the consolidated text read shows the original wording.
- <span class="vtag v-todo">to verify</span> Whether Implementing Decision (EU) 2015/1505 has been amended or replaced was not checked.
- <span class="vtag v-todo">to verify</span> The full list of qualified service type identifiers in TS 119 612 was not enumerated; the JSON field names of TS 119 602 and the locations of the live lists of trusted entities were not checked.
- <span class="vtag v-todo">to verify</span> That V2.4.1 of TS 119 612 is the latest version was not confirmed.
- The proposal's article cross-references are inconsistent in the copy read (Article 12 refers to a paragraph 5 that the text does not contain); treat as a drafting issue until the next text version.
- The consolidated eIDAS text is a documentation tool without legal effect; check article numbers against the Official Journal text before citing.

## Terms introduced

- **Trusted list:** the signed list a Member State publishes of the qualified providers and services it is responsible for (eIDAS Article 22).
- **List of trusted lists (LOTL):** the Commission's signed list with pointers to the Member State lists and the certificates that sign them.
- **Scheme operator:** the body that issues and signs a trusted list.
- **Service digital identity:** the identity of a listed service, such as a certificate, used as trust anchor.
- **List of trusted entities (LoTE):** a list in the ETSI TS 119 602 data model, used for wallet-related roles.
- **Next update:** the date after which a list is treated as expired.

## References

SRC-EIDAS-CONSOL, SRC-ETSI-119612, SRC-ETSI-119602, SRC-ARF-TRUST, SRC-EC-ID-2015-1505, SRC-EBW-PROPOSAL. Full entries with version, date and URL are in the source register (`_data/graph/sources.yml`).

## Change log

| Date | Change | Reviewer |
|---|---|---|
| 2026-10-03 | First draft from ETSI TS 119 612 V2.4.1, TS 119 602 V1.1.1, eIDAS Articles 20 to 23, ARF chapter 6 and COM(2025) 838 | pending |
