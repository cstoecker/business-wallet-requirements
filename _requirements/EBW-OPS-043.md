---
req_id: EBW-OPS-043
title: Recovery after loss of the key-holding device or module
category: OPS
statement: The wallet provider shall document, for each custody model it offers, how the owner regains the ability to use a wallet unit after loss of the device or module that holds its keys, and which backup copies of keys exist.
rationale: 'Derived (criterion C5 of the DEC-03 page): keys are not exportable and backup of remote qualified keys is limited to the minimum, so recovery has to be designed per custody model; the sources are silent.'
sources:
- id: SRC-EIDAS-CONSOL
  location: Article 29a(1)(b)
provenance: D
legal_status: in force
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
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the number of duplicated datasets must not exceed the minimum needed to ensure continuity of the service
---
