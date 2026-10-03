---
req_id: EBW-TRU-057
title: No DID method fallback on failed validation
category: TRU
statement: Where the wallet or an agent authenticates with DID-based agent identity, the verifier shall fail authentication on resolution or validation failure and shall not fall back to another DID method or use an unvalidated DID Document.
rationale: Fallback would let an attacker choose the weakest identity method.
sources:
- id: SRC-W3C-AIAP-ID
  location: DID Resolution and Verification Method Selection
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MUST NOT fall back to another DID method
---
