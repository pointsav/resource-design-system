# Leapfrog 2030 audit synthesis — home.woodfinegroup.com + home.pointsav.com

Registers the 2026-06-02 browser-in-the-loop audit from project-marketing (three
independent Opus agents — Alpha/accessibility, Beta/design, Gamma/mobile-performance
— synthesised into one prioritised backlog). Source:
`clones/project-marketing/.agent/drafts-outbound/DESIGN-RESEARCH-synthesis-audit-2026-06-02.draft.md`
(+ sibling drafts `DESIGN-RESEARCH-alpha-accessibility.draft.md`,
`-beta-leapfrog2030.draft.md`, `-gamma-mobile-performance.draft.md`, same directory).
Raw evidence: `outputs/audit-2026-06-02/` (24 screenshots, 36 JSON audit files),
`scripts/audit-2026-06-02*.py`, both in project-marketing.

## Scope note — this is a site audit, not a token/component registration

Unlike prior DESIGN-RESEARCH intakes, most findings here are implementation bugs in
`app-mediakit-marketing`'s own markup/CSS (keyboard trap, empty anchor, missing H1,
mobile nav breakpoint), not gaps in this design system's shared primitives. The
`--ink-2`/`--ink-3`/`--accent`/`--paper` tokens the findings reference are local to
`app-mediakit-marketing`'s own `tokens.css` — not yet present in this design system
at all — so the ~17h of P0+P1 remediation is app-mediakit-marketing's own
implementation work, not something to fix here. This document registers the audit
as citable research and answers the open questions routed to project-design;
it does not fold any new tokens into `dtcg-bundle.json`.

## Highest-confidence findings (all three agents agree)

- Keyboard trap — cyclic tab order (WCAG 2.1.2, Level A)
- Mobile nav unusable at 375px
- Nav/footer touch targets 17px, fail WCAG 2.5.5
- 2.4 MB inline HTML bundle — performance crisis (~72% inline WOFF2 font data)
- Missing H1 on both home pages
- All SVGs missing `<title>`

These four (tab loop, mobile nav, touch targets, bundle size) define the minimum
v0.0.2 remediation scope per the source synthesis; ~17h total P0+P1 effort.

## Answers to "Open questions for project-design"

1. **H1 visibility** — hidden (SR-only) for v0.0.2. Ratifies Alpha's recommendation
   over Beta's visible-heading alternative: conflating an accessibility fix with a
   visual hero redesign risks stalling the fast, safe fix. A visible display
   heading can follow in a later dedicated visual pass.
2. **Mobile nav approach** — two-row (Gamma's recommendation), consistent with the
   existing "no hamburger" IA constraint. Full CSS is in the synthesis draft §P0-2.
3. **Font extraction timing** — do P0-7 (font extraction) and P2-3 (variable-font
   consolidation) together in one pass. Doing them separately produces two CLS
   events instead of one; the synthesis draft already makes this case.
4. **Brand differentiation (Woodfine vs PointSav divergence)** — not a project-design
   architecture call; needs an explicit operator decision (this is a brand-identity
   choice, not a technical one). Flagged back to project-marketing/operator, not
   answered here.
5. **Tab-loop root cause** — bundler-side (duplicated `<nav>` DOM) vs template-side
   (`tabindex` on `<body>`) can't be determined from this document; needs inspection
   of the actual bundler output in app-mediakit-marketing. Not resolved here.

## P2 items worth a future design-system generalization (not registered now)

Once `app-mediakit-marketing`'s own token file stabilizes post-remediation, these
P2 items are candidates for promotion into this design system rather than staying
engine-local: dark-mode token mapping (P2-1), `oklch()`-computed brand tint (P2-4),
and the Woodfine/PointSav brand-differentiation token split (P2-7, pending the
operator decision in item 4 above). Not fabricated as tokens here — no stable
values to register yet.
