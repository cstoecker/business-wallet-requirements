---
req_id: EBW-INT-097
title: EU power of attorney states whether the attorney may delegate onward
category: INT
statement: The issuer of an EU power of attorney attestation shall include an attribute stating whether the attorney may delegate the granted powers to a third party, with the values allowed, not allowed or limited.
rationale: Without this attribute a relying party cannot tell whether a power exercised by a substitute is covered; the rulebook lists the attribute among the attributes of the attestation but names the issuer only implicitly (derived from the issuer rules in section 2.9).
sources:
- id: SRC-WEBUILD-RB
  location: rb-eu-poa/README.md, sections 2.3 and 2.8 (scope_of_representation_power_of_substitution)
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- attestation issuer
- authorised representative
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Whether the attorney may delegate the granted powers to a third party
---
