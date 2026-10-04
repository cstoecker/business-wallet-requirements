---
req_id: EBW-TRU-173
title: Issuer establishes the principal's authority before issuing a power of attorney
category: TRU
statement: The issuer of an EU power of attorney attestation shall reject the issuance if the authority of the principal to act on behalf of the company cannot be established.
rationale: The rulebook gives this check as protection against invalid delegation chains in which a person without authority grants powers.
sources:
- id: SRC-WEBUILD-RB
  location: rb-eu-poa/README.md, section 2.9, integrity rule IR-03
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- attestation issuer
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Issuer SHALL reject issuance if principal authority cannot be established.
---
