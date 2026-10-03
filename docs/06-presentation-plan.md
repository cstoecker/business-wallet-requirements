# 06 — 30-slide presentation: structure, audience and the future skill

Status: DRAFT concept for approval. Following the Spherity deck workflow, nothing is designed until this concept is approved. Formats: HTML, PowerPoint and PDF from one source.

## 1. Audience and intent

Policy makers (what it is, what it changes, what is open), researchers (concepts, sources, gaps), implementers (architecture, protocols, requirements, conformance), business leaders (where it applies, what to do). External deck. The deck summarises the site and links every slide to the concept or page it comes from. Slot length to be confirmed (30 slides suit about 45 minutes plus discussion).

## 2. Concept: one line per slide, with the master it uses

Masters: M1 title, M2 section divider, M3 content (and its approved specialisations), M4 quote, M5 closing. One sub-brand accent for the whole deck (proposal: EIDA, identity and wallet).

| # | Slide | Master | Audience focus | Source page |
|---|---|---|---|---|
| 1 | European Business Wallets: requirements from law to conformance | M1 | all | home |
| 2 | Why legal-person identity matters now | M3 | policy, business | Legal and compliance |
| 3 | Agenda | Agenda | all | |
| 4 | Foundations | M2 | | |
| 5 | What the EBW proposal (COM(2025) 838) says | M3 | policy | Legal and compliance |
| 6 | Core functions: identify, sign and seal, store, deliver, mandate | CardGrid | all | Requirements |
| 7 | Who is involved: owner, provider, representative, public bodies | M3 | policy, implementers | Concepts |
| 8 | Status and timeline: what is a proposal, what can change | Roadmap | policy, business | Roadmap |
| 9 | EBW and EUDI Wallet: how they differ and connect | M3 | all | EBW and EUDIW interaction |
| 10 | Architecture | M2 | | |
| 11 | Three planes: trust, control, data (Figure) | M3 | implementers, researchers | Concepts |
| 12 | Trust plane: trust lists and discovery | M3 | implementers | Trust list |
| 13 | Control plane: policy engine and mandates | M3 | implementers | Control plane |
| 14 | Data plane and verifiable evidence | M3 | researchers, implementers | Data plane, Evidence graph |
| 15 | Levels of assurance and qualified trust services | M3 | policy, implementers | Levels of assurance |
| 16 | Perspectives | M2 | | |
| 17 | B2B: counterparties, mandates, contracts | M3 | business | Perspectives |
| 18 | B2G reporting: authenticate, authorise, report | M3 | policy, business | B2G reporting |
| 19 | B2G registries and authority access | M3 | policy | B2G registry obligations |
| 20 | B2C: consumers, representatives and the EUDI Wallet | M3 | policy, business | EBW and EUDIW |
| 21 | Ecosystems | M2 | | |
| 22 | Data spaces: Catena-X, Manufacturing-X, energy data-X and DSP/DCP | CardGrid | implementers, business | Ecosystem |
| 23 | Digital Product Passports and CIRPASS-2 | M3 | policy, business | EBW and DPP |
| 24 | WE BUILD: what the pilot tests | M3 | all | Ecosystem |
| 25 | Trusted AI: agent mandates and accountability | M3 | researchers, business | Trusted AI |
| 26 | Method | M2 | | |
| 27 | From law to conformance check: the traceability chain (Figure) | M3 | researchers, implementers | Methodology |
| 28 | What each audience can do next | CardGrid | all | |
| 29 | Open questions and gaps | M3 | policy, researchers | per concept |
| 30 | Join the discussion | M5 | all | Contact, Discussions |

Quote slide (M4) only if a named person with a role agrees to be quoted. Imagery: figures from the site; no invented imagery; no decoration.

## 3. Production pipeline (one source, three outputs)

1. **Source:** `deck/slides.yml` (slide, master, title, body points, figure ID, source page, speaker notes, audience tags). Content is derived from published concept and ecosystem pages, not retyped.
2. **HTML:** 1280×720 slides on the approved masters with Spherity tokens, keyboard navigation, speaker notes, one URL per slide for citation.
3. **PDF:** print stylesheet and headless Chromium, 16:9, text at least 24px at 1920-wide equivalent.
4. **PowerPoint:** built from the same YAML with the Spherity template (python-pptx or the pptx skill), editable text and native shapes, figures as SVG/PNG.
5. **Checks:** 30 slides, one emphasis per slide, text size, footer on every slide, brand review, claim check against the site, internal-only slides excluded, accessibility (reading order, alt text, contrast).

## 4. Specification of the future skill "ebw-deck"

Pre-flight (audience, slot, internal or external), concept in Markdown with approval gate, source-bound slide text, figure reuse from the figure registry, build to HTML/PPTX/PDF, brand review and compliance check, export of PDF only when requested, and a changelog that records which site version the deck summarises. It re-runs when concept articles are published so the deck can be refreshed.
