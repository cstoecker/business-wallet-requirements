---
req_id: EBW-TRU-162
title: Revoke a mandate attestation when the principal withdraws the mandate
category: TRU
statement: The issuer of a power of attorney or power of representation attestation shall revoke it when the principal withdraws the mandate.
rationale: The rulebook lists the trigger as mandatory but names no duty-holder; the issuer is derived from sections 4.14, 6.7 and 6.13, where the issuer validates the request and updates the status.
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
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Principal withdraws mandate | SHALL
---
