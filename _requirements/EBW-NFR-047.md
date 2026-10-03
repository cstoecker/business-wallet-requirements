---
req_id: EBW-NFR-047
title: Use recommended cryptographic suites for new signatures and seals
category: NFR
statement: The trust service provider shall use only recommended cryptographic mechanisms and key sizes to generate new signatures and seals, and shall use legacy mechanisms only where needed for interoperability with existing infrastructures.
rationale: Fixes a clear baseline for algorithm selection and phase-out.
sources:
- id: SRC-ETSI-TS-119312
  location: Clause 4, Use of SOG-IS Agreed Mechanisms
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
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-PQC
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: only SOG-IS recommended mechanisms and key sizes or cryptographic suites using these cryptographic mechanisms and key sizes should be used
---
