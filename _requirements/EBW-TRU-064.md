---
req_id: EBW-TRU-064
title: Credentials alone do not authorise agent actions
category: TRU
statement: A verifier shall not treat possession of a verifiable credential as authorisation of an action without evaluating an accompanying authorisation framework that checks the scope of the delegation.
rationale: VCDM states that credentials identify subjects and that authorisation needs an accompanying framework.
sources:
- id: SRC-VCDM-2.0
  location: Section 5.9 (non-normative)
provenance: D
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- A2A
actors:
- verifier
- relying party
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Authorization is not an appropriate use for this specification without an accompanying authorization framework.
---
