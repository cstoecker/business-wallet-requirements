---
req_id: EBW-TRU-060
title: Open mandates bound to the agent's key
category: TRU
statement: A mandate that has not yet been bound to a transaction shall carry the confirmation key of the AI agent authorised to use it.
rationale: Binding to the agent's key lets a verifier confirm that the presenter is the delegated agent and no one else.
sources:
- id: SRC-AP2
  location: Agent Authorization, Mandate Structure; cf. RFC 7800 Section 3.1
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- A2A
actors:
- wallet owner
- AI agent
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Because Open Mandates need to be bound to a particular transaction before use, they MUST support cryptographic Key Binding.
---
