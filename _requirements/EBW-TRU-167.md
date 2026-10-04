---
req_id: EBW-TRU-167
title: Actions outside the mandate scope are rejected
category: TRU
statement: A relying party shall reject an action that falls outside the scope defined in the mandate of the acting representative.
rationale: The rulebook names verification as the point of enforcement and rejection of the action as the failure behaviour; this limits an employee or other representative to the powers granted.
sources:
- id: SRC-WEBUILD-RB
  location: rb-poa-pox/README.md, section 2.9, integrity rule IR-18
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- relying party
- authorised representative
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A mandate SHALL NOT authorize actions outside its defined scope
---
