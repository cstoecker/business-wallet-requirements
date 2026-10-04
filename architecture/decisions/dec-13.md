---
title: "DEC-13 Delegation and mandates for employees, machines and AI agents"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 13
permalink: /architecture/decisions/dec-13/
description: "How employees, machines and AI agents get authority to act for an organisation with a business wallet: roles in the wallet, mandate credentials, legal powers of attorney, protocol-level delegation, and how that authority is limited, delegated onward, shared, suspended, revoked and attributed. Facts, criteria, options and conditions."
keywords: [delegation, mandate, power of attorney, employees, machines, AI agents, suspension, revocation, four-eyes, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-04"
---

# DEC-13 Delegation and mandates for employees, machines and AI agents

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text (ST 9684/26, 2 June 2026) and the Parliament committee draft report differ and are cited by name. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

An organisation that owns an EBW needs one model for how authority is **created**, **limited** (scope, amounts, time), **delegated onward**, **shared** (joint or four-eyes representation), **suspended or revoked**, **ended** (a person leaves, a machine is decommissioned, an agent is retired), **attributed** in the audit trail, and tied to a level of **assurance**. The authority goes to three actor classes: **employees** (natural persons), **machines** (devices, plants, services, technical users, machine-to-machine) and **AI agents**. Whether one integrated model is wanted, or separate treatment of agents (see [DEC-10]({{ '/architecture/decisions/dec-10/' | relative_url }})) and machines, is a project choice that no source states. The decision builds on the employee question in [DEC-02]({{ '/architecture/decisions/dec-02/' | relative_url }}) and on the status and revocation question in [DEC-12]({{ '/architecture/decisions/dec-12/' | relative_url }}).

## What the requirement set says

Cluster K03 (authorisation, mandates and delegation) holds 117 requirements: 28 priority P1, 74 P2 and 15 P3. The 28 priority P1 requirements concern the authorisation model and access decisions, legal mandates and the power of attorney, agent mandates, audit bound to proofs of authorisation, and user identification independent of the wallet unit. No K03 requirement covers machines, devices, plants, technical users or decommissioning. Onward delegation (AIF-025, TRU-063, INT-029), joint representation (TRU-168, INT-088), suspension (TRU-159, TRU-085) and leaving a role (TRU-163, FUN-058) are present at priority P2 or P3. No requirement ties the assurance level to the actor class. The architecture-shaping ones:

{% include cluster-drivers.html cluster="K03" %}

## Facts from the sources

Each fact has a source. Items marked <span class="vtag v-todo">to verify</span> were not read in the original or were read only in part.

**Commission proposal, Council text and Parliament draft.**
- Purpose: owners create, manage and delegate "mandates to authorised representatives" (Commission, Article 3(1)(c)); the Council says "authorisations ... to European Business Wallet users" (SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26). The Parliament draft adds "mandates and roles" (Amendment 50; SRC-EP-ITRE-DRAFT-REPORT, a draft, not an adopted position).
- Commission definitions: an authorised representative is a natural or legal person; a mandate is the authorisation granted to such a representative (Article 3(18), (19)). The Council deletes Article 3(18) and defines "authorisation" as the grant and "the corresponding access-control decision that permits each concrete request" (Article 3(19)). A user is "a natural or legal person, or a natural person representing another natural person or a legal person" (Article 3(22)). Machines and agents are not named in any of these definitions.
- Core function: owners can authorise multiple users and "manage and revoke such authorisations" (Article 5(1)(j)). The Council adds role-associated authorisations "without prejudice to any power of attorney or legal mandate"; the Parliament draft adds auditable and restricted delegations (Amendment 64).
- Unattended use: providers support protocols for interaction "automatically without manual intervention" (Commission Article 6(1)(d)); the Council adds "or through direct European Business Wallet user action". The text does not say under whose authority an automatic interaction runs.
- Role integrity (Article 6(2)(b), Commission and Council): role-attribute mappings are "verifiable, auditable, revocable and traceable to their legitimate issuers"; "conflicts of roles, over-delegation, or expired authorisations are automatically detected and prevented in real time".
- Recital 18: the Commission describes a "mandate and role-based authorisation system", with a technical and an administrative mandate and "compatibility with the EU digital power of attorney". The Council replaces "mandate" by "authorisation", calls it "of a technical nature" and says it does not "create, limit, or otherwise affect any power of attorney or legal mandate".
- Agents and assets: recital 28 mentions "agentic AI" as a new use case (Commission and Council); the Council adds "the provision of a digital identity to an owner's asset". The Parliament draft would add recital 20a and Article 3(19a) on automated transactions by a digital or AI-driven agent under "a valid, auditable and revocable authorisation" (Amendments 17 and 55).
- Annex point 12 (Commission Annex and Council Annex, same in substance; SRC-EBW-ANNEX-CELLAR): access decisions rest on attestations of the acting subject, the formal role, "the scope, validity and constraints of any mandate, delegation, or power of attorney" and context. Visibility is conditioned on access rights, roles and mandates are validated in real time, and events are "logged, timestamped, and bound to cryptographically verifiable proofs of authorisation". Implementing acts cover role formats, interoperability of mandates and delegations, policy language and secure logging. No depth limit for onward delegation and no four-eyes rule is named. An earlier project note treated point 12 as Council-only; the Commission Annex contains it.
- Authentication: wallet users authenticate by a notified eID means of at least assurance level substantial, or "an alternative authentication mechanism recognised as equivalent" (Annex point 1). A machine has no notified eID; the content of the alternative clause is not specified.
- Onboarding through a representative: Commission "substantial" or "high"; Council and the Parliament draft "high" (Article 6(1)(e)).
- Revocation and logs: the wallet is revocable on request, compromise or "permanent or temporary cessation of activity" of the owner (Article 6(2)(f)); providers inform affected users within 24 hours of a unit attestation revocation (Annex 6). The logged fields in Annex 7 (time, relying party, data types, reason for non-completion) do not name the acting user or the authority relied on.
- Not stated in the EBW texts read: liability between owner, user and provider, onward delegation depth, joint approval, suspension of an authorisation, decommissioning.

**Company law and eIDAS.**
- Digital EU power of attorney (Directive (EU) 2025/25, Article 16c of Directive 2017/1132): a template for companies in Annexes II and IIB to authorise a person to represent the company in procedures under that Directive in another Member State; drawn up, amended or revoked under national requirements including verification by courts, notaries or competent authorities; authenticated by trust services; accepted "as evidence of the authorised person's entitlement to represent the company" (SRC-DIR-2025-25). Implementing acts on the template were due by 31 July 2026 and were not found published on 3 October 2026; transposition is due 31 July 2027 and application starts 31 July 2028. Employees acting day to day, machines and agents are not within that wording.
- The register shows whether persons authorised to represent a company act alone or jointly (Article 14(d)(i)). Limits on the powers of organs "may not be relied on as against third parties" (Article 9(2)); both read in the 2017 original text, consolidated numbering <span class="vtag v-todo">to verify</span> (SRC-DIR-2017-1132).
- eIDAS: the PID may represent "the natural person representing the natural or legal person" (Article 5a(5)(f)); Annex VI item 9 lists "Powers and mandates to represent"; a revoked qualified attestation of attributes "shall not in any circumstances be reverted" (Article 45d(4)); qualified certificates for signatures and seals may be suspended under national rules (Articles 28(5), 38(5)); no suspension rule was found for attestations of attributes (SRC-EIDAS-CONSOL). A seal can authenticate "software code or servers" (recital 65) and its creator is a legal person (Article 3(24)) (SRC-REG-2014-910-ORIG). Recital 19 of Regulation 2024/1183 refers to e-mandates (SRC-REG-2024-1183, partly read).
- ARF: the topic on wallet units for legal persons is empty; the representation rulebooks cover a natural person representing another person, with validity, nature of representation and permitted operations (SRC-ARF-HLR). Revocation triggers in the personal wallet name the provider and the user, not the employer (carried from DEC-02; SRC-CIR-2024-2977, SRC-CIR-2025-1569, SRC-CIR-2024-2979).

**WE BUILD material (SRC-WEBUILD-RB, SRC-WEBUILD-ARCH).**
- The Power of X model has three authority types: power of attorney (explicit mandate with scope, duration, limitations), power of representation (from law, statutes or register) and power of employment. The power of employment "will NOT be covered in MVP Pilot scenarios". The proxy is a legal entity or a natural person; there is no machine or agent proxy. Attributes include scope, a limitation flag, constraints, assurance level (by origin of information) and positions such as Joint Administrator. A relying party cannot read how many co-signatories are needed.
- "Possession of a valid attestaion SHALL NOT automatically imply authorization". Revocation is permanent; suspension makes the attestation invalid, but the status values listed are active, revoked, expired and unknown, with no suspended value; "Representative leaves organization" is a revocation trigger (reason code `EMPLOYMENT_TERMINATED`). The version cloned is v0.7; a v0.8 of 2026-09-04 exists and was not read <span class="vtag v-todo">to verify</span>.
- Consent: wallets "MUST NOT ... Auto-consent" (cs-02), while the e-invoice rulebook describes wallet-to-wallet and machine-to-machine presentation and the handshake rulebook lets the holder backend decide by the owner's policies. No WE BUILD text on agents or technical users was found.

**Format and protocol specifications.**
- W3C VCDM 2.0 has validity and status fields and no delegation construct (SRC-VCDM-2.0). Bitstring Status List has a reversible `suspension` purpose and an irreversible `revocation` purpose (SRC-VC-BSL-1.0). The IETF Token Status List draft-21 has `INVALID` and `SUSPENDED` (SRC-IETF-OAUTH-STATUS-LIST, a draft).
- RFC 8693 separates delegation from impersonation, uses nested `act` claims in which only the current actor counts for access control, and says revocation propagation "is not a general property" (SRC-RFC-8693). RFC 9396 carries typed authorisation details, for example an amount and currency (SRC-RFC-9396). GNAP delegates authorisation to software that "runs autonomously" (SRC-RFC-9635).
- UCAN (community specification): each delegation restates or attenuates capabilities, delegation does not transfer keys, revocation is irreversible with no suspension; identifiers are DIDs with no link to a legal person (SRC-UCAN-SPEC, SRC-UCAN-DELEGATION, SRC-UCAN-REVOCATION).
- ODRL has permissions, prohibitions, duties and constraints and no delegation or revocation vocabulary (SRC-ODRL-IM-2.2, SRC-ODRL-VOCAB-2.2). The Dataspace Protocol uses ODRL and has a SUSPENDED transfer state; DCP says human-consent presentation protocols "are not applicable" (SRC-DSP, SRC-DCP; carried). Catena-X CX-0018 describes the connector; "technical user" was not found in the cached Catena-X standards and occurs only in the Tractus-X portal changelog (SRC-CX-0018, SRC-TX-PORTAL-ASSETS-CHANGELOG, snippet). SRC-CX-0149 is registered as "WalletRequirements" v2.1.0 while the library lists another title <span class="vtag v-todo">to verify</span>.

**Machine identity.**
- IEC 62443 parts 3-3 and 4-2 were read as publisher abstracts only (identification and authentication control, use control) <span class="vtag v-todo">to verify</span> (SRC-IEC-62443-3-3, SRC-IEC-62443-4-2, SRC-ISA-62443-SERIES). OPC UA Part 2 defines application instance certificates and an authorisation service returning access tokens with roles (partly read; SRC-OPCUA-P2). IDTA-01004 Part 4 uses attribute-based access rules with claims, says subject attributes "need to be mapped to the subject in an authenticated way" and does not specify native signatures (partly read; SRC-IDTA-AAS-P4). A SPIFFE ID names a workload within a trust domain, with a path whose meaning the administrator defines, and has no link to a legal person (SRC-SPIFFE-ID, SRC-SPIFFE-X509-SVID).
- The Cyber Resilience Act requires products to control unauthorised access, record relevant activity and let the user remove data permanently (Annex I Part I (2)(d), (l), (m)); it binds manufacturers and says nothing on how an owner delegates authority to a device (SRC-CRA).

**AI agents.**
- MCP: OAuth-based authorisation, "there SHOULD always be a human in the loop" (SRC-MCP-AUTH, SRC-MCP-TOOLS, SRC-MCP-SEC). A2A: signed agent cards, OAuth2 client credentials and mutual TLS, no mapping of a signer to a legal person (SRC-A2A). AP2 v0.2: open mandates include the agent's public key (`cnf`) and a short `exp`; Human Present and Human Not Present modes; a two-step delegation of open and closed mandates; no revocation found (SRC-AP2). OIDF, WIMSE and IETF identity-chaining drafts, carried from DEC-10, call chain revocation and recursive delegation unsolved.
- AI Act (consolidated text of 27 July 2026, SRC-AIACT-CONSOL-2026-07): a deployer uses a system "under its authority"; human oversight under Article 14 is "commensurate with the risks, level of autonomy and context of use"; two natural persons are required only for remote biometric identification (Article 14(5)); deployers assign oversight to competent natural persons, keep logs at least six months and inform workers before workplace use (Article 26(2), (6), (7)). Chapter III obligations apply from 2 December 2027 (Annex III systems) and 2 August 2028 (Annex I systems). The Act does not define an agent mandate; whether a wallet agent is high-risk was not analysed.

**Suspension and revocation across sources.** Qualified attestations: revocation final, no suspension. Qualified certificates: national suspension, status visible. Wallets (eIDAS Article 5e): suspension on breach, revocation after three months. EBW: "temporary cessation" is a revocation ground of the owner's wallet. WE BUILD: suspension defined, no status value. Bitstring Status List and Token Status List: suspension available. UCAN: none. RFC 8693 and RFC 9396: not defined.

**Assurance.** Unit user authentication substantial; onboarding via a representative substantial or high (Commission) or high (Council); critical operations substantial (Article 6(1)(l)); EUDI Wallet high (Article 5a(11)); WE BUILD assurance by origin, high where a business register is the source. No source ties the required level to the actor class or to the size of the authority granted.

## Decision criteria

"Source" names a text that states the criterion. "Driver" is an architecture or business driver that no source states, class A until a stakeholder confirms. The criterion IDs are those of the research note and are not requirement priorities.

| # | Criterion | Basis |
|---|---|---|
| P1 | Authority is created by the owner or its lawful representative and bound to a verifiable legal person | source: Article 5(1)(j), Annex 12(1); AI Act Article 26(2) |
| P2 | Scope, validity and constraints are machine-readable and checked at the moment of use | source: Annex 12(1)(c), 12(2)(b); ARF representation rulebook; AP2 |
| P3 | Quantitative limits (amount, rate, time window, counterparty) | source (partial): RFC 9396; WE BUILD constraint; driver for the EBW |
| P4 | Authority neither creates nor limits legal capacity; statutory powers stay with national and Union law | source: Council recital 18, Article 5(1)(j); Directive 2025/25 recital 28 |
| P5 | Compatibility with the digital EU power of attorney and acceptance as evidence | source: Directive 2025/25 Article 16c; EBW recital 18 |
| P6 | Onward delegation is explicit, attenuating and depth-bounded | source (partial): Article 6(2)(b) "over-delegation"; RFC 8693; UCAN; the depth limit is a driver |
| P7 | Joint (four-eyes, n-of-m) representation can be required, expressed and enforced | source (partial): Directive 2017/1132 Article 14(d)(i); WE BUILD Joint Administrator; EBW: driver |
| P8 | Segregation of duties and role-conflict prevention in real time | source: Article 6(2)(b), Annex 12(3)(b) |
| P9 | Suspension distinct from revocation, with a defined effect on relying parties | source (partial): status list specifications, eIDAS 28(5)/38(5); no EBW text; driver for authorisations |
| P10 | Revocation reaches the actor and relying parties within a stated time, including along delegation chains | source (partial): Annex 12(3)(a); RFC 8693; UCAN; the time bound is a driver |
| P11 | Termination events: person leaves, machine decommissioned, agent retired; keys and credentials end | source (partial): WE BUILD revocation trigger; CRA Annex I (2)(m); EBW: driver |
| P12 | Continuity: handover of roles, pending actions or keys when staff change or a plant changes owner | driver |
| P13 | Attribution: each act records actor, principal and authority relied on; agents are distinguishable from principals | source: Annex 12(2)(c); RFC 8693; AI Act Article 12 if high-risk |
| P14 | Non-repudiation and evidence usable "for audit and legal proceedings" | source: Annex 12(2)(c); eIDAS Articles 25 and 35 |
| P15 | Assurance level proportionate to actor class and authority granted | source (partial): Annex 1, Article 6(1)(e), Article 5a(11); proportionality is a driver |
| P16 | Human oversight and approval above defined limits, ability to interrupt | source (conditional): AI Act Articles 14 and 26 if high-risk; MCP SHOULD; AP2 modes; otherwise driver |
| P17 | The actor never holds the owner's wallet keys; own keys per actor; seal versus signature | source: Annex 3 to 5 and 8; eIDAS Articles 3(9), 3(24), 36; UCAN; AIF-015 |
| P18 | Unattended (machine-to-machine) operation without breaking wallet consent rules | source (partial): Article 6(1)(d); cs-02; DCP |
| P19 | Interoperability across wallets, Member States and protocols; protocol-neutral requirements | source: Article 6(2)(b), Annex 12(3)(c), 12(4)(b); driver for protocols |
| P20 | HR, IAM and OT integration (joiner-mover-leaver, asset registers) and automated revocation | source (partial): Article 6(1)(d); driver |
| P21 | Privacy of actor and principal in presentations; GDPR roles for employee data | source (partial): GDPR recital 39; Annex 7(5); AI Act Article 26(7); driver |
| P22 | Maturity and legal status of the instruments (proposal, Council text, draft, community specification) | source: versions in the facts |

## Options

**Option A. Roles and authorisations inside the wallet, with users of the wallet unit.** Each employee, service account or agent is a user of the owner's wallet with owner-managed authorisations decided by the provider's access-control mechanism (Annex 12).
- *Enables.* A core function with manage and revoke by the owner (Article 5(1)(j)); detection of role conflicts and over-delegation (Article 6(2)(b)); real-time validation and proof-bound logs (Annex 12(2)); employees named in recital 18; automatic interaction (Article 6(1)(d)); the Parliament draft would admit agents under revocable authorisation. Provider-side removal of a user is simple for the owner. Combines with seals and qualified certificates for users (Annex 8).
- *Restricts.* The authorisation is "of a technical nature" and creates no legal power (Council recital 18). Parties outside the provider cannot see it unless it is presented as a credential. User authentication is substantial by an eID or an equivalent mechanism, so employees need a personal eID and machines and agents have no defined route. The definitions cover persons. No onward-delegation depth, joint approval or suspension text. Logs are readable by the provider "where it is necessary" (Annex 7(5)).
- *Leaves open.* Whether a machine or agent may be a user, what identifies it, key custody, how an outside relying party sees the authority, what the audit record of the acting user contains.

**Option B. Mandates as verifiable credentials with scope and limits, issued by the owner's wallet.** The owner issues a mandate attestation (principal, agent, scope, limits, validity, status, optionally an onward-delegation flag) to the actor's key.
- *Enables.* Relying parties outside the provider can verify who authorised what (Annex 12(1); Article 5(1)(h)); non-qualified attestations keep legal effect as evidence (eIDAS Article 45b(1)); validity and status in VCDM and status lists, with suspension available there. Patterns exist: WE BUILD Power of X, ARF representation rulebooks, AP2 mandates bound to the agent key. A device key can be bound to a mandate; sealing for non-human assets is contemplated in eIDAS recital 65.
- *Restricts.* No machine or agent vocabulary in any rulebook; the power of employment is outside the MVP; an agent mandate schema is unspecified. A mandate credential does not by itself authorise; relying-party policy decides. Status mechanisms differ: the rulebook has no suspended value and qualified attestations cannot be un-revoked. Presentation protocols assume holder consent (cs-02).
- *Leaves open.* Issuer type (owner as non-qualified attestation provider, qualified provider, register-based public-sector attestation); legal weight against a power of attorney; depth and attenuation rules; status list operator and speed; vocabulary for quantitative limits.

**Option C. Legal power of attorney and representation credentials (Directive 2025/25 and company law).** Authority is evidenced by the digital EU power of attorney and by register-based representation credentials drawn up under national law.
- *Enables.* Legal capacity: acceptance as evidence in all Member States (Article 16c(2)); register information on joint or sole representation (Article 14(d)(i)); trust-service authentication and EUDI Wallet compatibility; high assurance by origin; consistent with the Council's "without prejudice" wording.
- *Restricts.* Reach is limited to company procedures under Directive 2017/1132 in another Member State, for Annex II and IIB companies; the template implementing acts were not found published; application starts 2028. Creation needs courts, notaries or competent authorities, which suits registered authority and not day-to-day roles (the sources are silent on operational use). Limits on organs cannot be relied on against third parties. Joint representation is carried by the register and a position attribute, not by an enforceable n-of-m presentation protocol.
- *Leaves open.* How a relying party combines a representation credential with an employee identity; how fast revocation reaches relying parties; whether a machine or agent can be an authorised person in any Member State (not stated).

**Option D. Token-based delegation at the protocol layer (OAuth 2.0, GNAP, UCAN-style capabilities).** Authority is carried as short-lived access tokens or capability chains.
- *Enables.* Per-request enforcement, audience and scope binding, amount and action limits (RFC 9396), separation of actor and principal (RFC 8693), key rotation and token revocation (GNAP), unattended software. Fits MCP, A2A client credentials, OPC UA access tokens and AAS access claims. UCAN: attenuation as a rule and delegation without key transfer.
- *Restricts.* Tokens do not identify the legal person or its authority to a third party; revocation across exchanged tokens is not a general property (RFC 8693); only the current actor counts; UCAN revocation is irreversible; no defined depth limit in RFC 8693, RFC 9396 or GNAP. Not an EBW core function; no EU text names it.
- *Leaves open.* Binding to a legal person and a trust list; audit evidence for legal proceedings; cross-domain federation and recursive delegation; mapping of credential scopes to token scopes.

**Option E (A and B).** Roles and users inside the wallet for access to wallet functions; the same authorisations exported as mandate credentials where a relying party or another wallet must verify them.
- *Enables.* P1, P2, P4 (technical against legal separation), P9, P13.
- *Restricts.* Two representations of one authority must be kept consistent; mapping rules are not defined.
- *Leaves open.* Which system leads on revocation.

**Option F (B and D).** The wallet issues the mandate credential and binds the actor key; an authorisation server derives short-lived, audience-bound tokens from it (as option O4 in [DEC-10]({{ '/architecture/decisions/dec-10/' | relative_url }})).
- *Enables.* Runtime limits and chain notation (`act`) with a verifiable root.
- *Restricts.* Mapping of mandate scope to token scope; chain revocation.
- *Leaves open.* Where the policy decision point sits (Annex 12 does not say).

**Option G (C, B, A and D by actor class).** Legal instruments for statutory and registered authority and cross-border procedures; mandate credentials for operational authority of employees and agents; wallet users for internal access; protocol tokens at run time for machines and agents.
- *Enables.* Each source is used where it applies.
- *Restricts.* Four mechanisms and four status regimes; propagation between them is unspecified.
- *Leaves open.* Precedence when sources disagree, for example an internal limit against a register entry.

## Per-actor matrix

What the sources support per actor class and option. "Not stated" means that no source read says it; it is not a negative.

| Actor | A Roles and unit users | B Mandate credentials | C Legal power of attorney or representation | D Protocol tokens | Combinations E, F, G |
|---|---|---|---|---|---|
| Employees | Named in recital 18; owner manages and revokes (Article 5(1)(j)); authentication by eID at least substantial. Not stated: employer-driven exit event, key handover, GDPR roles | Patterns exist (employee and contact-person rulebooks as drafts, ARF representation rulebooks); the employer is issuer. Not stated: legal weight of a non-qualified employer attestation, real-time status at relying parties | Statutory representatives and attorneys in company procedures; high assurance. Not stated: day-to-day roles | Access to services and APIs by OAuth user delegation. Not stated: link to the legal person and to personal identity at third parties | E combines access inside and a mandate outside; G adds C for officers |
| Machines | Article 6(1)(d) allows automatic interaction; Council recital 28 names "an owner's asset". Not stated: user definition for machines, authentication route, key custody, decommissioning | A credential can bind a device key; seal under the legal person contemplated (eIDAS recital 65). Not stated: machine proxy type, asset-identity rulebook, revocation trigger for decommissioning | Not stated; company law deals with persons authorised to represent a company | OPC UA access tokens, AAS access claims, SPIFFE identities, OAuth client credentials, GNAP software clients, mutual TLS. Not stated: binding to the legal person, EU trust anchors, audit for legal proceedings | F pairs a device-binding credential with runtime tokens; CRA Annex I supplies device-side access control and data removal |
| AI agents | Parliament draft recital 20a and Article 3(19a) would admit agents; Commission and Council texts mention agentic AI only in recital 28. Not stated: user status, identity, oversight | AP2 open and closed mandates (SD-JWT, agent key, short `exp`, Human Present or Not Present). Not stated: standard mandate vocabulary, revocation in AP2, legal weight | Not stated; Directive 2025/25 does not mention agents | RFC 8693 delegation and `act`, RFC 9396 limits, MCP and A2A OAuth; chain revocation described as unsolved (OIDF, carried) | F is the layered form in DEC-10; AI Act duties attach to high-risk systems only (conditional) |

By criterion: onward delegation (P6) is stated for option A only as prevention of "over-delegation"; B and D have notations; C has none. Joint representation (P7) is stated for C through the register and described but not enforced in B; A and D are silent. Suspension (P9): A silent for authorisations; B possible by status type; C national law only; D tokens expire, UCAN has none. Termination (P11): A owner removes the user; B has a reason code and trigger for persons and none for machines; C national revocation; D token expiry or revocation.

## Preliminary reading

*The analysis of this project, not a statement of a source. No weights are set; weights belong to stakeholders.*

1. **Employees.** On the sources read, option E fits: users and roles inside the wallet for access, and a mandate credential where an outside relying party must verify the authority; option C is added for officers and attorneys in company procedures. This holds if the Council wording on a technical authorisation survives and if a relying party accepts an employer-issued attestation.
2. **Machines.** The sources support a binding of a device or workload identity to the owner and runtime tokens for access (option F). No EBW text defines a machine as a user and no rulebook has a machine proxy, so any machine model rests on drivers and on Council recital 28.
3. **AI agents.** Option F, as in DEC-10, is the layered form the specifications allow: a verifiable root mandate, short-lived derived tokens, delegation not impersonation. The legal basis in the EBW texts is the Parliament draft only.
4. **Cross-cutting.** Suspension separate from revocation, a depth limit for onward delegation, joint approval and an assurance level per actor class have no EBW text; they are driver-based criteria (P6, P7, P9, P15) until stakeholders confirm them.

**Conditions under which this reading holds.** The final text keeps Article 5(1)(j), Article 6(2)(b) and Annex point 12; implementing acts define role and mandate formats; the Parliament position on agents is carried into the final text or an equivalent route is created.

**What would change it.** Trilogue texts (the Parliament report A10-0240/2026 was not read); the implementing acts under Annex 12(4); the template of the digital EU power of attorney; a GLEIF, ETSI or WE BUILD rulebook for machine or agent authority; a stakeholder decision on one integrated model against separate treatment; the classification of wallet agents under the AI Act.

## Gaps and next steps

- No EU text defines authority for machines, devices, plants or technical users of an EBW owner; "user" is a natural or legal person.
- No text on decommissioning a machine or retiring an agent, beyond data removal by the user under the CRA.
- No EBW text on onward delegation depth, joint approval for wallet operations, suspension of an authorisation, quantitative limits, or assurance level per actor class.
- No source states the time within which revocation of an authorisation must reach relying parties; the only figure is 24 hours for informing users of a unit attestation revocation.
- No source allocates liability between owner, user, provider and relying party, including for acts of an AI agent.
- No source defines who may issue a mandate credential for operational authority and with what legal weight.
- No wallet-level text on approval of an unattended presentation (cs-02 against Article 6(1)(d)) and no policy language chosen (Annex 12(4)(c)).
- The acting user is not a log field in Annex 7; the balance of privacy and accountability is open.
- Not read: the IEC 62443 texts, ETSI TS 119 472 status clauses, ISO/IEC 18013-5, CX-0152, DSP policy evaluation, the EDPS comments of 20 January 2026, vLEI role credentials, the Council text adopted on 9 June 2026 and the Parliament report A10-0240/2026 <span class="vtag v-todo">to verify</span>.
- Next: write the requirements the gaps imply (machine and service authority, termination, suspension, onward delegation, joint representation, assurance by actor class, log content) after stakeholder confirmation of the drivers; check the Commission Annex point 12 against requirement notes that treat it as Council-only.

## References

SRC-EBW-PROPOSAL, SRC-EBW-ANNEX-CELLAR, SRC-COUNCIL-ST-9684-26, SRC-EP-ITRE-DRAFT-REPORT, SRC-DIR-2025-25, SRC-DIR-2017-1132, SRC-EIDAS-CONSOL, SRC-REG-2014-910-ORIG, SRC-REG-2024-1183, SRC-ARF-HLR, SRC-CIR-2024-2977, SRC-CIR-2025-1569, SRC-CIR-2024-2979, SRC-WEBUILD-RB, SRC-WEBUILD-ARCH, SRC-VCDM-2.0, SRC-VC-BSL-1.0, SRC-IETF-OAUTH-STATUS-LIST, SRC-RFC-8693, SRC-RFC-9396, SRC-RFC-9635, SRC-UCAN-SPEC, SRC-UCAN-DELEGATION, SRC-UCAN-REVOCATION, SRC-ODRL-IM-2.2, SRC-ODRL-VOCAB-2.2, SRC-DSP, SRC-DCP, SRC-CX-0018, SRC-CX-0149, SRC-TX-PORTAL-ASSETS-CHANGELOG, SRC-IEC-62443-3-3, SRC-IEC-62443-4-2, SRC-ISA-62443-SERIES, SRC-OPCUA-P2, SRC-IDTA-AAS-P4, SRC-SPIFFE-ID, SRC-SPIFFE-X509-SVID, SRC-CRA, SRC-MCP-AUTH, SRC-MCP-TOOLS, SRC-MCP-SEC, SRC-A2A, SRC-AP2, SRC-AIACT-CONSOL-2026-07. All are registered in the source register. Cited without a registered source: the OIDF whitepaper, the IETF WIMSE and identity-chaining drafts and GDPR recital 39 (not registered under a separate ID in this note).
