---
req_id: EBW-TRU-165
title: Authenticate the requester before accepting a unit revocation request
category: TRU
statement: The provider of European Business Wallets shall authenticate the person who requests revocation of a wallet unit before accepting the request.
rationale: Derived by mapping the ARF rule for EUDI wallets to the European Business Wallet, whose Annex point 1 already requires an authentication mechanism for users who request revocation; the ARF names a natural-person user, the EBW requester is an owner or authorised user.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 38, WURevocation_10
provenance: D
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
actors:
- wallet provider
- wallet owner
- wallet user
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The Wallet Provider SHALL authenticate the User before accepting a request to revoke the Wallet Unit.
---
