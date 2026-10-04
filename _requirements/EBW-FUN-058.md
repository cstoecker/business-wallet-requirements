---
req_id: EBW-FUN-058
title: Owner withdraws a user authorisation to use keys
category: FUN
statement: The wallet provider shall enable the wallet owner to withdraw the authorisation of a named user to use any private key of the wallet unit and to deactivate a key held on a device that the user holds.
rationale: 'Derived (criteria C1, C14 of the DEC-03 page): the proposal lets owners manage and revoke user authorisations, and the sources are silent on how that reaches a key on a device held by a departed user.'
sources:
- id: SRC-EBW-PROPOSAL
  location: Article 5(1), point (j)
provenance: D
legal_status: proposal
plane: control
perspectives:
- B2B
- B2G
- G2B
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
quote: for the European Business Wallet owner to manage and revoke such authorisations
---
