---
req_id: EBW-AIF-022
title: No new closed mandate before the previous is resolved
category: AIF
statement: An AI agent shall not present a further closed mandate under the same open mandate before it has received a rejection receipt for the previous one.
rationale: This prevents one open mandate from approving several overlapping actions.
sources:
- id: SRC-AP2
  location: Specification, Autonomous (Human Not Present)
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2B
- A2A
actors:
- AI agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Shopping Agents MUST NOT present any subsequent open Payment or Checkout Mandates without receiving a rejection receipt from the previous one.
---
