---
req_id: EBW-NFR-092
title: Strict access controls for contents hosted at the provider
category: NFR
statement: Where the contents of a wallet unit are stored in a service on the wallet provider back-end, the wallet provider shall specify and implement strict controls that limit its own access to those contents.
rationale: A hosted architecture cannot rule out provider access technically, so the controls must be defined and auditable.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 40, WIAM_12c
provenance: S
legal_status: standard
plane: assurance
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL specify and implement strict controls to limit access by the Wallet Provider to the contents of the Wallet Unit
---
