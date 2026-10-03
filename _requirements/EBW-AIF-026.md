---
req_id: EBW-AIF-026
title: Signed receipt for every mandate presentation
category: AIF
statement: Upon accepting or rejecting a presented mandate, the verifier shall return a signed receipt that references a hash of the received mandate.
rationale: The receipt gives both parties evidence of what was presented and with what outcome.
sources:
- id: SRC-AP2
  location: Agent Authorization, Action Authorization
provenance: S
legal_status: ecosystem
plane: assurance
perspectives:
- B2B
- A2A
actors:
- verifier
- AI agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Upon acceptance or rejection of the Mandate, the Verifier MUST return a signed Mandate Receipt.
---
