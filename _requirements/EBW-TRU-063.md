---
req_id: EBW-TRU-063
title: Derived grants never exceed the source authorisation
category: TRU
statement: When an authorisation server issues a derived token or grant from a presented token, it shall verify that the requested scope is not higher privileged than the scope of the presented token.
rationale: Each delegation step may narrow but never widen the principal's authorisation.
sources:
- id: SRC-IETF-IDENTITY-CHAINING
  location: Section on controlling scope (informative text)
provenance: S
legal_status: standard
plane: control
perspectives:
- B2B
- A2A
- M2M
actors:
- authorisation server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Authorization Servers need to verify that the requested scopes are not higher privileged than the scopes of the presented subject_token.
---
