---
req_id: EBW-NFR-111
title: Mediating API sees attestation types, not attributes
category: NFR
statement: By default the wallet shall disclose to a mediating operating system or browser interface only the presence of the types of stored attestations, and shall not disclose their attributes or values.
rationale: Limits what the platform layer learns about a user or an organisation when a request is routed through it. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-ETSI-119472-2
  location: Clause 6.5.2, OIDFVP-HAIP-ADD-API-01
provenance: S
legal_status: standard
plane: data
perspectives:
- B2B
- B2G
- B2C
actors:
- wallet unit
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The EUDI Wallet shall by default disclose the presence of all stored EAAs' type to the mediating API
---
