---
req_id: EBW-TRU-113
title: Security level assigned to every keystore
category: TRU
statement: The wallet provider shall assign a security level to every keystore of a wallet unit, corresponding to the level of resistance for which the keystore was certified.
rationale: Credential issuers use the level to decide whether a keystore may hold the keys of a credential.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 40, WIAM_08a
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the Wallet Provider SHALL assign a security level to every keystore
---
