---
req_id: EBW-DAT-040
title: Format check of other identifiers such as LEI
category: DAT
statement: The service provider shall check that the format of an other identifier, such as DUNS, LEI, EIN, UBI or GLN, is valid.
rationale: LEI and similar identifiers are checked for format only, not against their issuer.
sources:
- id: SRC-CX-0076
  location: Section 2.1.8
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: It MUST be checked that the format of Other Identifier (such as, but not limited to DUNS, LEI, EIN, UBI, GLN) is valid.
---
