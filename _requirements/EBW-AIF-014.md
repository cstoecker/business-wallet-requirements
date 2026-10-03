---
req_id: EBW-AIF-014
title: Agent keys separate from principal credentials
category: AIF
statement: The agent provider shall ensure that an AI agent cannot access, or use without a trusted surface, the signing key used to create mandates for that agent.
rationale: If the agent can use the key that creates its own mandates, it can authorise itself beyond the owner's consent.
sources:
- id: SRC-AP2
  location: Agent Authorization, Trusted Agent Provider
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- A2A
actors:
- agent provider
- AI agent
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The Agent Provider MUST ensure that the Agent is not able to access the Agent Provider signing key, or use it without the Trusted Surface.
---
