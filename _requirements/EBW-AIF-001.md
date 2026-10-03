---
req_id: EBW-AIF-001
title: Human can deny wallet tool invocations
category: AIF
statement: Where the wallet or an agent exposes wallet functions as MCP tools, the application shall let the user deny each tool invocation that has legal or financial effect, and shall indicate clearly when a tool is invoked.
rationale: The specification only says SHOULD; for signing, sealing or submitting on behalf of a legal person a human decision point is derived as an obligation.
sources:
- id: SRC-MCP-TOOLS
  location: Tools, User Interaction Model
provenance: D
legal_status: ecosystem
plane: governance
perspectives:
- B2B
- B2G
- B2C
actors:
- wallet user
- agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AI-SAFETY
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: there SHOULD always be a human in the loop with the ability to deny tool invocations
---
