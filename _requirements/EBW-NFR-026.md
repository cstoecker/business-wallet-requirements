---
req_id: EBW-NFR-026
title: Explicit consent before one-click local server setup
category: NFR
statement: Where the wallet or an agent supports one-click configuration of local MCP servers, it shall show the exact command without truncation, identify it as a dangerous operation and require explicit user approval before running it.
rationale: A local server runs with the privileges of the client, which in a wallet context can reach key material.
sources:
- id: SRC-MCP-SEC
  location: Local MCP Server Compromise, Mitigation
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2C
- B2B
actors:
- wallet user
- agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AI-SAFETY
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Show the exact command that will be executed, without truncation
---
