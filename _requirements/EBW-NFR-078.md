---
req_id: EBW-NFR-078
title: Transaction log records reason for non-completion
category: NFR
statement: For each non-completed transaction, the wallet transaction log shall record the reason for the non-completion.
rationale: Failed transactions must be explainable for support and audit.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 7(2)(d)
provenance: L
legal_status: proposal
plane: data
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: in the case of non-completed transactions, the reason for such non-completion
---
