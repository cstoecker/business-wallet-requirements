---
req_id: EBW-TRU-117
title: Instance attestation expires within 24 hours of the integrity check
category: TRU
statement: The wallet provider shall set the expiry of each wallet instance attestation less than 24 hours after the time at which it verified the integrity of the wallet instance.
rationale: A short technical validity keeps the attestation fresh, while revocation status is maintained separately for longer.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(b), TR-WIA-2.1
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the time they will indicate in the 'exp' header parameter of the issued wallet instance attestation shall be less than 24 hours
---
