---
req_id: EBW-AIF-034
title: Logging capability supports traceability and monitoring
category: AIF
statement: The provider of a high-risk AI system shall provide logging capabilities that record events relevant for identifying risk situations or substantial modifications, for post-market monitoring and for deployer monitoring of operation.
rationale: Complements EBW-LEG-040 (existence of logging) by fixing the purposes the log content must serve, relevant for audit trails of agent actions on wallet data. Applies only if the AI system is classified high-risk under Article 6; mapping to a wallet or agent operator is a derivation.
sources:
- id: SRC-AIACT
  location: Article 12(2)
provenance: D
legal_status: in force
plane: assurance
perspectives:
- B2B
- A2A
actors:
- provider of high-risk AI system
- agent operator
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUSTED-AI
- CON-AGENT-MANDATE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: logging capabilities shall enable the recording of events relevant for
---
