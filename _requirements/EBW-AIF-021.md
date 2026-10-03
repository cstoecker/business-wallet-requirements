---
req_id: EBW-AIF-021
title: Cumulative budget across agent actions
category: AIF
statement: When a mandate contains a budget constraint, the verifier shall track the total of previous actions under that mandate and reject an action that would exceed the budget.
rationale: Per-action limits alone do not bound the total exposure of a reusable mandate.
sources:
- id: SRC-AP2
  location: Payment Mandate, Budget constraint
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2B
- A2A
actors:
- verifier
- AI agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the requested amount plus the total sum of amounts from previously closed Payment Mandates MUST be less than or equal to max
---
