---
req_id: EBW-NFR-113
title: Issuers cannot track use after issuance
category: NFR
statement: The business wallet provider shall ensure that attestation providers and other parties cannot, after issuance, obtain data that allows transactions or user behaviour to be tracked, linked or correlated unless the owner explicitly authorises it.
rationale: Article 5a(16) states this for the EUDI Wallet; the proposal has no matching text, so the project needs an explicit requirement or a decision not to apply it.
sources:
- id: SRC-EIDAS-CONSOL
  location: Article 5a(16)(a)
provenance: D
legal_status: in force
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- attestation provider
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: to obtain data that allows transactions or user behaviour to be tracked, linked or correlated
---
