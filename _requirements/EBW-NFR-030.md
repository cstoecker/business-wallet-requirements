---
req_id: EBW-NFR-030
title: Extended Agent Card requires authentication
category: NFR
statement: Where the wallet or an agent offers an A2A extended Agent Card, it shall require authentication, using a scheme declared in the public card, before returning it.
rationale: Extended cards may carry organisation-specific capabilities that must not be public.
sources:
- id: SRC-A2A
  location: Section 13.3 Extended Agent Card Access Control
provenance: S
legal_status: ecosystem
plane: control
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The Get Extended Agent Card operation MUST require authentication
---
