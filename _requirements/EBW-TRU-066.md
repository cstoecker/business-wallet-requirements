---
req_id: EBW-TRU-066
title: Revocation propagated to agent and verifiers
category: TRU
statement: When the owner revokes a mandate, the wallet provider shall make the revocation effective for the AI agent and for verifiers within a defined time, and verifiers shall reject presentations of the revoked mandate.
rationale: Article 5(1)(j) and real-time validation are meaningless if a revoked mandate remains usable at counterparties.
sources:
- id: SRC-EBW-PROPOSAL
  location: Article 5(1)(j)
provenance: D
legal_status: proposal
plane: control
perspectives:
- B2B
- B2G
- A2A
actors:
- wallet provider
- wallet owner
- AI agent
- verifier
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-AGENT-MANDATE
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: for the European Business Wallet owner to manage and revoke such authorisations
---
