---
req_id: EBW-NFR-119
title: Provider-held keys used only on the authority of the owner
category: NFR
statement: Where a wallet provider holds private keys of an owner in its back-end, the wallet provider shall ensure that those keys are used only on the authorisation of the owner's authorised users and not by the wallet provider itself.
rationale: 'Derived (criteria C1, C7 of the DEC-03 page): Article 26(1)(c) sets sole control for advanced signatures and Article 36(1)(c) control for advanced seals, but no EBW text applies this to a non-qualified provider-hosted key.'
sources:
- id: SRC-EIDAS-CONSOL
  location: Article 26(1)(c)
provenance: D
legal_status: in force
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- wallet owner
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: created using electronic signature creation data that the signatory can, with a high level of confidence, use under his sole control
---
