---
req_id: EBW-TRU-074
title: Overlap interval between expiry and last certificate signed
category: TRU
statement: The certification service provider shall leave a suitable interval between the expiry date of the old CA certificate and the last certificate it signs, so that subjects, subscribers and relying parties can adapt to the key changeover.
rationale: An overlap period lets relying parties update trust anchors before the old key stops issuing.
sources:
- id: SRC-ETSI-EN-319411-1
  location: Clause 6.5.1, GEN-6.5.1-10
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
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: should be performed with a suitable interval between certificate expiry date and the last certificate signed
---
