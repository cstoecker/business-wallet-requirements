---
req_id: EBW-TRU-122
title: PID provider checks wallet status at least every 24 hours
category: TRU
statement: A provider of person identification data whose data has a technical validity period of more than 24 hours shall, during that period, check the revocation status of the wallet instance attestation and of the key attestation received at issuance at least once every 24 hours, and shall revoke the data where either is revoked.
rationale: It passes the revocation of a wallet unit on to the credentials bound to it within a day.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(d), LC_GEN-4
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall check the revocation status of both the wallet instance attestation and the key attestation received during issuance at least once every 24 hours
---
