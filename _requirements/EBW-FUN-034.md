---
req_id: EBW-FUN-034
title: Evaluate embedded disclosure policy against registration certificate
category: FUN
statement: The wallet unit shall evaluate an embedded disclosure policy together with the registration certificate information from the relying party to determine whether the relying party is permitted by the attestation provider to access the attestation.
rationale: Enforces issuer-defined access conditions in the wallet.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic on embedded disclosure policies, EDP_06
provenance: S
legal_status: standard
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: evaluate an embedded disclosure policy in conjunction with the information received from the requesting Relying Party in the registration certificate
---
