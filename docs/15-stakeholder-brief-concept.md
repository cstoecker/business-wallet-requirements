# Stakeholder brief: concept for the 20 to 30 key requirements

Status: concept for discussion, not yet built. Audience: Industry 4.0 (Plattform Industrie 4.0, Manufacturing-X), IPCEI-AI, IDTA (AAS and digital product passport work). Purpose: agree which architecture questions matter, not to present the whole catalogue (795 requirements, 118 at priority P1).

## What the stakeholders need to decide

Each group meets the European Business Wallet (EBW) from a different side. The brief should show the same 10 themes through three lenses.

| Group | Main interest | Typical question |
|---|---|---|
| Industry 4.0 and data spaces | Wallet as identity and authorisation layer for machine and company interaction across supply chains | Can the EBW replace or complement ecosystem identifiers (BPN, domain-specific) and connector credentials? |
| IPCEI-AI | Agents acting for companies, mandates, verifiable agent identity, machine-readable data | Can an agent hold or use a mandate, and who is liable? |
| IDTA | Asset administration shell, submodels, product passport, signed data | Which credential format carries AAS-related claims, and what stays outside the wallet? |

## Selection rule (reproducible, not editorial)

1. Start from priority P1 (118 requirements).
2. Keep wallet-general and business-wallet-specific items; drop provider-side-only and EUDI-profile-only items unless a decision depends on them.
3. Per cluster with a decision page (DEC-01 to DEC-11), keep the 2 to 4 requirements that most constrain the options: those that conflict with each other, or that exclude an option.
4. Add the open conflicts flagged in review (for example EBWOID versus selective disclosure, provider log access versus data minimisation, unit attestation visibility).
5. Cap at 30. Every selected item shows source, legal status (in force, proposal, standard, ecosystem) and provenance (L, S, D, A). Derived items (D) are labelled as derivations.

The selection is generated from the review data (`_data/review/requirement-review.yml`) by a script, so it can be rerun when the catalogue changes.

## Grouping: 10 decision themes instead of 18 clusters

18 clusters are too many for a 90 minute session. Group them by the decision they drive.

| Theme | Clusters | Decision pages | Question for the room |
|---|---|---|---|
| 1. Who is the wallet subject | K02 | DEC-02 | Employee in a personal EUDI Wallet, in the EBW, or both? |
| 2. Delegation and mandates (employees, machines, agents) | K03, K16 | DEC-13 | How do people, machines and agents get authority to act for the organisation, and how is it limited, delegated onward, shared, suspended, revoked and attributed? |
| 3. Formats and meaning | K01, K16 | DEC-01, DEC-10 | JSON-LD, SD-JWT VC, mdoc, AAS: which for which claim, and how is it machine-readable for agents? |
| 4. Keys and control | K04 | DEC-03 | Hosted, device, owner HSM or remote seal? |
| 5. Identity across borders | K06, K17 | DEC-05, DEC-11 | Primary and secondary identifiers, EBWOID, EUID, LEI, BPN: what maps to what? |
| 6. Trust and discovery | K05, K14 | DEC-04 | Which trust lists and ecosystem anchors does a relying party use? |
| 7. Lifecycle and evidence | K07, K10 | DEC-06, DEC-09 | Revocation, suspension, logging, audit without exposing employees |
| 8. Protocols and delivery | K08, K12 | DEC-07 | OID4VCI, OID4VP, DSP, delivery: what must interoperate? |
| 9. Privacy and adoption | K09, K15 | DEC-08 | Minimisation, controller roles, acceptance across ecosystems |
| 10. Planes and evidence graph | K18 (with K01, K10, K16) | DEC-12 | Where are policies decided and enforced, how do data and evidence move, and is one access-controlled linked-data evidence graph with open-world semantics the shared layer for policy, register, product passport and AI processes? |

Theme 9 is the integrating one: K18 (183 requirements, 45 at P1) tags the control-plane and data-plane requirements and the evidence graph concept, and links to themes 3, 4, 7 and 8. K11 (security) and K13 (governance) are shown as constraints on all themes, not as separate topics.

## Format of the brief

One page per theme, same layout, so stakeholders can compare:

1. The question in one sentence.
2. The 3 to 4 selected requirements, each with source, status and provenance.
3. The options, with what each enables and restricts (taken from the decision page).
4. What the sources say and what they are silent on (the gap is often the point).
5. What each stakeholder group would need from the answer (three short lines).
6. One question to decide in the session.

Plus a cover page (scope, how to read status labels) and a one-page map from themes to clusters.

## Output forms

- A page on the site, `architecture/brief/`, generated from the data, printable as PDF.
- A short slide deck (12 to 15 slides: cover, method, 10 themes, conflicts, next steps) to use in the session. The existing presentation plan (`docs/06-presentation-plan.md`) is the larger deck; this brief is a subset.
- A feedback sheet per theme (agree, disagree, missing) that feeds the existing review loop (`scripts/import_review_feedback.py`).

## Risks and how to handle them

- Provider-side and EUDI-profile rules can crowd out the business questions: handled by rule 2.
- Derived requirements can read as law: every D item is labelled and shows its derivation.
- Ecosystem material (Catena-X, IDTA) is preview or draft in places: show the version and status on each item.
- The EBW is not final law: the Council position and the Parliament vote are tracked on the roadmap; the brief states the date of the text it reads.
- AAS is an implementation artefact: only high-level requirements enter, as agreed in the methodology.

## Open points for you

- Which of the three groups should see which themes (all ten, or a subset per group)?
- Session length and language (English assumed).
- Whether the brief should show the Spherity position (recommended option per theme) or stay neutral until after the session. The decision pages currently hold a preliminary reading only.
