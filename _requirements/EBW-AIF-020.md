---
req_id: EBW-AIF-020
title: Unknown mandate constraints fail evaluation
category: AIF
statement: A verifier shall treat any mandate constraint it does not recognise as failing evaluation.
rationale: Failing closed prevents an agent from using constraint types the verifier cannot enforce.
sources:
- id: SRC-AP2
  location: Agent Authorization, Verification and Processing Rules
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- B2B
- A2A
actors:
- verifier
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Any unknown Constraints MUST be treated as failing evaluation.
---
