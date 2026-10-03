---
req_id: EBW-TRU-119
title: Separate key attestation per secure device and keystore
category: TRU
statement: The wallet provider shall provide a wallet unit with different key attestations for the wallet secure cryptographic device of the unit and for each of its keystores.
rationale: Each key store has its own revocation state, so a compromised keystore can be revoked without the device.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(b), TR_KA-2
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A wallet provider shall provide a wallet unit with different key attestations for the WSCD of the wallet unit and for each of its keystores.
---
