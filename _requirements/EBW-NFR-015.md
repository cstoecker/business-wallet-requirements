---
req_id: EBW-NFR-015
title: No presentation before authentication, policy and approval
category: NFR
statement: The wallet unit shall not present requested attributes until it has verified that the wallet user was authenticated by the secure cryptographic application, that embedded disclosure policies were processed, and that the user approved the presentation in part or in full.
rationale: Ensures user control over every disclosure.
sources:
- id: SRC-CIR-2024-2982
  location: Article 3(9)
provenance: L
legal_status: in force
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
- wallet user
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: do not present any requested attributes to wallet-relying parties or wallet units until the following requirements are met
---
