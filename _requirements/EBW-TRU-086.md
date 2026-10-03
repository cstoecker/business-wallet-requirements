---
req_id: EBW-TRU-086
title: Owner identification data anchors self-issued attestations
category: TRU
statement: The issuer of an electronic attestation of attributes that is not qualified shall include its owner identification data in the header of every such attestation, and the relying party shall verify it.
rationale: Shows how a secondary-identifier attestation issued after authentication is trusted through the primary identity.
sources:
- id: SRC-WEBUILD-RB
  location: rb-duns rulebook, Section 5.2
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
actors:
- attestation issuer
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-LEGAL-PERSON-ID
- CON-MULTI-TRUST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The EBWOID SHALL be included in the header of every EAA.
---
