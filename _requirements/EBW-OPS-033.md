---
req_id: EBW-OPS-033
title: Wallet provider keeps the unit-to-attestation association
category: OPS
statement: The wallet provider shall maintain, for each wallet unit it has activated, the set of instance attestations and key attestations it issued to that unit, so that the association cannot be confused with that of another unit, and shall document the procedures, controls and risk analysis in the policy on unit revocation.
rationale: Revoking one unit needs a reliable record of which status entries belong to it.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 9, WUA_37
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL maintain, for each Wallet Unit it has activated, the set of WIAs and KAs it has issued to that Wallet Unit
---
