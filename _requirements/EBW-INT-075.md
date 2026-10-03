---
req_id: EBW-INT-075
title: Signing interface specified by ETSI TS 119 432
category: INT
statement: The application programming interface of the signature creation application of a wallet unit shall comply with ETSI TS 119 432 v1.3.1, clauses 6.4.3, A.6, A.7 and A.8.
rationale: It replaces the earlier reference to the Cloud Signature Consortium specification and fixes how a relying party requests a signature from a wallet.
sources:
- id: SRC-CIR-2026-1731
  location: Annex VI, point 2, replacing point 3 of Annex IV to Implementing Regulation (EU) 2024/2979
provenance: L
legal_status: in force
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- signature creation application provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: ETSI TS 119 432 v1.3.1 (2026-03) clauses 6.4.3, A.6, A.7 and A.8
---
