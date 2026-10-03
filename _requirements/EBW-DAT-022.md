---
req_id: EBW-DAT-022
title: Credentials and presentations use one profile
category: DAT
statement: In a data space that uses the Decentralized Claims Protocol, a credential and the presentation that carries it shall use the same data model version and the same proof mechanism.
rationale: Mixed profiles inside one presentation cannot be verified by one verification path.
sources:
- id: SRC-DCP
  location: dcp.profiles.md, Homogeneity requirement
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- M2M
actors:
- holder
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-DSP-DCP
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: the same data model version and proof mechanism MUST be used for both credentials and presentations
---
