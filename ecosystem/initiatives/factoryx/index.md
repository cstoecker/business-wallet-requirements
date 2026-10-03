---
title: Factory-X
parent: Ecosystems & initiatives
grand_parent: Ecosystem
nav_order: 4
eco: ECO-FACTORYX
---

# Factory-X

## What it is and what it does

Factory-X is "an open and collaborative digital ecosystem for factory outfitters and operators, built on the foundations of Catena-X and the principles of Plattform Industrie 4.0", a lighthouse project of Manufacturing-X funded by BMWK. The consortium project **ended on 30 June 2026**; collaboration continues in the Manufacturing-X community and its GitHub organisation is archived. <span class="vtag v-ok">verified</span> [factory-x.org](https://factory-x.org/)

Its identity and access design is the **MX-Port "Leo"** configuration (specification v1.0, June 2026, <span class="vtag v-ok">verified</span>):
- **Discovery:** a company lookup service finds a company's servers by domain; a capability directory lists what a company offers.
- **Trust:** a trusted partner list names the trusted token issuers of a data space.
- **Identity token:** a minimal token issued by the consumer's token exchange service carries identity metadata; it distinguishes human and technical users.
- **Authentication versus authorisation:** shared services authenticate; the data provider authorises (for example attribute-based).

AAS is the data-access and model layer in Factory-X. It is context only and not a requirement source here.

## Governance

The governance paper FX-0097 (February 2026) proposes independent shared-service operators for the lookup and trusted-partner services; candidates named include IDTA GmbH, IDunion SCE and Cofinity-X. The specification lists "unified identity management and asset discovery" as future work, so identity is acknowledged as unfinished. <span class="vtag v-ok">verified</span>

## Relation to the European Business Wallet

None found in the Leo specification, the governance paper or the application guide. The Leo text does not mention DSP, DCP, DIDs or wallets. <span class="vtag v-todo">to verify</span> The project states 11 use cases <span class="vtag v-ok">verified</span>; their titles below come from a search summary only and are marked unverified.

{% include ecosystem-tables.html eco=page.eco %}
