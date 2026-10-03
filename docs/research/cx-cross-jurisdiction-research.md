# RES-cx-xj: Catena-X standards for cross-jurisdiction identity, identifiers and assurance (cluster K17)

Read 2026-10-03 from catenax-ev.github.io/docs/next/standards/ (CX-Neptune PREVIEW, go-live announced 24 Nov 2026) and, for comparison, /docs/standards/ (stable CX-Titan, "Current").

## Versions and what was read

| Standard | Preview (next) | Stable (Titan) | Read |
|---|---|---|---|
| CX-0010 BPN | v3.2.0 | v3.0.1 (differs slightly) | full |
| CX-0006 Registration/Onboarding | v2.1.0 (fast-track, "not eligible for certification yet") | v2.1.0 (same normative text) | full |
| CX-0049 DID Document | v2.3.0 | v2.3.0 | full (schema skimmed) |
| CX-0050 CX credentials | v2.2.1 | v2.2.1 | clauses 1 to 2.3 in full, 2.4 Dismantler skimmed |
| CX-0167 BPN-DID Resolution | v1.0.0 | page does not exist (404) | full (previously "partly-read", can be raised to read) |
| CX-0149 Wallet Requirements | v2.1.0 | v2.0.0 | full |
| CX-0018 Dataspace Connectivity | v4.3.0 | v4.2 | clauses 2.3 to 2.7 |
| CX-0076 Golden Record | v1.7.0 | v1.5.0 | full |
| CX-0152 Policy Constraints | v1.0.0 | v1.0.0 | clauses 2.1, 2.2 |
| CX-0135 Company Certificates | v2.4.0 | v2.4.0 | normative parts and 3.2, API payloads skimmed |
| CX-0009 Registration API | v2.0.0 (fast-track, not certifiable) | not fetched | endpoint descriptions only |
| CX-0074 Gate API, CX-0012 Pool API | v4.2.0, v5.2.0 | not fetched | grepped; API detail, no requirements extracted |
| CX-0154, CX-0081 | v1.1.0, v1.2.1 | not fetched | skimmed by header only; not identity related, skipped |

Not in the index: CX-0001 (404) and CX-0125. The index (standards changelog page) lists no other identity or jurisdiction standard. Quotes were checked as whitespace-normalised substrings of the fetched preview text; the hover glossary text that the site glues to terms (BPN, BPNL, BPNS, API) was removed before the check. Quotes are of the preview text; stable v3.0.1 of CX-0010 has the same issuance rules (checked by grep).

## Output

40 candidates (/tmp/cand/CX-xj.yml): DAT 17, TRU 11, INT 4, GOV 3, DOM 3, CER 2; 5 new sources (/tmp/cand/CX-xj-sources.yml: CX-0009, CX-0076, CX-0135, CX-0149, CX-0152). Dry run on the live repo reports 25 writable and 15 skipped only because the new sources are not yet registered; with the sources registered (tested on a scratch copy) all 40 pass. Duplicates skipped: EBW-DAT-003 (BPN credential issued by CSP) and EBW-DAT-004 (BPN stable). SRC-CX-0049 contributes no requirement (it contains no did:web or jurisdiction rule; did:web is in CX-0149).

## Findings relevant to K17

- BPNL is an ecosystem (secondary) identifier derived from a legal identifier. CX-0010 2.1 gives an ordered rule: VAT, else TIN, else national business register number, else international identifier (LEI, EORI), else no BPNL. LEI is the last resort, not a primary identifier. EUID is not an identifier type in the list; it only appears in a note on BRIS.
- The identifier type list in CX-0010 covers EU member states, GB, XI, CH and NO plus LEI (GLEIF_LEI) and EORI only. Mandatory BPN issuance is limited to EU, GB, CH, NO, Northern Ireland; all other countries are optional. CX-0076 Table 1 lists about 110 countries with country-specific rules (tax jurisdiction code for BR, CA, US), so non-EU handling exists in the Golden Record but not in the BPN identifier list.
- BPNL is issued for capital companies only; partnerships, sole proprietorships, associations and public sector bodies are optional. EBW covers all legal persons and public bodies (to verify against EBW scope).
- One issuing organisation only (footnote 7); the footnote itself names LEI's decentralised model as a possible alternative. Conflict with an EU model of many registers and the EBWOID provider(s).
- CX-0010 requires registration as ISO/IEC 6523 scheme with an ICD; this is the natural bridge to EUID/LEI/EBWOID in the EBW.
- CX-0076: Latin-script names are mandatory (script variants exist only in CX-0074, non-normative terminology); legal form uses the ISO 20275 ELF code (same list as LEI); confidence level (1/3/5 points) is an assurance analogue but not a level-of-assurance in the eIDAS sense; "is managed by" requires verified power of attorney, method left to the Catena-X association.
- Identity proofing (CX-0006 2.4) refers to a placeholder "CX-XXXX Identity Proofing" (stable page: "CX-NFR-IdP"); the assurance level is unspecified. Gap.
- Trust anchor: the core service provider-B is the only issuer of Membership/BPN credentials; CX-0167 says "properly signed by a trusted issuer" without defining who is trusted. CX-0009 adds an external Gaia-X clearing house trigger. No cross-jurisdiction issuers or trust lists.
- did:web is mandatory (CX-0149 2.1); identity is bound to a web domain, not to a legal register entry. CX-0049 and CX-0050 say nothing on legal-entity assurance. BPN credential schema has no required credentialStatus (membership has), so revocation of the BPN credential is unspecified (to verify). holderIdentifier is required but not defined in the text read.
- CX-0135 trust levels (none/low/medium/high/trusted) are in non-normative terminology (3.2.7) and are listed inconsistently (four names, five levels); not extracted.

## Gaps and to verify

- All pages are the CX-Neptune preview; CX-0006 and CX-0009 are fast-track and not yet certifiable. Re-check after the 24 Nov 2026 go-live. CX-0167 is absent from the stable release.
- Requirements derived from descriptive sentences in normative sections (CX-0050 2.1 issuer of Membership Credential; CX-0049 quotes) carry "shall" as a derivation; not a MUST in the source. Reviewer to confirm.
- Duty-holders: "Business Partner Data Management" (CX-0010 2.3) and "service provider" (CX-0076) are generic in the source; CX-0152 2.1 names no duty-holder, so data provider and consumer were taken from 2.2.
- CX-0076 country rule table (Table 2) and region rules were not extracted individually; a full jurisdiction rule set would need a separate pass.
- CX-0074, CX-0012 (API detail), CX-0018 clauses 1 to 2.2 and CX-0050 2.4 were not analysed in depth.
