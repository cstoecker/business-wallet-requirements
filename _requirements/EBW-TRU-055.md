---
req_id: EBW-TRU-055
title: Agent identity portable across trust domains
category: TRU
statement: Where the wallet or an agent operates across organisational boundaries, its identity shall be verifiable by a third party that has no visibility into its host environment.
rationale: Infrastructure-attested workload identity does not work across domains that share no trust infrastructure.
sources:
- id: SRC-OIDF-AGENTIC
  location: Section 2.8 Identity for AI Agents
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- A2A
actors:
- agent
- relying party
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-MULTI-TRUST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: An agent's identity must be portable and verifiable to a third party that has no visibility into its host environment.
---
