---
req_id: EBW-OPS-031
title: Maintain key storage revocation status until the stated time
category: OPS
statement: Where a wallet provider signs or seals a key attestation, it shall maintain the revocation status of the relevant wallet secure cryptographic device or keystore until the status expiry indicated in that attestation has passed.
rationale: It is the key-side counterpart of the commitment on instance status.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(d), LC_KA-3
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
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: it shall maintain the revocation status of the relevant WSCD or keystore until the 'key_storage_status.exp' indicated in that key attestation has passed
---
