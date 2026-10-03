---
req_id: EBW-INT-039
title: Unique attestation type value in a rulebook
category: INT
statement: The scheme provider of a rulebook shall specify a value for the attestation type that is unique within the scope of the wallet ecosystem.
rationale: Relying parties and wallets identify attestation types by this value.
sources:
- id: SRC-ARF-HLR
  location: Annex 2, Topic 12 Attestation Rulebooks, ARB_05
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
quote: SHALL specify a value for the attestation type, which SHALL be unique within the scope of the EUDI Wallet ecosystem
---
