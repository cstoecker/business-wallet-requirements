---
req_id: EBW-TRU-108
title: Wallet unit authenticates issuers before issuance
category: TRU
statement: When a wallet unit requests issuance of electronic attestations of attributes, the provider of European Business Wallets shall ensure the unit is able to authenticate the relying party.
rationale: Prevents attestations being obtained from or sent to unauthenticated parties.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 14(1)
provenance: L
legal_status: proposal
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
- CON-TRUST-PLANE
- CON-AUTHENTIC-SOURCES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: able to authenticate relying parties
---
