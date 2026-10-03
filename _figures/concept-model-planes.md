---
title: "Figure: the three planes and their main entities"
image: /assets/figures/concept-model-planes.svg
image_png: /assets/figures/concept-model-planes.png
width: 1200
height: 580
figure_type: concept model
alt: "Concept model with three bands. Trust plane: trust list, attestation, issuer. Control plane: policy engine, authorisation decision, EBW instance. Data plane: data transfer, evidence exchange, relying party. Lines show that a policy engine checks trust in a trust list and produces an authorisation decision, which is based on attestations and permits evidence exchange; the EBW instance holds attestations, enforces decisions and presents evidence to a relying party."
caption: "Concept model of the trust, control and data planes: who decides, what is trusted and how evidence moves."
description: "Reference concept model of the three core planes of a European Business Wallet architecture. The trust plane holds trust lists, attestations and issuers. The control plane holds the policy engine, the authorisation decision and the EBW instance that enforces it. The data plane carries evidence exchange and data transfer towards relying parties. It is the shared reference figure for the concept articles on the control plane, data plane and trust plane."
keywords: [trust plane, control plane, data plane, European Business Wallet, policy engine, attestation, trust list, relying party, concept model]
used_in: [/concepts/]
last_verified: "2026-10-03"
---
Style: peach entities, red relationship lines with crow's-foot cardinality, yellow highlight for the wallet instance and grey boxes for roles that are types, following the WE BUILD concept-model convention. This is the project's own reference model (see the methodology) and not a figure of any standard.
