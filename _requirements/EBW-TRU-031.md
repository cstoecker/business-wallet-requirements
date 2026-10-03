---
req_id: EBW-TRU-031
title: Privacy-preserving publication of wallet unit validity status
category: TRU
statement: When a wallet provider has revoked a wallet unit attestation, the wallet provider shall make the validity status publicly available in a privacy preserving manner and describe its location in the wallet unit attestation.
rationale: Relying parties and issuers need status without tracking users.
sources:
- id: SRC-CIR-2024-2979
  location: Article 7(4)
provenance: L
legal_status: in force
plane: assurance
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
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: make publicly available the validity status of the wallet unit attestation in a privacy preserving manner
full_quote: Where wallet providers have revoked wallet unit attestations, they shall make publicly available the validity status of the wallet unit attestation in a privacy preserving manner and describe the location of that information in the wallet unit attestation.
fidelity_checked: '2026-10-03'
---
