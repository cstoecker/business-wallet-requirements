---
req_id: EBW-OPS-020
title: Inform relying parties of CA key compromise
category: OPS
statement: On compromise, loss or suspected compromise of a CA private key, the certification service provider shall treat it as a disaster, inform all subscribers and relying parties, and indicate that certificates and status information issued with that key may no longer be valid.
rationale: Defines the incident response when a trust anchor key is compromised.
sources:
- id: SRC-ETSI-EN-319411-1
  location: Clause 6.4.8, OVR-6.4.8-08, -11 to -13
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
- CON-REVOCATION
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: shall address the compromise, loss or suspected compromise of a CA's private key as a disaster
---
