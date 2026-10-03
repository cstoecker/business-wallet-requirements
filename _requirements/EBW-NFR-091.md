---
req_id: EBW-NFR-091
title: Wallet provider does not read wallet contents
category: NFR
statement: The wallet provider shall not access the contents of a wallet instance, in particular the attestations present, their status, the attribute values and the transaction log.
rationale: It limits what a provider that also hosts keys or data can see; the business wallet texts allow provider log access where necessary, so the two rules differ.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 40, WIAM_12a
provenance: S
legal_status: standard
plane: trust
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
quote: SHALL NOT access the contents of a Wallet Instance
---
