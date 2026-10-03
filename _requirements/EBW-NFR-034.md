---
req_id: EBW-NFR-034
title: Sender-constrained agent tokens
category: NFR
statement: Where the wallet or an agent uses DPoP sender-constrained tokens, the resource server shall ensure that the public key from the DPoP proof matches the key bound to the access token.
rationale: It stops a leaked agent token from being replayed by another party.
sources:
- id: SRC-RFC-9449
  location: Section 7 Protected Resource Access
provenance: S
legal_status: standard
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- resource server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Resource servers supporting DPoP MUST ensure that the public key from the DPoP proof matches the one bound to the access token.
---
