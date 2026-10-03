---
req_id: EBW-TRU-075
title: CA public keys distributed with integrity and origin authentication
category: TRU
statement: The certification service provider shall make its CA signature verification keys available to relying parties in a manner that assures the integrity of the key and authenticates its origin.
rationale: Defines how trust anchors reach relying parties.
sources:
- id: SRC-ETSI-EN-319411-1
  location: Clause 6.5.1, DIS-6.5.1-16
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
- M2M
actors:
- trust service provider
- relying party
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: CA signature verification (public) keys shall be available to relying parties in a manner that assures the integrity of the CA public key
---
