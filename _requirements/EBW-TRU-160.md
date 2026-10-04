---
req_id: EBW-TRU-160
title: Reject mandate attestations that are not active
category: TRU
statement: A relying party shall reject every power of attorney or power of representation attestation whose status is not active, including revoked, expired and unknown.
rationale: Treating an unknown status as acceptable would let a revoked or suspended mandate pass whenever the status service is unreachable.
sources:
- id: SRC-WEBUILD-RB
  location: rb-poa-pox/README.md, section 6.9 (Attestation Status Values)
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
quote: Relying Parties SHALL reject every attestation except those having status `active`.
---
