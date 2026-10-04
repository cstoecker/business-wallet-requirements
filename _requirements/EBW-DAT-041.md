---
req_id: EBW-DAT-041
title: Identifier of a sole trader disclosed only as requested
category: DAT
statement: Where the owner is a natural person such as a self-employed person or sole trader, the wallet shall limit the unique identifier and other owner identification attributes it presents to a relying party to what that relying party needs for its purpose.
rationale: 'Derived: Recital 36 names sole traders among the owners; their unique identifier can identify a natural person, so GDPR data minimisation (EBW-LEG-010) applies (to verify); how this fits an atomic EBWOID is open (EBW-INT-057, EBW-INT-095).'
sources:
- id: SRC-COUNCIL-ST-9684-26
  location: Recital 36
provenance: D
legal_status: proposal
plane: data
perspectives:
- B2B
- B2G
- B2C
actors:
- wallet owner
- relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-PRIVACY
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: self-employed persons and sole traders, European Business Wallet owner identification data should be provided in a manner that is specifically designed to verify their identity
full_quote: including self-employed persons and sole traders, European Business Wallet owner identification data should be provided in a manner that is specifically designed to verify their identity and attested attributes within a business context.
fidelity_checked: '2026-10-03'
revision_note: Statement no longer says 'only as requested'; quote now from Council ST 9684/26 recital 36 and the duty marked as derived (GDPR minimisation, to verify).
---
