# Releases

Real, dated changes to this design system's server and token graph.
Unlike a version-numbered product changelog, this page tracks what
actually shipped and when — not an invented release-number history.

## 2026-07-15

- **Added** — Paper and Writing token pillars wired into the token
  gallery (`/tokens`) end-to-end: 185 → 381 tokens (Paper 164, Writing
  32). Both now have real CSS custom properties in `tokens.css`
  (276 variables, including decomposed typography composites), not
  just JSON/gallery-only data.
- **Added** — Paper nav entry (was missing entirely); Knowledge
  Platform, GIS, and Org Charts product-line pages (this section).
- **Fixed** — mobile navigation previously disappeared entirely below
  1300px viewport width with no replacement. Ported a JS-free
  hamburger/drawer mechanism.
- **Fixed** — a real WCAG AA contrast failure on the Critical button's
  resting-state color (4.44:1, below the 4.5:1 floor) — shifted to
  `color.critical-60` (7.33:1). See `components/button/accessibility.md`
  for the full writeup.
- **Changed** — card hover treatment now includes a lift (translateY +
  elevation shadow), not just a border-color change.

## Earlier

Real component and token history before this date lives in each
component's own recipe/changelog metadata (`dtcg-vault/components/*/recipe.json`)
and this repository's git history — not duplicated here as an
invented version-number timeline.
