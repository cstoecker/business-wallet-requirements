---
req_id: EBW-TRU-077
title: Access certificate status available beyond certificate validity
category: TRU
statement: The provider of wallet-relying party access certificates shall make validity or revocation status available on a per-certificate basis at any time and beyond the validity period of the certificate, automated, reliable and free of charge.
rationale: Lets verifiers check old signatures and certificates after expiry.
sources:
- id: SRC-CIR-2025-848
  location: Annex IV, point 5
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- access certificate provider
- wallet
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: at least on a per certificate basis at any time and at least beyond the validity period of the certificate
---
