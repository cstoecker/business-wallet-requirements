---
req_id: EBW-TRU-006
title: Invalid wallet provider status
category: TRU
statement: When the status of a wallet provider is set to invalid, issuers shall refuse to issue attestations to wallet units of that provider.
rationale: Lets a Member State stop the use of a wallet that is no longer trusted.
sources:
- id: SRC-ARF-TRUST
  location: section 6.2.3
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2G
- B2C
actors:
- Issuer
- Member State
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
---
