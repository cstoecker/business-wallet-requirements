---
req_id: EBW-TRU-138
title: Distribution point in trust tokens resolves to the latest list
category: TRU
statement: Where a trust service provider gives a distribution point for its trusted list in a trust service token, it shall ensure that the distribution point always resolves to the latest applicable trusted list or to a scheme list that points to it.
rationale: Lets a relying party find the applicable list from the token itself, which is the only discovery path that starts from the artefact being validated.
sources:
- id: SRC-ETSI-119612
  location: Clause 6.3 (TL Distribution Points in trust service tokens)
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- trust service provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST-DISCOVERY
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: always resolved to the latest available applicable TL or to a scheme including a pointer to it
---
