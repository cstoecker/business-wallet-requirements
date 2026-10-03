---
req_id: EBW-LEG-042
title: Resilience of high-risk AI systems against manipulation
category: LEG
statement: A high-risk AI system acting with wallet credentials shall be resilient against attempts by unauthorised third parties to alter its use, outputs or performance by exploiting vulnerabilities.
rationale: Prompt or input manipulation of an agent holding signing authority would directly compromise a legal person. Chapter III Sections 1-3 of Regulation (EU) 2024/1689 apply from 2 December 2027 (Annex III systems) or 2 August 2028 (Annex I systems) under Article 113 as amended by Regulation (EU) 2026/1744.
sources:
- id: SRC-AIACT
  location: Article 15(5)
provenance: D
legal_status: in force
plane: assurance
perspectives:
- A2A
- B2B
actors:
- AI agent provider
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AI-SAFETY
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities
---
