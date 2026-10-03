---
req_id: EBW-NFR-044
title: Cryptographic agility by modular design
category: NFR
statement: The wallet provider shall design wallet and trust-service components so that cryptographic algorithms and parameters can be replaced without redesigning the surrounding protocols or systems.
rationale: 'A post-quantum transition is only feasible when cryptographic components are replaceable. Derived: the NIS Cooperation Group roadmap only recommends this and is not binding law.'
sources:
- id: SRC-NISCG-PQC-ROADMAP
  location: Section 6.3 (Next Steps), first item; definition of cryptographic agility in Section 3.2
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
- trust service provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-PQC
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: When new products are being developed, support for cryptographic agility should be considered at first.
---
