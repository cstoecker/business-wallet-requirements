---
req_id: EBW-INT-098
title: Limited onward delegation lists its limitations
category: INT
statement: Where an EU power of attorney attestation states that substitution is limited, the issuer shall include the limitation details in the scope of representation powers and shall reject the attestation if they are missing.
rationale: A limited right to delegate onward is only verifiable if the limits are in the attestation, so that a chain of delegation cannot silently exceed them.
sources:
- id: SRC-WEBUILD-RB
  location: rb-eu-poa/README.md, section 2.9, integrity rule IR-04
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- attestation issuer
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: If `scope_of_representation_power_of_substitution` = `limited`, additional limitation details MUST be included in `scope_of_representation_powers`.
---
