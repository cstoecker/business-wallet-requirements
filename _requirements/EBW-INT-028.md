---
req_id: EBW-INT-028
title: Unknown authorisation detail types refused
category: INT
statement: An authorisation server shall refuse to process any authorisation details whose type is unknown or that do not conform to the definition of their type.
rationale: Fine-grained agent permissions are only safe if unparseable ones are rejected rather than ignored.
sources:
- id: SRC-RFC-9396
  location: Section 5
provenance: S
legal_status: standard
plane: control
perspectives:
- B2B
- A2A
- M2M
actors:
- authorisation server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The AS MUST refuse to process any unknown authorization details type or authorization details not conforming to the respective type definition.
---
