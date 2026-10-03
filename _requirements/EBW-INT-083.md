---
req_id: EBW-INT-083
title: Relay between delivery providers uses the push pattern
category: INT
statement: A provider that relays an electronic registered delivery message over AS4 shall use the push message exchange pattern only.
rationale: One exchange pattern across providers avoids pull-based polling differences that would break interoperability.
sources:
- id: SRC-ETSI-EN-319522-4-1
  location: Clause 5.2 (Generic requirements)
provenance: S
legal_status: standard
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified electronic registered delivery provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: ERDS shall only use the push message exchange pattern.
---
