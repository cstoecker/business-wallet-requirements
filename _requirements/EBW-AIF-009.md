---
req_id: EBW-AIF-009
title: Agent DID authentication separate from authorisation
category: AIF
statement: Where the wallet or an agent authenticates with the W3C AI Agent Protocol DID profile, the server shall evaluate its authorisation policy independently after authentication and return an authorisation failure when the DID lacks permission.
rationale: Proof of key control must not be mistaken for a mandate.
sources:
- id: SRC-W3C-AIAP-ID
  location: Authentication and Authorization Boundary
provenance: S
legal_status: ecosystem
plane: governance
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the server MUST independently evaluate its authorization policy.
---
