---
req_id: EBW-TRU-044
title: Accept only notified access certificate trust anchors
category: TRU
statement: For verification of access certificates, the wallet unit shall accept only the trust anchors in the lists of trusted entities of the access certificate authorities notified by Member States.
rationale: Closes the trust anchor set to notified authorities.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 6, RPA_04
provenance: S
legal_status: standard
plane: trust
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
- CON-TRUST-LIST
- CON-TRUST-LIST-DISCOVERY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: a Wallet Unit SHALL accept only the trust anchors in the LoTE(s) of all Access Certificate Authorities notified by Member States.
---
