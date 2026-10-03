---
req_id: EBW-OPS-030
title: Maintain instance revocation status until the stated time
category: OPS
statement: Where a wallet provider signs or seals a wallet instance attestation, it shall maintain the revocation status of the relevant wallet instance until the status expiry indicated in that attestation has passed.
rationale: Issuers can only chain the validity of a credential to a wallet if the provider commits to serving status for a stated time.
sources:
- id: SRC-CIR-2026-1731
  location: Annex III (new Annex Ib), point 2(d), LC_WIA_3
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: it shall maintain the revocation status of the relevant wallet instance until the 'wallet_instance_status.exp' indicated in that wallet instance attestation has passed
---
