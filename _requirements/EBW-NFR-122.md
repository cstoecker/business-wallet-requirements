---
req_id: EBW-NFR-122
title: Each auditable event identifies the acting application or machine
category: NFR
statement: Each auditable event of an asset interface shall contain information to determine which application or machine took the action, and the party responsible for the interface shall ensure that this information is sufficient to resolve a dispute about who acted.
rationale: Derived; the specification lets the identity of the actual user be left to the application, so a wallet has to link the machine identifier to the owner for the act to count as the owner's (see EBW-NFR-033 for agents).
sources:
- id: SRC-IDTA-AAS-P4
  location: Part 4 (IDTA-01004 v3.1), AAS Security requirements, FR2, Non-repudiation
provenance: D
legal_status: ecosystem
plane: assurance
perspectives:
- M2M
- B2B
actors:
- asset interface operator
- machine
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-CONTROL-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Each auditable event shall contain information to determine which AAS user application took a particular action on the AAS.
---
