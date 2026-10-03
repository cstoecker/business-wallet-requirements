---
req_id: EBW-INT-081
title: Presentation requests use the certificate-hash client identifier
category: INT
statement: A wallet-relying party shall identify itself in a presentation request with the x509_hash client identifier prefix and sign the request.
rationale: Fixes one relying party identification method for EU interoperability, so that any wallet can authenticate any registered relying party. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-ETSI-119472-2
  location: Clause 6.4.1, OIDFVP-HAIP-COMMON-REQ-01
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet-relying party
- wallet unit
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-EBW-EUDIW
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The Authorization Request shall use the Client Identifier Prefix x509_hash.
---
