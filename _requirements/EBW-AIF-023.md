---
req_id: EBW-AIF-023
title: Agent discloses only needed mandate content
category: AIF
statement: When presenting a mandate with selective disclosures, the AI agent shall disclose only the parts needed for the verifier to evaluate the closed mandate.
rationale: Mandate constraints can reveal business intent that the verifier does not need.
sources:
- id: SRC-AP2
  location: Specification, Autonomous (Human Not Present)
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- A2A
actors:
- AI agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Shopping Agents MUST present only the disclosures from the open Mandates needed in the evaluation of the closed Mandates.
---
