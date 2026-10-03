---
req_id: EBW-INT-082
title: Relayed delivery messages are signed and encrypted
category: INT
statement: The sending provider shall sign and encrypt every AS4 message that relays an electronic registered delivery message to another provider.
rationale: Protects integrity and confidentiality on the hop between providers, which the end-user signature does not cover.
sources:
- id: SRC-ETSI-EN-319522-4-1
  location: Clause 5.3 (Signing and encryption of the AS4 message)
provenance: S
legal_status: standard
plane: data
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
- CON-QUALIFIED-SERVICES
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: All AS4 messages exchanged between the ERDS shall be signed and encrypted by the sending ERDS.
---
