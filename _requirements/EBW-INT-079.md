---
req_id: EBW-INT-079
title: Status token for mdoc revocation carries an expiry
category: INT
statement: The token carrying the revocation list or status list of an mdoc attestation shall contain an expiry claim.
rationale: Relying parties need the time up to which they can rely on a cached list.
sources:
- id: SRC-CIR-2026-1731
  location: Annex IV (new Annex II), clause 6.2.10.1, EAA-6.2.10.1-08
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
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the exp claim shall be present
---
