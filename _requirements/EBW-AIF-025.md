---
req_id: EBW-AIF-025
title: Delegation depth bounded by the mandate
category: AIF
statement: A mandate shall state whether the AI agent may sub-delegate and the maximum number of delegation steps, and a verifier shall reject a chain that exceeds it.
rationale: AP2 leaves agent-to-agent delegation unspecified and Council text requires over-delegation to be prevented, so the depth must be bounded explicitly.
sources:
- id: SRC-AP2
  location: Specification, Agent-to-Agent Delegation; cf. ST 9684/26 Annex point 12(3)(b)
provenance: D
legal_status: ecosystem
plane: control
perspectives:
- B2B
- A2A
actors:
- wallet owner
- AI agent
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: it is possible to use this protocol to support delegation of Mandates from one Shopping Agent to another
---
