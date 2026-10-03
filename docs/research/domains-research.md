# Research note: domain overlays, BIZ, CON and DAT candidates (I5)

Output: /tmp/cand/I5-domains.yml (51 candidates: DOM 25, DAT 13, CON 7, BIZ 6), new sources in /tmp/cand/I5-new_sources.yml (9). Every quote was machine-checked as a whitespace-normalised substring of the text read (max 25 words). Dropped from a first list of 96 to avoid noise.

## What was read
- ESPR (EU) 2024/1781: Articles 9 to 13 and Annex III in full (OJ text via publications.europa.eu). Commission pages: ESPR overview and the DPP page (timeline, read 3 Oct 2026), plus the 17 July 2026 DPP news item.
- Batteries Regulation (EU) 2023/1542: Articles 77, 78; headings of 38, 39, 48.
- Directive 2011/62/EU (searched for safety features, database, wholesale; consolidated 2001/83 not read) and Delegated Regulation (EU) 2016/161 Articles 4, 5, 31 to 39.
- EUDR (EU) 2023/1115: Articles 3, 4, 6, 7, 9, 33. CSDDD (EU) 2024/1760: searched, no identification or authentication duty.
- UCC (EU) 952/2013: Articles 5, 6, 9, 15, 18, 19. eFTI (EU) 2020/1056: Articles 1 to 9.
- Directive (EU) 2019/944 Articles 23, 24; Implementing Regulation (EU) 2023/1162 Articles 1 to 14 and the Annex.
- Data Act (EU) 2023/2854 Articles 4, 5, 6, 8, 9, 10, 11, 12, 28 to 30, 33, 36. DGA (EU) 2022/868 Articles 10 to 12, 17, 18, 21, 22. EHDS (EU) 2025/327 Articles 51, 60, 77, 78 and definitions.
- Proposal COM(2025) 838 (explanatory memorandum, Articles 2, 5, 7, 16 to 21), Council ST 9684/26 (recitals 6 to 11, 18, Articles 2, 4, 7, 16 to 21), impact assessment SWD(2025) 837 sections 6 and 7.

## Not an obligation for a wallet (and why)
- ESPR Article 11 digital credentials: the Commission "may" adopt implementing acts; no act was found. The candidate is a derivation (D). Delegated acts: the Commission DPP page lists none as adopted for a product group; iron and steel is planned Q4 2026, textiles, tyres, aluminium 2027. The battery access-rights implementing act (Art 77(9), due 18 August 2026) is shown as planned for Q4 2026.
- ESPR Annex III (j), importer EORI: the delegated acts decide which data are included; no wallet duty.
- Batteries Articles 38 and 39 are manufacturer and cell-supplier conformity duties, not due diligence. Due diligence is Articles 48 to 52 (applicable date changed by later amendments, not read); no identification or authentication duty was used.
- CSDDD: obligations are risk-based due diligence and complaints; the text only mentions digital tools in recitals and guidelines. Nothing for a wallet.
- UCC Article 9: registration of economic operators; the base Regulation read does not use the term EORI (it is defined in the implementing and delegated acts, not read). EORI is attested through ESPR Annex III and EUDR Article 33(2)(a).
- Directive 2019/944 Articles 23 and 24 bind Member States and data managers; the Implementing Regulation Article 8 defines the permission administrator. These are domain parallels of wallet authorisations, not wallet duties.
- EHDS: Articles 60 and 77 oblige health data holders to describe datasets, but no rule on identifying health data holders was found; no candidate written.
- Data Act and DGA: duties fall on data holders, smart-contract vendors, data processing service providers and intermediaries. Applicability to a wallet provider or connector is a derivation and is stated in the rationale; where it is uncertain it says "to verify".
- BIZ and CON from the impact assessment (cost model, adoption ranges, PSB full adoption) are assumptions of the Commission analysis, written as provenance D, legal_status "proposal", and not as law.

## Council differences to track
- Council ST 9684/26 deletes the 36-month derogation for registered delivery (Article 16(2) and (3) deleted), adds Article 16(1a) on Member State measures, SME impact assessment in the review, Article 7(2a) on security-risk tools, and narrows equivalence to qualified trust services (Article 4). Outcome of the 9 June 2026 meeting not read.

## Gaps
- EUR-Lex Official Journal text only; amending acts for EUDR (application date), Batteries (due diligence date) and the consolidated Directive 2001/83 were not read.
- Pharma: EMVS governance documents (EMVO) are not EU texts and were not read. The legal-person identification in EMVS is in Article 37(b); no EU text prescribes the mechanism.
- Energy: national implementations and the identity service provider requirements are not specified at EU level.
- DPP: the delegated act for iron and steel and the DPP registry implementing act were not found as adopted texts; the DPP standards implementing decisions (July and September 2026) were not read.
- SRC-REG-952-2013 is registered as partly-read; the articles used here were read and can be upgraded.
- The Business Wallet Study (NTT Data, October 2025) behind the cost model was not read; only the Staff Working Document.
