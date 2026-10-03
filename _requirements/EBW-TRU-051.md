---
req_id: EBW-TRU-051
title: Wallet-published Agent Cards are signed
category: TRU
statement: Where the wallet or an agent publishes an A2A Agent Card, the publisher shall sign it with a JSON Web Signature so that clients can verify authenticity and integrity.
rationale: A2A makes signing optional; an unsigned card gives a relying party no proof that it comes from the claimed organisation.
sources:
- id: SRC-A2A
  location: Section 8.4 Agent Card Signing
provenance: D
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
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Agent Cards MAY be digitally signed using JSON Web Signature (JWS) as defined in RFC 7515
---
