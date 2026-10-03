---
req_id: EBW-NFR-021
title: Wallet attestations use ECCG agreed cryptographic mechanisms
category: NFR
statement: When issuing, presenting or verifying a wallet instance attestation or key attestation, the participants shall use only cryptographic algorithms included in the ECCG Agreed Cryptographic Mechanisms v2.0.
rationale: Fixes an algorithm baseline for interoperability and review.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 9, WUA_04
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- issuer
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-PQC
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL only use cryptographic algorithms included in the ECCG Agreed Cryptographic Mechanisms v2.0.
---
