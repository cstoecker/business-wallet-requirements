---
req_id: EBW-TRU-160
title: Reject mandate attestations that are not active
category: TRU
statement: A relying party shall reject every power of attorney or power of representation attestation whose status is not active, including revoked, expired and unknown.
rationale: Treating an unknown status as acceptable would let a revoked or suspended mandate pass whenever the status service is unreachable.
sources:
- id: SRC-WEBUILD-RB
  location: rulebooks/rb-poa-pox.md, section 6.9 (Attestation Status Values)
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Relying Parties SHALL reject every attestation except those having status `active`.
fidelity_checked: '2026-10-03'
revision_note: Location corrected to the registered catalogue path rulebooks/rb-poa-pox.md (commit de79cca, document version 0.7); section number and quote verified unchanged against that commit and against v0.8 of 2026-09-04.
---
