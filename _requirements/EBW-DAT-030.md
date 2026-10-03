---
req_id: EBW-DAT-030
title: International register identifier as last choice for BPNL
category: DAT
statement: Where none of the VAT, TIN and national business registration rules applies and the organisation has an international business registration identifier, the Golden Record shall contain that identifier.
rationale: Last step of the ordered preference; international identifiers such as LEI or EORI act only as fallback.
sources:
- id: SRC-CX-0010
  location: Section 2.1 (identifier rule 4)
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- M2M
actors:
- BPN issuing organisation
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-LEGAL-PERSON-ID
- CON-CROSS-SECTOR
created: '2026-10-03'
last_verified: '2026-10-03'
quote: an IBR identifier MUST be contained in the Golden Record
---
