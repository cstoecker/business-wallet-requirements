---
req_id: EBW-FUN-030
title: Check relying party against embedded disclosure policy
category: FUN
statement: The wallet instance shall verify whether the wallet-relying party complies with the embedded disclosure policy of an attestation and shall inform the wallet user of the result.
rationale: Lets attestation issuers restrict which relying parties may receive their attestations.
sources:
- id: SRC-CIR-2024-2979
  location: Article 10(3)
provenance: L
legal_status: in force
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet instance
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Wallet instances shall verify whether the wallet-relying party complies with the requirements of the embedded disclosure policy and inform the wallet user of the result.
---
