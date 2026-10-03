---
req_id: EBW-NFR-095
title: Explicit approval by the natural person for a legal-person signer
category: NFR
statement: Where the signer is a legal person and the authentication is linked directly to the identity, the signature activation protocol of a remote signature creation service shall include an explicit action of the natural person, identified during identity verification and allowed to sign in the name of the legal person, to approve the authorisation.
rationale: It shows how a business key held remotely is still tied to an accountable natural person at the moment of use.
sources:
- id: SRC-ETSI-TS-119431-1
  location: Clause 6.3.1, SIG-6.3.1-16
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- qualified trust service provider
- authorised representative
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-QUALIFIED-SERVICES
- CON-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: an explicit action (not just a checkbox) of the natural person identified during the identity verification process
---
