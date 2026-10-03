---
req_id: EBW-INT-001
title: Issuance and presentation protocols in the WE BUILD pilot
category: INT
statement: In the WE BUILD pilot, PID/LPID and EAA providers shall implement OpenID4VCI 1.0, relying parties shall implement OpenID4VP 1.0, and wallet providers shall implement both in wallet solutions; proximity flows are out of scope.
rationale: Gives pilot participants one protocol profile so that wallets, issuers and verifiers can be tested together.
sources:
- id: SRC-WEBUILD-ARCH
  location: adr/base-protocols.md, section Decision
provenance: S
legal_status: ecosystem
plane: data
perspectives:
- B2B
- B2G
actors:
- Issuer
- Wallet provider
- Relying party
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
full_quote: PID/LPID Providers, EAA Providers (including QEAA, Pub-EAA) MUST implement OpenID4VCI version 1.0. Relying Parties MUST implement OpenID4VP version 1.0. Wallet Providers MUST implement in wallet solutions OpenID4VCI version 1.0 and OpenID4VP version 1.0. Proximity flows are out of scope.
fidelity_checked: '2026-10-03'
revision_note: Statement narrowed to what the clause contains after a check against the full text.
---
