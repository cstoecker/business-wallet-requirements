---
title: "DEC-08 Privacy and data protection"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 8
permalink: /architecture/decisions/dec-08/
description: "How are minimisation, unlinkability and the controller and processor roles designed when the wallet owner is an organisation and the users are people? Facts from the sources, decision criteria, three role options and the conditions under which each holds."
keywords: [privacy, data protection, GDPR, controller, processor, joint controllers, minimisation, unlinkability, pseudonymisation, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-08 Privacy and data protection

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the Council text submitted for its general approach (ST 9684/26, 2 June 2026) differs from it, and the outcome of the Council meeting on 9 June 2026 was not read. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

The owner of an EBW is an organisation, but the people who act in the wallet, and whose data appears in it, are natural persons. How are **minimisation**, **unlinkability** and the **controller and processor roles** designed in that setting? Three things have to be settled together: who decides why and how user-level data is processed (owner, provider, Commission), which of the privacy rules that eIDAS sets for the EUDI Wallet are carried over to the EBW, and what the provider may see of the people who use the wallet.

The employee and identifier angles are treated elsewhere: employees acting for a company in [DEC-02]({{ '/architecture/decisions/dec-02/' | relative_url }}), identifiers and their combination in [DEC-11]({{ '/architecture/decisions/dec-11/' | relative_url }}). This page links to them and does not repeat them.

## What the requirement set says

The cluster K09 holds the requirements that bear on this decision:

{% include cluster-drivers.html cluster="K09" %}

Candidates found in the research and not yet written as requirements: provider processing under a processor contract, a joint-controller arrangement, owner measures for processing by users, pseudonymisation of the Directory where appropriate, and no tracking by the issuer after issuance. Existing entries already cover records of processing (EBW-LEG-016), pseudonymisation and encryption (EBW-LEG-017), the data protection impact assessment (EBW-LEG-020), unlinkability across relying parties (EBW-NFR-043) and logical separation (EBW-NFR-010).

## Facts from the sources

Each fact has a source and was read in the original text unless marked. The EDPS formal comments of 20 January 2026 and the EDPS opinion on the Commission proposal were not read; only their existence is stated in the texts. No CJEU judgment and no national employment-law rule was read.

**Who the data subjects are, and which data is involved.**
- The owner is "an economic operator or public sector body"; a user is "a natural or legal person, or a natural person representing another natural person or a legal person, that uses European Business Wallets" (proposal Article 3(7), 3(22)). Economic operators include natural persons "acting in a commercial or professional capacity" (Article 3(4)).
- The GDPR "does not cover the processing of personal data which concerns legal persons", including name, form and contact details of the legal person (recital 14). Natural persons behind a legal person, such as users, representatives and sole traders, remain data subjects.
- The Directory "includes personal data of economic operators". The minimum content in the Council text is the official name of the owner, a unique identifier, a digital address and the country (Council recital 38 and Article 10(3a)); the Commission recital 38 has the same first statement.
- Recital 39 says the GDPR "applies to all personal data processing activities under this Regulation" and that Directory processing will follow minimisation, purpose limitation, data protection by design and by default and "include, where appropriate, features of pseudonymisation" (Commission text; the Council recital is the same in substance). The legislative financial statement repeats this for the Commission. No article of the proposal repeats the duty.
- The Commission explanatory memorandum says selective disclosure "also serves as a measure for the protection of personal data"; Article 5(1)(b) provides for selective disclosure of owner identification data and attributes.
- Users, authorised representatives and their roles appear in logs, authorisation mappings and attestations (Article 5(1)(j), 6(2)(b); Council Annex 7 and 12). The articles read contain no controller, processor or joint-controller allocation between owner, user, provider and Commission. The words "controller" and "processor" do not occur in the Commission text or the Council text, apart from references to Regulation (EU) 2016/679 (searched).
- Supervisory bodies shall "cooperate with supervisory authorities established pursuant to Article 51 of Regulation (EU) 2016/679" (Article 13(5)(g)).
- The stems *unlink* and *correlat* do not occur in the proposal or in the Council text (searched). The Council Annex asks that "visibility of credentials and attestations is selective and conditioned on access rights" (Annex 12(2)(a)).
- The Council log content (time and date, relying party data, data types, reason for non-completion) lists no field for the acting user; separately, "all access and execution events are logged, timestamped, and bound to cryptographically verifiable proofs of authorisation" (Annex 7(2), 12(2)(c)). The acting person in the log is also treated in [DEC-02]({{ '/architecture/decisions/dec-02/' | relative_url }}).
- Council text: logs "shall be accessible to the European Business Wallets provider, where it is necessary for the provision of European Business Wallets services" without a consent condition (Annex 7(5)). For the EUDI Wallet the same access is "on the basis of explicit prior consent by the wallet user" (Regulation (EU) 2024/2979 Article 9(5)).

**GDPR provisions on roles and design.**
- A controller "alone or jointly with others, determines the purposes and means of the processing"; a processor "processes personal data on behalf of the controller" (Article 4(7), 4(8)).
- Joint controllers: "Where two or more controllers jointly determine the purposes and means of processing, they shall be joint controllers." They set responsibilities "by means of an arrangement" whose essence is made available to the data subject, who may exercise rights "in respect of and against each of the controllers" (Article 26(1) to (3)).
- Processing by a processor "shall be governed by a contract or other legal act", and the processor "processes the personal data only on documented instructions from the controller" (Article 28(3)(a)). A processor that determines purposes and means "shall be considered to be a controller in respect of that processing" (Article 28(10)). Persons acting under the authority of the controller or processor "shall not process those data except on instructions from the controller" (Article 29).
- Personal data shall be "adequate, relevant and limited to what is necessary in relation to the purposes" and kept identifiable "for no longer than is necessary"; the controller must demonstrate compliance (Article 5(1)(c), (e), 5(2)).
- Controllers implement measures "such as pseudonymisation" and, by default, process "only personal data which are necessary for each specific purpose" (Article 25(1), 25(2)).
- Controllers keep a record of processing activities with purposes, categories, recipients and, where possible, time limits for erasure (Article 30(1)); security measures include "the pseudonymisation and encryption of personal data" (Article 32(1)(a)).
- A data protection impact assessment is required "where a type of processing in particular using new technologies ... is likely to result in a high risk", before the processing; one assessment "may address a set of similar processing operations that present similar high risks" (Article 35(1), 35(7)). Breach notification to the authority is due "not later than 72 hours" after becoming aware (Article 33(1)).
- Member States may provide "more specific rules" for employees' data, with "suitable and specific measures" including "monitoring systems at the work place" (Article 88(1), (2)). Pseudonymised data "which could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person" (recital 26).

**EDPB guidelines.**
- "It is usually the organisation as such, and not an individual within the organisation", such as an employee, that acts as a controller (Guidelines 07/2020, executive summary). Processing by employees within the organisation's activities "may be presumed to take place under that organisation's control"; employees are generally persons acting under the authority of the controller (paragraph 19 and footnote 9). The organisation must ensure "adequate technical and organizational measures, including e.g. training and information to employees".
- A processor must be "a separate entity in relation to the controller" and process "on the controller's behalf"; essential means stay with the controller, non-essential means may be left to the processor. The criterion for joint controllership is "the joint participation of two or more entities in the determination of the purposes and means of a processing operation".
- In an example, a taxi booking platform used by a company for its employees is a controller of the employee data "in its own right", because it independently designed the platform and decides categories and retention; a call-centre provider that cannot use data for other purposes is a processor (examples near paragraph 83).
- Guidelines 01/2025 on pseudonymisation (consultation version, adopted 16 January 2025; a final version was not found): pseudonymised data that could be attributed by additional information "is to be considered information on an identifiable natural person", which "also holds true if pseudonymised data and additional information are not in the hands of the same person". "The GDPR does not impose a general obligation to use pseudonymisation." Effectiveness "is highly dependent on the choice of the pseudonymisation domain and its isolation from additional information".
- Guidelines 4/2019 on Article 25 (v2.0, 20 October 2020) were partly read: the table of contents and the minimisation headings only.

**eIDAS rules for the EUDI Wallet that the proposal does not repeat for the EBW.**
- "Users shall have full control of the use of and of the data in their European Digital Identity Wallet." The provider shall not collect usage information not necessary for the service nor combine personal data with other services, and personal data "shall be kept logically separate from any other data held by the provider" (Article 5a(14)).
- The technical framework shall not allow attestation providers or any other party, after issuance, "to obtain data that allows transactions or user behaviour to be tracked, linked or correlated", and shall "enable privacy preserving techniques which ensure unlinkability, where the attestation of attributes does not require the identification of the user" (Article 5a(16)(a), (b)).
- The wallet enables the user to "generate pseudonyms and store them encrypted and locally" and to access a log with options to request erasure and report a relying party (Article 5a(4)(b), (d)). Relying parties shall not request data beyond the registration and shall not refuse pseudonyms "where the identification of the user is not required by Union or national law" (Article 5b(3), 5b(9)). "Compliance of such processing with Regulation (EU) 2016/679 shall be demonstrated" (Article 5a(17)).
- Article 5a applies to European Digital Identity Wallets for natural persons, and the proposal narrows the mandatory EUDI Wallet to natural persons (Article 20, recital 55). Whether Article 5a(14) and (16) apply to business wallets is not stated in the articles read.

**Implementing rules and ARF.**
- Wallet instances "shall log all transactions with wallet-relying parties and other wallet units, including electronic signing and sealing"; providers "shall ensure integrity, authenticity and confidentiality of the logged information" (Regulation 2024/2979 Article 9(1) to (3)). Users can export the log (9(7)); logs "remain accessible for as long as they are required by Union law or national law" (9(6)).
- Wallet units shall "enable privacy preserving techniques which ensure unlinkability where the electronic attestations of attributes do not require the identification of the wallet user" (Regulation 2024/2982 Article 3(10)).
- ARF Topic 11: "A Relying Party SHALL NOT be able to derive the User's true identity, or any data identifying the User" from the pseudonym value, and pseudonym protocols must make it "impossible to correlate Pseudonyms based on their values or on metadata". Scope-rate-limited pseudonyms must not allow any entity or collusion of entities to link pseudonyms across relying parties (section E). Topic 10 section E requires support for batch issuance.
- ETSI TS 119 472-2: "The EUDI Wallet shall by default disclose the presence of all stored EAAs' type to the mediating API", but not attributes.

**Protocol-level privacy facts (OpenID4VC).**
- Issuers and wallets "SHOULD implement Credential Formats that support selective disclosure"; "The time logs are retained for should be minimized"; issuers "SHOULD NOT store the Issuer-signed Credentials if they contain privacy-sensitive data" (OpenID4VCI 1.0, sections 15.2 and 15.3).
- Unique values (claims, identifiers, issuer signature) can link presentations. Countermeasures include issuing a batch "to facilitate the use of a unique Credential per presentation or per Verifier" and discarding signature values after issuance (OpenID4VCI 15.4.1); one-time use of credential instances gives "Verifier-to-Verifier Unlinkable Presentations" (OpenID4VP 1.0, section 15.5).
- "Wallet Attestations MUST NOT be reused across different Issuers", and each credential has "its own unique, unpredictable status list index" (HAIP 1.0, sections 4.4.1 and 6.1).
- Wallets "SHOULD obtain explicit, informed consent"; "Transaction history and data within the Wallet SHOULD NOT be accessible to anyone other than the End-User", unless the user consents or another legal basis exists (OpenID4VP 15.1). Verifiers "SHOULD use DCQL queries that request only the minimal set of claims" (15.4.2).
- Information in a credential that identifies a particular issuer "may reveal information about the End-User"; a group may use a common issuer (OpenID4VCI 15.5). "Mechanisms that require online resolution can leak information that could be used to profile the usage of the Credentials" (OpenID4VP 15.10).

**AI Act.** Deployers that are employers using high-risk AI at the workplace "shall inform workers' representatives and the affected workers" before use (Article 26(7)). This is relevant only if an agent or AI component is a high-risk system.

**What no source read says.**
- No source allocates controller or processor roles for an EBW between owner, user, provider and Commission. The proposal names no controller for the Directory; the Commission text says the Directory is accessible to owners, authorised representatives and providers (Article 10(4)).
- No source says whether an employee's identity in a log is personal data of the employee vis-a-vis the owner, how an employee exercises access or erasure rights against an owner or provider, or how the owner's interest in accountability is balanced against the employee's privacy. The EDPB guidelines read describe the general principle, not the wallet case.
- No source gives a retention period for EBW logs other than "as long as required ... by Union law or national law" (Council Annex 7(6)).

## Decision criteria

Criteria marked **source** are stated or implied by a source; **driver** means a project driver that no source states and that a stakeholder has to confirm.

| # | Criterion | Basis |
|---|---|---|
| P1 | Role clarity per processing activity: who determines purposes and means | source: GDPR Article 4(7), 4(8), 26, 28; EDPB Guidelines 07/2020 |
| P2 | Contract and arrangement duties that follow from the roles, including the sub-processor chain | source: GDPR Article 28(3), 26(1) |
| P3 | Data minimisation and storage limitation by default | source: GDPR Article 5(1)(c), (e), 25(2); OpenID4VCI 15.3 |
| P4 | Unlinkability across relying parties and between issuer and verifier | source: eIDAS Article 5a(16) for the EUDI Wallet, Regulation 2024/2982 Article 3(10), HAIP, ARF pseudonyms; no corresponding EBW text |
| P5 | Pseudonymisation where appropriate, and its limits | source: proposal recital 39, GDPR Article 32(1)(a), EDPB Guidelines 01/2025 |
| P6 | Provider access to user-level data | source: consent for EUDI Wallet logs, "where necessary" in the Council EBW text |
| P7 | Separation of wallet-service data from other services of the provider | source: eIDAS Article 5a(14) for the EUDI Wallet |
| P8 | Data subject rights when the data subject is a user of an organisation's wallet | source: GDPR Chapter III, Regulation 2024/2982 Articles 6 and 7 for the EUDI Wallet |
| P9 | Impact assessment and records of processing: who carries them for owner-side and provider-side processing | source: GDPR Article 35, 30 |
| P10 | Employment-context rules of Member States and worker information when AI is used | source: GDPR Article 88, AI Act Article 26(7) |
| P11 | Security of processing and breach notification timelines | source: GDPR Article 32, 33; eIDAS Article 24(2)(fb) and NIS2 24-hour regimes for trust service providers |
| P12 | Transparency to the data subject | source: GDPR Article 26(2); Articles 13 and 14 not read |
| P13 | Employee privacy against owner accountability: which identifier of the acting person appears in which log, for whom, for how long | driver |
| P14 | Cost and complexity of single-use batch issuance for B2B volumes and for organisational credentials with no natural-person identification need | driver |
| P15 | Cross-border differences in employment and data protection law for multinational owners | driver |

## Options

The GDPR roles below are a derivation for wallet providers: this page applies the GDPR role tests and the EDPB guidelines to the EBW actors, and no source read does that for the EBW. The Commission's Directory role and the roles of the Member State supervisory bodies are separate from the provider-owner relation in all three options; the sources read do not name the Directory controller.

### (a) Owner as controller, provider as processor for user-level data

The organisation decides why and how users act in the wallet. The provider processes on documented instructions under an Article 28 contract and is controller only for its own operation data (account, security, billing).

**Enables.** Matches the EDPB reading that the organisation is the controller for processing by its employees. Article 28 gives a ready contract frame including audits and return of data. Fits the owner's right to export data and to instruct transfer or deletion (proposal Article 5(1)(l) and 7(6)(f)).

**Restricts.** The provider must not determine its own purposes and means for user data, or it becomes controller (Article 28(10)). A provider that designs the log content, retention and analytics itself resembles the platform example. The EUDI Wallet rules that forbid combining data and require logical separation have no stated EBW counterpart.

**Leaves open.** Who is controller of the Directory entry for sole traders (Commission, provider or owner); how employees exercise rights against the owner; how logs that identify the acting user are protected from the owner's own misuse.

### (b) Provider and owner as joint controllers for core wallet processing

Both determine purposes and means of core processing (for example log content, authorisation mappings, signing and sealing flows), with an Article 26 arrangement.

**Enables.** Reflects a provider that sets the technical and functional framework while the owner sets use. Each controller is reachable by the data subject (Article 26(3)). A single arrangement can cover cross-provider flows.

**Restricts.** The criterion of joint participation in the determination of purposes and means in the EDPB guidelines must be met. The essence of the arrangement must be made available to data subjects. Arrangements have to be negotiated with many small owners.

**Leaves open.** The liability split; how the Commission as Directory operator fits (as a third controller); the effect on the provider's duties as a qualified trust service provider.

### (c) Provider as independent controller for user-level data, owner as controller for business use

The provider treats user accounts, authentication and logs as its own processing for providing a regulated service. The owner decides on the use of attestations and mandates.

**Enables.** Aligns with the provider's own regulatory duties (eIDAS Article 24, NIS2, wallet provider rules including logging and security). Gives clarity for security monitoring and incident response. Fits the logic of the taxi example, where the service defines its own data model.

**Restricts.** The owner may lack control over user data held by the provider. Employee data flows between two controllers need a legal basis for each disclosure. The EUDI Wallet analogy (the provider may not combine data, Article 5a(14)) suggests limits that the EBW text does not state.

**Leaves open.** The lawful basis for provider processing of employee data; transparency duties towards employees who never contract with the provider; retention when the owner ends the contract.

## Assessment against the criteria

How far the *sources* support each option for each criterion. "Not stated" means no source speaks to it; the cell does not say the option fails.

| Criterion | (a) owner controller, provider processor | (b) joint controllers | (c) provider independent controller |
|---|---|---|---|
| P1 Role clarity | Follows the EDPB organisation-as-controller reading; the provider must stay within instructions | Needs joint determination of purposes and means; the criterion is stated, its application to the EBW is not | Follows the platform example; the split of purposes between provider and owner is not stated |
| P2 Contract and arrangement | Article 28(3) contract | Article 26 arrangement | Not stated; a basis for each disclosure between controllers is needed |
| P6 Provider access to user data | Only on documented instructions | Not stated | Provider's own processing; the Council text allows access to logs "where necessary" |
| P7 Separation from other services | Not stated for the EBW (Article 5a(14) is for the EUDI Wallet) | Not stated | Not stated; Article 5a(14) suggests limits |
| P8 Data subject rights | Against the owner; how an employee exercises them is not stated | Against each controller (Article 26(3)) | Against the provider and the owner; not stated in detail |
| P9 Impact assessment and records | Owner for its processing, provider for its own; the split is not stated | Shared through the arrangement | Each controller for its own processing |
| P12 Transparency | Not stated | Essence of the arrangement is made available | Not stated for employees who never contract with the provider |
| P3 to P5 Minimisation, unlinkability, pseudonymisation | Not stated per option; the protocol-level facts apply in every option | As (a) | As (a) |

## Preliminary reading

*This section is the analysis of this project, not a statement of a source.* Three observations follow from the facts.

1. **The role question is open in the sources, so it has to be settled in the design and the contracts.** No text read allocates the roles, and the GDPR tests (Article 4(7), 4(8), 28(10)) decide by who determines purposes and means. A provider that fixes log content, retention and analytics for user data moves from option (a) towards (c) whatever the contract says.
2. **Option (a) is the closest fit for user-level data, with the provider's own operation data as the exception.** It follows the EDPB reading for employees and uses an existing contract frame. Option (b) fits only where the provider really sets purposes and means with the owner. Option (c) fits provider-side processing that the provider's regulatory duties require, but it leaves the owner without control over the data of its own users.
3. **The EUDI Wallet privacy rules are the natural reference for the EBW design, but their application is not stated.** Logical separation, no combination of data, unlinkability and consent for provider access to logs are written for the EUDI Wallet. Taking them over for the EBW would be a design choice of this project, not a requirement of a source, until the final text says otherwise. Per-credential single-use issuance has a cost for B2B volumes (P14) that stakeholders have to weigh against organisational credentials that need no person identification.

**Conditions under which this reading holds.** The final text keeps recital 39 and does not allocate the roles in a way that contradicts the GDPR tests; providers do not set purposes for user data beyond the service; the Annex keeps the log and access-control requirements that the Council text has.

**What would change it.** An adopted text or implementing act that allocates controller and processor roles for the Directory, the logs and the authorisation mappings; the EDPS comments and opinion on the proposal, which were not read; a final version of the EDPB Guidelines 01/2025; a statement that eIDAS Article 5a(14) and (16) apply to EBW providers <span class="vtag v-todo">to verify</span>; national employment-law rules on logging of employee actions; CJEU case law on controllership and pseudonymised data.

## Evidence gaps and next steps

- Obtain the outcome of the Council meeting on 9 June 2026 and re-check the privacy and logging provisions; read the EDPS comments of 20 January 2026 and the EDPS opinion, which were not read.
- Check whether eIDAS Article 5a(14), (16) and Article 5b are intended to apply to EBW providers <span class="vtag v-todo">to verify</span>.
- Read GDPR Articles 13 to 22 (information and rights) and Chapter V (transfers), which were not analysed, and Guidelines 4/2019 beyond the headings read; search for EDPB guidance specific to wallets.
- Analyse the legal basis for processing the identification record of a sole trader or a representative (Article 6 text read, no source applying it to the EBW).
- Read national employment-law restrictions on monitoring and logging (Article 88) and CJEU case law on controllership and pseudonymised data.
- Write the requirement candidates listed above and review them with a named reviewer.
- Confirm the drivers P13 to P15 with stakeholders; they are assumptions until then. The log and acting-person angle continues in [DEC-02]({{ '/architecture/decisions/dec-02/' | relative_url }}) and the identifier combination angle in [DEC-11]({{ '/architecture/decisions/dec-11/' | relative_url }}).
- Not covered here: privacy of the Commission's third-country assessments, supervisory notifications and the unique identifier regime.

## References

SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26, SRC-GDPR, SRC-EIDAS-CONSOL, SRC-CIR-2024-2979, SRC-CIR-2024-2982, SRC-ARF-HLR, SRC-ETSI-119472-2, SRC-OID4VCI-1.0, SRC-OID4VP-1.0, SRC-HAIP-1.0, SRC-AIACT, SRC-EDPB-GL-07-2020, SRC-EDPB-GL-01-2025, SRC-EDPB-GL-04-2019. Full entries with version, date and URL are in the source register.
