---
req_id: EBW-AIF-017
title: Consent surface not driven by an AI model
category: AIF
statement: The trusted surface that obtains consent for a mandate shall be operated without a non-deterministic AI model handling its communication.
rationale: A model-driven consent surface could be manipulated by the same agent it is meant to constrain.
sources:
- id: SRC-AP2
  location: Specification, Agentic vs Non-Agentic
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2C
- A2A
actors:
- agent provider
- trusted surface
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AI-SAFETY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: 'The following role MUST be non-agentic:'
---
