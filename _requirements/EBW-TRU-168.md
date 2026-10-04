---
req_id: EBW-TRU-168
title: Joint representation requires two or more signatories acting together
category: TRU
statement: Where the representation type of the authorised signatories of a legal entity is joint, a relying party that verifies the authorised signatories attestation shall require that two or more signatories act together before it treats an act as made on behalf of the entity.
rationale: Derived from the code-list meaning of JOINT in the authorised signatories rulebook, which gives the definition but no verifier duty; the legal effect of a joint act is national law (to verify).
sources:
- id: SRC-WEBUILD-RB
  location: rulebooks/rb-authorised-signatories/README.md, section 2.8.1 (Representation Type Codes)
provenance: D
legal_status: ecosystem
plane: trust
perspectives:
- B2B
- B2G
actors:
- relying party
- authorised representative
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-MANDATE
- CON-AUTHORITY-ACCESS
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Two or more signatories are required to act together to make binding commitments on behalf of the legal entity
fidelity_checked: '2026-10-03'
revision_note: Reworded as verifier duty derived from the JOINT code-list definition; location moved to the registered catalogue path (commit de79cca); legal effect left to national law.
---
