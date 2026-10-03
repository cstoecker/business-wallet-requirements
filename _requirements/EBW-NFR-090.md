---
req_id: EBW-NFR-090
title: Isolation of assets of different units on a shared device
category: NFR
statement: Where a wallet secure cryptographic application, device or keystore holds cryptographic assets of several wallet units, the wallet provider shall ensure that a wallet unit can access only the assets related to that unit.
rationale: A provider-operated hardware module can serve many units, and one unit must never reach the keys of another.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 40, WIAM_09
provenance: S
legal_status: standard
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the Wallet Provider SHALL ensure that a Wallet Unit can only access assets that are related to that Wallet Unit
---
