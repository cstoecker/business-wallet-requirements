---
req_id: EBW-TRU-159
title: Suspended mandate attestation treated as invalid
category: TRU
statement: Where a power of attorney or power of representation attestation is suspended, the relying party shall treat it as invalid for as long as the suspension lasts.
rationale: A temporarily suspended mandate must not be exercisable, so a verifier that still accepts it would undo the owner's suspension.
sources:
- id: SRC-WEBUILD-RB
  location: rulebooks/rb-poa-pox.md, section 6.5 (Suspension)
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
fidelity_checked: '2026-10-03'
revision_note: Location corrected to the registered catalogue path rulebooks/rb-poa-pox.md (commit de79cca, document version 0.7); section number and quote verified unchanged against that commit and against v0.8 of 2026-09-04.
---
