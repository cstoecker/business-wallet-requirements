---
req_id: EBW-NFR-085
title: Only the secure application runs critical-asset operations
category: NFR
statement: The wallet provider shall ensure that the wallet secure cryptographic application is the only component able to execute wallet cryptographic operations and any other operation with critical assets in the context of electronic identification at assurance level high.
rationale: It confines the use of keys to one certified component, which decides what a hosted or device-based architecture must isolate.
sources:
- id: SRC-CIR-2024-2979
  location: Article 5(1)(h)
provenance: L
legal_status: in force
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
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: are the only components able to execute wallet cryptographic operations and any other operation with critical assets
---
