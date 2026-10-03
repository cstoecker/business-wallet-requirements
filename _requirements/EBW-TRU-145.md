---
req_id: EBW-TRU-145
title: Access certificate validation stays in the wallet
category: TRU
statement: The wallet unit shall authenticate and validate wallet-relying party access certificates itself and shall not delegate this to an operating system browser or other intermediary application.
rationale: Prevents the trust decision from moving to a platform component that the wallet provider does not control. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-CIR-2026-1731
  location: Article 4, point (2)(a) (amending Article 3(1) of Implementing Regulation (EU) 2024/2982)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- wallet unit
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: without delegating execution of these processes to an operating system browser or other intermediary application
---
