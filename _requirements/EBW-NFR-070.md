---
req_id: EBW-NFR-070
title: Protected channels between wallet components
category: NFR
statement: The provider of European Business Wallets shall ensure integrity, authenticity and confidentiality of the communication between the wallet back-end, front-end and secure cryptographic applications and device.
rationale: Splits across front-end, back-end and device would otherwise expose critical assets in transit. (EP Amendment 131 extends this to communication within and among all components.)
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 3(2)
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
quote: ensure integrity, authenticity and confidentiality of the communication between the Business Wallet’s back-end, front-end and secure cryptographic applications and device
---
