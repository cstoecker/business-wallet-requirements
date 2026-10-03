---
req_id: EBW-TRU-140
title: Trust evaluation of a delivery service from a trusted list
category: TRU
statement: A party that evaluates trust in an electronic registered delivery service from a trusted list shall validate the service signature, link the signing certificate to the service digital identity in the list, verify that the current status is granted, and verify that the service type fits the applicable trust domain.
rationale: Defines how a provider decides whether to relay a message to another provider, which is the discovery and trust step of the registered delivery channel.
sources:
- id: SRC-ETSI-EN-319522-4-3
  location: Clause 7.2 (EU Trusted List)
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified electronic registered delivery provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: verify that the signing certificate can be linked to the service digital identity in the TL
---
