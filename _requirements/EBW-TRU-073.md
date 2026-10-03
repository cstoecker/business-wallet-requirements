---
req_id: EBW-TRU-073
title: CA certificate rollover without disruption to relying parties
category: TRU
statement: Before its CA certificate used for signing subject keys expires, the certification service provider that continues the service shall generate a new such certificate and apply all necessary actions to avoid disruption to relying parties.
rationale: Rollover of signing certificates and trust anchors must not break validation.
sources:
- id: SRC-ETSI-EN-319411-1
  location: Clause 6.5.1, GEN-6.5.1-08 and GEN-6.5.1-09
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
- M2M
actors:
- trust service provider
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall apply all necessary actions to avoid disruption to the operations of any entity that may rely on the CA certificate
---
