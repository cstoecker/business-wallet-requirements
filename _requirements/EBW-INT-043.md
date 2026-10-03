---
req_id: EBW-INT-043
title: Catalogue request carries namespace, identifier and version
category: INT
statement: The requester of a catalogue entry for an attribute shall provide a namespace unique within the catalogue and an attribute identifier, unique within the namespace, together with the version of the attribute.
rationale: Gives each attribute a stable, versioned identity so issued attestations are unaffected by later changes.
sources:
- id: SRC-CIR-2025-1569
  location: Article 7(5)(d) and (e)
provenance: L
legal_status: in force
plane: trust
perspectives:
- B2B
- B2G
- G2B
actors:
- attribute requester
- Commission
verification_method: inspection
status: draft
reviewer: pending
concepts:
- CON-AUTHENTIC-SOURCES
- CON-CROSS-SECTOR
created: '2026-10-03'
last_verified: '2026-10-03'
quote: an identifier of the attribute, unique within the namespace, and the version of the attribute
---
