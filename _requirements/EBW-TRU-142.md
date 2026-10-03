---
req_id: EBW-TRU-142
title: Verifier can recognise several governance authorities
category: TRU
statement: A verifier in a data space shall be able to recognise the trust anchors of more than one data space governance authority.
rationale: Organisations that belong to several data spaces need one verification path that can honour each space own list of trusted issuers.
sources:
- id: SRC-DCP
  location: trust.model.md, Trust Relationships, Verifier
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- M2M
actors:
- verifier
- data space governance authority
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-MULTI-TRUST
- CON-DSP-DCP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Verifiers can recognize several Dataspace Governance Authorities.
---
