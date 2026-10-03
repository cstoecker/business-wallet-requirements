---
req_id: EBW-AIF-005
title: Agent identity carries model, version and capabilities
category: AIF
statement: Where the wallet or an agent presents an agent identity to a relying party, the identity shall be accompanied by metadata on the underlying model, version and capabilities so that the relying party can apply risk-based access control.
rationale: The whitepaper holds that workload identity says what an agent is but not how it behaves; the wording here is derived from that observation.
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
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Agent identity must be enriched with metadata about its underlying model, version
---
