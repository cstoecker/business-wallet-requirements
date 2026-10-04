---
req_id: EBW-INT-089
title: Authorisation states the total number of signatures
category: INT
statement: A signature application that authorises use of a remote signing credential shall indicate the total number of signatures to authorise.
rationale: It bounds each authorisation of a remotely held key, which matters for automated sealing of many documents; applies to the CSC API, not directly to the EBW.
sources:
- id: SRC-CSC-API-V2
  location: Clause 11.6 credentials/authorize
provenance: S
legal_status: standard
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- signature application
- remote signing service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The numSignatures parameter SHALL indicate the total number of signatures to authorize.
---
