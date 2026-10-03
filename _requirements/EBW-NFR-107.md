---
req_id: EBW-NFR-107
title: Dedicated status entry for each token of a batch
category: NFR
statement: Where credentials are issued in batches for one-time use, the issuer shall give every credential of the batch a dedicated status list entry.
rationale: A shared entry would let verifiers link the members of a batch.
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
quote: every Referenced Token MUST have a dedicated Status List entry
---
