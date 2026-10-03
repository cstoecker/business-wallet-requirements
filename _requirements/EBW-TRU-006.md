---
req_id: EBW-TRU-006
title: Invalid wallet provider status
category: TRU
statement: When the status of a wallet provider in the Wallet Provider LoTE is Invalid, PID providers and attestation providers shall refuse to issue PIDs and attestations to wallet units of that wallet provider.
rationale: 'Derived: ARF 6.2.3 describes that, once the Wallet Provider is set to Invalid in its LoTE, providers no longer trust its trust anchors and therefore refuse issuance to its Wallet Units. The shall form states this expected behaviour as a requirement on providers.'
sources:
- id: SRC-ARF-TRUST
  location: Section 6.2.3 Wallet Provider invalidation
provenance: D
legal_status: standard
plane: trust
perspectives:
- B2G
- B2C
actors:
- Issuer
- Member State
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
full_quote: As a result of this status change, PID Providers and Attestation Providers will no longer trust the trust anchors of the Wallet Provider ... They will therefore refuse to issue PIDs and attestations to any Wallet Unit provided by that Wallet Provider.
fidelity_checked: '2026-10-03'
revision_note: 'Marked as derived: the statement follows from the clause but is not literal.'
---
