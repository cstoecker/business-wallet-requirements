---
req_id: EBW-TRU-123
title: Type-shared key status revoked only for a device type vulnerability
category: TRU
statement: Where a wallet provider uses a status index shared by all key attestations of a type of secure device or keystore, it shall revoke that index only if the type has a security vulnerability.
rationale: A shared index revokes every unit with that device type at once.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(e), R_KA-4
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
quote: shall only revoke a 'key_storage_status.status' entry if the type of WSCD or keystore has a security vulnerability
---
