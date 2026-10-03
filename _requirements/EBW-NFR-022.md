---
req_id: EBW-NFR-022
title: Token requests name the target MCP server
category: NFR
statement: Where the wallet or an agent acts as an MCP client, the MCP client shall include the resource parameter (RFC 8707) identifying the target MCP server in both authorization requests and token requests.
rationale: Audience-restricted tokens stop a token granted for one tool server from being replayed against another.
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Resource Parameter Implementation
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- MCP client
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MUST identify the MCP server that the client intends to use the token with.
---
