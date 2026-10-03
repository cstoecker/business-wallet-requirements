---
req_id: EBW-INT-024
title: Agent Card canonicalised before signing
category: INT
statement: Where the wallet or an agent signs an A2A Agent Card, it shall canonicalise the card content with the JSON Canonicalization Scheme (RFC 8785) before signing and exclude the signatures field.
rationale: Canonicalisation lets any verifier reproduce the signed bytes regardless of JSON serialiser.
sources:
- id: SRC-A2A
  location: Section 8.4.1 Canonicalization Requirements
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the Agent Card content MUST be canonicalized using the JSON Canonicalization Scheme (JCS) as defined in RFC 8785
---
