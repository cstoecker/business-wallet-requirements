---
req_id: EBW-OPS-029
title: Remote signing key destroyed on the signer request
category: OPS
statement: The provider of a remote signature creation service shall destroy a signing key when the signer requests it.
rationale: It gives the signer an exit and a way to end a key held at a provider.
sources:
- id: SRC-ETSI-TS-119431-1
  location: Clause 6.3.2, DEL-6.3.2-02
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified trust service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The SSASP shall destroy a signing key when requested by the signer.
---
