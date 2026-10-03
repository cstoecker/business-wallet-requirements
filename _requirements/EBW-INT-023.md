---
req_id: EBW-INT-023
title: Agent Card available at discovery location
category: INT
statement: Where the wallet or an agent implements A2A as a server, it shall make an Agent Card available describing its identity, capabilities, skills and interaction requirements.
rationale: The card is the machine-readable entry point by which counterparties find and configure interactions with a business agent.
sources:
- id: SRC-A2A
  location: Section 8.1 Purpose
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
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-CONTROL-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A2A Servers MUST make an Agent Card available.
---
