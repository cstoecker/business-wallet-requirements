---
req_id: EBW-INT-088
title: A restricted power of attorney states the restricted faculty or service access
category: INT
statement: Where a power of attorney attestation indicates that the power is restricted, it shall state either the faculty or the service access to which the restriction applies.
rationale: A bare restriction flag gives a verifier no way to evaluate the limit placed on a representative.
sources:
- id: SRC-WEBUILD-RB
  location: rb-poa-pox/README.md, section 2.9, integrity rule IR-12
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- B2G
actors:
- attestation issuer
- relying party
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: either the value `ProxyPowerScope.Faculty` or `ProxyPowerScope.ServiceAccess` SHALL exist
---
