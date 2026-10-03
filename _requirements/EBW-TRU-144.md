---
req_id: EBW-TRU-144
title: Pre-authorised issuance only with physical presence
category: TRU
statement: A provider of person identification data that uses the pre-authorised code issuance flow shall perform user authorisation with the physical presence of the user.
rationale: The pre-authorised flow does not protect against hijacking in remote scenarios, so remote issuance at assurance level high is excluded from it. This is an EUDI Wallet profile; its use in the business wallet is part of DEC-07.
sources:
- id: SRC-ETSI-119472-3
  location: Clause 4.1, GEN-REQ-4.1-05
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2C
- B2G
actors:
- provider of person identification data
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-LOA
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: PID Providers implementing the Pre-Authorised Code Flow shall perform user authorisation with the physical presence.
---
