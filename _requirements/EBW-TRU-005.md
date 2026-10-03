---
req_id: EBW-TRU-005
title: Trust anchors and status checks by relying parties
category: TRU
statement: A relying party shall use the trust anchors published for the relevant role to verify a presented credential and to check its status or revocation information.
rationale: Trust anchors are only useful if they are used both for the credential and for its status.
sources:
- id: SRC-ARF-TRUST
  location: chapter 6, relying parties and trust anchors
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- B2C
actors:
- Relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
---
