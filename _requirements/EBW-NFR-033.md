---
req_id: EBW-NFR-033
title: Audit logs record principal and agent separately
category: NFR
statement: Where the wallet or an agent acts under delegated authority, the policy enforcement point shall record distinct identifiers for the human or legal-person principal and for the agent instance that performed each action.
rationale: It makes agent actions attributable for compliance and forensics.
sources:
- id: SRC-OIDF-AGENTIC
  location: Section 2.11 Closing the Auditability Gap
provenance: D
legal_status: ecosystem
plane: assurance
perspectives:
- B2B
- B2G
actors:
- agent
- policy enforcement point
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: unambiguously record not only who authorized an action but also which specific agent instance performed it
---
