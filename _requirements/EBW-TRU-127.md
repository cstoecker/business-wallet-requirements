---
req_id: EBW-TRU-127
title: Short-lived attestations need no revocation
category: TRU
statement: Revocation of a short-lived electronic attestation of attributes with a validity period of 24 hours or less shall not be required.
rationale: It allows an alternative to status checking and defines the threshold.
sources:
- id: SRC-CIR-2026-1731
  location: Annex IV (new Annex II to Implementing Regulation (EU) 2024/2979), clause 4.2.13, EAA-4.2.13-03
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
- qualified trust service provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Where short-lived electronic attestations of attributes with a validity period of 24 hours or less are issued, revocation shall not be required.
---
