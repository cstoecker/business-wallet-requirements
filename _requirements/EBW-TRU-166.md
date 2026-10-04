---
req_id: EBW-TRU-166
title: Revoked owner identification data leaves the structural trust of the unit intact
category: TRU
statement: When the owner identification data of a European Business Wallet unit is revoked or expires, the unit shall lose its identity validity while its wallet unit attestation stays valid.
rationale: The consortium decision separates identity trust from structural trust, so that only the owner-identification state changes; the ADR is proposed and not final.
sources:
- id: SRC-WEBUILD-ARCH
  location: adr/wallet-unit-lifecycle-management.md, Consequences and State Transitions
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
- M2M
actors:
- wallet provider
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-WUA
- CON-REVOCATION
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Revocation of EBWOID suspends identity validity while preserving structural trust.
---
