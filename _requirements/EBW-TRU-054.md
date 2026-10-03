---
req_id: EBW-TRU-054
title: Bind agent identity to the legal person outside A2A
category: TRU
statement: Where the wallet or an agent acts for a legal person over A2A, the wallet provider shall bind the agent to the legal person by wallet credentials or equivalent evidence, because A2A leaves identity semantics to the protocol layer.
rationale: A2A authenticates an agent as an application; it carries no statement of which legal person the agent represents.
sources:
- id: SRC-A2A
  location: Section 7 Authentication and Authorization
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- A2A
actors:
- wallet provider
- agent
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-LEGAL-PERSON-ID
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Identity information is handled at the protocol layer, not within A2A semantics.
---
