---
req_id: EBW-NFR-086
title: Wallet instance uses a secure cryptographic device
category: NFR
statement: The wallet provider shall ensure that each wallet instance uses at least one wallet secure cryptographic device to manage critical assets.
rationale: It sets the minimum key custody for EUDI Wallets and is the reference point for a business wallet back-end.
sources:
- id: SRC-CIR-2024-2979
  location: Article 4(1)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Wallet instances shall use at least one wallet secure cryptographic device to manage critical assets.
---
