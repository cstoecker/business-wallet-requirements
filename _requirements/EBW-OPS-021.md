---
req_id: EBW-OPS-021
title: Inform parties when an algorithm becomes insufficient
category: OPS
statement: When an algorithm or parameter used by the certification service provider or its subscribers becomes insufficient for its remaining intended usage, the provider shall inform all subscribers and relying parties with whom it has relations and publish that information for other relying parties.
rationale: Gives a trigger and communication duty for algorithm migration.
sources:
- id: SRC-ETSI-EN-319411-1
  location: Clause 6.4.8, OVR-6.4.8-15
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
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-PQC
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: become insufficient for its remaining intended usage then the TSP shall inform all subscribers and relying parties
---
