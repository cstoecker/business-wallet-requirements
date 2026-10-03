---
title: "DEC-02 Employees: EUDI Wallet or business wallet"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 2
permalink: /architecture/decisions/dec-02/
description: "Should employees act for their company with a personal EUDI Wallet, with users and authorisations inside the organisation's European Business Wallet, or with both? Facts from the sources, decision criteria, three options and the conditions under which each holds."
keywords: [employee wallet, EUDI Wallet, European Business Wallet, mandate, representation, authorisation, delegation, power of attorney, B2E]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-02 Employees: EUDI Wallet or business wallet

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. Analysis, not legal advice.*

## Question

A company wants its employees to sign, submit, authenticate and receive notifications on its behalf. Three setups are conceivable:

- **(a)** the employee uses a **personal EUDI Wallet** and receives attestations of mandate or employment;
- **(b)** the employee is a **user inside the organisation's European Business Wallet**, with authorisations managed by the owner;
- **(c)** a **hybrid**: the organisation's wallet holds authority and acts for the organisation, the personal wallet carries the person.

The decision touches clusters K02 (wallet subject model), K03 (mandates and delegation), and through them key custody, revocation, audit and privacy.

## What the requirement set says

The requirement set carries this decision only thinly. K02 has three tagged requirements and K03 twelve. The requirements that decide between the options are:

{% include cluster-drivers.html cluster="K03" %}

{% include cluster-drivers.html cluster="K02" %}

Gaps in the set (facts found in the research, not yet written as requirements): the definition of the EBW user (Article 3(22)), the right of representatives to request revocation of the wallet unit attestation (Article 7(6)(c)), the limit of the EUDI Wallet mandate to natural persons (recital 55, Article 20), the possible limit of free qualified signing to non-professional purposes (eIDAS Article 5a(5)(g)), the right-to-act check of attestation issuers (Regulation (EU) 2025/1569, Annex II, point 2(a)), and the ARF rules on representation attestations. They are candidates for the next requirement pass.

## Facts from the sources

Each fact has a source and was read in the original text unless marked.

**Who is owner, user and representative.**
- The owner of an EBW is "an economic operator or public sector body" (proposal Article 3(7)). A *user* is "a natural or legal person, or a natural person representing another natural person or a legal person, that uses European Business Wallets" (Article 3(22)); eIDAS Article 3(5a) uses the same wording for its own users.
- Recital 18 of the proposal names employees: the owner "can delegate authority to multiple users, including employees or other authorised natural or legal persons". It describes an administrative mandate, which assigns roles inside the organisation, and a technical mandate. Access to the wallet must be "controlled and auditable".
- The owner can "authorise multiple users" and "manage and revoke such authorisations" (Article 5(1)(j)). Role conflicts, over-delegation and expired authorisations must be detected and prevented in real time, and role-attribute mappings must be verifiable, revocable and traceable to their issuers (Article 6(2)(b)).
- The Council text deletes the definitions of *authorised representative* and *mandate* and replaces them with *authorisation* and *EBW user*. It states that EBW authorisations do not create or limit any power of attorney under national or Union law, so the legal capacity to act stays with national and Union law.
- No source in the read set mentions a *sub-wallet*. One owner may have several wallets (financial statement of the proposal); a wallet unit is provided to a specific owner (Article 3(25)).

**Personal EUDI Wallet.**
- eIDAS already contemplates a natural person representing a legal person (Article 3(5a), Article 5a(5)(f)). The person identification data annex of Regulation (EU) 2024/2977 has a table of legal-person identification data, and Annex VI of eIDAS lists "powers and mandates to represent natural or legal persons" as an attribute category. Issuers of attestations must verify that the requester "has the right to act" for the subject (Regulation (EU) 2025/1569, Annex II).
- The user has "full control" of the EUDI Wallet (Article 5a(14)). Only the wallet provider, the provider of the attestation or the user can revoke the wallet unit attestation or an attestation (Regulations 2024/2979 Article 7(1), 2024/2977 Article 5(2), 2025/1569 Article 4(2)). No source gives an employer a revocation path for a personal wallet, and none names the end of employment as a trigger.
- Free qualified signing for natural persons may be limited by Member States to non-professional purposes (Article 5a(5)(g)).
- The proposal restricts the mandatory EUDI Wallet to natural persons (recital 55, Article 20). The ARF has removed the legal-person wallet ("Topic 28" is empty), and its representation work (discussion paper, Topic I) leaves out a natural person representing a legal person.

**Between the two wallets.**
- The EBW must be able to request, share and issue attestations to and from EUDI Wallets (Article 5(1)(c) and (f)); onboarding of the EBW can use a representative's electronic identification means (Article 6(1)(e)); in the Council text a user authenticates with a notified eID of at least substantial level (Annex, point 1).
- The draft rulebooks of WE BUILD show both patterns: an *Employee* attestation issued into the employee's natural-person wallet, and *Contact person* attestations held in the company wallet. The EBWOID rulebook says a relying party should also ask for the representative's person identification data. The organisation, as issuer, can revoke the attestations it issued.

**Signing and sealing.** A signature is made by a natural person, a seal by a legal person (eIDAS Article 3(9) and (24)). The EBW core function is to "sign by means of qualified electronic signatures and seal by means of qualified electronic seals, as applicable" (Article 5(1)(d)).

**Exit, liability, privacy.** The owner can export data, and providers must transfer or delete owner data on instruction (Article 5(1)(l), 7(6)(f)). Wallet revocation grounds concern the owner (request, compromise, cessation of activity), not the departure of a single user (Article 6(2)(f)). No source allocates liability between owner, employee and provider for acts done through an EBW; provider liability for trust services is in eIDAS Article 13. The GDPR applies (recital 39), but no employee-specific rules were found.

**Acceptance.** Public sector bodies must enable economic operators to use the EBW core functions 24 months after entry into force (Article 16). The text does not say whether a personal EUDI Wallet is an accepted channel for employees.

## Decision criteria

Criteria marked **source** are stated in a source; **driver** means an architecture or business driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| C1 | Organisational control and revocation when an employee leaves | source (partial): owner manages and revokes authorisations; driver: the exit event and its speed |
| C2 | Continuity of authority when staff change | driver |
| C3 | Separation of private and professional use | driver; related: Article 5a(5)(g), 5a(14) |
| C4 | Accountability: who acted, on whose authority | source: Article 4, Article 5(1)(m), Council Annex 12 |
| C5 | Liability allocation between company, employee and provider | driver; only provider liability is stated |
| C6 | Delegation chains and their limits | source: Article 3(1)(c), 6(2)(b); depth limits are a driver |
| C7 | Segregation of duties and multi-party approval | source: role conflicts (Article 6(2)(b)); four-eyes approval is a driver |
| C8 | Audit trail | source: Article 5(1)(m), recital 18, Council Annex 7 and 12 |
| C9 | Authority limits (scope, validity, constraints; amounts) | source (partial): Council Annex 12(1)(c), ARF RP_01; amounts are a driver |
| C10 | Cost and onboarding effort, especially for small companies | source (partial): no obligation for companies; EUDI Wallet free for natural persons |
| C11 | HR and identity-management integration (joiner, mover, leaver) | source (partial): automatic interaction, role mappings; interfaces are a driver |
| C12 | Privacy of the employee | source (partial): GDPR, Article 5a(14); employee rules are a driver |
| C13 | Cross-border acceptance and legal effect | source: Article 4, 16, 45b(3) |
| C14 | Assurance level of the acting person and of the wallet | source: Article 5a(11), 6(1)(e), Council Annex 1 |
| C15 | Key custody; who can seal and who can sign | source (partial): Article 3(9), 3(24), 3(25) to (29) |
| C16 | Provider dependency and data exit for the organisation | source: Article 5(1)(l), 7(6)(f) |

## Options

### (a) Personal EUDI Wallet with mandate attestations

**What the sources enable.** The pattern exists in eIDAS terms (a natural person representing a legal person), issuers must check the right to act, and the employer can be the issuer of an employee or authorisation attestation that it can revoke as issuer. QES and assurance level high come with the wallet, free for natural persons, and sole traders can use it for registered delivery and signing without a full EBW.

**What they restrict.** The wallet is under the user's full control, and no employer revocation path exists for the wallet or the person identification data. Free qualified signing may be limited to non-professional use. The ARF has no legal-person wallet and no description of this pattern. A personal wallet cannot seal for the company, because a seal needs a legal-person creator. The acceptance duty in Article 16 is defined for the EBW core functions. Usage logs belong to the user, and provider access needs the user's consent.

**What they leave open.** Whether professional use of a personal wallet is permitted beyond signing, who is the controller for employee wallet data, how a relying party learns in real time that an employee's authority ended (status checks against short-lived attestations, ARF RP_02), and the legal weight of a non-qualified employer attestation of mandate compared with a qualified or register-based one.

### (b) Users and authorisations inside the organisation's EBW

**What the sources enable.** The owner is the legal person; multi-user authorisation with roles and owner-side revocation is a core function, employees are named in recital 18, and the proposal calls for logs, auditability and detection of role conflicts. The core functions come with the public-sector acceptance duty, and equivalence of legal effect (Article 4) applies to the owner's actions. Owner-level export, transfer and deletion are specified.

**What they restrict.** The proposal is not law, the Commission and Council texts differ (mandate deleted, authorisations "technical", onboarding level raised to high), and the Commission's annex was not available in the copy read. The user still needs a personal means to authenticate, so the employee does not go without a personal credential. No source describes employee-level wallet units, and authorisations do not replace statutory or delegated legal authority. The provider can read EBW logs where necessary. Application is at the earliest one year after entry into force, and the interim period under eIDAS alone is a risk named by the WE BUILD architecture decision on the LPID.

**What they leave open.** Whether an employee signs with a personal qualified certificate or the company seals ("as applicable"), how individual attribution appears in the log, key custody and recovery at the provider, what happens to the employee's personal certificates at exit, who is controller for user data in the wallet, and the interfaces to HR and identity management.

### (c) Hybrid

**What the sources enable.** The sources already couple the two wallets: the EBW exchanges attestations with EUDI Wallets, onboarding uses a representative's eID, and the EBWOID rulebook expects the representative's person identification data next to the EBWOID. Concerns separate naturally: owner-controlled authorisation and organisational acts in the EBW, person-bound identity and personal qualified signatures in the EUDI Wallet.

**What they restrict.** There are two revocation regimes with different controllers (owner for authorisations, issuer for attestations in the personal wallet, user and provider for the wallet and the person identification data), and no source defines how they propagate. Relying parties need rules for three presentations: EBWOID alone, EBWOID with person identification data, or an attestation in a personal wallet. The ARF leaves legal-person identity out of scope, and WE BUILD replaces the LPID with the EBWOID.

**What they leave open.** Which acts run under the organisation's identity and which under the person; how the employee's identity is disclosed in B2G submissions (privacy against accountability); who issues mandate attestations (the company, a qualified provider or a register); what the public sector accepts (Article 16 is silent on person identification data plus a mandate); data protection roles across two wallets; cost per employee for two wallet types; recognition of the EU digital power of attorney under Directive (EU) 2025/25, which was not read.

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | (a) personal wallet | (b) EBW users | (c) hybrid |
|---|---|---|---|
| C1 Employer revocation on exit | Only through issuer-revocable attestations; none for wallet or PID | Owner revokes user authorisations (Article 5(1)(j)) | Owner revokes in EBW; attestations by issuer; propagation not stated |
| C3 Private and professional separation | Not stated; QES may be limited to private use | Separate by construction (owner-level wallet) | Separate by construction for organisational acts |
| C4 Accountability | Log belongs to the user | Owner-level log, provider access where necessary | Both logs; linkage not stated |
| C7 Segregation of duties | Not stated | Role conflicts detected (Article 6(2)(b)) | As (b) for organisational acts |
| C13 Acceptance | Not stated for employees | Core functions carry the acceptance duty (Article 16) | As (b) for organisational acts |
| C14 Assurance | Wallet at high (Article 5a(11)) | User authentication at least substantial; onboarding substantial or high (Council: high) | Both |
| C15 Seal and sign | Signature yes, seal no | Seal and signature "as applicable" | Seal in EBW, signature in EUDI Wallet |
| C16 Exit and portability | EUDI Wallet portability (natural person) | Export, transfer, deletion, import (Council) | Both regimes |
| C10 Cost for small firms | EUDI Wallet free for natural persons | No obligation; provider price not stated | Two wallet types |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Three observations follow from the facts.

1. **Option (a) alone does not meet the control criteria.** The decisive difference is C1 and C2: the sources give the employer no revocation path for a personal wallet or person identification data, and they let the person keep full control. An employer can only revoke attestations it issued, which works if relying parties check their status. This makes (a) suitable as a *binding of the person*, not as the only instrument of organisational authority.
2. **Option (b) alone depends on text that is not final.** Multi-user authorisation, role-conflict detection and owner-side revocation are exactly the organisational controls the business criteria ask for, but the Council text weakens the legal meaning of authorisations and the Commission annex was not available. The employee still authenticates with a personal eID, so (b) does not remove the person-side credential.
3. **Option (c) follows the structure the sources already imply.** The proposal itself ties the EBW to the EUDI Wallet in three places, and the WE BUILD rulebooks use both patterns. A working split is: **organisational acts and authority in the EBW** (seals, B2G submissions, owner-controlled authorisations with revocation), **person-bound acts in the EUDI Wallet** (qualified signature, identity of the representative), and **mandates as attestations** issued by the company or a register, with short validity or checked status.

**Conditions under which this reading holds.** The final text keeps Article 5(1)(j) and Article 6(2)(b) (or an equivalent owner-side authorisation and revocation function); relying parties are willing to check an authorisation attestation next to the EBWOID; and the Annex provides the access-control and logging requirements that the Council text has.

**What would change it.** An adopted text that drops multi-user authorisation (then option (a) with employer-issued attestations remains); a rule that lets employers revoke or suspend professional use of a personal wallet; a Commission or ARF specification of the natural person representing a legal person; the Directive (EU) 2025/25 rules on the EU digital power of attorney; a clarified allocation of liability.

## Evidence gaps and next steps

- Obtain the Annex of COM(2025) 838 and the outcome of the Council meeting on 9 June 2026, then re-check Articles 3, 5, 6 and 7.
- Read Directive (EU) 2025/25 (digital power of attorney), the Parliament draft report, the EESC opinion and the EDPS comments on the proposal.
- Write the missing requirements (see "What the requirement set says") and review them with a named reviewer.
- Test the hybrid pattern in the WE BUILD pilot setting with the employee and contact-person rulebooks: exit of an employee, status check by a relying party, B2G submission with and without person identification data.
- Confirm the business drivers (C2, C3, C5, C7, C9, C11, C12) with stakeholders; they are assumptions until then.

## References

SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26, SRC-COUNCIL-ST-7659-26, SRC-EIDAS-CONSOL, SRC-CIR-2024-2977, SRC-CIR-2024-2979, SRC-CIR-2025-1569, SRC-ARF-HLR, SRC-WEBUILD-ARCH, SRC-WEBUILD-RB, SRC-OID2025. Full entries with version, date and URL are in the source register.
