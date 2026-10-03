---
req_id: EBW-NFR-035
title: Every authenticated agent request leaves a trace
category: NFR
statement: Where the wallet or an agent uses workload identity for authentication, each authenticated request shall leave a verifiable and inspectable trace regardless of the authorisation decision.
rationale: Denied requests are as relevant for incident analysis as granted ones.
sources:
- id: SRC-WIMSE-ARCH
  location: Section 3.4.5 Audit Trails
provenance: S
legal_status: standard
plane: assurance
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- wallet provider
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Each authenticated request MUST leave a verifiable and inspectable trace regardless of authentication and authorization decision.
---
