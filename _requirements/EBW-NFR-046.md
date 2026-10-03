---
req_id: EBW-NFR-046
title: Post-quantum mechanisms combined with classical mechanisms
category: NFR
statement: When the wallet provider deploys post-quantum asymmetric mechanisms, it shall use them in hybrid mode with a classically secure mechanism so that all combined mechanisms must be broken simultaneously to break the hybrid.
rationale: Hybrid use protects against regressions in the newer post-quantum schemes.
sources:
- id: SRC-ECCG-ACM-V2
  location: Section 1.4, Post-Quantum Cryptography; Notes 51 and 60
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
- M2M
actors:
- wallet provider
- trust service provider
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-PQC
created: '2026-10-03'
last_verified: '2026-10-03'
quote: These hybrid modes shall ensure that all combined pre or post-quantum cryptographic mechanisms need to be broken simultaneously
---
