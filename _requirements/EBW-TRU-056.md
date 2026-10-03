---
req_id: EBW-TRU-056
title: Trust-domain key mapping obtained securely and fresh
category: TRU
statement: Where the wallet or an agent uses workload identity credentials, the mapping from trust domain to trust anchors or JWK Set shall be obtained through a mechanism that ensures its authenticity, integrity and freshness.
rationale: This is the point where a business-wallet trust list could supply agent trust anchors; WIMSE leaves the mechanism out of scope.
sources:
- id: SRC-WIMSE-ARCH
  location: Section 3.1.1 Trust Domain
provenance: S
legal_status: standard
plane: trust
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
- relying party
verification_method: analysis
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-TRUST-LIST
- CON-MULTI-TRUST
created: '2026-10-03'
last_verified: '2026-10-03'
quote: This mapping MUST be obtained through a secure mechanism that ensures the authenticity and integrity of the mapping is fresh and not compromised.
---
