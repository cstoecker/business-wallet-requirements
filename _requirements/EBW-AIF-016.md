---
req_id: EBW-AIF-016
title: Informed consent on a trusted surface before mandate creation
category: AIF
statement: Before a mandate is created for an AI agent, a trusted surface shall present the mandate content to the principal and obtain the principal's informed consent.
rationale: A mandate that the agent drafts and the principal never saw gives no assurance of what was approved.
sources:
- id: SRC-AP2
  location: Specification, Roles
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2C
- A2A
actors:
- wallet owner
- agent provider
- trusted surface
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: a UI surface that is trusted to get informed user consent for an Intent before creating a user-signed Mandate
---
