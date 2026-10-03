---
req_id: EBW-FUN-053
title: Wallet tells the user about revocations it finds
category: FUN
statement: When the wallet instance finds that it, a secure device or keystore it uses, a PID or an attestation has been revoked, it shall notify the user.
rationale: The user learns of a revocation even if no issuer message arrives.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 7, VCR_19
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
- CON-REVOCATION
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: In case of any revocation, the Wallet Instance SHALL notify the User accordingly.
---
