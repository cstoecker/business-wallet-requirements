# RES-dec08-privacy: privacy and data protection (K09)

Scope: facts from primary sources only; no recommendation; not legal advice. Date of work: 2026-10-03. Decision question (DEC-08): how are minimisation, unlinkability and the controller and processor roles designed when the wallet owner is an organisation and the users are people?
Source IDs reuse `_data/graph/sources.yml`; sources not yet registered are marked (new) and listed in `/tmp/cand/I4-new_sources.yml`. Read states: read = the cited passage was read in the full text of the original; partly-read = the cited section was read, the rest of the document was not; snippet = read only through a search hit; unverified = not read.
Local texts used: EBW proposal /tmp/claude-0/s/838.txt; Council ST 9684/26 /tmp/w; eIDAS consolidated 2024-10-18; GDPR /tmp/claude-0/w/gdpr.txt (OJ text); CIR 2024/2979, 2024/2982, CIR 2026/1731; ARF Annex 2.02 /tmp/cand/eu/hl.txt; OpenID4VCI/4VP/HAIP; ETSI TS 119 472-2 V1.2.1; EDPB Guidelines 07/2020 v2.1 (adopted 7 July 2021, minor corrections 20 Sept 2022), Guidelines 01/2025 on pseudonymisation (adopted 16 January 2025, version for public consultation) and Guidelines 4/2019 v2.0 (downloaded from edpb.europa.eu).
Caveat 1: COM(2025) 838 is a proposal; the Council text of 2 June 2026 differs; the outcome of the Council meeting of 9 June 2026 was not read. The EDPS formal comments of 20 January 2026 and the EDPS opinion on the Commission proposal were not read (no access to the documents; only their existence is stated in the texts).
Caveat 2: the EDPB Guidelines 01/2025 are the consultation version; a final version was not found. Guidelines 4/2019 on data protection by design were read only for headings and the minimisation passages located by search (partly-read).
Caveat 3: no CJEU judgment was read (for example on the concept of personal data or on pseudonymised data), and no national employment-law rules were read.

## (A) FACTS FROM SOURCES

### A1 Who the data subjects and the data are in an EBW
- A1.1 Owner and user. The owner is "an economic operator or public sector body that owns or has a right of use of a European Business Wallet"; a user is "a natural or legal person, or a natural person representing another natural person or a legal person, that uses European Business Wallets" | SRC-EBW-PROPOSAL Art 3(7), 3(22) | read. Economic operators include natural persons "acting in a commercial or professional capacity" | Art 3(4) | read.
- A1.2 GDPR scope for legal persons. "This Regulation does not cover the processing of personal data which concerns legal persons", including name, form and contact details of the legal person. | SRC-GDPR recital 14 | read. Natural persons behind a legal person (users, representatives, sole traders) remain data subjects.
- A1.3 Directory content. The Directory "includes personal data of economic operators"; minimum content in the Council text: official name of the owner "as stated in the national register of the owner's country of establishment or habitual residence", unique identifier, digital address and country | SRC-COUNCIL-ST-9684-26 recital 38 and Art 10(3a) | read. Commission recital 38 has the same first statement | SRC-EBW-PROPOSAL | read.
- A1.4 Directory protection. Recital 39: GDPR "applies to all personal data processing activities under this Regulation"; Directory processing will follow minimisation, purpose limitation, data protection by design and by default and "include, where appropriate, features of pseudonymisation" | SRC-EBW-PROPOSAL recital 39 | read; Council recital 39 is the same in substance | read. The legislative financial statement says the Commission "shall implement the European Digital Directory in accordance with the relevant principles of data protection including, where appropriate, with the features of pseudonymisation" | SRC-EBW-PROPOSAL digital policy table | read. No article of the proposal repeats this duty.
- A1.5 Selective disclosure as privacy measure. The Commission explanatory memorandum says selective disclosure "also serves as a measure for the protection of personal data" | SRC-EBW-PROPOSAL fundamental rights section | read; Art 5(1)(b) provides for selective disclosure of owner identification data and attributes | read.
- A1.6 Other personal data in the wallet. Users, authorised representatives and their roles appear in logs, authorisation mappings and attestations (Art 5(1)(j), 6(2)(b); Council Annex 7, 12) | read. The articles read contain no controller, processor or joint-controller allocation between owner, user, provider and Commission. The words "controller" and "processor" do not occur in the Commission text or the Council text (searched), apart from references to Regulation (EU) 2016/679.
- A1.7 Supervisory cooperation. Supervisory bodies shall "cooperate with supervisory authorities established pursuant to Article 51 of Regulation (EU) 2016/679" | SRC-EBW-PROPOSAL Art 13(5)(g) | read.
- A1.8 No unlinkability clause. The stems unlink and correlat do not occur in the proposal or in the Council text (searched). The Council Annex asks that "visibility of credentials and attestations is selective and conditioned on access rights" | SRC-COUNCIL-ST-9684-26 Annex 12(2)(a) | read.
- A1.9 Logs and the acting person. The Council log content (time and date, relying party data, data types, reason for non-completion) lists no field for the acting user; separately "all access and execution events are logged, timestamped, and bound to cryptographically verifiable proofs of authorisation" | SRC-COUNCIL-ST-9684-26 Annex 7(2), 12(2)(c) | read.
- A1.10 Provider access to logs. Council text: logs "shall be accessible to the European Business Wallets provider, where it is necessary for the provision of European Business Wallets services" without a consent condition; for the EUDI Wallet the same access is "on the basis of explicit prior consent by the wallet user" | SRC-COUNCIL-ST-9684-26 Annex 7(5); SRC-CIR-2024-2979 Art 9(5) | read.

### A2 GDPR provisions on roles and design
- A2.1 Controller and processor. A controller "alone or jointly with others, determines the purposes and means of the processing"; a processor "processes personal data on behalf of the controller" | SRC-GDPR Art 4(7), 4(8) | read.
- A2.2 Joint controllers. "Where two or more controllers jointly determine the purposes and means of processing, they shall be joint controllers."; they set responsibilities "by means of an arrangement" whose essence is made available to the data subject; the data subject may exercise rights "in respect of and against each of the controllers" | Art 26(1) to (3) | read.
- A2.3 Processor contract. Processing by a processor "shall be governed by a contract or other legal act"; the processor "processes the personal data only on documented instructions from the controller" | Art 28(3)(a) | read; a processor that determines purposes and means "shall be considered to be a controller in respect of that processing" | Art 28(10) | read.
- A2.4 Persons under authority. Persons acting under the authority of the controller or processor "shall not process those data except on instructions from the controller" | Art 29 | read.
- A2.5 Principles. Personal data shall be "adequate, relevant and limited to what is necessary in relation to the purposes" and kept identifiable "for no longer than is necessary" | Art 5(1)(c), (e) | read; the controller must demonstrate compliance | Art 5(2) | read.
- A2.6 Design and default. Controllers implement measures "such as pseudonymisation" and, by default, "only personal data which are necessary for each specific purpose of the processing are processed" | Art 25(1), 25(2) | read.
- A2.7 Records and security. Controllers keep a record of processing activities with purposes, categories and recipients, and time limits for erasure "where possible" | Art 30(1) | read; security measures include "the pseudonymisation and encryption of personal data" | Art 32(1)(a) | read.
- A2.8 DPIA. Required "where a type of processing in particular using new technologies ... is likely to result in a high risk"; the controller does it "prior to the processing"; content in Art 35(7) | Art 35(1), 35(7) | read. A single assessment "may address a set of similar processing operations that present similar high risks".
- A2.9 Breach. Notification to the authority "not later than 72 hours" after becoming aware of a breach | Art 33(1) | read.
- A2.10 Employment. Member States may provide "more specific rules" for employees' data, with "suitable and specific measures" including "monitoring systems at the work place" | Art 88(1), (2) | read.
- A2.11 Recital 26. Pseudonymised data "which could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person" | SRC-GDPR recital 26 | read.

### A3 EDPB guidelines
- A3.1 Organisation as controller. "it is usually the organisation as such, and not an individual within the organisation", such as an employee, that acts as a controller | SRC-EDPB-GL-07-2020 (new) executive summary | read.
- A3.2 Employees. processing by employees within the organisation's activities "may be presumed to take place under that organisation's control"; footnote: employees are generally not controllers or processors but persons acting under the authority of the controller or processor (Art 29 GDPR) | paragraph 19 and fn 9 | read. The organisation must ensure "adequate technical and organizational measures, including e.g. training and information to employees" | paragraph 19 | read.
- A3.3 Processor test. A processor must be "a separate entity in relation to the controller" and process "on the controller's behalf"; "essential means" stay with the controller, non-essential means may be left to the processor | executive summary and the discussion of essential means | read.
- A3.4 Service provider as controller in its own right. In an example, a taxi booking platform used by a company for its employees is a controller of the employee data "in its own right" because it independently designed the platform and decides categories and retention; a call-centre provider that cannot use data for other purposes is a processor | examples near paragraph 83 | read.
- A3.5 Pseudonymised data stays personal. Pseudonymised data that could be attributed by additional information "is to be considered information on an identifiable natural person", which "also holds true if pseudonymised data and additional information are not in the hands of the same person" | SRC-EDPB-GL-01-2025 (new) executive summary | read.
- A3.6 No general obligation. "The GDPR does not impose a general obligation to use pseudonymisation." | executive summary | read.
- A3.7 Pseudonymisation domain. The context in which attribution is precluded is called the "pseudonymisation domain", often "the set of all authorised recipients"; effectiveness "is highly dependent on the choice of the pseudonymisation domain and its isolation from additional information" | executive summary | read.
- A3.9 Joint controllers. The criterion for joint controllership is "the joint participation of two or more entities in the determination of the purposes and means of a processing operation". | SRC-EDPB-GL-07-2020 executive summary | read.
- A3.8 Guidelines 4/2019 on Article 25 exist (v2.0, 20 October 2020); only the table of contents and the minimisation headings were read | SRC-EDPB-GL-04-2019 (new) | partly-read.

### A4 eIDAS rules for the EUDI Wallet that the proposal does not repeat for the EBW
- A4.1 Control. "Users shall have full control of the use of and of the data in their European Digital Identity Wallet." | SRC-EIDAS-CONSOL Art 5a(14) | read.
- A4.2 Provider limits. The provider shall not collect usage information not necessary for the service nor combine personal data with other services; "Personal data relating to the provision of the European Digital Identity Wallet shall be kept logically separate from any other data held by the provider" | Art 5a(14) | read.
- A4.3 Tracking and unlinkability. The technical framework shall "not allow providers of electronic attestations of attributes or any other party, after the issuance ... to obtain data that allows transactions or user behaviour to be tracked, linked or correlated" and shall "enable privacy preserving techniques which ensure unlinkability, where the attestation of attributes does not require the identification of the user" | Art 5a(16)(a), (b) | read.
- A4.4 Pseudonyms and dashboard. The wallet enables the user to "generate pseudonyms and store them encrypted and locally" and to access a log with options to request erasure and report a relying party | Art 5a(4)(b), (d) | read.
- A4.5 Relying parties. "Relying parties shall not request users to provide any data other than that indicated" in the registration; they shall not refuse pseudonyms "where the identification of the user is not required by Union or national law" | Art 5b(3), 5b(9) | read.
- A4.6 Demonstrating compliance. "Compliance of such processing with Regulation (EU) 2016/679 shall be demonstrated." | Art 5a(17) | read.
- A4.7 Applicability to the EBW. Article 5a applies to European Digital Identity Wallets for natural persons; the proposal narrows the mandatory EUDI Wallet to natural persons (Art 20, recital 55). Whether Article 5a(14) and (16) apply to business wallets is not stated in the articles read.

### A5 Implementing rules and ARF
- A5.1 Logging. "wallet instances shall log all transactions with wallet-relying parties and other wallet units, including electronic signing and sealing"; log content as in the Council Annex; "Wallet providers shall ensure integrity, authenticity and confidentiality of the logged information" | SRC-CIR-2024-2979 Art 9(1) to (3) | read. Users can export the log (9(7)); logs "remain accessible for as long as they are required by Union law or national law" (9(6)).
- A5.2 Unlinkability in the protocol rules. Wallet units shall "enable privacy preserving techniques which ensure unlinkability where the electronic attestations of attributes do not require the identification of the wallet user" | SRC-CIR-2024-2982 Art 3(10) | read.
- A5.3 Pseudonyms in the ARF. "A Relying Party SHALL NOT be able to derive the User's true identity, or any data identifying the User" from the pseudonym value and pseudonym protocols must make it "impossible to correlate Pseudonyms based on their values or on metadata" | SRC-ARF-HLR Topic 11 | read. Scope-rate-limited pseudonyms must not allow any entity or collusion of entities to link pseudonyms across relying parties | Topic 11 section E | read.
- A5.4 Batch issuance in the ARF. Providers and wallet units "SHALL support the features of OpenID4VCI enabling the batch issuance of technical PIDs or attestations" | SRC-ARF-HLR Topic 10 section E | read.
- A5.5 Mediating API. "The EUDI Wallet shall by default disclose the presence of all stored EAAs' type to the mediating API" but not attributes | SRC-ETSI-119472-2 OIDFVP-HAIP-ADD-API-01 | read.

### A6 Protocol-level privacy facts (OpenID4VC)
- A6.1 Minimum disclosure and storage. Issuers and wallets "SHOULD implement Credential Formats that support selective disclosure"; "The time logs are retained for should be minimized"; issuers "SHOULD NOT store the Issuer-signed Credentials if they contain privacy-sensitive data" | SRC-OID4VCI-1.0 15.2, 15.3 | read.
- A6.2 Correlation. Unique values (claims, identifiers, issuer signature) can link presentations; countermeasures include issuing a batch "to facilitate the use of a unique Credential per presentation or per Verifier" and discarding signature values after issuance | OID4VCI 15.4.1 | read; "Verifier-to-Verifier Unlinkable Presentations" via one-time use of credential instances | SRC-OID4VP-1.0 15.5 | read.
- A6.3 Wallet attestation. "Wallet Attestations MUST NOT be reused across different Issuers." and may not carry a unique identifier of one wallet instance | SRC-HAIP-1.0 4.4.1 | read. Each credential has "its own unique, unpredictable status list index" | HAIP 6.1 | read.
- A6.4 Verifier behaviour. Wallets "SHOULD obtain explicit, informed consent"; "Transaction history and data within the Wallet SHOULD NOT be accessible to anyone other than the End-User", unless the user consents or another legal basis exists | SRC-OID4VP-1.0 15.1 | read. Verifiers "SHOULD use DCQL queries that request only the minimal set of claims" | 15.4.2 | read.
- A6.5 Identifying the issuer. Information in a credential identifying a particular issuer "may reveal information about the End-User" (military organisation and rehabilitation centre examples); a group may use a common issuer | SRC-OID4VCI-1.0 15.5 | read.
- A6.6 Trusted authority queries. "Mechanisms that require online resolution can leak information that could be used to profile the usage of the Credentials." | SRC-OID4VP-1.0 15.10 | read.
- A6.7 Errors. A wallet "SHOULD NOT return any OpenID4VP protocol errors without End-User interaction" for the Digital Credentials API case | SRC-OID4VP-1.0 15.9.2 | read.

### A7 AI Act facts bearing on employees
- A7.1 Deployers that are employers using high-risk AI at the workplace "shall inform workers' representatives and the affected workers" before use | SRC-AIACT Art 26(7) | read. Relevant only if an agent or AI component is a high-risk system (see RES-dec09 for logs).

### A8 What no source read says
- A8.1 No source read allocates controller or processor roles for an EBW between owner, user, provider and Commission. The proposal names no controller for the Directory. The Commission text says the Directory is accessible to owners, authorised representatives and providers (Art 10(4)).
- A8.2 No source read says whether an employee's identity in a log is personal data of the employee vis-a-vis the owner, how an employee exercises access or erasure rights against an owner or provider, or how the owner's interest in accountability is balanced against the employee's privacy. The EDPB guidelines read describe the general principle (A3.1, A3.2), not the wallet case.
- A8.3 No source read gives a retention period for EBW logs other than "as long as required ... by Union law or national law" (Council Annex 7(6)).

## (B) NEUTRAL DECISION CRITERIA
[S] = stated or implied by a source; [D] = project driver, to be confirmed by stakeholders.
- B1 [S] Role clarity per processing activity: who determines purposes and means (Art 4(7), 4(8), 26, 28; EDPB 07/2020).
- B2 [S] Contract and arrangement duties that follow from the roles (Art 28(3), Art 26(1)); sub-processor chain.
- B3 [S] Data minimisation and storage limitation by default (Art 5(1)(c), (e); Art 25(2); OID4VCI 15.3).
- B4 [S] Unlinkability across relying parties and between issuer and verifier (eIDAS Art 5a(16) for EUDI Wallet; 2024/2982 Art 3(10); HAIP; ARF pseudonyms), with no corresponding EBW text (A1.8).
- B5 [S] Pseudonymisation where appropriate (Directory, recital 39; Art 32(1)(a)) and the limits of pseudonymisation (A3.5 to A3.7).
- B6 [S] Provider access to user-level data: consent for EUDI Wallet logs versus "where necessary" in the Council EBW text (A1.10).
- B7 [S] Separation of data of the wallet service from other services of the provider (Art 5a(14) for the EUDI Wallet).
- B8 [S] Data subject rights when the data subject is a user of an organisation's wallet (Chapter III GDPR; erasure and reporting in CIR 2024/2982 Art 6 and 7 for the EUDI Wallet).
- B9 [S] DPIA and records of processing: who carries them for owner-side and provider-side processing (Art 35, Art 30).
- B10 [S] Employment context rules of Member States (Art 88) and worker information when AI is used (AI Act Art 26(7)).
- B11 [S] Security of processing and breach notification timelines (Art 32, 33; eIDAS 24(2)(fb) and NIS2 24-hour regimes for trust service providers).
- B12 [S] Transparency to the data subject: arrangement essence for joint controllers (Art 26(2)); information duties (Art 13/14, not read).
- B13 [D] Employee privacy against owner accountability: which identifier of the acting person appears in which log, for whom, for how long.
- B14 [D] Cost and complexity of per-credential single-use issuance (batch) for B2B volumes and for organisational credentials with no natural-person identification need.
- B15 [D] Cross-border differences in employment and data protection law for multinational owners.

## (C) OPTIONS: what the sources enable, restrict, leave open (no recommendation)

### Option (a) Owner as controller, provider as processor for user-level data
The organisation decides why and how users act in the wallet; the provider processes on documented instructions under an Article 28 contract; the provider is controller only for its own operation (account, security, billing) data.
- Enables: matches the EDPB reading that the organisation is the controller for processing by its employees (A3.1, A3.2); Article 28 gives a ready contract frame including audits and return of data (A2.3); fits the owner's right to export and to instruct transfer or deletion (proposal Art 5(1)(l) and 7(6)(f)).
- Restricts: the provider must not determine its own purposes and means for user data or it becomes controller (A2.3, A3.4); a provider that designs the log content, retention and analytics itself resembles the platform example (A3.4); the EUDI Wallet rules that forbid combining data and require logical separation have no stated EBW counterpart (A1.8, A4.7).
- Leaves open: who is controller of the Directory entry for sole traders (Commission, provider or owner); how employees exercise rights against the owner; how logs that identify the acting user are protected from the owner's own misuse (A8.2).

### Option (b) Provider and owner as joint controllers for core wallet processing
Both determine purposes and means of core processing (for example log content, authorisation mappings, signing and sealing flows), with an Article 26 arrangement.
- Enables: reflects a provider that sets the technical and functional framework while the owner sets use (A2.2); each controller is reachable by the data subject (Art 26(3)); a single arrangement can cover cross-provider flows.
- Restricts: the criteria of joint determination in the EDPB guidelines (inseparable participation) must be met; the arrangement must be made available in essence to data subjects (A2.2, A3.9); contract negotiations for many small owners.
- Leaves open: liability split; how the Commission as Directory operator fits (a third controller); effect on the provider's duties as qualified trust service provider.

### Option (c) Provider as independent controller for user-level data; owner as controller for business use
The provider treats user accounts, authentication and logs as its own processing for providing a regulated service, and the owner decides on use of attestations and mandates.
- Enables: aligns with the provider's own regulatory duties (eIDAS Art 24, NIS2, wallet provider rules incl. logging and security); clarity for security monitoring and incident response; fits the taxi example logic where the service defines its own data model (A3.4).
- Restricts: the owner may lack control over user data held by the provider; employee data flows between two controllers need a legal basis for each disclosure; the EUDI Wallet analogy (provider may not combine data, A4.2) suggests limits that the EBW text does not state.
- Leaves open: lawful basis for provider processing of employee data; transparency duties towards employees who never contract with the provider; retention when the owner ends the contract.

(Across all options the Commission's Directory role and the Member State supervisory bodies' roles are separate from the provider-owner relation; the sources read do not name the Directory controller.)

## (D) OPEN QUESTIONS AND WHAT I COULD NOT READ
- D1 Controller and processor roles for Directory, provider logs, authorisation mappings and mandates are not stated in the proposal or Council text; the EDPS comments (20 January 2026) and the EDPS opinion were not read.
- D2 Whether eIDAS Article 5a(14), (16) and Article 5b (EUDI Wallet privacy rules) are intended to apply to EBW providers or only to EUDI Wallet providers.
- D3 GDPR Articles 13 to 22 (information and rights) and Chapter V (transfers) were not analysed; EDPB Guidelines 4/2019 were not read in depth; no EDPB guidance specific to wallets was searched.
- D4 Whether an EBW owner identification record of a sole trader or a representative is processed under a legal obligation, legitimate interest or contract was not analysed (Art 6 GDPR text read, no source applying it to the EBW).
- D5 National employment-law restrictions on monitoring and logging of employee actions (Art 88 GDPR) were not read.
- D6 CJEU case law on pseudonymised data and on controllership was not read.
- D7 Privacy of the Commission's third-country assessments, supervisory notifications and the unique identifier regime is outside this note.

## (E) REQUIREMENT CANDIDATES FOUND
In `/tmp/cand/I4-trust-protocols-privacy.yml`: provider-processing-under-processor-contract, joint-controller-arrangement, owner-measures-for-processing-by-users, directory-pseudonymisation-where-appropriate, no-tracking-by-issuer-after-issuance. Existing entries already cover records of processing (EBW-LEG-016), pseudonymisation and encryption (EBW-LEG-017), DPIA (EBW-LEG-020), unlinkability across relying parties (EBW-NFR-043) and logical separation (EBW-NFR-010).
