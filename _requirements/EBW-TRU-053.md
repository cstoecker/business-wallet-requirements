---
req_id: EBW-TRU-053
title: Verify a card signature before trusting the card
category: TRU
statement: Where the wallet or an agent consumes an A2A Agent Card to select a counterparty, it shall verify at least one card signature before trusting the card contents.
rationale: The specification only says SHOULD; for business transactions trusting unverified skill and endpoint claims is derived as unacceptable.
sources:
- id: SRC-A2A
  location: Section 8.4.3 Signature Verification
provenance: D
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
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Clients SHOULD verify at least one signature before trusting an Agent Card
---
