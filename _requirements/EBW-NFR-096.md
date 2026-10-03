---
req_id: EBW-NFR-096
title: Signing key generated in a qualified creation device
category: NFR
statement: A qualified provider managing a remote qualified signature or seal creation device shall generate the signing key of the signer in a qualified signature creation device.
rationale: It sets where the keys of a qualified remote service come into existence.
sources:
- id: SRC-ETSI-TS-119431-1
  location: Annex A, GEN-A.4-01
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified trust service provider
verification_method: certification
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Signer's signing key shall be generated in a QSCD.
---
