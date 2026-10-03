---
req_id: EBW-NFR-027
title: Least-privilege scopes for agent tokens
category: NFR
statement: Where the wallet or an agent acts as an MCP client, the MCP client shall request only the scopes necessary for the intended operation and elevate incrementally through step-up authorization.
rationale: Narrow scopes limit the damage if an agent token is stolen and keep audit trails meaningful.
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Scope Selection Strategy
provenance: D
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- MCP client
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP clients SHOULD follow the principle of least privilege by requesting only the scopes necessary
---
