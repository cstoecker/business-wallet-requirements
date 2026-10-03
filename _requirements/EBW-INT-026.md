---
req_id: EBW-INT-026
title: Agent mandates as structured authorization details
category: INT
statement: Where the wallet or an agent obtains OAuth tokens for transaction-specific authority, the request shall express the authority as authorization_details (RFC 9396) rather than only coarse scopes.
rationale: A mandate with amounts, counterparties and resource types needs structured fine-grained data that scopes cannot carry.
sources:
- id: SRC-RFC-9396
  location: Section 2 Request Parameter "authorization_details"
provenance: D
legal_status: standard
plane: control
perspectives:
- B2B
- B2G
actors:
- agent
- authorization server
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: allows clients to specify their fine-grained authorization requirements using the expressiveness of JSON
---
