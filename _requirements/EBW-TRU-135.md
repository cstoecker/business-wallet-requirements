---
req_id: EBW-TRU-135
title: Indeterminate status of owner identification data is not valid
category: TRU
statement: A relying party that checks the status of owner identification data shall treat an indeterminate status as not valid, in line with its risk policy.
rationale: It sets the default when status cannot be determined.
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
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Treat any indeterminate status as non-valid per risk policy.
---
