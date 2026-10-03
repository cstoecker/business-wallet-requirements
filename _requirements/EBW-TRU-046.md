---
req_id: EBW-TRU-046
title: Wallet checks issuer registration before requesting issuance
category: TRU
statement: Before requesting issuance, the wallet unit shall verify that the attestation type it requests is included in the registration certificate of the PID or attestation provider and shall warn the user if not.
rationale: Applies registration checks to issuers as well as verifiers.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 44, RPRC_23
provenance: S
legal_status: standard
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
- CON-B2G-REGISTRY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the type of attestation it wants to request from a PID Provider or Attestation Provider is included in the registration certificate
---
