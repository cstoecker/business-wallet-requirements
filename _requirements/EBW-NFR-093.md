---
req_id: EBW-NFR-093
title: Only the legitimate instance reaches a remote security module
category: NFR
statement: When a remote hardware security module holds critical assets of a wallet unit, the wallet provider shall take measures ensuring that only the legitimate wallet instance can access that module and use those assets.
rationale: It is the access control that makes a provider-hosted key store acceptable for a single unit.
sources:
- id: SRC-ARF-MAIN
  location: Section 4.5.2 Remote WSCD
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: certification
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the Wallet Provider takes appropriate measures to ensure that only the legitimate Wallet Instance can access the remote HSM
---
