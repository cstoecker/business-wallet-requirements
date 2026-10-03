---
req_id: EBW-AIF-003
title: Auth-required state is not itself an authorisation
category: AIF
statement: Where the wallet or an agent implements A2A, the agent shall not treat the TASK_STATE_AUTH_REQUIRED transition, by itself, as authorisation for any operation, and shall define how an authorised operation is identified and checked.
rationale: A2A does not define the scope or revocation of an in-task authorisation, so a mandate model must be supplied by the implementer.
sources:
- id: SRC-A2A
  location: Section 7.6.4 In-Task Authorization Scope
provenance: S
legal_status: ecosystem
plane: governance
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Agents MUST NOT treat the TASK_STATE_AUTH_REQUIRED state transition, by itself, as authorization for any particular operation.
---
