---
req_id: EBW-AIF-008
title: Each delegation hop scopes and re-binds context
category: AIF
statement: Where the wallet or an agent takes part in a multi-hop chain of agent delegation, each hop shall explicitly scope and re-bind the security context.
rationale: Without it authority can expand beyond what the principal granted.
sources:
- id: SRC-WIMSE-ARCH
  location: Section 3.4.11 AI and ML-Based Intermediaries
provenance: S
legal_status: standard
plane: governance
perspectives:
- B2B
- A2A
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
quote: each hop in the chain MUST explicitly scope and re-bind the security context
---
