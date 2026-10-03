---
req_id: EBW-NFR-098
title: Wallet status lists cover at least 10 000 attestations where possible
category: NFR
statement: The wallet provider shall size its wallet instance attestation status lists, taking account of scale and architecture, so that they are large enough to prevent correlation and, where possible, relate to at least 10 000 attestations.
rationale: List size is the privacy of status checks, and a small provider or a business wallet with few units gives a small list.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(e), R_WIA-5
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: At a minimum, a status list shall, where possible, relate to at least 10 000 attestations.
---
