---
req_id: EBW-NFR-018
title: Random status list indices and herd privacy
category: NFR
statement: When using an attestation status list, the provider shall randomly assign the index of each attestation and shall represent a sufficiently large number of attestations per list to ensure herd privacy.
rationale: Prevents the status index becoming a correlator.
sources:
- id: SRC-ARF-HLR
  location: Annex 2 topic 7, VCR_17 and VCR_18
provenance: S
legal_status: standard
plane: assurance
perspectives:
- B2B
- B2G
- G2B
actors:
- attestation provider
- wallet provider
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL randomly assign the index for each PID or attestation, to prevent this index from becoming a correlator.
---
