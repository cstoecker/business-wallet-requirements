---
req_id: EBW-TRU-087
title: GLN organisation credential links to the GS1 trust chain
category: TRU
statement: The GLN organisation data credential shall reference the matching GS1 company prefix licence credential, directly or through a GLN key credential.
rationale: Shows the chain by which a party GLN credential traces to its issuing authority.
sources:
- id: SRC-WEBUILD-RB
  location: rb-gln rulebook, Section 2.2.3
provenance: S
legal_status: ecosystem
plane: trust
perspectives:
- B2B
actors:
- GS1 member organisation
- credential issuer
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-CROSS-SECTOR
- CON-LEGAL-PERSON-ID
created: '2026-10-03'
last_verified: '2026-10-03'
quote: reference the matching `GS1CompanyPrefixLicenseCredential` directly
---
