---
req_id: EBW-OPS-032
title: Attestations show a status period of at least 31 days
category: OPS
statement: The wallet provider shall ensure that a wallet unit can always present wallet instance attestations and key attestations whose status expiry lies at least 31 days in the future at the time of presentation.
rationale: It lets issuers set credential validity without being forced to short lives.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(d), LC_GEN-1
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: at least 31 days in the future at the time of presentation
---
