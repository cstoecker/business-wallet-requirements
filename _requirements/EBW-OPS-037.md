---
req_id: EBW-OPS-037
title: Revoke a credential when its attribute values change
category: OPS
statement: The provider of a revocable PID or attestation shall revoke it if the value of one or more attributes of the corresponding logical credential changed, and the technical credential is still valid for at least 24 hours.
rationale: A credential must not keep stating values that are no longer true.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 7, VCR_09
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
- attestation provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: if the value of one or more of the attributes in the corresponding logical PID or attestation was changed
---
