---
req_id: EBW-INT-030
title: Representation attestation rulebooks limit authority
category: INT
statement: The scheme provider of a representation attestation rulebook shall specify the unique attestation type and the attributes defining the validity period, the nature of the representation and the operations the representative is authorised to perform.
rationale: Gives relying parties machine-readable limits of a representative.
sources:
- id: SRC-ARF-HLR
  location: Annex 2, Topic 29 Representation, RP_01
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
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the operations the representative is authorised to perform, thereby limiting the scope of its authorisation
---
