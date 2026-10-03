---
req_id: EBW-NFR-028
title: A2A server authenticates every request
category: NFR
statement: Where the wallet or an agent implements A2A as a server, it shall authenticate every incoming request based on the credentials provided and its declared authentication requirements.
rationale: Declared securitySchemes are only meaningful if each call is checked.
sources:
- id: SRC-A2A
  location: Section 7.4 Server Authentication Responsibilities
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- A2A server
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MUST authenticate every incoming request based on the provided credentials and its declared authentication requirements.
---
