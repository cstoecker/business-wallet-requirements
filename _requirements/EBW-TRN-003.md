---
req_id: EBW-TRN-003
title: Quantum-safe upgrade path with post-quantum signed updates
category: TRN
statement: The wallet provider shall ensure that wallet software that is expected to remain in use beyond 2030 can be upgraded to post-quantum cryptography and that its update mechanism incorporates post-quantum signature schemes for integrity and authenticity.
rationale: Authentic updates are the channel through which later algorithm migration reaches deployed wallets.
sources:
- id: SRC-NISCG-PQC-ROADMAP
  location: Section 4.2, Milestone 2 discussion
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
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-PQC
created: '2026-10-03'
last_verified: '2026-10-03'
quote: products entering the market with an expected lifetime beyond 2030 should be upgradable to PQC
---
