---
req_id: EBW-OPS-035
title: Tell the user of unit revocation outside the unit
category: OPS
statement: The wallet provider shall inform a user about the revocation of the user wallet unit through a communication channel that is independent of the wallet unit.
rationale: A revoked unit cannot be relied on to deliver the notice.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 38, WURevocation_16
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
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
quote: SHALL use a communication channel that is independent of the Wallet Unit
---
