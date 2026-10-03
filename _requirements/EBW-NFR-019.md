---
req_id: EBW-NFR-019
title: Transaction log excludes presented attribute values
category: NFR
statement: For presentation and wallet-to-wallet transactions, the wallet unit shall not store the values of presented attributes in the transaction log.
rationale: The log itself must not become a data leak.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 19, DASH_03a
provenance: S
legal_status: standard
plane: assurance
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the log SHALL NOT contain the value of any attributes presented to the Relying Party or the Verifier Wallet Unit.
---
