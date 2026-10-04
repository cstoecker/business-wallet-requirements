---
req_id: EBW-AIF-068
title: Owner can decommission an agent
category: AIF
statement: The wallet shall enable the owner to decommission an AI agent, which revokes all mandates and credentials issued to that agent.
rationale: Derived; the OpenID Foundation whitepaper (non-normative) says agents need a formal process through to decommissioning, and states that credentials must be revocable when no longer needed; EBW-TRU-065 and EBW-TRU-066 cover revocation of a single token or mandate but not the end of life of the agent.
sources:
- id: SRC-OIDF-AGENTIC
  location: Section 2.9, SSO and Provisioning (agent lifecycle management)
provenance: D
legal_status: ecosystem
plane: control
perspectives:
- A2A
- B2B
actors:
- wallet provider
- wallet owner
- agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: which require formal processes for creation, permissioning, and eventual decommissioning
---
