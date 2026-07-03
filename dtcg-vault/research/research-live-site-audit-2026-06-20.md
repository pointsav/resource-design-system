# Live-site design audit → 10x direction (2026-06-20)

Registers the 2026-06-20 browser-in-the-loop audit from project-knowledge (a 50-agent
Opus 4.8 swarm: a 5-agent research pass built a 43-dimension rubric; a dependency-free
CDP capture screenshotted and machine-checked every published page of all five live
sites at four viewports — 833 pages, 100% of each site's inventory — for horizontal
overflow and WCAG via axe-core; 35 persona agents plus 4 securities-regulator agents
(BCSC, SEC, CNMV, CNBV) audited from the real screenshots; 3 anchor advocates + a judge
chose the aesthetic; 2 agents synthesized). Source:
`clones/project-knowledge/.agent/drafts-outbound/research-live-site-audit-2026-06-20.draft.md`.
Full companion report: `.agent/audit/2026-06-20/REPORT.md` (scorecard, punch-list,
regulator review, screenshots index) in project-knowledge.

## Scope note — overlaps with two already-landed audits; not a duplicate

This is a distinct audit from [`wiki-institutional-redesign.md`](wiki-institutional-redesign.md)
(2026-06-03, a 9-agent Opus browser audit of the same 5-site wiki portfolio, already
master-cosigned on `--color-interactive`/body/nav sizing) and from
[`knowledge-platform-rewrite-analysis.md`](knowledge-platform-rewrite-analysis.md)
(2026-06-04, a 3-instance UX audit of `app-mediakit-knowledge` specifically). This
2026-06-20 audit is broader (50 agents, all five live sites including the marketing
engine, plus a 4-jurisdiction regulator review) and later — a future design pass
reconciling wiki-chrome findings should read all three together rather than treat
this as the sole source.

## The verdict in one line

These are **not "near hyperscaler" — they are pre-seed-grade execution wearing a
competent home page** (overall scores 1.4–2.1 / 5 across every lens). The gap is not
taste and not five separate problems: it is two engines (wiki = `app-mediakit-knowledge`;
marketing = `app-mediakit-shell`) that **share zero CSS** and **ignore the complete,
AAA-grade `pointsav-design-system` that already exists**.

## The single highest-leverage action

**Adopt this design system's DTCG tokens as the ONLY text/background/spacing source
in both engines, and give both engines one shared, constrained, responsive chrome.**
One per-engine pass retires the visual, brand, accessibility, and securities-regulator
findings simultaneously — because every P0 is a defect in shared chrome + hand-rolled
CSS, not in content.

What this design system needs to produce/ratify for that to be possible:

1. **An AAA neutral ramp wired as the single text/bg source**, with every muted /
   footer / meta / link token gated ≥ 4.5:1. The audit measured ~3,087 color-contrast
   violation nodes and ~2,713 `aria-hidden-focus` nodes — almost all from pale-gray
   hand values in the two stylesheets. Token adoption clears them at the root.
2. **A constrained editorial reading-measure token** — body locked to 60–75ch /
   max-width 680–720px, `margin-inline:auto` — plus an `overflow-wrap:anywhere` rule
   for H1 so long slug-titles wrap instead of shattering.
3. **A real breakpoint ladder token set** (≥320 → ultrawide) to replace the wiki
   engine's 3 ad-hoc breakpoints and dead 600–768px zone, and the marketing engine's
   legacy 140px fixed paddings (use `clamp()` side padding on an 8px grid).
4. **One disciplined accent** (navy) on the AAA neutral ramp — reserved for primary
   action/links/status only; the disclosure/FLI banner stays neutral.
5. **A shared chrome recipe** (masthead + footer + landmark scaffold: exactly one
   `<main>`, one de-slugged human `<h1>`, skip-link, `<html lang>` EN/ES, restored
   zoom) consumed by both engines and every route (home, article, search).

## Recommended aesthetic anchor (judge decision)

**Editorial authority — Bloomberg/FT register:** serif display heads + sans body on a
strict constrained column, a confident multi-track grid, ruled dividers, tabular data
treatment, one disciplined navy accent on a near-black-on-near-white AAA neutral ramp.
Grafts the chrome-vs-prose discipline from "bold brand-led," and the "reserved single
accent / disclosure-banner-stays-neutral" rule from "restrained institutional." It
satisfies the Goldman/regulator credibility lens and the knowledge-wiki surface and
aligns with the house Bloomberg article standard, while making disclosure
legible-by-default (the regulators' core finding was that safe-harbour text exists but
is rendered illegible by the breakage). It is also the lowest-risk path — it leans on
type, rule, and measure rather than imagery/motion the brand can't yet supply.

### Per-engine application

- **Wiki article shell (flagship P0):** `display:grid; grid-template-columns:
  minmax(0,1fr) 14em` with the prose track first and `min-width:0`; the "On this
  page" TOC becomes a real in-flow sticky sibling (≥1024px) that collapses to a
  static disclosure < 600px. Today the fixed 14em TOC floats over the H1 and the
  prose column starves to a one-word-per-line ~50–60px sliver on every desktop
  article — and because `scrollWidth===clientWidth` it never showed as "overflow,"
  so only the agents looking at screenshots caught it.
- **Marketing interior `/page/*`:** replace the fixed 1440px canvas + 140px paddings
  with a fluid `margin-inline:auto` + `clamp()` container and a real ≤768px
  single-column collapse for masthead / address grid / footer (`min-width:0` on the
  legal block). Today these clip 538–769px off-screen at tablet and the footer
  shatters to a one-word-per-line ribbon forcing sideways scroll on contact/disclaimer.

## Accessibility = design-system obligation, not a content fix

The axe debt is structural and repairable in the token + chrome pass: contrast
(token-gated), missing landmarks/H1 (shared chrome scaffold), `aria-hidden-focus`
(apply `inert`/`tabindex=-1` on interactive descendants of hidden containers),
restored zoom (viewport meta), table/`<pre>` wrapped in keyboard-focusable
`overflow-x:auto` regions.

## Open questions for the designer

1. **Serif display face:** which family for the Bloomberg/FT register, and is a
   variable font in-budget vs. the system serif stack (sovereignty vs. consistency —
   ties to the `token-knowledge-wiki-baseline` DESIGN-TOKEN-CHANGE Master co-sign
   question)?
2. **Per-tenant differentiation:** how much may the shared chrome diverge between
   PointSav and Woodfine (wordmark + accent only, or a controlled theme layer)? The
   audit found the corporate `/search` route leaking PointSav/monorepo dev chrome
   onto the Woodfine issuer domain — per-tenant identity must be a system-enforced
   band, not an accident.
3. **Disclosure/FLI banner token:** amber vs. neutral register for the
   forward-looking-information notice under BCSC posture (carried from prior token
   work).

## Sequencing (unanimous across personas, regulators, and all three anchor advocates)

Ship the shared-engine P0 grid/landmark/contrast/reflow/overflow fixes first (they
make pages render and clear most axe debt), then layer the editorial brand chrome.
Brand register must never delay legibility — every persona and every regulator walks
on the broken grid regardless of type pairing. Add 320/768/1440 screenshot regression
assertions as part of the P0 work so fixed-width chrome cannot silently re-break.

*(Engineering of the above happens in the two monorepo engines under
project-knowledge after operator sign-off — Phase 2. This document is the
design-system substrate ask: tokens, type system, shared-chrome recipe, contrast
gating.)*
