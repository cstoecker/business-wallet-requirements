---
req_id: EBW-TRU-110
title: Wallet unit verifies authenticity of received data
category: TRU
statement: The wallet unit shall verify the authenticity and validity of owner identification data and electronic attestations of attributes it receives.
rationale: Prevents storing forged or revoked credentials.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 14(2)(d)
provenance: L
legal_status: proposal
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
- CON-TRUST-PLANE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Wallet units shall verify the authenticity and validity of Business Wallets owner identification data
---
