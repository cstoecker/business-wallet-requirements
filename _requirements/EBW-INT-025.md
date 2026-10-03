---
req_id: EBW-INT-025
title: Delegation expressed with the act claim
category: INT
statement: Where the wallet or an agent represents delegation in a JWT, the token shall use the act (actor) claim to identify the acting party to whom authority has been delegated.
rationale: A standard claim lets any verifier see that delegation occurred and who the actor is.
sources:
- id: SRC-RFC-8693
  location: Section 4.1 "act" (Actor) Claim
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- A2A
actors:
- agent
- authorization server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The "act" (actor) claim provides a means within a JWT to express that delegation has occurred
---
