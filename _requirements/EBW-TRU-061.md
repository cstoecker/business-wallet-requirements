---
req_id: EBW-TRU-061
title: Access tokens of agents sender-constrained
category: TRU
statement: An authorisation server shall issue access tokens for AI agents as sender-constrained tokens bound to a key of the agent and shall not issue them as bearer tokens.
rationale: A stolen bearer token would let anyone act within the mandate.
sources:
- id: SRC-RFC-9449
  location: Abstract; Section 1; cf. RFC 9635 Section 2.1.1 (bearer flag)
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- A2A
- M2M
actors:
- authorisation server
- AI agent
- resource server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: mechanism for sender-constraining OAuth 2.0 tokens via a proof-of-possession mechanism on the application level
---
