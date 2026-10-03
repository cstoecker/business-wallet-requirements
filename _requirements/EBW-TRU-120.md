---
req_id: EBW-TRU-120
title: Sign a key attestation only after verifying key storage
category: TRU
statement: The wallet provider shall sign or seal a key attestation only after verifying that the keys attested are stored in the wallet secure cryptographic device or keystore described in the attestation.
rationale: The key attestation is the evidence of where a key lives, so the provider must have checked it.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(b), TR_KA-2.1
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: after the wallet provider has verified that the keys attested to in the key attestation are stored in the WSCD
---
