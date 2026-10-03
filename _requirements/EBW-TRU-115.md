---
req_id: EBW-TRU-115
title: Wallet checks that a remote device is part of a qualified service
category: TRU
statement: In remote signature creation scenarios, a wallet unit shall verify that the qualified electronic signature or seal creation device is part of a qualified service carried out by a qualified trust service provider.
rationale: It stops a wallet from sending signing requests to a device that gives no qualified effect.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 16, QES_15
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
- CON-QUALIFIED-SERVICES
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL verify that the qualified electronic signature or seal creation device is part of a qualified service
---
