---
req_id: EBW-TRU-128
title: Risk analysis where status information is unavailable
category: TRU
statement: A relying party shall perform a risk analysis considering all relevant factors for the use case to determine whether it accepts or refuses a PID or attestation when no reliable information on its revocation status is available.
rationale: Offline use, expired caches and non-revocable credentials need an explicit decision rule.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 7, VCR_14
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- relying party
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: to determine whether it will accept or refuse a PID or attestation in case no reliable information regarding the revocation status
---
