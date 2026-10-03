---
req_id: EBW-TRU-102
title: Unit attestation signed under a trusted-list certificate
category: TRU
statement: The provider of European Business Wallets shall sign or seal the European Business Wallet unit attestation with a certificate issued under a certificate listed in the trusted list referred to in Commission Implementing Regulation (EU) 2024/2980.
rationale: Anchors unit attestations in the same trust list as the EUDI wallet ecosystem; counterpart of EBW-TRU-029 for the business wallet.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 2
provenance: L
legal_status: proposal
plane: trust
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
- CON-TRUST-LIST
- CON-WUA
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The certificate used to sign or seal the Business Wallet unit attestation shall be issued under a certificate listed in the trusted list
---
