---
req_id: EBW-TRU-163
title: Revoke a mandate attestation when the representative leaves the organisation
category: TRU
statement: The issuer of a power of attorney or power of representation attestation shall revoke it when the representative leaves the organisation.
rationale: Authority held through an employer must end with the employment; the rulebook lists the trigger as mandatory, and the issuer is derived from sections 4.14, 6.7 and 6.13.
sources:
- id: SRC-WEBUILD-RB
  location: rb-poa-pox/README.md, section 6.6 (Revocation Triggers) with sections 6.7 and 6.13
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- attestation issuer
- wallet owner
- authorised representative
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Representative leaves organization | SHALL
---
