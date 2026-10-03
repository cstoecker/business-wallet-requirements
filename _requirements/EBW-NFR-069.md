---
req_id: EBW-NFR-069
title: Back-end uses secure cryptographic application and device
category: NFR
statement: The European Business Wallet back-end shall use at least one wallet secure cryptographic application and wallet secure cryptographic device to manage critical assets.
rationale: Business wallets are server-side, so critical assets must sit behind a tamper-resistant device.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 3(1)
provenance: L
legal_status: proposal
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: certification
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall use at least one Wallet secure cryptographic application and Wallets secure cryptographic device to manage critical assets
---
