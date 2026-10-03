---
req_id: EBW-NFR-036
title: Agent signing keys protected, hardware-backed where available
category: NFR
statement: Where the wallet or an agent holds a DID authentication key, the key shall be protected against disclosure and shall use hardware-backed storage, an HSM or a secure enclave where available.
rationale: The specification says SHOULD for hardware; agent keys that sign on behalf of a legal person warrant that.
sources:
- id: SRC-W3C-AIAP-ID
  location: Security Considerations
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- wallet provider
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-WUA
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Hardware-backed key storage, an HSM, or a system secure enclave SHOULD be used where available.
---
