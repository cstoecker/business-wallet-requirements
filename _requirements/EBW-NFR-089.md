---
req_id: EBW-NFR-089
title: Keys protected throughout their lifetime
category: NFR
statement: The wallet secure cryptographic application and device shall protect each private key they generated during the entire lifetime of the key, preventing its extraction in the clear.
rationale: Key protection must cover generation, use, backup and end of life, not only storage.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 40, WIAM_20
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL protect a private key it generated during the entire lifetime of the key
---
