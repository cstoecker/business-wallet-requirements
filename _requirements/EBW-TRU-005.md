---
req_id: EBW-TRU-005
title: Trust anchors and status checks by relying parties
category: TRU
statement: A relying party instance shall verify the signature over a presented PID, QEAA or PuB-EAA using a trust anchor of the provider obtained from a Trusted List or LoTE.
rationale: Trust anchors are only useful if they are used both for the credential and for its status.
sources:
- id: SRC-ARF-TRUST
  location: Section 6.6.3.6
provenance: S
legal_status: standard
plane: trust
perspectives:
- B2B
- B2G
- B2C
actors:
- Relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUST-PLANE
- CON-TRUST-LIST
created: '2026-10-03'
last_verified: '2026-10-03'
full_quote: To do this for PIDs, QEAAs, and PuB-EAAs, the Relying Party Instance uses a trust anchor of the Provider obtained from a LoTE or Trusted List.
fidelity_checked: '2026-10-03'
revision_note: Statement narrowed to what the clause contains after a check against the full text.
quote: the Relying Party Instance uses a trust anchor of the Provider obtained from a LoTE or Trusted List
---
