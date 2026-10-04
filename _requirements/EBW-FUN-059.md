---
req_id: EBW-FUN-059
title: Owner replaces the seal creation device or trust service provider
category: FUN
statement: The wallet provider shall enable the owner to replace the qualified seal or signature creation device, or the trust service provider, linked to a wallet unit with another one without replacing the wallet unit.
rationale: 'Derived (criterion C6 of the DEC-03 page): remote keys are generated and managed only by the trust service provider, so a change of provider means new keys and certificates, which the sources do not describe.'
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 8(2)
provenance: D
legal_status: proposal
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- wallet owner
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: local, external, or remotely managed qualified signature or seal creation devices
---
