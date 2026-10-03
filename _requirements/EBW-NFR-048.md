---
req_id: EBW-NFR-048
title: Audit log time synchronised with UTC daily
category: NFR
statement: The trust service provider shall synchronise the time used to record events in the audit log with UTC at least once a day.
rationale: Accurate event times underpin evidence value and incident reconstruction.
sources:
- id: SRC-ETSI-EN-319401
  location: Clause 7.10, REQ-7.10-06
provenance: S
legal_status: standard
plane: assurance
perspectives:
- B2B
- B2G
- G2B
- M2M
actors:
- trust service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The time used to record events as required in the audit log shall be synchronized with UTC at least once a day.
---
