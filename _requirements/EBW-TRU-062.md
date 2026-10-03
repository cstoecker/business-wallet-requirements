---
req_id: EBW-TRU-062
title: Closed mandate bound to the transaction authorised
category: TRU
statement: A closed mandate shall contain a reference that binds it to the specific transaction object it authorises.
rationale: A mandate stolen from one transaction cannot then authorise another.
sources:
- id: SRC-AP2
  location: Security and Privacy Considerations, Manipulated Checkout
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- A2A
actors:
- AI agent
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The Payment Mandate MUST contain a reference to its associated Checkout.
---
