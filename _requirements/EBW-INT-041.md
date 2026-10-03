---
req_id: EBW-INT-041
title: mdoc attributes defined in a unique namespace
category: INT
statement: The rulebook shall define each attribute of an ISO/IEC 18013-5 attestation within an attribute namespace that fully defines identifier, syntax and semantics and has an identifier unique in the ecosystem.
rationale: Avoids clashes between sectors defining attributes.
sources:
- id: SRC-ARF-HLR
  location: Annex 2, Topic 12 Attestation Rulebooks, ARB_06a
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
- CON-CROSS-SECTOR
created: '2026-10-03'
last_verified: '2026-10-03'
quote: An attribute namespace SHALL fully define the identifier, the syntax, and the semantics of each attribute within that namespace
---
