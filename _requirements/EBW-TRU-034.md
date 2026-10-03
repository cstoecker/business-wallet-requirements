---
req_id: EBW-TRU-034
title: Request issuance only from certified issuers
category: TRU
statement: The wallet unit shall request issuance of person identification data or attestations only from parties with an authentic and valid wallet-relying party access certificate attesting them as a provider of person identification data or of the relevant type of attestation.
rationale: Stops wallets receiving credentials from unregistered issuers.
sources:
- id: SRC-CIR-2024-2982
  location: Article 4(2)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
- issuer
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: request issuance of person identification data and electronic attestations of attributes only from parties having an authentic and valid wallet-relying party access certificate
---
