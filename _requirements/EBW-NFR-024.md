---
req_id: EBW-NFR-024
title: No token passthrough by MCP servers
category: NFR
statement: Where the wallet or an agent exposes an MCP server, the MCP server shall not accept or forward any token that was not issued for that server.
rationale: 'Token passthrough breaks accountability: downstream logs would attribute the action to the wrong identity.'
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Token Handling
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- wallet provider
- MCP server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP servers MUST NOT accept or transit any other tokens.
---
