---
req_id: EBW-TRU-139
title: Authenticate a pointed-to list before using it
category: TRU
statement: A relying party shall authenticate a trusted list or list of trusted entities that another list points to, using one of the digital identities given in the pointer, before it uses the pointed-to list.
rationale: Pointers are the discovery mechanism between lists; trusting a list without authenticating it with the key in the pointer would make the pointer an attack path.
sources:
- id: SRC-ETSI-119602
  location: Clause 6.3.13 (Pointers to other LoTEs), Semantics
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- relying party
- scheme operator
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST-DISCOVERY
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: One of such digital identities shall allow successful authentication of the pointed-to list before its use.
---
