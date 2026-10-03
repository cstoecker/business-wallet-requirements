---
req_id: EBW-AIF-024
title: Mandate validity no longer than the task needs
category: AIF
statement: A mandate for an AI agent shall carry an expiry no later than the time needed to complete the assigned task.
rationale: A short validity period limits the damage window if the agent or its key is compromised.
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
- wallet owner
- agent provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: to set the exp claim for these Mandates to the smallest value that will allow the Shopping Agent to complete the assigned task.
---
