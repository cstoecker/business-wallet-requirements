---
req_id: EBW-NFR-121
title: Audit trail records changes to accounts and access rules
category: NFR
statement: The asset interface shall keep, as a minimum, audit events for unauthorised access attempts, changes to identity configuration, changes to accounts of applications and users, and changes to access rules.
rationale: Derived; shows who granted, changed or withdrew machine and user authority and when, which is what an owner needs to answer for acts of its machines.
sources:
- id: SRC-IDTA-AAS-P4
  location: Part 4 (IDTA-01004 v3.1), AAS Security requirements, FR2, Auditable Events, Table 1 (S1 to S4)
provenance: D
legal_status: ecosystem
plane: assurance
perspectives:
- M2M
- B2B
actors:
- asset interface operator
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-CONTROL-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: As a minimum the events listed in Table Table 1 SHALL be kept in an AAS interface audit trail.
---
