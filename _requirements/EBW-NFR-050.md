---
req_id: EBW-NFR-050
title: ERDS signing key in a certified secure cryptographic device
category: NFR
statement: The registered delivery service provider shall hold and use the signing private key within a secure cryptographic device certified to Common Criteria EAL 4 or higher, or, until 31 December 2030, FIPS 140-3 level 3.
rationale: Fixes key protection and shows a dated sunset for one certification route.
sources:
- id: SRC-CIR-2025-1944
  location: Annex, REQ-ERDSP-7.5-03
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- registered delivery service provider
verification_method: certification
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The ERDS signing private key shall be held and used within a secure cryptographic device which is a trustworthy system certified
---
