---
req_id: EBW-DAT-038
title: Legal entity type set after register match
category: DAT
statement: The service provider shall set the type of a record to legal entity (BPNL) if the combination of identifier, legal name and address is found in the commercial register or an equivalent official register.
rationale: Authoritative register lookup decides the legal-entity status.
sources:
- id: SRC-CX-0076
  location: Section 2.1.6
provenance: S
legal_status: ecosystem
plane: assurance
perspectives:
- B2B
- M2M
actors:
- service provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-LEGAL-PERSON-ID
- CON-CROSS-SECTOR
- CON-AUTHENTIC-SOURCES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: found in the commercial register or equivalent official register, the type of this record MUST be set to BPNL
---
