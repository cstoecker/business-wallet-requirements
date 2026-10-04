---
req_id: EBW-NFR-118
title: Migration object contains no private keys
category: NFR
statement: The migration object of a wallet unit shall not contain private keys of PIDs or device-bound attestations.
rationale: Keys do not move between wallet solutions, so exit means re-creating keys and re-issuing attestations; stated for the EUDI Wallet, no EBW text says whether keys can move.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 34, Mig_03
provenance: S
legal_status: standard
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL NOT contain any private keys of the PID or device-bound attestation
---
