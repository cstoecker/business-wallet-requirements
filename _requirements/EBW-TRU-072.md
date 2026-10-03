---
req_id: EBW-TRU-072
title: Maintenance process for CA, TSU, CRL and OCSP keys
category: TRU
statement: When a CA, time-stamping unit, CRL issuer or OCSP responder key will not remain suitable for its foreseen period, the trust service provider shall apply a maintenance process before the algorithm is broken.
rationale: Prevents a key from being relied on after its algorithm weakens.
sources:
- id: SRC-ETSI-TS-119312
  location: Clause 9.5, Time period resistance for other keys
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
- CON-REVOCATION
- CON-PQC
created: '2026-10-03'
last_verified: '2026-10-03'
quote: If they do not remain suitable for the foreseen time period, a maintenance process shall be applied before the algorithm is broken.
---
