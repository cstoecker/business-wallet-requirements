---
req_id: EBW-TRU-169
title: Custody model recorded per private key
category: TRU
statement: The wallet provider shall record for each private key of a wallet unit the custody model that holds it (device held by the owner, module operated by the provider, module operated by the owner, or remote service of a qualified trust service provider) and shall make the record available to the owner on request.
rationale: 'Derived (criteria C1, C6, C9 of the DEC-03 page): no source says where keys must be held, so the choice must at least be recorded; Annex point 3(1) requires a secure cryptographic device but not its placement.'
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 3(1)
provenance: D
legal_status: proposal
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- wallet owner
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-TRUST-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall use at least one Wallet secure cryptographic application and Wallets secure cryptographic device to manage critical assets
---
