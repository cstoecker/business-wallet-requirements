---
req_id: EBW-FUN-037
title: Access decisions based on the current actor only
category: FUN
statement: When applying access control policy to a delegated token, the consumer shall consider only the top-level claims and the party identified as the current actor.
rationale: Treating prior actors as authorised would let any earlier delegate's rights leak into later steps.
sources:
- id: SRC-RFC-8693
  location: Section 4.1
provenance: S
legal_status: standard
plane: control
perspectives:
- B2B
- A2A
- M2M
actors:
- resource server
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the consumer of a token MUST only consider the token's top-level claims and the party identified as the current actor
---
