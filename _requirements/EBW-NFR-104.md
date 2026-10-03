---
req_id: EBW-NFR-104
title: No authentication to download status lists
category: NFR
statement: A provider of person identification data, an attestation provider or a wallet provider shall not require a relying party to authenticate itself before downloading an attestation status list or attestation revocation list.
rationale: Authenticated downloads would tell the issuer who checks which list.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 7, VCR_16
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- PID provider
- attestation provider
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL NOT require the Relying Party or Relying Party Instance to authenticate itself before downloading
---
