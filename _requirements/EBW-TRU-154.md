---
req_id: EBW-TRU-154
title: Catalogue request token scope covers membership, BPN and framework credentials
category: TRU
statement: The token for requesting a catalogue shall include a scope covering the Membership Credential, the BPN Credential and the Framework Agreement Credential.
rationale: Counterparties are identified by ecosystem credentials before any data offer is shown.
sources:
- id: SRC-CX-0018
  location: Section 2.3
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- M2M
actors:
- data space participant
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-DSP-DCP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: The scope of the token for requesting a Catalog MUST include the following credentials as defined in CX-0050
---
