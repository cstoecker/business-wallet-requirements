---
req_id: EBW-DAT-033
title: Inactive business partner stays accessible
category: DAT
statement: The business partner data management shall keep a business partner and its BPN accessible after the business partner becomes inactive.
rationale: Historical transactions can still be resolved to a legal entity that no longer exists.
sources:
- id: SRC-CX-0010
  location: Section 2.3
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- M2M
actors:
- Business Partner Data Management
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-LEGAL-PERSON-ID
- CON-CROSS-SECTOR
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Even if a business partner becomes inactive, the business partner and its BPN MUST be further accessible
---
