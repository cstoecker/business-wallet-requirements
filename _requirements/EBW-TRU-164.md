---
req_id: EBW-TRU-164
title: Revoke mandate attestations when the company is dissolved
category: TRU
statement: The issuer of a power of attorney or power of representation attestation shall revoke it when the represented company is dissolved.
rationale: Delegated authority cannot outlive the principal; the rulebook lists the trigger as mandatory, and the issuer is derived from sections 4.14, 6.7 and 6.13.
sources:
- id: SRC-WEBUILD-RB
  location: rulebooks/rb-poa-pox.md, section 6.6 (Revocation Triggers) with sections 6.7 and 6.13
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- attestation issuer
- wallet owner
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-REVOCATION
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Company dissolved | SHALL
fidelity_checked: '2026-10-03'
revision_note: Location corrected to the registered catalogue path rulebooks/rb-poa-pox.md (commit de79cca, document version 0.7); section number and quote verified unchanged against that commit and against v0.8 of 2026-09-04.
---
