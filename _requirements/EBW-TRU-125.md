---
req_id: EBW-TRU-125
title: Revoked unit attestations of a withdrawn solution stay revoked
category: TRU
statement: When a Member State withdraws a wallet solution, it shall ensure that the wallet unit attestations of the affected units are revoked, cannot revert to a valid state and that no new unit attestation is issued to existing units of that solution.
rationale: It prevents a withdrawn solution from coming back through its status entries.
sources:
- id: SRC-CIR-2025-847
  location: Article 8(2), points (a) to (c)
provenance: L
legal_status: in force
plane: trust
perspectives:
- G2B
- G2G
actors:
- Member State
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the wallet unit attestations cannot revert to a valid state
---
