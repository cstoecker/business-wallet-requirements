---
req_id: EBW-NFR-045
title: Agility without in-protocol cipher suite negotiation
category: NFR
statement: The wallet provider shall not rely on run-time cipher suite negotiation as the means of achieving cryptographic agility unless downgrade attacks are demonstrably prevented.
rationale: The roadmap warns that negotiating suites during protocol execution often leads to downgrade attacks.
sources:
- id: SRC-NISCG-PQC-ROADMAP
  location: Section 3.2, definition of cryptographic agility
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- G2B
- M2M
actors:
- wallet provider
- wallet-relying party
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-PQC
created: '2026-10-03'
last_verified: '2026-10-03'
quote: This concept must not be confused with a requirement to negotiate the cipher suite during protocol execution
---
