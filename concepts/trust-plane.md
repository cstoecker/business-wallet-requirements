---
title: "Trust plane"
layout: concept
concept: CON-TRUST-PLANE
parent: Concepts
grand_parent: Start here
description: "The trust plane answers who or what a relying party can trust and why: supervised qualified providers on signed trusted lists, lists of trusted entities for wallet roles, and status information, as set out in eIDAS, ETSI trusted-list standards and the EUDI trust model."
permalink: /concepts/trust-plane/
schema_type: TechArticle
keywords: [trust plane, trusted list, qualified trust service provider, list of trusted entities, supervisory body, relying party, eIDAS, European Business Wallet, ETSI TS 119 612, ETSI TS 119 602]
about: [Trust plane, Trusted list, Qualified trust service provider, eIDAS, European Business Wallet]
last_verified: "2026-10-03"
figures: [trust-plane-concept-model, trust-plane-flow]
faq:
  - q: "What is the trust plane in a European Business Wallet architecture?"
    a: "The trust plane is the part of the architecture that establishes who or what can be trusted and why. It consists of supervised providers, signed trusted lists and lists of trusted entities, and status information about providers and credentials. It does not decide who may do what; that is the control plane."
  - q: "Who maintains the trusted lists?"
    a: "Under Article 22 of Regulation (EU) No 910/2014 each Member State establishes, maintains and publishes trusted lists of the qualified trust service providers it is responsible for. The Commission publishes information on the bodies that run them. For wallet-related roles, the EUDI ARF describes lists of trusted entities provided by the Commission."
  - q: "Does the European Business Wallet proposal use trusted lists for wallet providers?"
    a: "The articles read in the proposal COM(2025) 838 use notification to a supervisory body and a list of notified wallet providers published by the Commission, plus a European Digital Directory. They do not describe a trusted list for wallet providers. The proposal is not adopted law and may change."
---

## Summary

The trust plane is the part of an architecture that answers one question for a relying party: who or what can I trust, and why. In the European framework the answer rests on three things: providers that are supervised and audited, signed lists that say which providers and services currently hold that status, and status information that says whether a provider or credential is still valid. The trust plane supplies these facts; it does not decide what a party may do with them.

## Definition

{% include concept-definition.html id="CON-TRUST-PLANE" %}

What it is not. It is not the control plane, which evaluates policies and makes authorisation decisions using trust facts. It is not the data plane, which moves credentials and evidence. And it is not a technology: a trust anchor is a role that a signing key or certificate plays, and the word "trust anchor" itself does not occur in the consolidated eIDAS text (the ARF uses it).

## Why it matters

A relying party cannot check every counterparty itself. It relies on rules, supervision and published lists that others maintain. The ARF puts it this way: trust is "primarily rooted in authority and in procedural measures", such as oversight, policies and audits ({% include concept-ref.html id="CON-LOA" %} describes how much confidence each kind of result gives).

- **B2B.** A company that receives a sealed document or a credential from a supplier checks that the issuing service is a qualified trust service listed on a trusted list.
- **B2G.** An authority that accepts a report from a business relies on the same lists to trust the seal and the timestamp ({% include concept-ref.html id="CON-B2G-REPORTING" %}).
- **B2C.** A wallet of a natural person checks that an issuer or relying party is registered or listed before it shares data.

## How it works

{% include figure.html id="trust-plane-concept-model" no=1 %}

**Oversight and audit.** A qualified trust service provider is audited at least every 24 months by a conformity assessment body; the audit report goes to the supervisory body (eIDAS Article 20(1)). A qualified provider is one that "is granted the qualified status by the supervisory body" (Article 3(20)).

**Qualified status and the trusted list.** A provider that intends to start a qualified service notifies the supervisory body with a conformity assessment report. The supervisory body verifies compliance, grants the status and informs the body that maintains the trusted list, which updates it within three months. The provider may begin the qualified service only after the status is indicated in the list (Article 21). Each Member State establishes, maintains and publishes its trusted lists; they are electronically signed or sealed and suitable for automated processing (Article 22(1) and (2)). The Member State notifies the Commission of the list body, the place of publication and the signing certificates, and the Commission publishes this information in signed form (Article 22(3) and (4)). The format and the mechanisms for locating, accessing and authenticating a trusted list are specified in ETSI TS 119 612.

**Lists of trusted entities for wallet roles.** For roles around the EUDI Wallet, the ARF describes lists of trusted entities provided by the Commission: wallet providers are notified by the Member State and their trust anchors are included in a wallet provider list; PID providers and providers of attestations issued by public sector bodies are notified and listed; non-qualified attestation providers are not notified. ETSI TS 119 602 defines the data model for such lists and generalises TS 119 612.

**Status.** A revoked qualified electronic attestation of attributes loses its validity and that status cannot be reverted (Article 45d(4)). In the ARF, a provider whose status is set to invalid in a list is no longer trusted, and issuers refuse to issue to its wallet units; relying-party registration certificates use a status list.

## Interaction flow

{% include figure.html id="trust-plane-flow" no=2 %}

1. The provider notifies the supervisory body with a conformity assessment report (Article 21(1)).
2. The supervisory body verifies compliance and grants qualified status (Article 21(2)). If it is not granted, the provider has to rework; the regulation text read does not describe the loop in detail, so the figure shows it only as the logical alternative. <span class="vtag v-todo">to verify</span>
3. The list body updates the trusted list, not later than three months after the supervisory body informs it (Article 21(2)).
4. The provider may begin the qualified service after the status is shown in the list (Article 21(3)) and may then use the EU trust mark and must link to the list on its website (Article 23).
5. Relying parties validate signatures, seals and credentials against the list and check status (ETSI TS 119 612; ARF chapter 6).

## Roles and responsibilities

| Role | Responsibility | Source |
|---|---|---|
| Supervisory body | grants qualified status, supervises; designated bodies for the wallet framework under Article 46a | eIDAS Articles 21, 46a |
| Conformity assessment body | audits qualified providers at least every 24 months | eIDAS Article 20 |
| Member State | establishes, maintains and publishes trusted lists; notifies the Commission | eIDAS Article 22 |
| Commission | publishes list information; provides lists of trusted entities for wallet roles | eIDAS Article 22; ARF chapter 6 |
| Qualified trust service provider | provides qualified services after listing; keeps functionally separate QEAA services | eIDAS Articles 21, 45g(3) |
| Wallet provider and attestation provider | notified or registered according to role; status can be set to invalid | ARF chapter 6 |
| Relying party | validates against lists and status; is registered and receives access certificates | ARF chapter 6 |

## Related concepts

- {% include concept-ref.html id="CON-TRUST-LIST" %} describes the list itself and its governance.
- {% include concept-ref.html id="CON-TRUST-LIST-DISCOVERY" %} describes how a relying party finds the right list.
- {% include concept-ref.html id="CON-LOA" %} describes how much assurance each result carries.
- {% include concept-ref.html id="CON-MULTI-TRUST" %} describes what changes when several trust domains meet.
- {% include concept-ref.html id="CON-CONTROL-PLANE" %} uses trust facts to make authorisation decisions.
- {% include concept-ref.html id="CON-DATA-PLANE" %} carries the credentials and evidence that the trust plane vouches for.

## Requirements and obligations

Obligations found in the sources, not yet derived into EBW requirements (each still needs a technology-neutral requirement and a named reviewer). Categories: TRU, GOV.

| Source obligation | Source | Candidate category |
|---|---|---|
| Qualified providers are audited at least every 24 months | SRC-EIDAS-CONSOL, Article 20(1) | CER |
| A qualified service starts only after the status is shown in the trusted list | SRC-EIDAS-CONSOL, Article 21(3) | TRU |
| Trusted lists are signed or sealed and machine-processable | SRC-EIDAS-CONSOL, Article 22(2) | TRU |
| Wallet providers must be on the Commission list of notified providers (proposal) | SRC-EBW-PROPOSAL, Articles 7(1) and 12 | GOV |
| The Commission runs a European Digital Directory for wallet owners (proposal) | SRC-EBW-PROPOSAL, Article 10 | FUN |
| Relying parties use trust anchors to check credentials and status | SRC-ARF-TRUST, chapter 6 | TRU |
| Issuers register before testing; wallets and relying parties validate against the lists (pilot) | SRC-WEBUILD-ARCH, ADR trusted-lists | TRU |

## Standards and specifications

- **ETSI TS 119 612 V2.4.1 (2025-08), Trusted Lists:** format and mechanisms for establishing, locating, accessing and authenticating a trusted list (SRC-ETSI-119612).
- **ETSI TS 119 602 V1.1.1 (2025-11), Lists of trusted entities, data model:** generalises TS 119 612; profiles for lists of wallet providers, PID providers, access certificate providers and public sector attestation issuers (SRC-ETSI-119602).
- **EUDI ARF v3.0.0, chapter 6 Trust model:** roles, notification and registration, certificates and status (SRC-ARF-TRUST).
- **WE BUILD ADR "trusted lists":** the pilot's Trust Registry group provides the lists, starting from TS 119 612 V2.3.1, an older version than V2.4.1 (SRC-WEBUILD-ARCH).

## Design choices and alternatives

1. **Where the list lives.** Member State trusted lists for qualified services, Commission lists of trusted entities for wallet roles, or a consortium list of lists in a pilot. The more lists, the more important discovery becomes.
2. **Notification versus listing.** The proposal for the European Business Wallet, as read, uses notification to a supervisory body plus a Commission list and directory, not a trusted list for wallet providers; qualified trust service providers are exempt from the review step (Article 11(3)).
3. **Offline versus online status.** Checking signed lists periodically is cheap; checking status at every use costs more but detects revocation sooner. The choice depends on the {% include concept-ref.html id="CON-LOA" %} that the use case needs.

## Examples

- **Qualified attestation provider.** A company wants to issue qualified attestations. It notifies the supervisory body with an audit report; after qualified status it appears on the national trusted list and may start (eIDAS Articles 21 and 22).
- **Failing wallet provider.** A wallet provider fails its certification. The Member State has its status set to invalid in the wallet provider list, and issuers refuse its wallet units (ARF 6.2.3).
- **Business wallet provider (proposal).** A qualified trust service provider that wants to offer business wallets notifies the supervisory body, which informs the Commission within two working days; the provider may then offer wallets and appears on the Commission list (proposal Articles 11(3) and 12). This is a proposal and may change.

## Open questions and limitations

- <span class="vtag v-todo">to verify</span> The proposal's Article 7 refers to "Article 12(5)" while the Article 12 text read has three paragraphs; treat as a drafting inconsistency until the next text version.
- <span class="vtag v-todo">to verify</span> The ARF states that qualified attestation providers appear on the Article 22 trusted lists; that sentence was not found in the regulation text read.
- <span class="vtag v-todo">to verify</span> That ETSI TS 119 612 V2.4.1 is the latest version, and the content of ARF Topic U (EUDI Wallet trust mark), were not confirmed.
- The consolidated eIDAS text is a documentation tool without legal effect; article numbers must be checked against the Official Journal text before a legal citation.
- The ARF source repository could not be read; the published rendering at eudi.dev was used.
- Council documents ST 7659/26 and ST 9684/26 on the proposal were not yet read.

## Terms introduced

- **Trust service provider:** provides one or more trust services, qualified or non-qualified (Article 3(19)).
- **Qualified trust service provider:** granted qualified status by the supervisory body (Article 3(20)).
- **Trusted list:** the signed list that a Member State publishes of the qualified providers and services it is responsible for (Article 22).
- **List of trusted entities (LoTE):** list of trusted entities in the ETSI TS 119 602 data model, used for wallet-related roles.
- **Trust anchor:** the key or certificate that a relying party takes as the starting point of trust (term used by the ARF).
- **Status information:** information on whether a provider, certificate or credential is still valid.

## References

SRC-EIDAS-CONSOL, SRC-EBW-PROPOSAL, SRC-ETSI-119612, SRC-ETSI-119602, SRC-ARF-TRUST, SRC-WEBUILD-ARCH. Full entries with version, date and URL are in the source register (`_data/graph/sources.yml`).

## Change log

| Date | Change | Reviewer |
|---|---|---|
| 2026-10-03 | First draft from the sourced research briefing | pending |
