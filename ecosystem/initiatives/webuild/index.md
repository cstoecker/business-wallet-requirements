---
title: WE BUILD
parent: Ecosystems & initiatives
grand_parent: Ecosystem
nav_order: 2
eco: ECO-WEBUILD
---

# WE BUILD

## What it is and what it does

WE BUILD is a Commission-funded **Large-Scale Pilot** that uses the EUDI Wallet and the European Business Wallet to reduce red tape for cross-border business. The project website reports 200+ organisations from 28 countries, including 13 national business registers; the General Assembly is led by the Dutch Ministry of Economic Affairs and project management by KVK (NL). ✅ [webuildconsortium.eu](https://www.webuildconsortium.eu/) Start and end dates, grant number and funding amount are not verified. 🔎

**Approach (✅ from the consortium blueprint D4.1 and ADRs):** use-case driven; work packages provide shared building blocks (architecture, semantics, wallet providers, PID/EBWOID provider, QTSP, trust registry infrastructure, test infrastructure). Consortium rules are set through **ADRs**, **conformance specifications** and **attestation rulebooks** that fill gaps of the ARF during the pilot. WE BUILD runs its own pilot trust infrastructure (list of trusted lists, trusted lists, relying-party access certificates, QEAA, test identities) and does **not** certify wallets.

**Use cases:** 13 in three areas: business (BU1–BU6), supply chain (SC1, SC2, SC5) and payments (PA1–PA4). SC3 and SC4 are not listed on the website. 🔎

## Rulebooks

The attestation rulebooks catalog holds pilot-level rulebooks (identity and authority: EBWOID, PID, EU company certificate, EU power of attorney, authorised signatories, ownership, control; identifiers: VAT ID, DUNS, GLN; business data: A1, ESG, e-invoice, approved supplier; payments and consumer attestations). Production rulebooks of the EUDI ecosystem are in the Commission's EUDI attestation rulebooks catalogue.

## Relation to the European Business Wallet

The blueprint anchors on Regulation (EU) 2024/1183 for natural persons and on the EBW proposal COM(2025) 838 final for economic operators. EBWOID, QERDS and the Digital Directory (EBW Art. 10) derive from the proposal, which is not yet in force; the ADRs record this interim risk. ✅

The ADR on the preferred attestation format (W3C VCDM) exists only on a contributor branch and is flagged as *proposed* in the requirement list. Spherity contributes to WE BUILD.

{% include ecosystem-tables.html eco=page.eco %}
