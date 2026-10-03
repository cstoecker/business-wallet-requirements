---
req_id: EBW-NFR-020
title: Intermediary deletes attributes right after forwarding
category: NFR
statement: An intermediary shall delete any attestations and user attributes obtained from the wallet unit completely and immediately after sending the attributes to the intermediated relying party.
rationale: Limits data retention by intermediaries.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 52, RPI_10
provenance: S
legal_status: standard
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- intermediary
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL delete any PIDs or attestations it obtained from the Wallet Unit, including any User attributes, completely and immediately
---
