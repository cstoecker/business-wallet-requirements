---
req_id: EBW-FUN-054
title: Transaction data is carried in the presentation
category: FUN
statement: A wallet that receives transaction data in a presentation request shall include a representation or reference to that data in the presentation, or shall return an error where it does not support transaction data.
rationale: Binds the user authentication to the authorisation of a specific transaction, for example a qualified signature, which gives evidential value.
sources:
- id: SRC-OID4VP-1.0
  location: Section 8.4 (Transaction Data)
provenance: S
legal_status: standard
plane: assurance
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-EBW-EUDIW
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The Wallet that received the transaction_data parameter in the request MUST include a representation or reference to the data in the respective Credential presentation.
---
