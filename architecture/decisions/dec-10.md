---
title: "DEC-10 AI-first: agent protocols, identity and mandates"
parent: Architecture decisions
grand_parent: Architecture
nav_order: 10
permalink: /architecture/decisions/dec-10/
description: "Which agent protocols (MCP, A2A), which form of verifiable agent identity and agent card, and which mandate model should a business wallet support so that AI agents act for an organisation under control? Facts from the specifications, criteria, options and conditions."
keywords: [AI agents, MCP, A2A, agent card, verifiable agent identity, mandate, delegation, OAuth token exchange, AP2, European Business Wallet, AI Act]
schema_type: TechArticle
toc: true
last_verified: "2026-10-03"
---

# DEC-10 AI-first: agent protocols, identity and mandates

*Analysis for decision, not a decision. Analysis, not legal advice. "Not stated" means that no source read says it.*

## Question

AI agents will act for organisations: they call tools, talk to other agents, submit documents and trigger payments. Which **protocols** must a business wallet support, how is an agent **identified** in a way a relying party can verify (a *verifiable agent card*), and how does an organisation give an agent a **mandate** that is limited, checkable and revocable? The decision connects the formats of DEC-01, the owner and user model of DEC-02 and the trust lists of DEC-04.

## What the requirement set says

The new category AIF (AI-first and agent interoperability) holds the requirements drawn from the agent specifications, the AI Act and the machine-readability duties. They are drafts: many are derivations (class D) because the specifications bind implementers of a protocol, not wallet providers, and the AI Act duties apply only where a system is high-risk under Article 6. The architecture-shaping ones for clusters K16 and K03:

{% include cluster-drivers.html cluster="K16" %}

The Commission proposal itself mentions agents once, in recital 28 ("agentic AI" as a new use case that implementing acts should allow). The mandate provisions it contains (Article 5(1)(j), Article 6(2)(b)) concern users of the wallet and apply to agents only by interpretation.

## Facts from the specifications

| Specification | Version | What it says about agent identity | What it leaves open |
|---|---|---|---|
| Model Context Protocol, authorization and security | revision 2026-07-28 | The client ID is the agent's identity: a Client ID Metadata Document (a SHOULD), pre-registration, or Dynamic Client Registration, which the revision deprecates. The server is an OAuth resource server found by metadata (RFC 9728). Tokens are bound to an audience and token passthrough is forbidden. | No identity of the server operator, no agent credential, no link to a legal person. The authorisation server is out of scope. Human approval is only a SHOULD. |
| Agent2Agent (A2A) | 1.0.0 | An Agent Card is mandatory. Signing it with JWS is optional (MAY): RFC 8785 canonicalisation, `kid` and `jku` headers, and verification that rejects expired or revoked keys. Authentication schemes are declared in the card; an authenticated extended card exists. | No trust framework for card signers and no mapping of a signing key to an organisation. Credential scope and revocation are not defined. The publication date was not given on the page read. |
| OpenID Foundation whitepaper on agentic identity | October 2025 | Informative. Agents act by delegation, not impersonation, and stay distinguishable from the principal; identity can carry model, version and capabilities; RFC 8693 (`act` claim) is the building block. | No normative text. Revocation along delegation chains, recursive delegation and cross-domain federation are called unsolved. |
| IETF WIMSE architecture | draft-08, July 2026 | Workload identifiers and credentials are scoped to a trust domain; autonomous and delegated actions must be distinguishable; each delegation hop re-scopes; every authenticated request leaves an audit trace. | Still a draft. The mapping of trust domains to trust anchors is out of scope. No binding to a legal person. |
| RFC 8693, RFC 9396, RFC 9449 | RFCs | Token exchange with `act` and `may_act` (delegation), Rich Authorization Requests for structured fine-grained authority, DPoP for sender-constrained tokens. | None defines an agent identity or a mandate vocabulary. |
| Agent Payments Protocol (AP2) | v0.2 | Open and closed checkout and payment mandates, a trusted-surface role and signed receipts. | No revocation mechanism. The earlier terms *Intent Mandate* and *Cart Mandate* are no longer used. |
| W3C AI Agent Protocol Community Group | draft | DID-based agent authentication (did:wba, did:web, did:webvh) with HTTP Message Signatures; authentication kept separate from authorisation. | Not a standard; much of it is marked tentative. No organisational binding or mandate model. |

**Across all of them:** no specification binds an agent to a legal person or to a verifiable mandate. A business wallet, through credentials and trust lists, is where that binding can come from.

**Law.** Directive (EU) 2025/25 provides for a digital EU power of attorney (Article 16c; transposition dates not read). The AI Act duties for providers and deployers of high-risk systems (risk management, logging, human oversight, six-month log retention) apply only where Article 6 classifies the system as high-risk; Articles 4 and 50 apply to all AI systems. Whether a given wallet agent is high-risk was not analysed. The Council text of the EBW proposal deletes the definitions of authorised representative and mandate and keeps authorisations technical (see DEC-02).

## Decision criteria

| # | Criterion | Basis |
|---|---|---|
| A1 | The agent is bound to a legal person that a relying party can verify | driver; the sources show the gap |
| A2 | The mandate states principal, agent, scope, limits and validity | source (partial): ARF RP_01 for representation attestations, Council Annex 12(1)(c); the rest is a driver |
| A3 | Mandate presentation and verification at the time of use | driver; related: Article 6(2)(b) |
| A4 | Delegation chain with a bounded depth and re-scoping | source (partial): WIMSE, RFC 8693; depth limits are a driver |
| A5 | Revocation reaches the agent and the relying party quickly | source (partial): Article 5(1)(j); OIDF names it unsolved |
| A6 | Human approval above defined limits and ability to override | source: AI Act Article 14 (if high-risk); otherwise a driver |
| A7 | Non-repudiable evidence of what the agent did, under which mandate | source (partial): WIMSE audit trace; AI Act Article 12 (if high-risk) |
| A8 | Protocol interoperability and neutrality (MCP, A2A and later protocols) | driver |
| A9 | Trust anchors for agent cards (lists of trusted agents or issuers) | driver; related: DEC-04 |
| A10 | Privacy of the agent's and the principal's identity in presentations | source (partial): GDPR; driver for agents |
| A11 | Correct allocation of AI Act and GDPR roles (provider, deployer, controller) | source: the acts; the mapping to wallet roles is a derivation |
| A12 | Maturity of the specifications | source: versions above |

## Options

**O1. Protocol-native identity only.** Use the client IDs of MCP and the signed or unsigned Agent Cards of A2A as the agent's identity, with the organisation as an unverified claim.
- *Enables:* quick interoperability today.
- *Restricts:* no verified binding to a legal person, no mandate, no revocation path to relying parties.
- *Leaves open:* how a relying party decides whom to trust.

**O2. Wallet-anchored agent identity and mandate.** The organisation's wallet issues an agent credential and a mandate credential (principal, agent, scope, limits, validity, status). The key that signs the agent card is bound to that credential; relying parties verify card, credential, trust list and mandate status.
- *Enables:* A1 to A5 and A7 directly, a place to apply the owner and user model of DEC-02, reuse of formats from DEC-01.
- *Restricts:* needs a mandate vocabulary and trust framework for agents that no specification provides; the issuing and checking effort falls on the wallet.
- *Leaves open:* the vocabulary, status mechanism and legal weight of a non-qualified mandate.

**O3. Token-based delegation only.** Carry authority in OAuth tokens (RFC 8693 exchange with `act`, RFC 9396 rich authorisation, DPoP sender constraint) issued by an authorisation server of the organisation.
- *Enables:* works with MCP's authorisation model and existing identity providers.
- *Restricts:* tokens express runtime authority, not a verifiable mandate or the legal person; cross-domain federation and chain revocation are called unsolved.
- *Leaves open:* who the issuer is for a relying party in another domain.

**O4. Layered: O2 for binding and mandate, O3 for runtime.** The wallet issues the mandate credential and binds the agent's signing key; at run time an authorisation server derives short-lived, audience-bound tokens from the mandate (`act`, rich authorisation, DPoP); MCP and A2A carry the tokens and the card; the relying party can always resolve the card to the organisation and the mandate status.
- *Enables:* A1 to A9 together, protocol neutrality, short-lived runtime credentials.
- *Restricts:* two layers to build, and the mapping between mandate and token scopes must be defined.
- *Leaves open:* the mapping rules and the mandate vocabulary.

## Preliminary reading

*The analysis of this project, not a statement of a source.*

1. **The sources show the gap, not the answer.** All specifications assume that identity is handled elsewhere. The business wallet is the natural place for the binding to a legal person and for the mandate, which is the one thing none of them provides.
2. **O4 is the only option that meets A1 to A9.** O1 fails A1 to A5, O3 fails A1 and A9, and O2 alone lacks a runtime mechanism for short-lived delegation. The cost is the mapping layer and a mandate vocabulary that has to be defined, ideally as an attestation scheme in the catalogue sense of DEC-01.
3. **Keep the requirements protocol-neutral.** The current AIF and NFR requirements derived from MCP, A2A and DPoP are protocol-specific and should become *profiles* of neutral requirements ("the agent presents a verifiable credential that binds it to a legal person"; "authority is audience-bound and time-limited").
4. **Condition AI Act duties.** Log retention, oversight and risk management attach to high-risk systems; the wallet should provide the capability (logs, approval thresholds, override) without assuming classification.

**Conditions under which this reading holds.** The Commission or Council text keeps owner-side authorisation and revocation; a mandate can be expressed as an attestation under a registered scheme; relying parties accept a mandate presentation next to the agent card.

**What would change it.** A standardised agent identity or mandate credential by W3C, IETF or OpenID with legal-person binding; A2A or MCP adding a trust framework for signers; final rules on agents in the EBW text or its Annex; classification guidance for wallet agents under the AI Act; the transposition of Directive (EU) 2025/25.

## Gaps and next steps

- Write requirements for agent identity lifecycle and revocation (K07), discovery and trust in lists of trusted agents (K05), the mandate credential format (K01) and its presentation protocol (K08), liability for agent actions (K13), and privacy of agent identity (K09). The review of the AIF requirements found these missing.
- Read the AP2 specification again in its current version, the MCP client features (elicitation, roots, sampling), the A2A repository for signed-card enhancements, and the Annexes of the AI Act for the high-risk mapping.
- Check whether the AI Act's high-risk obligations have been postponed by later amendments before relying on the dates.
- Confirm with stakeholders which agent use cases matter first (B2G submissions, procurement, payments, supply chain).

## References

SRC-MCP-AUTH, SRC-MCP-SEC, SRC-MCP-TOOLS, SRC-A2A, SRC-OIDF-AGENTIC, SRC-WIMSE-ARCH, SRC-RFC-8693, SRC-RFC-9396, SRC-RFC-9449, SRC-AP2, SRC-W3C-AIAP-ID, SRC-DIR-2025-25, SRC-AIACT, SRC-GDPR, SRC-EBW-PROPOSAL, SRC-COUNCIL-ST-9684-26. Full entries with version, date and URL are in the source register.
