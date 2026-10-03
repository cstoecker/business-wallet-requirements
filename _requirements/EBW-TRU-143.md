---
req_id: EBW-TRU-143
title: Signed issuer metadata with the access certificate
category: TRU
statement: A provider of person identification data or electronic attestations of attributes shall publish its issuer metadata as signed metadata, signed with its access certificate.
rationale: Lets the wallet tie the issuer endpoint and the supported credentials to a registered, authenticated provider before it requests issuance. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-ETSI-119472-3
  location: Clause 4.2.1, ISS-MDATA-4.2.1-02
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- B2C
actors:
- credential issuer
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The signing certificate of the signature on the Issuer Metadata shall be the access certificate of the PID/EAA Provider.
---
