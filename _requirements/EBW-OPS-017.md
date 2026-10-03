---
req_id: EBW-OPS-017
title: Destroy or withdraw private keys on termination
category: OPS
statement: Before the trust service provider terminates its services, it shall destroy or withdraw from use its private keys, including backup copies, so that they cannot be retrieved.
rationale: Prevents misuse of keys of a ceased provider.
sources:
- id: SRC-ETSI-EN-319401
  location: Clause 7.12, REQ-7.12-07
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
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the TSP's private keys, including backup copies, shall be destroyed, or withdrawn from use, in a manner such that the private keys cannot be retrieved
---
