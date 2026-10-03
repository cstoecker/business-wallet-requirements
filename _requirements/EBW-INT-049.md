---
req_id: EBW-INT-049
title: SD-JWT VC attestations carry vct pointing to Type Metadata
category: INT
statement: The issuer of an SD-JWT VC attestation shall include the vct claim and point it to the SD-JWT VC Type Metadata.
rationale: The type identifier is the anchor for semantics in this format.
sources:
- id: SRC-ETSI-119472-1
  location: Clause 5.2.1.2, EAA-5.2.1.2-01 and -02
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- attestation provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-CROSS-SECTOR
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The vct claim shall point to the SD-JWT VC Type Metadata
---
