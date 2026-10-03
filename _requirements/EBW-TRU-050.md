---
req_id: EBW-TRU-050
title: Server operator identity is not provided by MCP
category: TRU
statement: Where the wallet or an agent exposes an MCP server to counterparties, the wallet provider shall make the identity of the operating legal person verifiable through wallet or trust-list mechanisms, because MCP authorization defines no server-operator identity beyond OAuth endpoints and TLS.
rationale: MCP leaves the authorization server implementation and the operator identity out of scope, so the legal-person binding must come from the wallet trust layer.
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Roles
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- wallet provider
- relying party
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-LEGAL-PERSON-ID
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The implementation details of the authorization server are beyond the scope of this specification.
---
