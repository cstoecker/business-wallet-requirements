---
req_id: EBW-TRU-071
title: Trust anchors stay secure for the whole verification period
category: TRU
statement: The trust service provider shall ensure that a trust anchor remains secure during the whole period in which signatures relying on it need to be verified, and shall apply a maintenance process before the trust anchor becomes insecure.
rationale: Trust anchors may need to outlive the certificates they sign, which drives rollover and maintenance planning.
sources:
- id: SRC-ETSI-TS-119312
  location: Clause 9.4, Time period resistance for trust anchors
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
- M2M
actors:
- trust service provider
- relying party
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST
- CON-PQC
created: '2026-10-03'
last_verified: '2026-10-03'
quote: A trust anchor shall remain secure during the whole time period
---
