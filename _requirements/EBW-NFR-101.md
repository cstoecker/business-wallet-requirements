---
req_id: EBW-NFR-101
title: Key attestation shown only to issuers
category: NFR
statement: A wallet unit shall present a key attestation only to a provider of person identification data or an attestation provider as part of issuance of a person identification data or key-bound attestation, and not to a relying party or any other entity.
rationale: It keeps the key attestation from becoming a correlation handle at relying parties.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 9, WUA_07
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL present a KA only to a PID Provider or Attestation Provider
---
