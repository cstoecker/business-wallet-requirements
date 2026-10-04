---
req_id: EBW-OPS-042
title: Provider states before onboarding what happens to keys on exit
category: OPS
statement: The wallet provider shall state to the owner before onboarding whether the private keys of a wallet unit can be exported or must be re-created when the owner changes provider, and which attestations and certificates must then be re-issued.
rationale: 'Derived (criterion C6 of the DEC-03 page): the texts require export of data but none says whether keys move; the ARF excludes key export, so exit needs new keys and re-issued attestations.'
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 10
provenance: D
legal_status: proposal
plane: data
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
created: '2026-10-03'
last_verified: '2026-10-03'
quote: support the secure export and portability of an owner's European Business Wallet data in at least an open format
---
