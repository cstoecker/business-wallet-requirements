---
req_id: EBW-TRU-159
title: Suspended mandate attestation treated as invalid
category: TRU
statement: Where a power of attorney or power of representation attestation is suspended, the relying party shall treat it as invalid for as long as the suspension lasts.
rationale: A temporarily suspended mandate must not be exercisable, so a verifier that still accepts it would undo the owner's suspension.
sources:
- id: SRC-WEBUILD-RB
  location: rb-poa-pox/README.md, section 6.5 (Suspension)
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- relying party
- authorised representative
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: During suspension the attestation SHALL be treated as invalid.
---
