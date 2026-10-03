---
req_id: EBW-OPS-034
title: Wallet provider regularly verifies unit security
category: OPS
statement: During the lifetime of a wallet unit, the wallet provider shall regularly verify that the security of the unit is not breached or compromised, and shall revoke the unit where a breach affects its trustworthiness or reliability.
rationale: Compromised units are only revoked if someone looks for compromise.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 38, WURevocation_09
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL regularly verify that the security of the Wallet Unit is not breached or compromised
---
