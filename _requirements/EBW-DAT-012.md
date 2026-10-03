---
req_id: EBW-DAT-012
title: Smart contracts can be safely terminated or interrupted
category: DAT
statement: The vendor of an application using smart contracts to execute a data sharing agreement shall ensure that a mechanism exists to terminate the continued execution of transactions and that the smart contract includes internal functions that can reset or instruct it to stop or interrupt operation.
rationale: A kill switch and stop function for automated data sharing, relevant for revocation of data-space participation.
sources:
- id: SRC-DATAACT
  location: Article 36(1)(b)
provenance: L
legal_status: in force
plane: control
perspectives:
- B2B
- M2M
actors:
- smart contract vendor
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-DSP-DCP
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: safe termination and interruption, to ensure that a mechanism exists to terminate the continued execution of transactions
---
