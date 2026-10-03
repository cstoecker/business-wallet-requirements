---
req_id: EBW-DAT-023
title: Data space participant identifier is a DID
category: DAT
statement: A participant in a data space that uses the Decentralized Claims Protocol shall use a decentralized identifier as its participant identifier.
rationale: A stable, resolvable identifier is the starting point for finding the credential service and the keys of a participant.
sources:
- id: SRC-DCP
  location: base.protocol.md, Identities
provenance: S
legal_status: ecosystem
plane: data
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
- CON-WALLET-CONNECTOR
created: '2026-10-03'
last_verified: '2026-10-03'
quote: This specification prescribes the Participant ID MUST be a DID.
---
