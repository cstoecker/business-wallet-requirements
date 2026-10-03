---
req_id: EBW-AIF-012
title: Agent actions distinguishable in wallet log
category: AIF
statement: The European Business Wallet shall record, for each action performed by an AI agent, the agent identifier and the mandate relied on, so that it is distinguishable from direct user action in the log of transactions.
rationale: Article 6(1)(d) allows automatic interaction without manual intervention; auditors must still tell agent actions from human ones.
sources:
- id: SRC-EBW-PROPOSAL
  location: Article 5(1)(m); Article 6(1)(d)
provenance: D
legal_status: proposal
plane: assurance
perspectives:
- B2B
- B2G
- A2A
actors:
- wallet provider
- wallet owner
- AI agent
verification_method: test
status: draft
reviewer: pending
concepts:
- CON-AGENT-MANDATE
- CON-TRUSTED-AI
created: '2026-10-03'
last_verified: '2026-10-03'
quote: to allow interaction with the European Business Wallets automatically without manual intervention or through direct user action
---
