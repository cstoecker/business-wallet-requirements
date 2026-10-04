---
req_id: EBW-TRU-174
title: Reject acts of a substitute where substitution is not allowed
category: TRU
statement: Where an EU power of attorney attestation states that substitution is not allowed, a relying party shall reject an act that a third party performs under powers the attorney has passed on.
rationale: Derived; the rulebook defines the attribute as the attorney's right to delegate the granted powers to a third party but states no verifier behaviour for the value not_allowed.
sources:
- id: SRC-WEBUILD-RB
  location: rb-eu-poa/README.md, section 2.8 (code list of scope_of_representation_power_of_substitution)
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Whether the attorney may delegate the granted powers to a third party
---
