---
req_id: EBW-CER-012
title: Activate a unit only with a certified secure device
category: CER
statement: The wallet provider shall activate a new wallet unit only after verifying that the unit includes a wallet secure cryptographic application and device certified as compliant with the requirements for assurance level high.
rationale: It ties activation of a unit to the certification evidence of the key custody component.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 40, WIAM_08
provenance: S
legal_status: standard
plane: assurance
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
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL only activate a new Wallet Unit if it has verified that the Wallet Unit includes a WSCA/WSCD that is certified
---
