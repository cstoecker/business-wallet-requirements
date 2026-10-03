---
req_id: EBW-NFR-110
title: Wallet attestation does not identify one wallet instance
category: NFR
statement: A wallet attestation presented to an issuer shall not be reused across issuers and shall not carry an identifier specific to a single wallet instance.
rationale: A per-instance identifier in the attestation would let issuers collude to link the same wallet across services. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-HAIP-1.0
  location: Section 4.4.1 (Wallet Attestation)
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- B2C
actors:
- wallet provider
- credential issuer
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: They MUST NOT introduce a unique identifier specific to a single Wallet instance.
---
