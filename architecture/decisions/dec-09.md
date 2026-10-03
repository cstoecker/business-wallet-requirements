---
title: "DEC-09 Evidence, logging and audit"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 9
permalink: /architecture/decisions/dec-09/
description: "What is logged, by whom, with which integrity, retention and access rules, so that actions in a European Business Wallet are attributable and auditable without exposing employees unnecessarily? Facts from the sources, decision criteria, three options and the conditions under which each holds."
keywords: [logging, audit trail, evidence, retention, integrity, time stamp, registered delivery, preservation, transparency log, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-09 Evidence, logging and audit

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. The Commission Annex is not in the copy read. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

An organisation acts through its European Business Wallet: it signs, seals, sends, receives and grants access. Someone has to be able to show later what happened, when, and on whose authority. The decision fixes **what is logged**, **who keeps the log**, **which integrity, time, retention and access rules apply**, and **how far the log can serve as evidence** with counterparties, supervisors and in proceedings, without showing individual employees to more parties than necessary.

The accountability angle (who acted for the company) is treated in [DEC-02]({{ '/architecture/decisions/dec-02/' | relative_url }}); the logs of AI agents acting through the wallet are treated in [DEC-10]({{ '/architecture/decisions/dec-10/' | relative_url }}). This page does not repeat them. Roles for logs under data protection law are discussed in the research for DEC-08.

## What the requirement set says

The cluster K10 (evidence, logging and audit) carries this decision. The requirements that shape the options are:

{% include cluster-drivers.html cluster="K10" %}

Requirement candidates found in the research and not yet written as requirements: a log asset list derived from the risk assessment, log retention with backup and protection, audit events that cannot easily be deleted, a termination plan that keeps records accessible, and preservation evidence that uses qualified time stamps. Existing entries already cover log integrity and export (EBW-NFR-013, -014, -039, -040, -041, -049), UTC synchronisation (EBW-NFR-048) and records kept after cessation (EBW-OPS-007). Agent audit trails and AI Act logs are covered by EBW-AIF-034, -035, EBW-NFR-032, -033 and EBW-LEG-040 (see DEC-10).

## Facts from the sources

Each fact has a source and was read in the original text unless marked.

**Commission proposal and Council text.**
- Providers shall enable owners to "access a log of all transactions" and to export "communication logs, and interaction records" in a structured machine-readable format (proposal Article 5(1)(m) and 5(1)(l)). Access to wallets and functions is "controlled and auditable" (recital 18). Role-attribute mappings "are verifiable, auditable, revocable and traceable to their legitimate issuers" (Article 6(2)(b)).
- The owner's action "shall have the same legal effect as if the action had been lawfully carried out in person, in paper form" (Article 4). This gives records weight in dealings but is not an evidence rule.
- Council text: providers "shall provide an appropriate logging policy that shall include, at a minimum, electronic signing, electronic sealing, and notifications of all transactions" with relying parties, other business wallet units and EUDI Wallet units, "irrespective of whether the transaction is successfully completed" (Annex 7(1)). The log holds time and date, relying party name, contact details, unique identifier and Member State, the type of data requested and presented, and the reason for non-completion (Annex 7(2)). No field for the acting user or the authorisation used appears in 7(2).
- Council text: the provider must "ensure integrity, authenticity, availability and confidentiality of the logged information"; the back-end "shall log reports sent by the European Business Wallet user to the competent authorities"; logs are accessible to the provider "where it is necessary for the provision of European Business Wallets services"; they "shall remain accessible for as long as required to be accessible by Union law or national law" (Annex 7(3) to 7(6)).
- Council text: "all access and execution events are logged, timestamped, and bound to cryptographically verifiable proofs of authorisation, suitable for audit and legal proceedings" (Annex 12(2)(c)). Implementing acts shall cover "requirements for secure logging, timestamping and auditability of authorisation events" (Annex 12(4)(d)).
- When the provider ends service, owner data is transferred or deleted on instruction, and export covers communication logs and interaction records (Article 5(1)(l), 7(6)(f)). Providers shall "respond without undue delay to any request for information or documentation necessary to verify compliance" (Article 7(6)(d)); the audit powers of supervisory bodies beyond this were not analysed.

**eIDAS: qualified trust service providers and legal effect.**
- A qualified trust service provider shall "record and keep accessible for as long as necessary after the activities of the qualified trust service provider have ceased" all relevant information on data issued and received, for evidence in legal proceedings and for continuity (Article 24(2)(h)). It uses trustworthy systems to store data "in a verifiable form" so that only authorised persons make entries and changes and "the data can be checked for authenticity" (Article 24(2)(f)). Significant breaches are notified "without undue delay and in any event within 24 hours of the incident" (Article 24(2)(fb)).
- A qualified time stamp "is based on an accurate time source linked to Coordinated Universal Time" and carries a presumption of accuracy of date and time and of integrity (Articles 42(1)(b), 41(2)). Data sent through a qualified registered delivery service enjoys the presumption of integrity, of sending by the identified sender, of receipt by the identified addressee and of accuracy of date and time; the dates and times "are indicated by a qualified electronic time stamp" (Articles 43(2), 44(1)(f)).
- A qualified preservation service uses "procedures and technologies capable of extending the trustworthiness of the qualified electronic signature beyond the technological validity period" (Article 34(1)); it applies to seals under Article 40. The EUDI Wallet dashboard gives access to "a log of all transactions carried out through the European Digital Identity Wallet" (Article 5a(4)(d)).

**Implementing regulations.**
- EUDI Wallet instances "shall log all transactions with wallet-relying parties and other wallet units, including electronic signing and sealing" with four content fields; the provider ensures "integrity, authenticity and confidentiality of the logged information"; logs are accessible to the provider "on the basis of explicit prior consent by the wallet user"; they are kept "for as long as they are required by Union law or national law"; the user can export them (SRC-CIR-2024-2979, Article 9, not amended by CIR 2026/1731 as far as searched). The ARF adds that the Wallet Unit logs all transactions "including any transactions that were not completed successfully" (SRC-ARF-HLR, Topic 19).
- Qualified providers keep a termination plan "including how information is kept accessible in accordance with Article 24(2), point (h)", reviewed "at least every two years"; the records must allow evidence of compliance with Regulation (EU) No 910/2014 and Regulation (EU) 2016/679 and continued verification of earlier outputs (SRC-CIR-2025-2530, Article 3(1), 3(4), 3(7)(e), 3(8)). Where the Annex standards and Articles 1 to 3 differ, the Articles prevail (Article 4(2)).
- Registered delivery: "The ERDS shall generate and make available to legitimate interested parties ERDS evidence about ERD events" and "The ERDSP shall archive the evidence and/or evidence digests for each evidence that it issued" (SRC-CIR-2025-1944, Annex I, REQ-ERDS-5.4.1-06 and -07). Preservation: qualified preservation services ensure "long-term integrity, authenticity, proof of existence and accessibility of preservation evidence", and time stamps in preservation evidence "shall be qualified time-stamps" (SRC-CIR-2025-1946, recital 1 and Annex OVR-A-03).
- NIS2 implementing rules for trust service providers require procedures and tools "to monitor and log activities", logs that are maintained, documented and reviewed, a list of assets to be logged, logs kept and backed up "for a predefined period" and protected "from unauthorised access or changes", synchronised time sources and redundant logging systems (SRC-CIR-2024-2690, Annex 3.2.1 to 3.2.7). A trust service is significantly affected if it is unavailable "for more than 20 minutes" or if integrity, confidentiality or authenticity is compromised for "more than 0,1 % of users or relying parties" (Article 14).

**Standards.**
- EN 319 401 V3.2.1, clause 7.10: the provider keeps records accessible "for an appropriate period of time", "including after the activities of the TSP have ceased"; the confidentiality and integrity of current and archived records are maintained; the time used in the audit log is "synchronized with UTC at least once a day"; the retention period is "as notified in the TSP's terms and conditions"; events are logged "in a way that they cannot be easily deleted or destroyed" (SRC-ETSI-EN-319401-V3.2.1). Clause 7.9.1: logs cover network traffic, user administration, authentication events, privileged activity and access to critical configuration; they are backed up for a predefined period and protected from unauthorised access or changes. Annexes A and C map the clauses to DORA Article 30 and to CIR 2024/2690. The registered source SRC-ETSI-EN-319401 is V3.1.1, the version cited by CIR 2025/1944 and 2025/1946; V3.2.1 (2026-01) is the version read.
- EN 319 411-1 V1.5.1: "All security events shall be logged"; all revocation requests and the resulting action are logged; the retention period must be documented precisely; the CA key life-cycle event log and the registration documentation are kept "at least seven years after any certificate based on these records ceases to be valid"; "The TSP shall maintain the privacy of subject information" (SRC-ETSI-EN-319411-1).
- EN 319 522-1: an ERDS evidence is "an attestation provided by an ERDS that a specific event related to the process of transferring some specific data ... happened at a certain time"; it "can be used to prove to third parties, if needed also in legal proceedings"; an evidence repository keeps evidence for a period that depends on the service policy (SRC-ETSI-EN-319522-1).
- TS 119 511 V1.2.1 sets policy and security requirements for long-term preservation of digital signatures and of general data, with storage, no-storage and temporary-storage strategies (SRC-ETSI-119511); TS 119 512 V1.2.1 specifies the protocols between client and preservation service (SRC-ETSI-119512). Both were partly read: the scope clauses only. CIR 2025/1946 cites TS 119 511 as V1.1.1 (2019-06).

**Horizontal law.**
- AI Act: high-risk AI systems "shall technically allow for the automatic recording of events (logs) over the lifetime of the system"; providers keep logs for a period appropriate to the purpose, "at least six months, unless provided otherwise" in other Union or national law, "in particular in Union law on the protection of personal data" (SRC-AIACT, Article 12(1), 19(1)). Documentation is kept for 10 years after placing on the market (Article 18(1)); deployers keep logs for at least six months (Article 26(6)). Employer-deployers inform workers' representatives and the affected workers before using a high-risk system at the workplace (Article 26(7)). Whether the timetable for high-risk systems changed after the text of 13 June 2024 was not checked.
- NIS2 Article 21(2) lists ten minimum measures; logging is not named. Trust service providers fall under the implementing rules of Article 21(5). Significant incidents trigger an early warning "within 24 hours", and for trust service providers a notification "within 24 hours of becoming aware" (SRC-NIS2, Article 23(4)).
- DORA: contracts with ICT third-party providers include provisions on access, recovery and return of data on termination and, for critical or important functions, "unrestricted rights of access, inspection and audit" (SRC-DORA, Article 30(2)(d), 30(3)(e)(i)). The regulatory technical standard requires logging procedures covering access control, change, operations and network traffic, protection against tampering, detection of logging failure and clock synchronisation; the financial entity sets the retention period from its objectives, the reason for the log and the risk assessment (SRC-DORA-RTS-1774, Article 12).
- GDPR: identifiable data is kept "for no longer than is necessary" (Article 5(1)(e)); security includes the ability to ensure ongoing confidentiality, integrity, availability and resilience (Article 32(1)(b)) (SRC-GDPR).

**Protocol level.**
- OpenID4VP transaction data "enables a binding between the user's identification/authentication and the user's authorization", signed with the key used for proof of possession (SRC-OID4VP-1.0, 8.4). The specification defines no verifier-side audit record format (8.6). Wallet history "SHOULD NOT be accessible to anyone other than the End-User" (15.1).
- OpenID4VCI: parties should store credentials with privacy-sensitive data "only for as long as needed, including in log files" (SRC-OID4VCI-1.0, 15.3).

**Audit-log and transparency specifications.** These are options only; no law read mandates them, and no source read links them to the EBW or to eIDAS evidence rules.
- RFC 9162 (Certificate Transparency 2.0) provides "append-only logs of issued certificates" and is described as a general mechanism "that could be used for transparently logging any form of binary data" (SRC-RFC-9162, section 1).
- RFC 9943 (SCITT architecture, June 2026, Standards Track) likens registering a signed statement with a Transparency Service to "a notarization procedure" and has the service issue a receipt. Its scope text is "limited to use cases originating from the software supply chain domain" (SRC-RFC-9943, section 1). Only the introduction and terminology were read; the protocol sections and RFC 9942 (COSE receipts) were not.

**What no source read says.**
- No source read fixes a retention period for EBW transaction logs; the Council text refers to Union or national law. Reference points from other regimes: at least six months (AI Act), at least seven years after a certificate ceases to be valid (EN 319 411-1), 10 years for AI Act documentation, entity-defined (DORA technical standard) and "predefined period" (NIS2 rules).
- No source says which identifier of the acting person goes into the EBW log or how it is protected. Annex 12(2)(c) requires access events to be bound to proofs of authorisation, while Annex 7(2) lists no actor field.
- No source says whether the owner's copy or the provider's copy of a log is the authoritative evidence in proceedings.
- No source says how logs of an AI agent relate to the AI Act deployer logs (see DEC-10).

## Decision criteria

Criteria marked **source** are stated or implied by a source; **driver** means an architecture or business driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| L1 | Completeness: all transactions including failed ones, signing, sealing and notifications | source: Council Annex 7(1), CIR 2024/2979 Article 9 |
| L2 | Attribution: access and execution events bound to proofs of authorisation; acting user identity | source (partial): Council Annex 12(2)(c); the actor field is not stated in Annex 7(2) |
| L3 | Integrity, authenticity, availability and confidentiality of logs; tamper resistance | source: Council Annex 7(3), EN 319 401 clause 7.10, CIR 2024/2690 |
| L4 | Time: UTC-linked source, daily synchronisation, qualified time stamps for delivery events | source: eIDAS Articles 41 and 42, EN 319 401 7.10, DORA RTS Article 12 |
| L5 | Retention after the activity and after cessation of service | source (partial): eIDAS Article 24(2)(h), EN 319 401; no EBW period is fixed |
| L6 | Continuity: termination plans and accessibility of records after the provider ceases | source: CIR 2025/2530 Article 3, proposal Article 5(1)(l) |
| L7 | Access separation between user, owner, provider and authorities | source: Council Annex 7(5), CIR 2024/2979 Article 9 |
| L8 | Evidential value: presumptions for time stamps and delivery evidence; use in proceedings | source: eIDAS Articles 41 to 44, EN 319 522-1 |
| L9 | Long-term verifiability of signatures and seals in archived records | source: eIDAS Article 34, CIR 2025/1946, TS 119 511 |
| L10 | Minimisation and storage limitation in logs | source: GDPR Article 5(1)(e), OpenID4VCI 15.3 |
| L11 | Incident and supervision timelines that rely on logs | source: eIDAS Article 24(2)(fb), NIS2 Article 23(4), CIR 2024/2690 Article 14 |
| L12 | Export and portability of logs | source: proposal Article 5(1)(l) and (m), CIR 2024/2979 Article 9 |
| L13 | Employee exposure: which log view shows which person to whom (owner administrator, auditor, authority, counterparty) | driver |
| L14 | Third-party verifiability without trusting the provider | driver |
| L15 | Cost, storage volume and operational burden for small owners | driver |
| L16 | Cross-border admissibility beyond the equivalence rule (national procedural law) | driver |
| L17 | Alignment with AI agent audit needs (principal and agent recorded separately) | driver; see DEC-10 |

## Options

### (a) Provider-operated log under trust-service-provider style controls

The provider keeps a tamper-resistant transaction and access log under policies modelled on EN 319 401 and the NIS2 rules for trust service providers, and gives owners access and export.

**What the sources enable.** A direct fit to Council Annex 7 and 12 and to CIR 2024/2979 Article 9. Established controls for integrity, time and archiving (EN 319 401 clauses 7.9.1 and 7.10). The same controls are already assessed for qualified providers, and export and termination duties are already stated.

**What they restrict.** The owner depends on the provider for availability and for evidence after exit, unless the export is complete and verifiable. Provider access to logs is limited to necessity (Council) or consent (EUDI Wallet), which constrains analytics. Retention periods must be set by the provider and stated in its terms.

**What they leave open.** Whether the provider's copy or the owner's export is the evidence, how user identity is represented, and how long logs are kept after termination.

### (b) Owner-held evidence store with provider-signed receipts

The provider issues signed, time-stamped receipts per event; the full record sits with the owner, who is responsible for retention and access.

**What the sources enable.** Owner control and minimisation at the provider. Qualified time stamps and registered delivery evidence already exist as signed evidence, and portability is a core function.

**What they restrict.** The owner, including a small firm, has to run archiving and long-term preservation (TS 119 511 and 119 512, qualified preservation services). Provider-side duties for logs of its own operation remain (CIR 2024/2690, EN 319 401 7.9.1). Breach investigation by the provider may be harder without full logs.

**What they leave open.** How receipts are verified after the provider ends service, who is liable for lost owner archives, and how supervisors access owner-held logs.

### (c) Provider log plus an external transparency or preservation layer

Option (a) plus an external, independently verifiable layer for selected events: qualified time stamps, qualified preservation, or a transparency log with receipts (RFC 9162 style or SCITT style).

**What the sources enable.** Third-party verifiability and detection of log tampering. Legal presumptions where qualified time stamps or preservation are used. Long-term proof of existence of signed records (CIR 2025/1946).

**What they restrict.** Neither transparency specification is mandated by law or tied to the EBW, and the published scope of SCITT is software supply chains. Publishing events can conflict with minimisation and confidentiality unless only digests are published. Qualified services have a cost per event, which no source quantifies.

**What they leave open.** Which events are anchored, whether the provider or the owner anchors them, and how deletion requests under data protection law interact with append-only structures (not addressed in any source read).

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | (a) provider log | (b) owner store with receipts | (c) provider log plus external layer |
|---|---|---|---|
| L1 Completeness | Council Annex 7(1) and CIR 2024/2979 Article 9 describe this form | Not stated for receipts; full record with the owner | As (a) |
| L2 Attribution | Annex 12(2)(c) binds events to proofs of authorisation; actor field not stated | Not stated | As (a); anchoring adds no actor information (not stated) |
| L3 Integrity and tamper resistance | EN 319 401 7.10 and CIR 2024/2690 controls | Provider signs receipts; owner archive controls not stated | Adds append-only structures or qualified evidence (RFC 9162, eIDAS) |
| L4 Time | UTC synchronisation (EN 319 401 7.10) | Qualified time stamps exist (eIDAS Article 42) | Qualified time stamps for selected events |
| L5 Retention | Set by the provider and stated in terms (EN 319 401) | Owner sets it; not stated | As (a); retention of anchored digests not stated |
| L6 Continuity after exit | Termination plan and export (CIR 2025/2530, proposal Article 5(1)(l)) | Depends on owner archive; receipt verification after exit not stated | As (a), with externally held proofs |
| L7 Access separation | Provider access by necessity (Council Annex 7(5)) | Owner-controlled; supervisor access not stated | As (a) |
| L8 Evidential value | Which copy is evidence is not stated | Presumptions where qualified services are used | Presumptions where qualified services are used |
| L9 Long-term verifiability | Not stated for EBW logs | Owner needs preservation (CIR 2025/1946) | Qualified preservation available |
| L10 Minimisation | Provider holds the full log | Provider holds receipts only | Digests only, if so designed (not stated) |
| L12 Export | Core function (Article 5(1)(l)) | Record already with the owner | As (a) |
| L14 Verifiability without trusting the provider | Not stated | Receipts signed by the provider | Transparency log or qualified evidence |
| L15 Cost for small owners | Not stated; provider price not stated | Owner runs archiving | Cost per event for qualified services; not quantified |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Three observations follow from the facts.

1. **Option (a) is the baseline the texts already describe.** The Council Annex 7 and 12 and CIR 2024/2979 Article 9 describe a provider-side log with integrity, confidentiality and limited provider access, and EN 319 401 gives the control set. It does not by itself settle which copy is evidence or how the acting person is recorded.
2. **Option (b) moves duties to the owner that the sources place on providers.** Archiving, preservation and retention are stated for providers; for small owners the sources do not say how they would be met. It fits better as an export format than as the primary store.
3. **Option (c) adds evidential value only where the events matter.** Qualified time stamps and registered delivery evidence carry presumptions in eIDAS; the transparency specifications are not tied to the EBW and would be a project choice. If an external layer is used, publishing digests rather than event content is the form that fits the minimisation criterion.

On employee exposure (L13), the sources point in two directions: Annex 12(2)(c) asks for attribution to proofs of authorisation, while the Council log fields in Annex 7(2) name no actor. A working split is a log that records the authorisation used for each event and shows the person identifier only to roles that need it. Which roles those are is a driver to be confirmed (see the employment-law question in the gaps below).

**Conditions under which this reading holds.** The final text keeps the Council Annex 7 and 12 content or an equivalent; the implementing acts under Annex 12(4)(d) do not require a different log structure; the retention period is fixed by Union or national law or by the provider's terms; stakeholders confirm the drivers L13 to L17.

**What would change it.** The Commission Annex or the implementing acts on secure logging and timestamping; a retention period set for EBW logs; a rule that names the actor identifier in the log; a source that makes a transparency log or SCITT applicable to the EBW; a clarification of which copy is evidence; the AI Act timetable amendments, which were not checked.

## Evidence gaps and next steps

- Obtain the Annex of COM(2025) 838, the implementing acts under Council Annex 12(4) and the outcome of the Council meeting on 9 June 2026, then re-check the logging provisions. <span class="vtag v-todo">to verify</span>
- Settle which retention period applies to EBW logs and who sets it. <span class="vtag v-todo">to verify</span>
- Settle whether the owner's administrators may see the identity of each acting user, and under which employment-law constraints (see the research for DEC-08). <span class="vtag v-todo">to verify</span>
- Read what was read for scope only or not at all: TS 119 511 and 119 512 beyond clause 1, EN 319 522-2 (evidence semantics) and EN 319 521, RFC 9942 (COSE receipts) and the protocol sections of RFC 9943, and CIR 2025/2160 (risk management framework referenced by CIR 2025/2530). No W3C audit-log specification was identified.
- Check NIS2 national transposition, the Commission list of reference standards for qualified trust services beyond CIR 2025/2530, and the AI Act timetable amendments (digital omnibus). <span class="vtag v-todo">to verify</span>
- Write the requirement candidates listed under "What the requirement set says" and review them with a named reviewer.
- Confirm the business drivers L13 to L17 with stakeholders; they are assumptions until then.

## References

SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26, SRC-EIDAS-CONSOL, SRC-CIR-2024-2979, SRC-ARF-HLR, SRC-CIR-2025-2530, SRC-CIR-2025-1944, SRC-CIR-2025-1946, SRC-CIR-2024-2690, SRC-ETSI-EN-319401-V3.2.1, SRC-ETSI-EN-319411-1, SRC-ETSI-EN-319522-1, SRC-ETSI-119511, SRC-ETSI-119512, SRC-AIACT, SRC-NIS2, SRC-DORA, SRC-DORA-RTS-1774, SRC-GDPR, SRC-OID4VP-1.0, SRC-OID4VCI-1.0, SRC-RFC-9162, SRC-RFC-9943. Full entries with version, date and URL are in the source register.
