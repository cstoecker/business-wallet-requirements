---
req_id: EBW-TRU-118
title: Key attestation states storage and authentication level
category: TRU
statement: A key attestation that mentions a wallet secure cryptographic device shall state the key storage and user authentication level 'iso_18045_high'.
rationale: Credential issuers read the level to decide whether to bind a credential to the key.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(c), C_KA-1
provenance: L
legal_status: in force
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
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The 'key_storage' and 'user_authentication' attributes shall have value 'iso_18045_high' where a key attestation mentions a WSCD
---
