---
req_id: EBW-TRU-141
title: Rulebook states how to obtain the trust anchor
category: TRU
statement: The scheme provider of a rulebook for a non-qualified attestation shall specify how a relying party obtains the trust anchor needed to verify the attestation signature.
rationale: Non-qualified attestation providers are not on a Commission list, so without a rulebook mechanism a relying party cannot find the anchor.
sources:
- id: SRC-ARF-TRUST
  location: Section 6.3.2.4 (trust anchors conditionally included in a Trusted List or LoTE)
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- scheme provider
- relying party
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-TRUST-LIST-DISCOVERY
- CON-MULTI-TRUST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: it must know how to obtain the trust anchor it needs to verify the signature over that EAA
---
