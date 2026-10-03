---
req_id: EBW-TRU-158
title: Wallet provider verifies wallet instance integrity and signs the instance attestation
category: TRU
statement: The wallet provider shall verify the integrity of the wallet instance and sign or seal the wallet instance attestation.
rationale: Ties the instance attestation to a checked wallet instance, which issuers rely on before issuing person identification data.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib to Implementing Regulation (EU) 2024/2979), point 2(b), TR-WIA-2
provenance: L
legal_status: in force
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A wallet provider shall verify the integrity of the wallet instance and sign or seal the wallet instance attestation.
---
