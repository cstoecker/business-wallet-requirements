---
req_id: EBW-AIF-039
title: Measures against data poisoning and adversarial inputs
category: AIF
statement: The provider of a high-risk AI system shall include, where appropriate, technical solutions to prevent, detect, respond to, resolve and control attacks on training data, pre-trained components, adversarial inputs and confidentiality attacks.
rationale: Extends EBW-LEG-042 (resilience against manipulation) with the AI-specific attack classes that matter for prompt injection and model evasion against wallet-connected agents. Applies only if the AI system is classified high-risk under Article 6; mapping to a wallet or agent operator is a derivation.
sources:
- id: SRC-AIACT
  location: Article 15(5)
provenance: D
legal_status: in force
plane: control
perspectives:
- B2B
- A2A
actors:
- provider of high-risk AI system
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AI-SAFETY
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: data poisoning
---
