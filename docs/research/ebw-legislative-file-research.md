# Research note: European Business Wallet legislative file COM(2025) 838 (2025/0358(COD))

Retrieved 2026-10-03. All quotes are verbatim and 25 words or fewer.

## 1. Commission Annex: retrieved in full

- Route that worked: `https://publications.europa.eu/resource/celex/52025PC0838` with `Accept: application/xhtml+xml` and `Accept-Language: eng` returns an HTTP 300 list of two items. DOC_1 is the act (1_EN_ACT_part1_v7.html). DOC_2 is the Annex (1_EN_annexe_proposition_part1_v5.html).
- Annex URL: http://publications.europa.eu/resource/cellar/bfd78780-c5de-11f0-8da2-01aa75ed71a1.0001.03/DOC_2 (read state: read in full, 17 points, title "Requirements for minimum functionalities and technical requirements of European Business Wallets").
- Not working: eur-lex.europa.eu legal-content HTML/PDF (HTTP 202, empty, AWS WAF challenge); the europarl.europa.eu RegData copy `COM_COM(2025)0838_EN.pdf` returns the act only (ends before the Annex, same 4144 lines as the local /tmp/p.txt); the Commission digital-strategy page links only the newsroom document 121737 (not fetched).
- Local copies: /tmp/review/annex.txt, /tmp/review/act.txt.

### Annex structure (Commission text)

| Point | Subject | Commission-only features (Council general approach differs) |
|---|---|---|
| 1 | Unit authentication, LoA substantial via notified eID or equivalent | none material |
| 2 | Unit integrity, unit attestation signed under trusted-list certificate (IR 2024/2980) | none |
| 3 | Secure communication and critical assets | 3(3) LoA substantial design rules (deleted by Council) |
| 4 | Wallet secure cryptographic applications | 4(1)(b) and (g) LoA substantial (deleted by Council) |
| 5 | Unit authenticity and validity | none |
| 6 | Revocation of unit attestations, 24 h notice | none |
| 7 | Transaction logs | 7(2)(b) no "if available"; 7(3) no "availability" |
| 8 | Qualified signatures and seals | none |
| 9 | Signature creation applications | none |
| 10 | Export and portability at LoA substantial | Council: export, import, user authenticated per point 1 |
| 11 | Secure legal communication channel (QERDS) | 11(2)(a) "designate one" service; Council: designate protocol and standards |
| 12 | Access control mechanism | 12(3)(c) interoperable "across Member States"; Council: "between European Business Wallets" |
| 13 | Protocols and interfaces | wording on EUDI access certificates differs |
| 14 | Issuance of attestations to units | 14(2)(c) LoA substantial; Council: high |
| 15 | Presentation of attributes | none |
| 16 | Issuance of owner identification data | Commission: competent (national) authorities; Council: providers of wallets |
| 17 | Issuance of attestations | 17(2) identify by "wallet-relying party access certificate"; Council drops it |

Verbatim anchors (Annex, Commission text):
- Point 1: "Access to the European Business Wallets Unit shall be granted only after the European Business Wallets user has been successfully authenticated"
- Point 6(2): "no later than 24 hours from the revocation of their European Business Wallets units"
- Point 11(2)(a): "designate one qualified electronic registered delivery service that shall serve as the mandatory secure legal communication channel"
- Point 12(2)(c): "all access and execution events are logged, timestamped, and bound to cryptographically verifiable proofs of authorisation"

Cross-references from the articles into the Annex that the candidates serve: Art 5(4) (core functionalities per Annex), Art 6(4) (technical features per Annex), Art 7(6)(c) ("point 1 of the Annex" for revocation requests), Art 5(1)(i) (QERDS "set out in the Annex" in the Council text).

Typo-level errors in the Commission Annex worth noting for the catalogue: point 9(3) cites "Article 5" and point 9(2) "Article 6" for implementing-act empowerments (the examination procedure is Article 19); point 14(2)(c) carries a dangling footnote "(11)"; point 12(2) has "nables".

## 2. Procedural status (as of 2026-10-03)

### Timeline

| Date | Event | Source (read state) |
|---|---|---|
| 2025-01 | Commission announced the initiative in the Competitiveness Compass | Legislative Train (read) |
| 2025-05-15 to 2025-06-12 | Public consultation | Legislative Train (read) |
| 2025-11-19 | Commission proposal COM(2025) 838, SWD(2025) 837 | Observatory (read) |
| 2025-12-18 | Eero Heinäluoma (S&D, FI) appointed ITRE rapporteur | Observatory (read) |
| 2026-01-12 / 2026-02-16 | JURI (Axel Voss, EPP) and IMCO (Veronika Cifrová Ostrihoňová, Renew) opinion rapporteurs appointed | Observatory (read) |
| 2026-01-19 | Referral announced in Parliament; EESC consulted | Observatory, ST 9684/26 (read) |
| 2026-01-20 | EDPS Opinion 5/2026 | EDPS PDF (read) |
| 2026-02-10, 03-10, 04-14 | Cyprus Presidency compromise proposals 1, 2, 3 (3rd dated 27 March in ST 7604/26) | ST 9684/26 (read) |
| 2026-03-03 to 03-31 | National parliament contributions (IT Chamber, PT, NL Senate, CZ Chamber, RO Senate) | Observatory (read) |
| 2026-03-18 | EESC opinion INT/1110 (rapporteur Philip von Brockdorff) | EESC page (snippet) |
| 2026-04-01 | ITRE draft report PE785.244 (ST 9684/26 says 20 March) | draft report (read) |
| 2026-04-23 | Amendments tabled in ITRE (PE787.816, PE787.818) | Observatory (not opened) |
| 2026-05-22 / 05-27 | ST 7659/26 to Coreper; Coreper agreed to submit text to Council unchanged | ST 7659/26, ST 9684/26 (read) |
| 2026-06-02 | ST 9684/26 general approach note | read |
| 2026-06-04 / 06-08 | IMCO and JURI opinions adopted (PE786.736, PE786.718) | Observatory (cover only) |
| 2026-06-09 | TTE (Telecommunications) Council adopts negotiating position (general approach) | Legislative Train (read); Council press release (not retrievable) |
| 2026-07-01 | Committee of the Regions opinion CDR4359/2025 | Observatory (not opened) |
| 2026-09-10 | ITRE vote on report and decision to open interinstitutional negotiations | Observatory, Legislative Train (read) |
| 2026-09-23 | Report A10-0240/2026 tabled for plenary | Observatory (read; report itself not retrievable) |

Facts and quotes:
- Council outcome: "On 9 June 2026, the Council adopted its negotiating position on the file." (Legislative Train, updated 20/09/2026). ST 9684/26 para 10-11 shows Coreper sent the text "without any changes" for "a general approach at its meeting of 9 June 2026". The press-release title is "European business wallets: Council adopts negotiating position". The press release page returned HTTP 403, so its text was not read. A search snippet attributes to it the aim of "a political agreement by the end of 2026" (snippet only, unverified).
- Whether the 9 June text is identical to ST 9684/26 is not confirmed from an outcome-of-proceedings document; treat ST 9684/26 as the Council mandate text.
- Parliament: committee responsible ITRE (dossier ITRE/10/04583); opinions IMCO and JURI; LIBE and BUDG gave no opinion. Observatory status: "Awaiting Parliament's position in 1st reading". Key event: "Committee decision to open interinstitutional negotiations with report adopted in committee" (10/09/2026). Legislative Train status: "Tabled".
- Trilogue dates: none published in the sources reached. No plenary vote date found, so the mandate may still need plenary confirmation or announcement under Rule 72 (not verified).
- EESC: key points include "calls for more harmonised identity matching and mandate structures" and a clear split between the identity wallet and the business wallet. Opinion text not downloaded.
- EDPS Opinion 5/2026 (20 Jan 2026): two recommendations, to extend Recital 39 to all personal data processing and to cite Regulation 2018/1725, and to add a Commission duty to cooperate with the EDPS in Article 15 (as supervisor of Union entities). It welcomes selective disclosure and the access limits on the European Digital Directory.

## 3. Differences

Sources: Commission = act.txt (DOC_1) and annex; Council = ST 9684/26 (2 June 2026); EP = ITRE draft report PE785.244 amendment numbers. The adopted committee report A10-0240/2026 was not retrievable, so EP positions may have moved.

| Topic | Commission | Council (ST 9684/26) | EP draft report |
|---|---|---|---|
| Definitions: mandate and representative | Art 3(18) 'authorised representative', 3(19) 'mandate' | Both deleted; new 3(19) 'authorisation' (rights granted to a "user", plus the access-control decision); 'user' renamed 'European Business Wallet user' | Keeps representative and mandate (Am 50 adds "roles ... and users"); Am 55 new 'automated transaction' by "digital or AI-driven agent" under revocable authorisation |
| Definitions: secure crypto components | 3(28) application, 3(29) device defined | 3(28), 3(29) deleted (3(18) too) | kept; Am 58 widens 'critical assets' to owner operational, financial or reputational impact |
| Definitions: owner and issuers | Owner "owns or has a right of use"; owner-ID providers include "the Commission" | Owner "owns" only; Commission not listed as provider; 'economic operator' enumerates entity types; new 3(33a) 'significant incident' (NIS2) | Am 52 owner identity "verified from an authentic source"; Am 59 'supporting infrastructure service provider' (cloud, key management) |
| Art 4 equivalence | Applies to any core functionality | Only qualified trust services among core functionalities; national electronic-format rules "remain applicable" | Am 60: only core functionalities "based on qualified trust services" |
| Art 5 core functionalities | (a) includes "issue"; (i) QERDS; (l) export "at the request of the owner" or on termination; no import | (a) drops "issue"; (f) issuance "by the provider on behalf of" the owner; (j) roles, "without prejudice to any power of attorney"; (l) export only on termination; new (la) import; (m) log of "communications and transactions"; 5(5) deadline 1 year | Am 61 drops "issue"; Am 63 QERDS must comply with Art 7(2) and Annex; Am 64 auditable restricted delegations; Am 65 minimisation on requests; Am 66 import; Am 67 extra functions must meet Art 6(2)(c) |
| Art 6 technical features | 6(1)(e) onboarding via authorised representative, LoA substantial or high; 6(1)(k) unit attestations with keys in secure device; 6(1)(l) critical assets | 6(1)(e) via legal representative, LoA high only; (k) simplified; (l) deleted; new 1a standalone digital address for public bodies not owners; (ea) accessibility; 6(2)(b) logic interoperable "between" wallets; 6(5) deadline, data exchange with national registers | Am 74 LoA high; Am 73 automated processes verifiable and auditable; Am 77 deletes 6(1)(l); Am 78 owner ID "cryptographically bound"; Am 79 "document security controls"; Am 80 deletes 6(2)(d) |
| Art 7 provider duties | 7(3) Art 19a eIDAS applies, not to QTSPs; 7(4) NIS2 compliance | 7(3) carve-out not in the text; 7(4) deleted; 7(2a) tools for third-country control, 8 months; 7(6)(e) adds intent to cease; new 7(6a) to (6c) risk assessment, self-assessment every 24 months | Am 87 EU establishment extended to supporting infrastructure providers, data "exclusively stored and processed in the Union"; Am 88 cites Cybersecurity Act 2 (COM(2026)11); Am 91 notify without undue delay |
| Art 16 public sector bodies | 24 months after entry into force; 16(2) must hold wallets with QERDS; 16(3) alternatives until 36 months | 16(1) without date; 1a Member States take organisational and technical measures; 16(2), 16(3) deleted; applies 2 years after last implementing act (Art 22(1c)) | Am 117 24 months after implementing acts; Am 118 exempts municipalities with 10,000 inhabitants or fewer; Am 120 derogation until 36 months after implementing acts |
| Annex 3(3), 4(1)(b), 4(1)(g) | LoA substantial rules for crypto components | all deleted | Am 132, 133, 134 delete the same points |
| Annex 7 logs | 7(2)(b) unconditional; 7(3) no availability | 7(2)(b) "if available"; 7(3) adds availability | Am 135 logging policy "implement and document" |
| Annex 10 portability | Export, LoA substantial | Export, import, user authenticated per point 1 | Am 136 adds import, keeps LoA substantial |
| Annex 11 QERDS | 11(2)(a) one service designated | Commission designates "protocol" and standards | Am 137 one or more services complying with Art 7(2); Am 138 provider ensures procedures |
| Annex 14(2)(c) | LoA substantial | LoA high | Am 140 LoA high |
| Annex 16 and 17(2) | Competent authorities issue owner ID; issuers use access certificate | Providers of wallets ensure; no certificate wording | not amended |

Effect for requirements: Commission-only items (Annex 3(3), 4(1)(b) and (g), 11(2)(a) "one service") are flagged in the candidates as at risk; LoA moves from substantial to high at onboarding and owner ID issuance in both Council and EP; data localisation and supporting-infrastructure establishment are EP-only additions.

## 4. Open questions

1. Obtain the text of the 9 June 2026 Council press release and any outcome-of-proceedings document (consilium.europa.eu returned 403 to all clients); confirm the mandate equals ST 9684/26.
2. Retrieve A10-0240/2026 and the ITRE amendments PE787.816 and PE787.818 (doceo returns a WAF challenge); check whether the Annex amendments (131 to 140) were kept and whether the June Council LoA positions were adopted.
3. Read IMCO and JURI opinions (PDFs downloaded to /tmp/review/imco.pdf and juri.pdf) and the EESC opinion docx.
4. Trilogue calendar: not found in official sources.
5. The Annex numbering errors (cross-references to Article 5 and 6 for implementing acts, dangling "(11)") may be fixed in later texts; check before citing.
6. Whether the Commission text point 2 "certificate listed in the trusted list" under IR 2024/2980 still stands in the Council text: yes, unchanged in ST 9684/26.

## 5. URLs used

- https://publications.europa.eu/resource/celex/52025PC0838
- https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0358(COD)
- https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-european-business-wallet
- https://www.europarl.europa.eu/RegData/commissions/itre/projet_rapport/2026/785244/ITRE_PR(2026)785244_EN.pdf
- https://data.consilium.europa.eu/doc/document/ST-9684-2026-INIT/en/pdf, ST-7659-2026-INIT, ST-7604-2026-INIT
- https://www.edps.europa.eu/system/files/2026-01/26-01-20_opinion_establishment_of_european_business_wallets_en.pdf
- https://www.eesc.europa.eu/en/our-work/opinions-information-reports/opinions/european-business-wallets
