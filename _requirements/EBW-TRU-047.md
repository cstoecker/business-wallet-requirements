---
req_id: EBW-TRU-047
title: Relying parties verify revocation status or document a risk analysis
category: TRU
statement: The relying party instance should verify the revocation status of a revocable attestation on receipt, and a relying party that does not shall perform a risk analysis covering the use case.
rationale: Keeps status checking the default without forcing it.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 7, VCR_13
provenance: S
legal_status: standard
plane: assurance
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
quote: SHALL perform a risk analysis considering all relevant factors for the use case
---
