# RES-K1: delegation chains, four-eyes, suspension, leavers, machine and agent authority (K03)

Output: /tmp/cand/K1-delegation.yml (24 candidates; dry run clean, all 24 quotes machine-checked as whitespace-normalised substrings, longest 23 words). New source: SRC-IDTA-AAS-P4 (/tmp/cand/K1-new_sources.yml). NOTE: register_sources.py writes directly, so SRC-IDTA-AAS-P4 is already appended to _data/graph/sources.yml (needed for the dry run); remove it if the batch is dropped.

## Added, by gap
- (a) Onward delegation: INT-097 (PoA states whether substitution is allowed, not allowed, limited), INT-098 (limits listed when limited), TRU-173 (issuer establishes principal authority; invalid delegation chains), TRU-174 (D, reject substitute acts when not allowed), LEG-077 (COM(2026) 321 Art 43(5): delegates of directors bound by directors' duties). Sources: rb-eu-poa v0.1 (draft, 9.4.2026; same repo as SRC-WEBUILD-RB, verify against registered commit de79cca), COM(2026) 321.
- (b) Four-eyes and joint: LEG-078 (Art 43(1) joint representation by default, proposal), GOV-055 (D, DORA RTS 2024/1774 Art 21(b) segregation of duties), GOV-056 (D, EN 319 401 7.1.2).
- (c) Suspension vs termination: OPS-044 (D, RTS 1774 Art 20(2)(b) lists temporary deactivation and termination separately), OPS-046 (D, periodic access update).
- (d) Leavers and decommissioning: OPS-045 (D, RTS 1774 Art 21(e)(iii), employment ends or access no longer necessary; covers generic and system accounts by derivation), LEG-079 (CRA Annex I Part I (2)(m), permanent data removal), AIF-068 (D, agent decommissioning, OIDF whitepaper, non-normative).
- (e) Machines and devices: TRU-175 (D, RTS 1774 Art 20(1) systems), TRU-176 (D, IDTA Part 4 authenticate application), OPS-047 (D, IDTA role alignment between identity service and interface), NFR-121 (D, IDTA audit of account and access-rule changes), LEG-080 (CRA (2)(l) activity recording).
- (f) Agent authority: AIF-064 (AI Act Art 14(3) oversight commensurate with autonomy), AIF-065 (14(4)(a)), AIF-066 (14(4)(b) automation bias), AIF-067 (Art 26(7) employer informs workers). Art 14(4)(d)/(e), 26(2), 26(5), 26(6) already exist (AIF-038, LEG-041, AIF-043, 044, 035). Text read from consolidated 02024R1689-20260727; Art 14 and 26 content checked, 2026/1744 does not alter the quoted wording of 14(3), 14(4), 26(7) (to verify against the OJ amendment articles).
- (g) Attribution: GOV-057 (D, RTS 1774 Art 21(c) limits generic and shared accounts), NFR-122 (D, IDTA non-repudiation, machine identified per event). Agent attribution already exists (AIF-012, NFR-033, TRU-054).

## Already covered, not re-added
AIF-004/006/007/008/025/028 (delegation chains for agents), INT-025/029 (act claim, nested actors), TRU-159..168 (mandate status, joint signatories), FUN-055, FUN-058, LEG-034 (CRA 2(d)), DAT-009/010 (Data Act user verification, party acting for user), LEG-041, AIF-037/038, AIF-042..044, NFR-032/033/035, TRU-065/066.

## Gaps where sources are silent (not invented)
1. Catena-X CX-0018 and CX-0006 (cached) contain no "technical user" or machine-user rule; CX-0018 covers connector credential verification only (TRU-154). No requirement written.
2. IEC 62443 is paywalled; not citeable as primary. Only IDTA Part 4's stated derivation from it is used (high level).
3. IDTA Part 4 "MAY" lines (application may stand for a non-person user) and "SHOULD" lines (error handling, input validation) not hardened.
4. Data Act (2023/2854): Art 4(5) verification of user status and Art 5(1) acting for the user already in DAT-009/010; user definition (owner or holder of temporary rights) is a definition, not a duty. No Data Act duty on machine authority found.
5. No Union text prescribes approval by a second person for wallet use as such. AI Act Art 14(5) (two natural persons) applies to Annex III point 1(a) biometric identification only; EN 319 411-1 dual control (GEN-6.4.3-02, GEN-6.5.1-04) is CA key ceremony specific; both left out.
6. No source defines when an employee's wallet access ends; DORA RTS applies to financial entities only (OPS-045 is D). No source for machine decommissioning beyond CRA (device-side) and the OIDF whitepaper.
7. No source defines suspension of a user authorisation as distinct from revocation (RTS 1774 gives only the account-lifecycle terms; rb-poa-pox 6.5 vs 6.9 inconsistency from J1 remains).
8. WIMSE draft-08 (workload credentials, async actor chain) is SHOULD-level; not hardened. MCP, A2A and AP2 add nothing beyond existing AIF/NFR items for authority limits.
9. Council compromise texts ST-11829/12824 recital 33 (two or three directors jointly) are recitals; not used. COM(2026) 321 Art 43 may change in trilogue (proposal).

## Caveats
Priorities and cluster tags to be set by ebw-requirements-review. The DORA, EN 319 401 and IDTA items are D because the duty-holder differs from the wallet provider.
