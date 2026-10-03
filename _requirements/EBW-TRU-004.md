---
req_id: EBW-TRU-004
title: Irreversible revocation of qualified attestations
category: TRU
statement: When a qualified electronic attestation of attributes is revoked, it shall lose its validity and its status shall not be reverted.
rationale: 'Gives relying parties a stable rule: revocation of a qualified attestation is final.'
sources:
- id: SRC-EIDAS-CONSOL
  location: Article 45d(4)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- B2C
actors:
- Attestation provider
- Relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
---
