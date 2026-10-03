---
req_id: EBW-NFR-103
title: Status index and list address unique per credential
category: NFR
statement: The provider of an mdoc attestation shall ensure that the combination of status index and status list address is unique per mobile security object.
rationale: A shared index would let relying parties correlate presentations.
sources:
- id: SRC-CIR-2026-1731
  location: Annex IV (new Annex II), clause 6.2.10.1, EAA-6.2.10.1-13.2
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
- qualified trust service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the combination of status index and URI shall be unique per MSO
---
