---
req_id: EBW-NFR-108
title: No double allocation of status list entries
category: NFR
statement: The status issuer shall prevent any unintended double allocation of a status list address and index to more than one credential.
rationale: Address and index together are a unique identifier that can be used for tracking.
sources:
- id: SRC-IETF-TSL
  location: Section 13.3 Default Values and Double Allocation
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
quote: The Status Issuer MUST prevent any unintended double allocation.
---
