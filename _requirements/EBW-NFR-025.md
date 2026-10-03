---
req_id: EBW-NFR-025
title: Per-client consent in MCP proxy servers
category: NFR
statement: Where the wallet or an agent operates an MCP proxy server in front of a third-party API, the proxy shall keep a per-user registry of approved client IDs and obtain consent for each client before forwarding to the third-party authorization flow.
rationale: It prevents the confused-deputy attack that obtains tokens without the user's explicit approval.
sources:
- id: SRC-MCP-SEC
  location: Confused Deputy Problem, Mitigation
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2B
- M2M
actors:
- wallet provider
- MCP proxy server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MCP proxy servers MUST implement per-client consent and proper security controls
---
