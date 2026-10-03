---
req_id: EBW-INT-029
title: Delegation chain represented as nested actors
category: INT
statement: Where authority passes through several actors, the token or mandate shall represent the chain with the current actor outermost and prior actors nested within it.
rationale: A verifiable history of delegation lets auditors reconstruct who passed authority to whom.
sources:
- id: SRC-RFC-8693
  location: Section 4.1
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- A2A
actors:
- authorisation server
- AI agent
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The outermost "act" claim represents the current actor while nested "act" claims represent prior actors.
---
