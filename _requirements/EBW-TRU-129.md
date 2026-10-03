---
req_id: EBW-TRU-129
title: PID revoked when the wallet unit attestation is revoked
category: TRU
statement: A provider of person identification data shall revoke person identification data issued to a wallet unit where the wallet unit attestation of that unit has been revoked.
rationale: It carries the revocation of the wallet down to the credentials bound to it.
sources:
- id: SRC-CIR-2026-1731
  location: Article 1(3), replacing Article 5(4)(b) of Implementing Regulation (EU) 2024/2977
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: where the wallet unit attestation of the wallet unit to which the person identification data was issued to has been revoked
---
