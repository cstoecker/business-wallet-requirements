---
req_id: EBW-TRU-052
title: Verifier checks Agent Card signature and key status
category: TRU
statement: When the wallet or an agent verifies a signed A2A Agent Card, it shall retrieve the public key via kid and jku or from a trusted key store, verify the signature over the canonicalised card and not use expired or revoked keys.
rationale: It ties card trust to key status, which a business wallet can anchor to its own trust framework.
sources:
- id: SRC-A2A
  location: Section 8.4.3 Signature Verification
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Expired or revoked keys MUST NOT be used for verification
---
