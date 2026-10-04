---
req_id: EBW-TRU-176
title: Authenticate the calling machine or application before granting access
category: TRU
statement: Before granting an application or machine access to protected asset data or restricted services, the party operating the asset interface shall identify and authenticate that application.
rationale: Derived from the IDTA security specification for the asset administration shell, an implementation artefact; only this high-level rule is used. The specification maps the rule from IEC 62443 and allows the application to stand for a non-person user.
sources:
- id: SRC-IDTA-AAS-P4
  location: Part 4 (IDTA-01004 v3.1), AAS Security requirements, FR1, Identification and authentication of AAS user applications and AAS interface
provenance: D
legal_status: ecosystem
plane: trust
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
quote: the AAS interface SHALL ensure the identification and authentication of the AAS user application
---
