---
req_id: EBW-AIF-047
title: Machine-readable marking of AI-generated output
category: AIF
statement: The provider of an AI system generating synthetic audio, image, video or text content shall ensure that the outputs are marked in a machine-readable format and detectable as artificially generated or manipulated, using technical solutions that are effective, interoperable, robust and reliable as far as technically feasible.
rationale: AI-generated documents or messages entering the wallet's data plane must be machine-detectable as synthetic; applies to any AI system, not only high-risk. Mapping to a wallet-integrated generator is a derivation (D). Marking exceptions in Art 50(2) not reproduced. Providers of systems placed on the market before 2 August 2026 have until 2 December 2026 (Article 111(4)).
sources:
- id: SRC-AIACT
  location: Article 50(2)
provenance: D
legal_status: in force
plane: data
perspectives:
- B2B
- B2G
- A2A
actors:
- provider of AI system
- business wallet provider
- agent operator
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-TRUSTED-AI
- CON-DATA-PLANE
created: '2026-10-03'
last_verified: '2026-10-03'
quote: marked in a machine-readable format and detectable as artificially generated or manipulated
---
