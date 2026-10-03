---
req_id: EBW-NFR-097
title: Session limit for identity-based remote signing
category: NFR
statement: Where the authentication is linked directly to the identity, a qualified provider managing a remote qualified creation device shall end the signature session at most 30 minutes after the end of the identity verification process.
rationale: It bounds how long a verified identity can be used to activate a hosted key.
sources:
- id: SRC-ETSI-TS-119431-1
  location: Annex A, SIG-A.5-09
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified trust service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the signature session shall end at most 30 minutes after the end of the identity verification process
---
