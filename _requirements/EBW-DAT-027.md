---
req_id: EBW-DAT-027
title: VAT identifier first for BPNL
category: DAT
statement: Where the country of the legal address has a VAT identifier type and the organisation is subject to value-added tax, the Golden Record of the legal entity shall contain a VAT identifier.
rationale: First step of the ordered preference of legal identifiers (VAT, TIN, national register, international register).
sources:
- id: SRC-CX-0010
  location: Section 2.1 (identifier rule 1)
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
quote: a VAT identifier MUST be contained in the Golden Record
---
