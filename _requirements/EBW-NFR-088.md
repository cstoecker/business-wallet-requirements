---
req_id: EBW-NFR-088
title: Secure application does not export private keys
category: NFR
statement: The wallet secure cryptographic application shall not enable the export of private keys from the wallet secure cryptographic device.
rationale: Non-exportable keys keep custody with the device, and make the exit path re-creation of keys rather than copying.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 9, WUA_16a
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: certification
status: draft
reviewer: pending
concepts:
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A WSCA SHALL NOT enable export of private keys from a WSCD.
---
