---
req_id: EBW-TRU-048
title: MCP client obtains a registered client identifier
category: TRU
statement: Where the wallet or an agent acts as an MCP client with authorization, the MCP client shall obtain a client ID through Client ID Metadata Documents, pre-registration or Dynamic Client Registration before starting the authorization flow.
rationale: The client ID is the only agent identifier the MCP authorization layer defines.
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Client Registration
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- MCP client
- authorization server
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP clients MUST obtain a client ID through one of three registration mechanisms
---
