---
name: ebw-brand-review
description: Review the European Business Wallet site against the Spherity design system and brand rules (colour, type, shape, motion, icons, layout, voice). Use before releases, after UI changes, or when asked to check design compliance.
---

# Brand review of the site

Canonical rules: the `spherity-design` plugin at https://github.com/spherity/claude-plugins (`spherity-design/skills/spherity-design/reference/hard-rules.md` and `design-system-guide.md`; review axes in `skills/spherity-brand-review/SKILL.md`). In sessions where the plugin is not installed, clone it read-only (`add_repo` for `spherity/claude-plugins`, then read the files) or use the bundled snapshot in the `spherity-compliance` skill. Tokens are in `assets/css/tokens/`; site styles in `_sass/custom/custom.scss`.

## Checks (cite file and line; no general impressions)

1. **Colour:** only token ramps (no raw hex outside SVG figures, and figure hexes must be on the ramps); Petrol primary, Cyan the single accent, status colours only for status; text on Cyan is Petrol; no second accent.
2. **Type:** Archivo and IBM Plex Mono only; body text at least 16 px (mono captions 12 px allowed); H1 36/700, H2 26/600.
3. **Shape and elevation:** radius 8 compact, 12 cards, 16 ceiling; resting surfaces have a border and no shadow; never border and shadow together; overlays may use `--sph-shadow-overlay` without a border.
4. **Layout:** card accent is the 6 px top bar, never a side stripe; two container levels at most; content areas pad 64 px on wide screens; no identical-weight grid where content has hierarchy (note it).
5. **Motion:** durations 80, 120, 220, 350 ms; ease-out; animate only `transform`, `opacity`, `grid-template-rows` (never width, height, padding, margin); a `prefers-reduced-motion` block; focus ring 2 px Cyan with 2 px offset; hover darkens.
6. **Icons:** Untitled UI only (`assets/icons/`, 1.5 px stroke, `currentColor`), 16/20/24 px; no emoji or Unicode glyphs as icons; status by shape as well as colour.
7. **Voice:** no intensity words, at most two em-dashes per piece of body copy, claims literally true, no emoji, English only on this site.
8. **Figures:** straight lines, no wobble, no gradients inside illustrations, SVG metadata present.
9. **Process:** training-crawler permission is not decided (Legal); never change `robots.txt` crawler rules on your own.

## Report

Group by severity: Violation (a hard rule), Off-spec (a token or scale not honoured), Note (judgement). One line each: `file:line - what is wrong -> fix`. Close with the single highest-leverage fix. Fix violations, rebuild, re-check.
