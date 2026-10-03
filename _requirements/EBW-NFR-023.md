---
req_id: EBW-NFR-023
title: MCP server validates token audience
category: NFR
statement: Where the wallet or an agent exposes an MCP server, the MCP server shall validate that each access token was issued specifically for it as the intended audience.
rationale: It enforces the security boundary between wallet-facing tools and other services.
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP servers MUST validate that access tokens were issued specifically for them as the intended audience
---
