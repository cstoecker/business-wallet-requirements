---
req_id: EBW-TRU-045
title: Warn when requested attributes exceed registration
category: TRU
statement: After receiving a presentation request, the wallet unit shall verify that all requested attributes are included in the attributes of the registration certificate in the same request and shall warn the user if they are not.
rationale: Detects over-asking by relying parties.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 44, RPRC_21
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet unit
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-B2G-REGISTRY
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: verify that all attributes requested in the request are included in the list of attributes in the registration certificate
---
