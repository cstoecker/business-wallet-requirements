---
req_id: EBW-TRU-155
title: BPN access constraints validated through credentials
category: TRU
statement: Data providers and data consumers shall validate access policy constraints on the BPN or on BPNLs of a business partner group through the Membership Credential or the BPN Credential.
rationale: Access decisions for named partners rest on issuer-attested BPNs.
sources:
- id: SRC-CX-0152
  location: Section 2.1 (validation mechanism of constraints)
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- M2M
actors:
- data provider
- data consumer
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-LEGAL-PERSON-ID
- CON-CROSS-SECTOR
- CON-DSP-DCP
created: '2026-10-03'
last_verified: '2026-10-03'
quote: BusinessPartnerNumber and of the BPNLs contained in the BusinessPartnerGroup MUST be done via the MembershipCredential or the BpnCredential.
---
