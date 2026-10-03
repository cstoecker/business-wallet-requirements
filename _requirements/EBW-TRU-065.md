---
req_id: EBW-TRU-065
title: Principal-initiated revocation of agent tokens
category: TRU
statement: The authorisation server shall provide a means for the principal side to revoke an access token so that the server invalidates it for all purposes.
rationale: The owner must be able to withdraw an agent's access without waiting for expiry.
sources:
- id: SRC-RFC-9635
  location: Section 6.2
provenance: S
legal_status: standard
plane: control
perspectives:
- B2B
- A2A
- M2M
actors:
- authorisation server
- wallet owner
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the AS SHOULD invalidate the access token for all purposes
---
