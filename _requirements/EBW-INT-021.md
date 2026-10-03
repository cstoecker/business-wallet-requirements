---
req_id: EBW-INT-021
title: MCP server publishes protected resource metadata
category: INT
statement: Where the wallet or an agent exposes an MCP server over an HTTP-based transport with authorization, the MCP server shall implement OAuth 2.0 Protected Resource Metadata (RFC 9728).
rationale: Clients can only discover the trusted authorization server for a business-wallet tool endpoint through this metadata.
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
- wallet provider
- MCP server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-CONTROL-PLANE
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP servers MUST implement OAuth 2.0 Protected Resource Metadata (RFC9728).
---
