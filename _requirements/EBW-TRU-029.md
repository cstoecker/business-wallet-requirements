---
req_id: EBW-TRU-029
title: Wallet unit attestation signed under a listed certificate
category: TRU
statement: The wallet provider shall sign or seal at least one wallet unit attestation for each wallet unit using a certificate listed in the trusted list notified under Implementing Regulation (EU) 2024/2980.
rationale: Lets issuers and relying parties authenticate the wallet unit against a trust anchor.
sources:
- id: SRC-CIR-2024-2979
  location: Article 3(2)
provenance: L
legal_status: in force
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
- CON-WUA
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Wallet providers shall, for each wallet unit, sign or seal, at least one wallet unit attestation
---
