---
req_id: EBW-TRU-076
title: Schedule revocation of certificates using an insufficient algorithm
category: TRU
statement: When an algorithm or parameter becomes insufficient for its remaining intended usage, the certification service provider shall schedule the revocation of every affected certificate.
rationale: Ensures weak-algorithm certificates leave circulation in a planned way.
sources:
- id: SRC-ETSI-EN-319411-1
  location: Clause 6.4.8, OVR-6.4.8-16
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
- CON-PQC
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: then the TSP shall schedule a revocation of any affected certificate
---
