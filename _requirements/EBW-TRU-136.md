---
req_id: EBW-TRU-136
title: A valid unit attestation is required to operate
category: TRU
statement: A European Business Wallet unit shall hold a valid wallet unit attestation in order to operate within the business wallet ecosystem.
rationale: It ties the operation of a unit to the attestation, so that revoking the attestation stops the unit.
sources:
- id: SRC-WEBUILD-ARCH
  location: adr/wallet-unit-lifecycle-management.md, Decision (status Proposed, 11 Feb 2026)
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A valid WUA is required for a Wallet Unit to operate within the EBW ecosystem.
---
