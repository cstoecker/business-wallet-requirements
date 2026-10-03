---
req_id: EBW-NFR-076
title: Transaction log records relying party identity
category: NFR
statement: The wallet transaction log shall record the name, contact details and unique identifier of the corresponding relying party and its Member State of establishment, or, for other wallet units, relevant information from the wallet unit attestation.
rationale: Makes each transaction attributable to a counterparty.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 7(2)(b)
provenance: L
legal_status: proposal
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the name, contact details, and unique identifier of the corresponding Business-Wallet-relying party and the Member State
---
