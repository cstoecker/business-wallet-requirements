---
req_id: EBW-AIF-006
title: Delegation path verifiable end to end
category: AIF
statement: Where the wallet or an agent delegates sub-tasks to other agents, a resource server at the end of the chain shall be able to cryptographically verify the entire delegation path back to the original principal and each step shall narrow scope.
rationale: Verifying only the final agent leaves the origin of authority unprovable.
sources:
- id: SRC-OIDF-AGENTIC
  location: Section 3.2 Delegated Authorization and Transitive Trust
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- A2A
actors:
- agent
- resource server
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: must be able to cryptographically verify the entire delegation path back to the original user
---
