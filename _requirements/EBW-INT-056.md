---
req_id: EBW-INT-056
title: LEI as legal person identity type in certificates
category: INT
statement: When the legal person semantics identifier is used, an LEI in the organizationIdentifier attribute shall be prefixed LEI with the country code XG followed by the LEI.
rationale: Documents a non-KERI, standards-based carrier for the LEI in qualified seal certificates.
sources:
- id: SRC-ETSI-EN-319412-1
  location: Clause 5.1.4, LEG-5.1.4-03 point 4
provenance: S
legal_status: standard
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- trust service provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-LEGAL-PERSON-ID
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: '"LEI" for a global Legal Entity Identifier as specified in ISO 17442'
---
