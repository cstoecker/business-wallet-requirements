---
req_id: EBW-INT-042
title: Rulebook states disclosure mode for every SD-JWT VC claim
category: INT
statement: The scheme provider of a rulebook using SD-JWT VC shall specify for all claims whether an attestation provider must, may or must not make that claim selectively disclosable.
rationale: Makes selective disclosure behaviour predictable for relying parties.
sources:
- id: SRC-ARF-HLR
  location: Annex 2, Topic 12 Attestation Rulebooks, ARB_30
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- attestation scheme provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: whether an Attestation Provider MUST, MAY, or MUST NOT make that claim selectively disclosable
---
