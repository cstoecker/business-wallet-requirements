---
req_id: EBW-AIF-013
title: Agent identified separately from principal
category: AIF
statement: An AI agent acting for an owner shall be identified by an identifier of its own that is distinct from the identifier of the principal and expressed as the actor of the delegation.
rationale: Verifiers and auditors must tell who acts from on whose behalf the action is taken.
sources:
- id: SRC-RFC-8693
  location: Section 4.1
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- A2A
actors:
- AI agent
- wallet owner
- authorisation server
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: express that delegation has occurred and identify the acting party to whom authority has been delegated
---
