# RES-J2: key custody candidates (cluster K04, DEC-03)

Date 2026-10-04. File: /tmp/cand/J2-custody.yml (17 candidates, dry run via scripts/import_candidates.py passes, 0 skipped). No new sources: all cited IDs are registered; J2-new_sources.yml not needed. Generator and quote check: /tmp/cand/j2/gen.py (all quotes whitespace-normalised substrings of the cached texts, max 25 words, none fails).

Cached sources reused (from docs/research/dec03-keys-research.md): eIDAS consolidated 18.10.2024 (/tmp/claude-0/s/eidas.txt), COM(2025) 838 and Annex, Council ST 9684/26, ARF HLR, CIR 2024/2981, CSC API v2.0.0.2, ETSI TS 119 431-2. Not re-read: EN 419 241-1/-2 (paywalled), CSC 2.2, full TS 119 432.

## Duplicates skipped (already in _requirements/)
Annex 3(1), 4(1), 5(1), 8, 9(3), 10 (NFR-069..075, 082, TRU-103, FUN-041/050, INT-070/075); Art 26(1), 36(1) (FUN-019/022); Art 29(1a), 29a(1)(b), 30(3a), 39a (NFR-008/009, CER-005/006); Art 7(2) (GOV-002); Council (la) (NFR-042); WUA_16a, WIAM_09/12a/12c/20 (NFR-088..092); QES_15, QES_23 (TRU-115, CER-019); TS 119 431-1 key destruction, activation, session limit (OPS-028/029, NFR-094..097, TRU-114); CIR 2026/1731 key attestation (TRU-116..120); CIR 2024/2981 WSCD (CER-012..017); OPS-017 key destruction on TSP termination.

## Candidates
L/S (new, verbatim-backed): Annex II 1(d) device protection against use by others (L); Art 29a(1)(c) certification report (L); CSC 11.6 numSignatures (S); TS 119 431-2 OVR-B.1-02 seal certificate (S); ARF QES_06 (S, EUDI only); ARF Mig_03 no private keys in migration object (S, EUDI only).
D (11): custody model recorded per key; custody evidence in the self-assessment; provider-held keys used only on owner authority; owner withdraws user access to keys; log names user per key use; key-holding parties and Art 7(2); exit disclosure on key export versus re-creation; replace sealing device or QTSP; owner-operated HSM evidence before activation; recovery after key-holder loss; allocation of responsibility. Each D statement is anchored on a verbatim quote of the nearest source and its rationale names the DEC-03 criterion (C1 to C14).

## Gaps listed, not written as requirements (sources silent)
- Where keys must be held: no EBW text decides hosted, device-bound, owner HSM or QTSP custody. The D items only require recording, evidence and disclosure, not a choice.
- Required assurance level of the WSCD in the Council text (Commission "substantial" clauses deleted); NFR-082 / CER-009 / CER-010 remain Commission-only.
- Whether an owner-operated HSM is a WSCD in the sense of Art 3(29), and who certifies it (EBW-CER-023 is a derived safeguard only).
- Key transfer between providers or QTSPs; how keys held by a delisted provider pass on (Art 6(2)(f), 13(5)(k)).
- Liability allocation for key misuse (EBW-LEG-069 is a documentation duty; legal review needed). ARF Topic AB 4.2 is a discussion paper, not normative.
- Sole-control levels for seals: TS 119 431-1 applies EN 419 241-1 "mutatis mutandis"; the EN was not read, so no requirement quotes SCAL for seals. ARF Topic N and Topic 34 note that a remote-HSM migration inside one provider needs no key export (discussion text, not turned into a duty).
- Multi-user activation of one legal-person seal key (TS 119 431-1 gives one identified natural person per activation).

## Cautions for review
- EBW-FUN-055 (QES_06) and EBW-NFR-118 (Mig_03) are ARF rules for EUDI Wallets; they bind the EBW only if the implementing acts refer to them. Reviewer may demote or drop.
- EBW-INT-088 binds CSC API clients, not the EBW directly; CIR 2026/1731 replaced the CSC reference in Annex IV with TS 119 432.
- EBW-GOV-050 widens Art 7(2) to key custodians: derivation, to verify.
- Stale item EBW-TRU-029 (cites deleted CIR 2024/2979 Art 3(2)) already corrected by its location text; not touched.
- Statuses: draft, reviewer pending. Not written (dry run only); next steps are --write, ebw-requirements-review, changelog.
