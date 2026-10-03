---
req_id: EBW-NFR-109
title: Presentation responses are encrypted
category: NFR
statement: The wallet shall encrypt the authorisation response that carries a presentation to the wallet-relying party.
rationale: Protects the disclosed attributes from intermediaries and from the browser or platform layer that relays the response. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-ETSI-119472-2
  location: Clause 6.4.1, OIDFVP-HAIP-COMMON-RESP-01
provenance: S
legal_status: standard
plane: data
perspectives:
- B2B
- B2G
- G2B
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
quote: The EUDI Wallet shall encrypt the authorization response.
---
