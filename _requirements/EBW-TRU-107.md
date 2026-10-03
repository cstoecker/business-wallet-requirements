---
req_id: EBW-TRU-107
title: Authenticate relying party for restricted-audience attestations
category: TRU
statement: The European Business Wallet unit shall require authentication of the relying party where an attestation is intended for a restricted audience.
rationale: Open attestations may be shown to anyone; restricted ones need an authenticated verifier.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 13(1)
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
- CON-TRUST-PLANE
- CON-MULTI-TRUST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Authentication of the relying party shall be required where attestations are intended for a restricted audience
---
