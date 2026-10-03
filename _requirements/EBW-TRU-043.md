---
req_id: EBW-TRU-043
title: Authenticate relying party in every presentation
category: TRU
statement: The wallet unit and the relying party instance shall perform relying party authentication using an access certificate in all presentation transactions, proximity or remote.
rationale: Relying party authentication must not depend on channel type.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 6, RPA_03
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
- relying party instance
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall perform Relying Party authentication in all PID or attestation presentation transactions to Relying Parties, whether proximity or remote, using an access certificate.
---
