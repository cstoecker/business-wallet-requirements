---
req_id: EBW-NFR-012
title: Wallet user authentication before any function
category: NFR
statement: The wallet unit shall not perform any wallet function other than wallet user authentication until the wallet unit has successfully authenticated the wallet user.
rationale: Prevents use of a lost or unattended wallet.
sources:
- id: SRC-CIR-2024-2979
  location: Article 3(1)
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
quote: Wallet units shall not perform any functionality listed in Article 5a(4) of Regulation (EU) No 910/2014, except wallet user authentication
---
