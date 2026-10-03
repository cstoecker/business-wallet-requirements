# Research note: accessibility obligations bearing on the European Business Wallet (I1)

Date of research: 2026-10-03. All quotes are verbatim (max 25 words). Candidates: /tmp/cand/I1-accessibility.yml (22), new sources: /tmp/cand/I1-new_sources.yml (6). A previous file /tmp/cand/H1-accessibility.yml holds only the two assumptions that became EBW-NFR-055/056 and was not touched.

## 1. Sources and read state

| Source | Where read | Read state |
|---|---|---|
| Directive (EU) 2019/882 (EAA) | publications.europa.eu celex 32019L0882, OJ text | Read in full: Articles 1 to 4, 7, 13 to 16, 32 to 35, Annexes I, V, VI; recitals 29, 87, 95, 97, 110, 112 by search. Articles 8 to 12 and 17 to 31 (product operators, market surveillance) not read. |
| Directive (EU) 2016/2102 (WAD) | celex 32016L2102 | Read in full from Article 1 to 11. Recitals not read. |
| Decision (EU) 2018/2048 | celex 32018D2048 | Read in full. |
| Decision (EU) 2021/1339 (amends 2018/2048) | celex 32021D1339 | Read in full. |
| EN 301 549 V3.2.1 (2021-03) | etsi.org PDF | Read: front matter, introduction, clauses 1, 5.2-5.3, 9.0, 9.6, 10.0, 11.0, 11.7, 12.1-12.2; clauses 5 to 8, 9.1-9.4 and 11.1-11.6 and the annexes not read line by line. |
| COM(2025) 838 | /tmp/cand/p.txt | Searched in full for accessib*, disabilit*, plain, user-friendly, inclusion; hits read in context. |
| Council ST 9684/26 | data.consilium.europa.eu PDF | Searched in full with the same terms; hits read in context. |
| EUDI ARF Annex 2 (eudi.dev) | /tmp/cand/eu/hl.txt | Topic 54 read; other hits by search. |
| CIR (EU) 2024/2979 and the other 2024/2977-2982, 2025/848, 1569, 1944 | /tmp/cand/eu | Searched for disability, 2019/882, user-friendly, plain language; only 2024/2979 Article 7(3) has a relevant hit. |
| Regulation (EU) 2018/1724 (SDG) | celex 32018R1724 | Read: Articles 8, 18, recitals 36-37 (by search), Article 14 header. |

Not verified: whether a Commission implementing decision publishes EN 301 549 as a harmonised standard under the EAA (Article 15(1)); the Commission page cited below does not say, and my guessed CELEX lookup returned not found. No EN 301 549 version later than V3.2.1 was found (the Commission page on the standard says the last change in the Web Accessibility Directive context was in August 2021).

## 2. Facts

### 2.1 European Accessibility Act, Directive (EU) 2019/882 (OJ text)

- Scope of products. Art 2(1): "This Directive applies to the following products placed on the market after 28 June 2025" (consumer general purpose computer hardware and operating systems, payment terminals, ATMs and other self-service terminals, consumer terminal equipment for electronic communications and audiovisual media, e-readers).
- Scope of services. Art 2(2): "this Directive applies to the following services provided to consumers after 28 June 2025", listing electronic communications services (except machine-to-machine transmission), access to audiovisual media, passenger transport elements, consumer banking services, e-books and dedicated software, and e-commerce services.
- Consumer definition. Art 3(22): "any natural person who purchases the relevant product or is a recipient of the relevant service for purposes which are outside his trade, business, craft or profession".
- Business-facing definitions. Art 3(28) "consumer banking services" means "the provision to consumers" of listed banking services; Art 3(30) "e-commerce services" are services "at the individual request of a consumer with a view to concluding a consumer contract".
- Microenterprise exemption. Art 4(5): "Microenterprises providing services shall be exempt from complying with the accessibility requirements referred to in paragraph 3". Art 3(23) defines a microenterprise as fewer than 10 persons and turnover or balance sheet up to EUR 2 million. Art 4(5) refers to "paragraph 3 of this Article", and Art 4(3) covers both Section III and Section IV of Annex I, so on the text the exemption reaches both sections for services (not the product duties of Art 4(2)).
- Core duty. Art 4(1): Member States "ensure ... that economic operators only place on the market products and only provide services that comply with the accessibility requirements set out in Annex I". Art 13(1): "Service providers shall ensure that they design and provide services in accordance with the accessibility requirements of this Directive."
- Service provider duties. Art 13(2) information per Annex V in public, written and oral, accessible format; Art 13(3) procedures keep conformity, with changes taken into account; Art 13(4) corrective measures and immediate information of competent authorities; Art 13(5) information on reasoned request and cooperation.
- Annex V point 1: the information goes "in the general terms and conditions, or equivalent document" and, in addition to Directive 2011/83/EU consumer information, contains a service description in accessible formats, explanations and a description of how Annex I is met. Point 3: provide "information demonstrating that the service delivery process and its monitoring ensure compliance".
- Exceptions. Art 14(1): the requirements apply only to the extent compliance "does not require a significant change ... that results in the fundamental alteration" and "does not result in the imposition of a disproportionate burden". Art 14(3) five-year retention; Art 14(5) renewal at least every five years.
- Annex I Section III (all services): accessibility of the products used, information on the functioning of the service via more than one sensory channel, "making websites, including the related online applications, and mobile device-based services, including mobile applications, accessible in a consistent and adequate way", and support services giving accessibility information.
- Annex I Section IV (specific services): consumer banking (e): identification methods, electronic signatures, security and payment services "perceivable, operable, understandable and robust" and information not above CEFR level B2; e-commerce (g): accessibility of "the functionality for identification, security and payment" and of identification methods and electronic signatures. Recital 97: "The appropriate accessibility requirements should also apply to identification methods, electronic signature and payment services, since they are necessary for concluding consumer banking transactions."
- Annex I Section I point 2 (products only): "the product shall provide an alternative to biometrics identification and control".
- Presumption of conformity. Art 15(1): products and services in conformity with harmonised standards whose references are published in the OJ "shall be presumed to be in conformity". Annex I Section VII lists functional performance criteria (for example usage without vision, limited cognition).
- Transition. Art 32(1): until 28 June 2030 service providers may continue to use products lawfully used before that date.
- Relation to WAD: recital 110 says the Directive's exceptions mirror the WAD and that activities on public sector websites that fall within the EAA scope (passenger transport, e-commerce) must also meet the EAA.

### 2.2 Web Accessibility Directive, Directive (EU) 2016/2102

- Scope. Art 1(2): "requiring Member States to ensure that websites, independently of the device used for access thereto, and mobile applications of public sector bodies meet the accessibility requirements set out in Article 4".
- Art 3(1) "public sector body": State, regional or local authorities, bodies governed by public law, and associations of them, "not having an industrial or commercial character".
- Art 3(2) "mobile application" means application software designed and developed by or on behalf of public sector bodies "for use by the general public on mobile devices".
- Art 4: "Member States shall ensure that public sector bodies take the necessary measures to make their websites and mobile applications more accessible by making them perceivable, operable, understandable and robust." The text sets principles, not technical criteria; the technical criteria come from the standard (Art 6).
- Art 5: disproportionate burden, assessed by the public sector body, with an explanation in the accessibility statement.
- Art 6(1): content meeting harmonised standards whose references are published in the OJ "shall be presumed to be in conformity". Art 6(3) names EN 301 549 V1.1.2 as a fallback only when no harmonised reference exists.
- Art 7(1): accessibility statement, in an accessible format, with a feedback mechanism and a link to the enforcement procedure; Member States ensure an adequate response within a reasonable period. Art 8: monitoring, three-yearly reports. Art 9: enforcement procedure.
- Exclusions. Art 1(3): public service broadcasters and NGOs not providing essential services; Art 1(4)(g): "content of extranets and intranets ... published before 23 September 2019, until such websites undergo a substantial revision" (content published later is in scope); Art 1(4)(e) third-party content outside the body's control.
- The WAD binds Member States; it contains no obligation on private providers.

### 2.3 Decisions (EU) 2018/2048 and 2021/1339, and EN 301 549

- Decision 2018/2048 published the reference of EN 301 549 V2.1.2 (2018-08) as the harmonised standard for websites and mobile applications under the WAD (Annex row 1).
- Decision 2021/1339 Annex deletes row 1 and inserts "EN 301 549 V3.2.1 (2021-03)"; Article 2: "Point (1) of the Annex shall apply from 12 February 2022." So V3.2.1 is the version referenced in the OJ for the WAD, as read.
- EN 301 549 V3.2.1 clause 9.0: "Conformance with W3C Web Content Accessibility Guidelines (WCAG 2.1) [5] Level AA is equivalent to conforming with all of clauses 9.1 to 9.4". The standard says it "reflects the content of the W3C WCAG 2.1 Recommendation" and does not reference WCAG 2.2 (the string "WCAG 2.2" does not occur). Clause 11 covers non-web software including mobile applications; clause 10 documents; clause 12 documentation and support services; clause 5.3: biometrics "shall not rely on the use of a particular biological characteristic as the only means of user identification". Annex A maps the standard to the WAD for web pages and documents (Table A.1) and mobile applications (Table A.2).
- Scope of the standard (clause 1): "intended for use by both providers and procurers", for "ICT products and services"; it is a free download at ETSI.
- The ARF Topic 54 note still cites V1.1.2 (2015-04), which Art 6(3) of the WAD names only as fallback and which the Decisions superseded.

### 2.4 COM(2025) 838 and Council ST 9684/26

- COM(2025) 838, operative articles and recitals: no occurrence of "disability" or "persons with disabilities". Recital 20 speaks of "a consistent user experience". Art 7(6)(b) and (c) require that owners and authorised representatives be "clearly informed, in a user-friendly, concise and accessible manner" of terms and conditions and of rights (covered by existing EBW-GOV-025 in part).
- COM(2025) 838, legislative financial and digital statement, point 4.3 table: accessibility is catered for because the implementing-act standards "will refer to accessibility requirements as it was the case for the EUDIW"; the text continues that providers "will be the private sector and as such their will need to comply with the Accessibility Directive 2019/882" (words split across table cells in the PDF). This is explanatory text, not an operative provision.
- Council ST 9684/26 (general approach note, 2 June 2026): Article 6(2) point (ea): "make the European Business Wallets they provide accessible for use, by persons with disabilities, on an equal basis with other users". Recital 20: providers "should also provide accessibility for persons with disabilities, including in accordance with Annex I of Directive (EU) 2019/882, to the extent relevant". Paragraph 9 of the note lists accessibility for persons with disabilities among the topics amended by the Presidency. Article 7(6)(b) and (c) as in the proposal, with (c) extended to "authorised European Business Wallet users". Annex point 6(2): revocation information "concise, easily accessible and using clear and plain language".
- The Council text is a proposal text; the outcome of the Council meeting and the Parliament position were not read.

### 2.5 EUDI ARF and Commission Implementing Regulations

- ARF Annex 2, Topic 54 (ecosystem specification, not law): ACC_01 "Wallet Providers SHALL ensure that their Wallet Units comply with applicable requirements and standards in Directive 2016/2012" (sic; the WAD is 2016/2102); ACC_02: "comply with accessibility requirements for products and services established under Directive (EU) 2019/882". ACC_02 corresponds to eIDAS Article 5a(21) (EBW-NFR-055) and was not duplicated.
- CIR (EU) 2024/2979 Article 7(3): revocation information "concise, easily accessible and using clear and plain language" (already EBW-OPS-009). No CIR among 2024/2977-2982, 2025/848, 1569, 1944 contains a disability or Directive 2019/882 provision; these Regulations carry no accessibility requirements of their own.
- Other user-experience requirements in the ARF (RPA_10 user-friendly description of intended use, DASH_01 user-friendly dashboard, PA_08 user-friendly pseudonym management) are usability, not accessibility; they are wallet-user (natural person) requirements and were not turned into candidates here.

### 2.6 Single Digital Gateway, Regulation (EU) 2018/1724

- Art 8: "The Commission shall make those of its websites and webpages through which it grants access to the information referred to in Article 4(2) and to the assistance and problem-solving services referred to in Article 7 more accessible by making them perceivable, operable, understandable and robust."
- Art 18(4)(d): the common user interface "meets the following web accessibility requirements: perceivability, operability, understandability and robustness". Recital 37 says the WAD does not apply to Union institutions.
- Article 14 (once-only technical system) as read contains no accessibility provision. The gateway accessibility duties bind the Commission for its own pages and the common interface; they do not reach the OOTS exchange or the business wallet. No candidate was produced; this belongs to the list of interfaces a European Business Wallet might link to.

## 3. Scope analysis (stated from the texts; inference marked)

| Instrument | Who is bound | Business wallet provider | Authority portal | Business user |
|---|---|---|---|---|
| EAA 2019/882 | Economic operators (manufacturers, importers, distributors, service providers), through Member States (Art 4(1), Art 13) | Bound only for products and services listed in Art 2 provided to consumers. A wallet for legal persons is not listed as such. Inference: a business wallet provider is not directly in scope for B2B wallet services; it is in scope if it also offers an Art 2(2) service to consumers (for example an e-commerce or electronic communications service) or places a consumer product in Art 2(1) on the market. Microenterprise service providers are exempt (Art 4(5)). | Not bound by the EAA as such; recital 110 says that where a public sector site carries an in-scope activity (passenger transport, e-commerce) the EAA applies too. | Not bound. A business user acting for business purposes is not a "consumer" (Art 3(22)); inference: B2B services are outside Art 2(2), because every listed service is "provided to consumers". An employee with a disability is protected, if at all, through other law (not read). |
| WAD 2016/2102 | Member States, who ensure that public sector bodies comply (Art 1(2), Art 4) | Not bound; the Directive names no private provider. Inference: a private provider that builds an authority's portal or app "on behalf of" the authority (Art 3(2)) delivers into the authority's duty; Art 7(3) invites Member States to extend the rules to other sites. | Bound: websites and mobile applications of public sector bodies, including portals through which businesses interact with authorities. Open: Art 3(2) mobile app definition says "for use by the general public"; an authority app for registered business users may fall outside that definition (inference). Extranets published after 23 September 2019 are in scope (Art 1(4)(g)). | Not bound; holds rights: feedback mechanism and enforcement procedure (Art 7(1), Art 9). |
| Decisions 2018/2048, 2021/1339; EN 301 549 | The Decisions only publish a reference; the standard is voluntary, with presumption of conformity (WAD Art 6(1); EAA Art 15(1) when a reference exists) | Not bound; the standard is the practical test basis for any wallet UI (inference). | Presumption of conformity with the WAD if V3.2.1 is met. | Not bound. |
| eIDAS Art 5a(21), Art 15 (already EBW-NFR-055, NFR-005) | Wallet providers (EUDI Wallet), and providers of electronic identification means, trust services and the end-user products used for them | See existing requirements. The business wallet is not an EUDI Wallet; whether it is an "end-user product" used for trust services is open. | Not bound. | Not bound. |
| COM(2025) 838 | Providers of European Business Wallets | No operative accessibility duty in the text read; only the "user-friendly, concise and accessible" information duty in Art 7(6)(b) and (c), and the statement that implementing acts will refer to accessibility requirements. | Not covered. | Beneficiary of Art 7(6) information. |
| Council ST 9684/26 | Providers of European Business Wallets | Bound by Art 6(2)(ea), if adopted as drafted; Annex I of the EAA is the named yardstick "to the extent relevant" (recital 20). | Not covered. | Beneficiary. |
| ARF Topic 54 | Wallet Providers of EUDI Wallets (ecosystem specification) | Not directly; the business wallet reuses the EUDI framework. | Not covered. | Not covered. |
| SDG 2018/1724 | The Commission for its gateway pages; Member States for information and procedures | Not bound. | Art 8 and 18(4) only for Commission pages; Member State portals via WAD. | Not bound. |

Net effect (inference, to be confirmed by legal review): the binding accessibility obligation on the wallet itself would come from the Council's Art 6(2)(ea) if retained in the adopted Regulation, or from implementing acts that "will refer to accessibility requirements"; the EAA reaches the provider only for consumer-facing services; the WAD binds the authority portals the wallet connects to. EN 301 549 V3.2.1 is the shared technical basis for all.

## 4. Mapping to the catalogue

- Covered already, not duplicated: EBW-NFR-005 (eIDAS Art 15), EBW-NFR-055 (Art 5a(21), ARF ACC_02 equivalent), EBW-NFR-056 (assumption, now has Council Art 6(2)(ea) as support), EBW-OPS-001 (support mechanism), EBW-OPS-009 (revocation information in plain language), EBW-GOV-025 (information to representatives, Council extends it to authorised users).
- New candidates: 22 in I1-accessibility.yml: NFR 12, LEG 8, INT 2; provenance L 12, S 6, D 4; legal_status in force 12 (EAA/WAD/Decision), proposal 3, standard 6, ecosystem 1.
- Suggested follow-up for review: link EBW-NFR-056 to ebw-council-wallet-accessible and consider marking 056 as superseded once the Council wording is confirmed.

## 5. Open questions

1. Does a European Business Wallet fall within Article 2 EAA at all? The services list is consumer-oriented; the wallet's owners are legal persons and their users act for business purposes. Needs legal review; the Council added a specific duty, which suggests the co-legislator did not rely on the EAA alone.
2. Microenterprise exemption: many wallet owners are microenterprises, but the exemption in Art 4(5) concerns the service provider, not the customer. On the text it covers Sections III and IV (Art 4(5) refers to paragraph 3 of Art 4); whether micro providers of a business wallet are in scope at all is the prior question.
3. Is an authority's app for registered business users a "mobile application" within WAD Art 3(2) ("for use by the general public")? Is a B2G web portal behind login covered as a website (probably yes, Art 1(4)(g) treats extranets as in scope for content published after 2019)?
4. Which accessibility conformance level will the implementing acts of the Business Wallet Regulation require, and which version of EN 301 549 (V3.2.1 is current in the OJ for the WAD; WCAG 2.2 is not part of it)? Is a harmonised EAA reference of EN 301 549 published in the OJ? Not verified.
5. The ARF text cites "Directive 2016/2012" and EN 301 549 V1.1.2; should the catalogue note an upstream correction?
6. Council text status: the outcome of the general approach and the Parliament position were not read; legal_status stays "proposal".
7. Employees with disabilities as wallet users: employer duties under other law (Directive 2000/78/EC, national law) were not in scope and not read.
