---
req_id: EBW-INT-078
title: Relying party that checks status supports both mdoc mechanisms
category: INT
statement: A wallet-relying party that needs to verify the revocation status of person identification data or attestations in the mdoc format shall support both the attestation status list mechanism and the attestation revocation list mechanism.
rationale: Issuers may choose either mechanism, so a checking relying party must handle both.
sources:
- id: SRC-CIR-2026-1731
  location: Annex IV (new Annex II), clause 6.2.10.1, EAA-6.2.10.1-05.1
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: it shall support both the attestation status list mechanism and the attestation revocation list mechanism
---
