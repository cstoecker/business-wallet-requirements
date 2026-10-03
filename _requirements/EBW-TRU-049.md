---
req_id: EBW-TRU-049
title: Domain-bound client identity via metadata documents
category: TRU
statement: Where the wallet or an agent acts as an MCP client towards authorization servers it does not control, the agent shall support OAuth Client ID Metadata Documents so that its client identity is bound to a domain it controls.
rationale: The source only states SHOULD; for a business wallet a domain-bound client identity is needed so a relying party can attribute requests to an organisation.
sources:
- id: SRC-MCP-AUTH
  location: Authorization, Overview
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- authorization server
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Authorization servers and MCP clients SHOULD support OAuth Client ID Metadata Documents
---
