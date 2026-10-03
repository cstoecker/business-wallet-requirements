---
req_id: EBW-TRU-030
title: Only the wallet provider revokes wallet unit attestations
category: TRU
statement: Only the wallet provider that provided a wallet unit shall be capable of revoking that wallet unit attestation, and the provider shall publish a policy on the conditions and timeframe of revocation.
rationale: Gives a single accountable revoker with predictable rules; a wallet unit attestation now comprises wallet instance and key attestations (Annex Ib, point 1).
sources:
- id: SRC-CIR-2024-2979
  location: Article 7(1)-(2) (not amended by Implementing Regulation (EU) 2026/1731; consolidated text 02024R2979-20260811)
provenance: L
legal_status: in force
plane: assurance
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
quote: Wallet providers shall be the only entities capable of revoking wallet unit attestations for wallet units that they have provided.
fidelity_checked: '2026-10-03'
revision_note: 'Checked against the consolidated text as amended by Implementing Regulation (EU) 2026/1731: Article 7 unchanged, wording still current.'
---
