---
req_id: EBW-TRU-022
title: Revocation published within 24 hours
category: TRU
statement: When revoking a qualified certificate, the qualified trust service provider shall register the revocation and publish the revocation status within 24 hours of receiving the request, with immediate effect on publication.
rationale: Bounds the revocation latency relying parties must expect.
sources:
- id: SRC-EIDAS-CONSOL
  location: Article 24(3)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
actors:
- qualified trust service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: in any event within 24 hours after the receipt of the request
---
