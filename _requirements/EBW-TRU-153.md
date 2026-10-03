---
req_id: EBW-TRU-153
title: BPN-DID resolution checks the Membership Credential
category: TRU
statement: The BPN-DID resolution service shall check the validity of the provided Membership Credential, including type, expiry, revocation and a signature by a trusted issuer, and deny access if the check fails.
rationale: Access to the identifier directory depends on a trusted-issuer check; who is trusted is not specified.
sources:
- id: SRC-CX-0167
  location: Section 2.1
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- M2M
actors:
- core service provider-B
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-REVOCATION
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: MUST check the validity of the provided Membership Credential, e.g., correct type, not expired, not revoked, properly signed by a trusted issuer
---
