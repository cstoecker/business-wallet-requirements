---
req_id: EBW-AIF-018
title: Mandate verification in deterministic code
category: AIF
statement: Validation of mandates and processing of their constraints shall be performed in deterministic code, not by an AI model.
rationale: Verification that depends on a language model can be steered by prompt injection.
sources:
- id: SRC-AP2
  location: Specification, Agentic vs Non-Agentic
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2B
- A2A
actors:
- verifier
- relying party
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AI-SAFETY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: it MUST happen in deterministic code regardless of whether the role is agentic or not
---
