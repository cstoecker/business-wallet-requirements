---
req_id: EBW-TRU-124
title: Revoke all instance status indices of a unit
category: TRU
statement: Where a wallet unit must be revoked, the wallet provider shall revoke the index values in all wallet instance attestations associated with that unit.
rationale: Revoking only one attestation would leave the unit usable through the others.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(e), R_WIA-4
provenance: L
legal_status: in force
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
quote: shall revoke the index values in the 'client_status.status' claim in all wallet instance attestations associated with that wallet unit
---
