---
req_id: EBW-NFR-071
title: Cryptographic operations only after user authentication
category: NFR
statement: The wallet secure cryptographic applications and devices shall perform cryptographic operations involving critical assets, other than those needed to authenticate the owner, only where they have successfully authenticated the wallet user.
rationale: Prevents key use by an unauthenticated session.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 4(1)(a)
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: only in cases where those applications have successfully authenticated Wallets users
---
