---
req_id: EBW-OPS-047
title: Keep roles and accounts aligned between the identity service and the asset interface
category: OPS
statement: Where a detached service authenticates users or applications and assigns their roles, the party responsible for the asset interface shall ensure that the account information, including roles, is aligned between that service and the interface.
rationale: Derived; a revoked or suspended role in the identity service must not stay valid in the asset interface, which is a precondition for timely termination of machine and employee authority.
sources:
- id: SRC-IDTA-AAS-P4
  location: Part 4 (IDTA-01004 v3.1), AAS Security requirements, FR1, Account management
provenance: D
legal_status: ecosystem
plane: governance
perspectives:
- M2M
- B2B
actors:
- asset interface operator
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the AAS responsible SHALL ensure that the account information is aligned between the AAS and the detached service
---
