---
req_id: EBW-NFR-031
title: In-band credentials bound to the originating agent
category: NFR
statement: Where the wallet or an agent passes in-task credentials in-band through a chain of A2A agents, the credentials shall be bound to the agent that originated the request.
rationale: Otherwise any intermediary agent in the chain could reuse a credential issued for the originator.
sources:
- id: SRC-A2A
  location: Section 7.6.3 In-Task Authorization Security Considerations
provenance: D
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Credentials SHOULD be bound to the agent which originated the request
---
