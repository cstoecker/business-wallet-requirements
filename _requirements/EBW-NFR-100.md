---
req_id: EBW-NFR-100
title: Instance attestation shown only to issuers
category: NFR
statement: A wallet unit shall present a wallet instance attestation only to a provider of person identification data or an attestation provider as part of issuance, and not to a relying party or any other entity.
rationale: Showing the attestation to relying parties would expose a tracking handle and is not how EUDI Wallets are verified; the business wallet texts and the WE BUILD rulebook differ.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 9, WUA_24
provenance: S
legal_status: standard
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
- CON-WUA
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL present a WIA only to a PID Provider or Attestation Provider
---
