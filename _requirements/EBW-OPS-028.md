---
req_id: EBW-OPS-028
title: Remote signing key destroyed when its certificate is revoked
category: OPS
statement: The provider of a remote signature creation service shall destroy the signing key when the corresponding public key certificate is revoked.
rationale: It ends the life of a hosted key together with its certificate and keeps revoked keys from being used.
sources:
- id: SRC-ETSI-TS-119431-1
  location: Clause 6.3.2, DEL-6.3.2-01
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified trust service provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: If the public key certificate is revoked, the corresponding signing key shall be destroyed.
---
