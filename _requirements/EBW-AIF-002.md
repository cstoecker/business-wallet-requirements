---
req_id: EBW-AIF-002
title: Tool annotations treated as untrusted
category: AIF
statement: Where the wallet or an agent acts as an MCP client, it shall treat tool annotations as untrusted unless they come from a trusted server.
rationale: A malicious server could otherwise label a destructive wallet action as read-only to skip confirmation.
sources:
- id: SRC-MCP-TOOLS
  location: Tools, Data Types (annotations)
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
- CON-AI-SAFETY
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: clients MUST consider tool annotations to be untrusted unless they come from trusted servers.
---
