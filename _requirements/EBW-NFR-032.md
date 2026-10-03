---
req_id: EBW-NFR-032
title: Audit trail for sensitive agent operations
category: NFR
statement: Where the wallet or an agent implements A2A, the agent shall keep audit trails for sensitive operations and shall exclude credentials and unneeded personal data from the logs.
rationale: The specification says SHOULD for trails and MUST NOT for sensitive log content; both are needed to attribute agent actions.
sources:
- id: SRC-A2A
  location: Section 13.4 General Security Best Practices
provenance: D
legal_status: ecosystem
plane: assurance
perspectives:
- M2M
- A2A
- B2B
actors:
- agent
verification_method: audit
status: draft
reviewer: pending
concepts:
- CON-AISP
- CON-PRIVACY
created: '2026-10-03'
last_verified: '2026-10-03'
quote: Agents SHOULD provide audit trails for sensitive operations
---
