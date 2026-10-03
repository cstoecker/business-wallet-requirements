---
req_id: EBW-TRN-002
title: No stand-alone quantum-vulnerable mechanisms after 2030
category: TRN
statement: After 31 December 2030 the wallet provider shall not use quantum-vulnerable public-key mechanisms stand-alone for high-risk use cases and shall complete their transition to post-quantum or hybrid mechanisms by then.
rationale: 'High-risk uses include long-term confidentiality and long-lived signing infrastructure, which the roadmap sets as the first deadline. Derived: the roadmap addresses Member States and is not binding on providers.'
sources:
- id: SRC-NISCG-PQC-ROADMAP
  location: Section 4.1, Overview (paragraph on hybrid solutions) and Timeline, milestone 2
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
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-PQC
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: For high-risk use cases, quantum-vulnerable public-key mechanisms shall not be used stand-alone after the end of 2030
---
