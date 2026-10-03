---
req_id: EBW-AIF-019
title: Mandate limits enforced outside the agent
category: AIF
statement: The verifier or the wallet, not the AI agent, shall enforce the limits of a mandate on each action the agent attempts.
rationale: AP2 treats every agent and model as a potential attacker, so limits cannot depend on the agent's own compliance.
sources:
- id: SRC-AP2
  location: Security and Privacy Considerations
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2B
- A2A
actors:
- verifier
- wallet provider
- AI agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AI-SAFETY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: all LLMs and Agents MUST be considered potential attackers and are explicitly included in the threat model
---
