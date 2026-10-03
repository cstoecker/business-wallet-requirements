---
req_id: EBW-TRU-137
title: A unit cannot be valid without a valid unit attestation
category: TRU
statement: A European Business Wallet unit shall not be in the state valid unless it holds both a valid wallet unit attestation and valid owner identification data.
rationale: The consortium separates structural trust of the unit from identity trust of the owner.
sources:
- id: SRC-WEBUILD-ARCH
  location: adr/wallet-unit-lifecycle-management.md, State Transitions
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- M2M
actors:
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A Wallet Unit cannot be VALID without a valid WUA.
---
