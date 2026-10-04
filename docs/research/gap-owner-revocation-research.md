# RES-J1: owner-side revocation, suspension and representation (K02, K03)

Output: /tmp/cand/J1-owner-revocation.yml (16 candidates, dry run clean, all 16 quotes machine-checked as substrings, none over 19 words). No new sources needed; all cite registered sources (SRC-WEBUILD-RB, SRC-WEBUILD-ARCH, SRC-COUNCIL-ST-9684-26, SRC-ARF-HLR). J1-new_sources.yml not created.

## Already covered (not re-added)
FUN-010/011 (multi-user and RP authorisations, manage and revoke), FUN-029, TRU-013 (wallet revocation incl. owner request and cessation), TRU-066, TRU-085, TRU-069, INT-030, FUN-035/036/042/043, FUN-015 (role conflicts, over-delegation, expired authorisations), GOV-025/026, OPS-026, TRU-106, FUN-053, TRU-134/135/136/137, LEG-045/046/047, TRU-097, NFR-095, LEG-068.

## Added
- Mandate status (a): TRU-159 suspension = invalid, TRU-160 reject unless active, TRU-161 verify before accepting, TRU-162/163/164 revocation on principal withdrawal, representative leaving, company dissolved (provenance D: rulebook gives the trigger without a duty-holder), OPS-041 automation and sync with authentic sources, GOV-049 revocation authority by law. Source: WE BUILD rb-poa-pox sections 4.14, 6.5-6.13.
- Owner ID data (a): TRU-166 (WE BUILD ADR, status Proposed).
- Mandates in the wallet (a, c): FUN-055 role-associated authorisations (Council Art 5(1)(j) only; the Commission text lacks it), LEG-069 (D) authorisation changes do not alter legal mandates (Art 5(1)(j), recital 17).
- Owner side (b): FUN-056 (D) owner can check own unit status, TRU-165 (D) authenticate before accepting revocation request (ARF WURevocation_10 mapped from EUDIW).
- Representative limits and multi-user (c): TRU-167 (IR-18), INT-088 (IR-12), TRU-168 (D) JOINT representation.

## Gaps where sources are silent (not invented)
1. No source gives triggers or procedure for revoking or suspending EBWOID (rb-ebwoid chapter 8 is a TODO; WE BUILD WP4 task 5). Only TRU-134/135/137/166 exist.
2. No Union or WE BUILD text defines suspension (as opposed to revocation) of owner ID data, of the wallet unit, or of a user authorisation. Council Art 6(2)(f) treats temporary cessation of activity as a revocation ground; rb-poa-pox 6.5 allows suspension but its status values (6.9) have no suspended value, an inconsistency to raise with WE BUILD.
3. No owner-side duty to notify the provider of cessation, or to review users' authorisations periodically, or to remove a leaving employee's wallet access within a set time. Only the leaving-employee mandate attestation (TRU-163) is sourced.
4. No four-eyes or approval-threshold rule for wallet use by multiple users; TRU-168 is the nearest (D) and applies to signatories, not generic wallet operations.
5. ARF WURevocation_13 (wallet checks its own and its attestations' status) is a SHOULD; not hardened.
6. Directive (EU) 2025/25 Art 16c(3) (Member States may require register filing of PoA and revocation; fee cap) is an option for Member States and not wallet-relevant; left out.
7. Council Art 12(3) of Article 6(5)-type implementing acts on exchange of authorisation data with national registers: only an empowerment, no obligation yet.
8. rb-employee and rb-authorised-signatories sections 4.1/6.2 are copy-pasted from other rulebooks (CompanyInfo, Contact Person wording); not used as sources.

Caveats: rb-poa-pox in the cache is v0.8 (2026-09-04), newer than the registered SRC-WEBUILD-RB commit de79cca (v1.0 catalogue, 2026-08-09); verify the section numbers against the registered commit before --write. No eIDAS 910/2014 or CIR 2024/2977/2979/1569 text speaks to owner-side suspension (grep for "suspen" found nothing in 2977, 2979, 1569).
