---
req_id: EBW-NFR-029
title: A2A authorisation checks on every operation
category: NFR
statement: Where the wallet or an agent implements A2A as a server, it shall perform authorisation checks on every A2A operation and limit results to the authenticated caller's authorised boundaries.
rationale: It prevents one counterparty from seeing the tasks of another.
sources:
- id: SRC-A2A
  location: Section 13.1 Data Access and Authorization Scoping
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- A2A server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Servers MUST implement authorization checks on every A2A Protocol Operations request
---
