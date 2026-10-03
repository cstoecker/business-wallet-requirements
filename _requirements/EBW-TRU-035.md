---
req_id: EBW-TRU-035
title: PID provider verifies wallet unit attestation before issuance
category: TRU
statement: Before issuing person identification data to a wallet unit, the provider of person identification data shall authenticate and validate the wallet unit attestation and verify that the wallet unit belongs to a wallet solution it accepts.
rationale: Prevents issuance to untrusted or non-certified wallets.
sources:
- id: SRC-CIR-2024-2977
  location: Article 3(9)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- provider of person identification data
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: authenticate and validate the wallet unit attestation of the wallet unit
---
