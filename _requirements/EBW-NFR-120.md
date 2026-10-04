---
req_id: EBW-NFR-120
title: Log names the authorised user for each signing or sealing
category: NFR
statement: The wallet provider shall record in the transaction log, for each use of a signing or sealing key, the authorised user who triggered it.
rationale: 'Derived (criteria C4, C14 of the DEC-03 page): the log content in Annex point 7(2) names the relying party and data types but not the user, so use of one seal key by several users cannot be attributed.'
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 7(1)
provenance: D
legal_status: proposal
plane: assurance
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
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall include, at a minimum, electronic signing, electronic sealing, and notifications of all transactions
---
