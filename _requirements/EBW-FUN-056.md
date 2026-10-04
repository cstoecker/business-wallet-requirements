---
req_id: EBW-FUN-056
title: Owner can check the validity status of its own wallet unit
category: FUN
statement: The provider of European Business Wallets shall give the owner a means to check the current validity status of the owner's own wallet unit attestation.
rationale: Derived; the sources give provider-side publication of the status (Annex point 6(3)) and the ARF notes that a wallet instance can check its own revocation status through its attestations (WURevocation_13, a should), but no owner-side duty.
sources:
- id: SRC-COUNCIL-ST-9684-26
  location: Annex point 6(3); Article 6(2), point (e); cf. ARF Annex 2.02 Topic 38 WURevocation_13
provenance: D
legal_status: proposal
plane: control
perspectives:
- B2B
- B2G
actors:
- wallet provider
- wallet owner
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: make publicly available the validity status of the European Business Wallet unit attestation
---
