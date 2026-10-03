---
req_id: EBW-INT-022
title: MCP client discovers authorization server via metadata
category: INT
statement: Where the wallet or an agent acts as an MCP client with authorization, the MCP client shall use OAuth 2.0 Protected Resource Metadata to discover the authorization server.
rationale: It prevents an agent from being pointed at an arbitrary token issuer configured out of band.
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Overview
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
- CON-CONTROL-PLANE
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP clients MUST use OAuth 2.0 Protected Resource Metadata for authorization server discovery.
---
