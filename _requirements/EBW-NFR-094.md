---
req_id: EBW-NFR-094
title: Remote signing key usable only with consent
category: NFR
statement: The provider of a remote signature creation service shall allow a signing key to be used only in cases for which the signer consent has been obtained.
rationale: It is the control that keeps a provider-held key under the control of its owner.
sources:
- id: SRC-ETSI-TS-119431-1
  location: Clause 6.3.1, SIG-6.3.1-09
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified trust service provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Signing keys shall be usable in only those cases for which the signer's consent has been obtained.
---
