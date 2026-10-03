---
req_id: EBW-NFR-099
title: Fresh unlinkable index for each instance attestation
category: NFR
statement: Where a wallet provider does not reuse one status index per credential issuer, it shall assign a fresh, unlinkable index value to each wallet instance attestation it issues.
rationale: A reused index would let issuers link their interactions with the same unit.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(e), R_WIA-3
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the wallet provider shall assign a fresh, unlinkable index value to each wallet instance attestation it issues
---
