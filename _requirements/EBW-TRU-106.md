---
req_id: EBW-TRU-106
title: Public validity status of revoked unit attestations
category: TRU
statement: When the provider of European Business Wallets has revoked a wallet unit attestation, it shall make the validity status of that attestation publicly available and describe the location of that information in the attestation.
rationale: Verifiers need a discoverable status source. Unlike the EUDI counterpart (EBW-TRU-031) no privacy-preserving manner is stated in the proposal annex.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 6(3)
provenance: L
legal_status: proposal
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: make publicly available the validity status of the European Business Wallet unit attestation
---
