---
req_id: EBW-TRU-121
title: PID technical validity ends before the status commitments
category: TRU
statement: A provider of person identification data shall end the technical validity period of the data before both the status expiry of the wallet instance attestation and the status expiry of the key attestation received in the issuance process.
rationale: Credential validity cannot outlast the period in which the wallet provider serves status for the wallet.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(d), LC_GEN-3
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The technical validity period of person identification data shall end before both the 'client_status.exp'
---
