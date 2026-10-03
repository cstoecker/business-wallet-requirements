---
req_id: EBW-INT-077
title: Revocation method for mdoc attestations
category: INT
statement: 'The provider of person identification data, of qualified attestations or of public-sector attestations issued in the mdoc format shall use one of the following revocation methods: short-lived attestations of 24 hours or less, an attestation status list, or an attestation revocation list.'
rationale: It limits the choices of revocation mechanism for the mdoc format.
sources:
- id: SRC-CIR-2026-1731
  location: Annex IV (new Annex II), clause 6.2.10.1, EAA-6.2.10.1-02
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
quote: shall use one of the following methods for revocation of person identification data
---
