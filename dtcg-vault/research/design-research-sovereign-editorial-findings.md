# Sovereign Editorial — token/component registration

Registers 6 items recommended by project-knowledge's Phase 2→6 wiki redesign
(2026-06-20 to 2026-06-29) into this design system. Source draft:
`clones/project-knowledge/.agent/drafts-outbound/design-research-sovereign-editorial-findings.draft.md`
(DESIGN-RESEARCH-sovereign-editorial-knowledge-wiki). No content edits — values
copied verbatim from the implemented CSS in `app-mediakit-knowledge/static/style.css`,
live on documentation.pointsav.com, projects.woodfinegroup.com, corporate.woodfinegroup.com.

## What was registered

1. **Surface token set** (dark mode) — `tokens/editorial-surface/editorial-surface.dtcg.json` `surface.*`
2. **Category tile accent palette** (7-color oklch) — same file, `category-tile.*`
3. **Footer token set** — same file, `footer.*`
4. **Pull-quote component** — `components/pull-quote/guide.md`
5. **Slides component** — `components/slides/guide.md`
6. **Per-tenant `[data-instance]` accent pattern** — same file, `brand-accent.*` group,
   documented once (per the source draft's ask) rather than per-engine

## Not registered / follow-up

- The slides component's engine-local tokens (`--sp-*`, `--radius-*`, `--text-*`,
  `--border`, `--bg-subtle`, `--fg-1`/`--fg-3`/`--fg-4`) are not yet aliased to this
  design-system's canonical spacing/radius/type-scale primitives — flagged as a known
  gap in `components/slides/guide.md`, not fabricated here.
- `slide-deck.js` (90 lines, first-party) is referenced from
  `app-mediakit-knowledge/static/slide-deck.js`, not inlined or vendored — it has no
  canonical design-system home yet.
- Engine adoption: `app-mediakit-knowledge` implements these directly (design-system
  registration was pending, now closed by this commit); `app-mediakit-marketing` and
  `app-mediakit-distributions` have not adopted the design system at all yet
  (per source draft §7) — that adoption work is out of scope here.
