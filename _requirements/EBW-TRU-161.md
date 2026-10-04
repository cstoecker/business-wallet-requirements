---
req_id: EBW-TRU-161
title: Verify identifier, status, validity and issuer before accepting a mandate
category: TRU
statement: Before accepting a power of attorney or power of representation attestation, the relying party shall verify the attestation identifier, its current status, its validity period and the status of its issuer.
rationale: Status checking of a mandate has to include the issuer, because a suspended issuer can no longer vouch for the mandate.
sources:
- id: SRC-WEBUILD-RB
  location: rb-poa-pox/README.md, section 6.10 (Status Verification)
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the Relying Party SHALL verify attestation identifier, current status, validity period and issuer status
---
