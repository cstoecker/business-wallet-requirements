---
req_id: EBW-FUN-052
title: Trust mark no longer shown after unit revocation
category: FUN
statement: Where the wallet provider has revoked a wallet unit attestation, it shall ensure that the trust mark is no longer displayed by the corresponding wallet unit.
rationale: The mark signals a certified, valid wallet, so a revoked unit must not show it.
sources:
- id: SRC-CIR-2026-1731
  location: Article 2(9), inserting Article 14a(8) of Implementing Regulation (EU) 2024/2979
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
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: they shall ensure that the EU Digital Identity Wallet Trust Mark is no longer displayed by the corresponding wallet unit
---
