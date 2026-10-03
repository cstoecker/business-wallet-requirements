---
req_id: EBW-NFR-106
title: Fresh status list entry for every re-issued token
category: NFR
statement: Where a credential is re-issued, the issuer shall allocate a fresh status list entry to the re-issued credential.
rationale: Re-using an entry would make the index a correlation handle across re-issuances.
sources:
- id: SRC-IETF-TSL
  location: Section 13.2 Linkability Mitigation
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- credential issuer
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: every re-issued Referenced Token MUST have a fresh Status List entry
---
