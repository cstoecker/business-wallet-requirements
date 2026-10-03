---
req_id: EBW-OPS-026
title: Notify users within 24 hours of unit revocation
category: OPS
statement: When the provider of European Business Wallets revokes a wallet unit attestation, it shall inform the affected wallet users without undue delay and no later than 24 hours after the revocation, stating the reason and the consequences, in concise and plain language.
rationale: Gives users prompt, understandable notice; counterpart of EBW-OPS-009 in the business wallet annex.
sources:
- id: SRC-EBW-PROPOSAL
  location: Annex, point 6(2)
provenance: L
legal_status: proposal
plane: control
perspectives:
- B2B
- B2G
- G2B
actors:
- wallet provider
- wallet user
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
created: '2026-10-03'
last_verified: '2026-10-03'
quote: no later than 24 hours from the revocation of their European Business Wallets units
---
