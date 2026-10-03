---
req_id: EBW-INT-076
title: Wallet provider uses token status lists for instance and key status
category: INT
statement: The wallet provider shall use Token Status Lists as the revocation mechanism for both key attestations and wallet instance attestations.
rationale: It fixes one format for the status of wallet components.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(e), R_GEN-1
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A wallet provider shall use Token Status Lists (specified in IETF Token Status List) as the revocation mechanism
---
