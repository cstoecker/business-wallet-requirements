---
req_id: EBW-TRU-103
title: Unit attestation holds public keys, private keys in secure device
category: TRU
statement: The provider of European Business Wallets shall ensure that each wallet unit attestation contains public keys and that the corresponding private keys are protected by a wallet secure cryptographic device.
rationale: Allows verifiers to bind the unit to keys that cannot be extracted.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 5(1)
provenance: L
legal_status: proposal
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
quote: contain public keys and that the corresponding private keys are protected by a Wallets secure cryptographic device
---
