---
req_id: EBW-TRU-134
title: Support revocation for owner identification data valid over 24 hours
category: TRU
statement: The provider of owner identification data shall support revocation of owner identification data that has a validity longer than 24 hours.
rationale: The rulebook of the pilot treats owner identification data as long-lived but revocable.
sources:
- id: SRC-WEBUILD-RB
  location: rb-ebwoid/README.md, section 6
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- M2M
actors:
- owner identification data provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Validity longer than 24 hours is permitted; therefore, revocation MUST be supported.
---
