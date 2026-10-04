---
req_id: EBW-FUN-057
title: Wallet supports at least one remote qualified signing option
category: FUN
statement: 'The wallet provider shall ensure that its wallet solution supports at least one of the following options for remote qualified electronic signature creation: authentication to a signature web portal of the trust service provider, creation channelled by the wallet unit, or creation channelled by a relying party.'
rationale: It fixes how a wallet reaches a remotely held qualified key; stated for the EUDI Wallet and not for the EBW, where Annex point 8 is silent on the channel.
sources:
- id: SRC-ARF-HLR
  location: Annex 2.02, Topic 16, QES_06
provenance: S
legal_status: standard
plane: control
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
- CON-QUALIFIED-SERVICES
- CON-EBW-EUDIW
created: '2026-10-03'
last_verified: '2026-10-03'
quote: SHALL ensure that their Wallet Solution supports at least one of the following options for remote QES signature creation
---
