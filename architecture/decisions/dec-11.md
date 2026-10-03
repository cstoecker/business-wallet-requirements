---
title: "DEC-11 Identifiers, assurance and partners outside the EU"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 11
permalink: /architecture/decisions/dec-11/
description: "Primary identifiers (EUID, EBWOID, EU Company Certificate), secondary identifiers (BPN, LEI, party GLN, EORI, VAT, DUNS), LEI credentials without KERI, levels of assurance, and interaction with partners outside the EU and with partners without a business wallet: facts, criteria, options and conditions."
keywords: [EUID, EBWOID, EU Company Certificate, LEI, vLEI, KERI, GLN, BPN, EORI, level of assurance, third countries, non-EBW, European Business Wallet]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-11 Identifiers, assurance and partners outside the EU

*Analysis for decision, not a decision. The European Business Wallet (EBW) is a Commission proposal (COM(2025) 838); the EU Company Certificate and the EUID are Directive law that Member States apply through national transposition (deadline 31 July 2027 for Directive (EU) 2025/25). Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

An EU organisation needs one reliable **primary identifier** and, depending on the partner, several **secondary identifiers** (supply chain, customs, tax, finance, data spaces). Once the organisation has authenticated with its primary identifier, a secondary identifier should be issued quickly. For partners **outside the EU** the owner wants **LEI credentials without KERI**. Counterparties may have **no business wallet** (non-EBW). The decision also fixes which **levels of assurance** apply and how **legal compliance across Member States** is kept.

## What the requirement set says

The cluster K17 (cross-jurisdiction identity, identifiers and assurance) was added for this decision. The requirements already in the set cover the EUID in the proposal (Article 9), the form and content of owner identification data (Article 8), third countries (Articles 17 and 18) and company-law provisions. The architecture-shaping ones:

{% include cluster-drivers.html cluster="K17" %}

## Facts from the sources

**Primary identifiers.**
- The proposal says that where an EUID exists, "that identifier shall be used as the unique identifier" (Article 9(1)); otherwise a unique identifier is created under an implementing act (Article 9(2)); an owner gets no more than one (Article 9(4)). Owner identification data is issued by providers as a qualified attestation, as an attestation by or for a public body for an authentic source, or by the Commission (Article 8(1), (3)); its minimum content is the official name and the unique identifier (Article 8(5)).
- The EUID is a register-to-register identifier under Directive (EU) 2017/1132, Article 16, covering companies in Annexes II and IIB (capital companies and partnerships), not sole traders, associations or public bodies. It follows ISO 6523 with a mandatory country code, register identifier and registration number (Implementing Regulation (EU) 2021/1042, Annex, point 9).
- The EU Company Certificate (Directive (EU) 2025/25, new Article 16b of Directive 2017/1132) is accepted in all Member States as sufficient evidence of incorporation at the time of issue, contains the EUID, can be obtained electronically through the business registers, must be authenticated by trust services and be "compatible with the European Digital Identity Wallet". The digital EU power of attorney (Article 16c) is a template to authorise a representative, with the same compatibility. Both are exempt from legalisation (Article 16d).
- WE BUILD replaces the legal-person identification data (LPID) with the EBWOID rulebook: the `id` is the EUID where available, otherwise a similarly constructed identifier; attributes of the EBWOID "SHALL NOT be selectively disclosable" in that rulebook, which the proposal's selective-disclosure core function (Article 5(1)(b)) leaves open.

**Secondary identifiers.** Official or standard sources describe these forms:

| Identifier | Issuer and basis | Credential form found |
|---|---|---|
| LEI (ISO 17442) | Accredited local operating units under GLEIF; free public data | vLEI (KERI/ACDC, see below); LEI in X.509 certificates (ISO 17442-2, ETSI EN 319 412-1 "LEI" with "XG"); optional attribute in legal-person identification data (Implementing Regulation (EU) 2024/2977, table 4) |
| Party GLN | GS1 member organisations (company prefix licence) | GS1 organisation data credential on the W3C data model; WE BUILD rulebook rb-gln adds an SD-JWT VC wrapper |
| Catena-X BPN | Catena-X issuing organisation; standard CX-0010 (preview) | BPN credential issued by the core service provider (CX-0050) |
| EORI | National customs authorities; Implementing Regulation (EU) 2015/2447 | No attestation scheme found; optional attribute in 2024/2977 |
| VAT number | National tax administrations | WE BUILD rb-vat-id (public-sector attestation); ETSI organisation identifier prefix "VAT" |
| DUNS | Dun & Bradstreet (commercial) | WE BUILD rb-duns: self-issued attestation chained to the EBWOID, which "SHALL be included in the header of every EAA" |

**LEI without KERI.** GLEIF's governance framework says all vLEI credentials "MUST be ACDC compliant", issuer and holder identifiers "MUST be KERI AIDs" and signatures use Ed25519 in CESR format (vLEI Ecosystem Governance Framework v4.0, technical requirements part 2). ISO 17442-3:2024 defines the vLEI with ACDC and KERI (summary read; the standard text is paywalled). **No official GLEIF or ISO page read defines an LEI credential in W3C VC or SD-JWT VC form, and none says a non-KERI vLEI conforms.** A GLEIF blog of 24 February 2026 calls bridging KERI/ACDC and SD-JWT VC "future work" towards the EUDI business wallet. The non-KERI carriers that official or standard sources do contain are the three in the table above.

**Assurance.** The proposal names assurance levels only for onboarding through a representative's eID means ("substantial" or "high", Article 6(1)(e); the Council text says "high") and for critical operations (substantial, Article 6(1)(l)). It states no level for the EBWOID or for relying on it. Implementing Regulation (EU) 2015/1502 gives legal-person proofing criteria per level; for "high" it needs "at least one unique identifier representing the legal person used in a national context" checked against an authoritative source. A qualified provider verifying identity before issuing a qualified attestation must use high-confidence methods (eIDAS Article 24(1a)); it may verify attributes by means of a qualified attestation (Article 24(1b)(c)).

**Partners outside the EU and partners without a wallet.**
- The Commission may recognise third-country business wallets by implementing act (Article 17); a third-country operator may own an EBW once it has an EBWOID and a unique identifier, with identity proofing by the eIDAS Article 24(1a) methods, and only one set (Article 18). The identifier rules for such operators follow the Article 9 implementing act, not yet drafted in the sources read. LEI, EORI, GLN and KERI do not occur in the proposal text.
- eIDAS recognises third-country trust services only by implementing act or agreement (Article 14). Cross-border recognition of attestations (Article 45b(3)) concerns public-body attestations from authentic sources and says nothing on third countries or private-source credentials such as LEI, GLN or BPN.
- The proposal does not define how a counterparty without a wallet verifies a presentation. The Directory is open only to owners, representatives and providers. Public routes that exist: the EUID in the business register portal, the EU Company Certificate in paper form through its protocol number, qualified signatures and seals through trusted lists, the LEI through free GLEIF data, and registered delivery. Persons that do not use the EUDI Wallet "shall not in any way be restricted or made disadvantageous" (eIDAS Article 5a(15)).

## Decision criteria

| # | Criterion | Basis |
|---|---|---|
| I1 | One primary identifier per owner, EUID where it exists | source: proposal Article 9(1), (4) |
| I2 | Coverage of sole traders, associations, public bodies and non-EU entities | source (partial): EUID scope limit; rest is a driver |
| I3 | Secondary identifier issued quickly after authentication with the primary identifier | driver; the only time figures are one working day for the Directory and 24 hours for revocation publication |
| I4 | Secondary credentials anchored in the primary identity | source: WE BUILD rb-duns pattern; driver for the EU level |
| I5 | Authentic source of each identifier | source: differs per identifier |
| I6 | LEI credential without KERI | driver (owner's requirement); source facts above |
| I7 | Recognition of the LEI-based evidence outside the EU | driver; no legal effect text found |
| I8 | Level of assurance of the primary and the secondary credentials | source (partial): Regulation 2015/1502, eIDAS Article 24; a level for the EBWOID is not stated |
| I9 | Verification by a counterparty without a wallet | driver; public routes exist |
| I10 | Unlinkability and control of how identifiers are combined | source (partial): selective disclosure; the EBWOID id appears in every chained credential |
| I11 | Compliance across Member States (national registers differ) | source: Directive 2025/25 acceptance rules; Article 8(2) authentic-source notifications |
| I12 | Persistence of the identifier over conversions and mergers | driver |

## Options

**Primary identifier.**
- *P1. EUID alone where it exists, a national equivalent otherwise* (proposal text). Simple, but does not cover entities outside Annexes II and IIB beyond the Article 9(2) implementing act.
- *P2. EBWOID as the single primary attestation with the EUID inside* (WE BUILD profile). Fits Article 9(4); the unresolved point is selective disclosure.
- *P3. EBWOID as primary, the EU Company Certificate as richer supporting evidence.* The certificate is a register-issued proof of incorporation and representation, not a second identifier; WE BUILD's advice records that the EBWOID must not preclude fuller identity attestations.
- *P4. Several primary identifiers per owner.* Conflicts with Article 9(4) and Article 18(2) as stated.

**Secondary identifiers after authentication.**
- *S1. The authentic-source issuer issues a credential after verifying a presented EBWOID* (tax, customs, register, as qualified or public-sector attestation).
- *S2. A self-issued attestation of the owner, anchored in the EBWOID* (WE BUILD pattern for DUNS).
- *S3. An ecosystem authority issues after validating the EBWOID* (GS1 member organisation, Catena-X core service provider, vLEI issuer).
- *S4. The business-wallet provider issues all secondary credentials on the owner's behalf.* Not stated in the sources.

**LEI credential without KERI** (all outside the official GLEIF scheme).
- *L1. LEI as an attribute in an EBWOID-type or legal-person identification attestation* (table 4 of 2024/2977).
- *L2. A qualified or public-sector attestation of the LEI, issued by a qualified provider that checks the LEI record against free GLEIF data.* Not defined in the sources.
- *L3. LEI in qualified certificates* (ETSI EN 319 412-1; ISO 17442-2).
- *L4. A GLEIF-governed LEI credential in SD-JWT VC or W3C VC form.* No such offering found; it would need a GLEIF or Regulatory Oversight Committee decision.
- *L5. vLEI through a gateway.* KERI-based, excluded by the owner.

**Partners outside the EU.**
- *N1. The partner obtains an EBW under Article 18*, with an EBWOID and an Article 9(2) identifier.
- *N2. The Commission recognises a third-country framework* (Article 17).
- *N3. Acceptance of LEI-based evidence by relying-party policy*, without legal effect text.
- *N4. Presentation of the EBWOID or the EU Company Certificate through non-wallet channels* (registered delivery, a signed document with a qualified seal, a public register link).

## Preliminary reading

*The analysis of this project, not a statement of a source.*

1. **Treat the EBWOID as the single primary identity and the EU Company Certificate as supporting evidence.** This is the combination the proposal's Article 9(4) allows and the WE BUILD profile uses; it avoids two competing primaries. Whether EBWOID attributes can be disclosed selectively has to be settled, because every chained credential carries the EBWOID.
2. **Model secondary identifiers as credentials bound to the EBWOID** (options S1 to S3, by authentic source): the issuer verifies a presented EBWOID, issues a credential that references it, and the credential carries its own status. This gives the "quick issue after authentication" the owner wants, but "quick" needs a target set by stakeholders (driver I3), because no source gives one.
3. **LEI without KERI: be explicit about what it is.** The official sources contain no non-KERI LEI credential, so a non-KERI credential would be an *LEI attestation*, not a vLEI, and must not be presented as one. Of the options, L1 and L3 exist today; L2 depends on the legal weight of a qualified provider's attestation of an LEI; L4 needs GLEIF. A practical path is L2 for the credential and L3 for sealing, with a request to GLEIF to state its position on non-KERI carriers. The claim "the LEI credential is accepted outside the EU" cannot be made yet (I7).
4. **Partners outside the EU:** combine N1 for partners that want a wallet, N3 for LEI-based evidence at relying-party policy level, and N4 for partners without any wallet; N2 depends on the Commission. For every channel the page should say what the counterparty can verify without a wallet (the public register, GLEIF data, trusted lists).
5. **Levels of assurance:** state the level per credential class instead of per wallet. A primary credential issued after identity proofing under Article 24(1a) methods corresponds to the "high" criteria of Regulation 2015/1502 only where a national unique identifier is checked against an authoritative source, which the EUID is; secondary credentials inherit the assurance of the presented primary credential plus the issuer's own checks. A level for the EBWOID is not stated in any source, so this is a proposal.

**Conditions under which this reading holds.** The final text keeps Articles 8, 9, 17 and 18; Member States notify authentic sources; qualified providers accept to attest identifiers; relying parties accept chained credentials.

**What would change it.** The Article 9 implementing act (format of non-EUID identifiers and of identifiers of non-EU entities); a Commission decision under Article 17; a GLEIF position on non-KERI LEI credentials or ISO work on them; the Commission annex of the proposal; the national transposition of Directive 2025/25 and the implementing acts on the Certificate and the power of attorney; the EU Inc proposal COM(2026) 321, which refers to the Business Wallet signing function and the EUID.

## Gaps and next steps

- Write the requirements the gaps imply (LoA per credential class, verification path for non-wallet counterparties, selective disclosure of the EBWOID, secondary-credential issuance rules) after stakeholder confirmation of the drivers.
- Read: GS1 pages (blocked to automated access), the GLEIF governance documents beyond the technical requirements, the ISO 17442-3 text through an authorised copy, the VAT and anti-money-laundering rules on the EUID, and the outcome of the Council meeting of 9 June 2026.
- Ask GLEIF and the Regulatory Oversight Committee whether a non-KERI LEI credential is conceivable under their governance.
- Check whether the implementing acts on the EU Company Certificate and the power of attorney exist yet.

## References

SRC-EBW-PROPOSAL, SRC-EIDAS-CONSOL, SRC-CIR-2024-2977, SRC-CIR-2021-1042, SRC-DIR-2017-1132, SRC-DIR-2025-25, SRC-COM-2026-321, SRC-WEBUILD-RB, SRC-WEBUILD-ARCH, SRC-ARF-HLR, SRC-CX-0050. Further sources for LEI, GS1, Catena-X and customs identifiers are in the source register.
