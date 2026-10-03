---
req_id: EBW-INT-001
title: Issuance and presentation protocols in the WE BUILD pilot
category: INT
statement: Issuers and wallets in the pilot shall use OpenID4VCI 1.0 for issuance, and relying parties and wallets shall use OpenID4VP 1.0 for presentation.
rationale: Gives pilot participants one protocol profile so that wallets, issuers and verifiers can be tested together.
sources:
- id: SRC-WEBUILD-ARCH
  location: ADR base-protocols
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- B2G
actors:
- Issuer
- Wallet provider
- Relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
---
