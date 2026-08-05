---
schema: foundry-design-research-v1
component_or_token: financial-report-layout
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-totebox DESIGN-COMPONENT-financial-report-layout.draft.md (V2, originating_cluster project-proforma) + project-proforma DESIGN-TOKEN-CHANGE-engine-finance-bundle.draft.md + BRIEF-client-a-proforma-engine-recapitalization.md
ai_consumption_hint: "Explicitly a SIBLING of financial-statement-yearend, not the same register: different page geometry (landscape vs. portrait), different density (up to 11 period columns vs. 3), different tone (tinted semantic-row fills vs. pure black-on-white). The dashboard-theme CSS is real and print-tested; the statement-theme's specific token values are PROVISIONAL pending not-yet-implemented Rust engine work — do not treat the two at equal confidence."
---

# Financial Report Layout (Proforma / Projection Dashboard) — token consolidation rationale

> **SUPERSEDED 2026-07-29 — read `component-financial-report-layout.md` §8 first.**
> This file's "dashboard theme (real) vs. statement theme (provisional)" framing
> predates the V5 canonical design audit, which unified both into one applied,
> live-engine-verified system (the live proforma engine). The specific color/rule/
> type values below are pre-V5 and historical only — do not use them for new
> work. The "why a separate recipe from financial-statement-yearend" reasoning
> below is still current and unaffected.

This component's CSS was extracted verbatim from a real, delivered Client B V2 proforma
report — print-tested, genuinely production-grounded. Its companion `engine.finance.*`
token bundle is a separate concern: `BRIEF-client-a-proforma-engine-recapitalization.md`
states the underlying Rust engine work (the classic
`statement` theme) is "planned but deliberately not yet implemented" — that
statement predates V5 landing on the real engine; that renderer
is now confirmed (V8 audit) to be a legitimately separate classic-
statement family, not this component's provisional second theme.

## Why this is a separate recipe, not a variant of financial-statement-yearend

The operator's "one recipe per document family" rule keys on genuine document family,
not just tone. This family and financial-statement-yearend disagree on:

- **Page geometry**: this family is letter landscape (`1.5cm 2cm 1.5cm 1.5cm` asymmetric
  margins); the yearend statement is letter portrait (1in symmetric). This is the
  sharpest divergence — they do not share a page-geometry primitive.
- **Density**: up to 11 period columns (label 22-25%) vs. 3 value columns (label 55%).
- **Tone**: tinted 3-saturation blue semantic-row fills + navy section-banner text vs.
  pure black-on-white, zero fills.
- **Nil glyph and page-number placement**: em-dash `—` / `@bottom-right` here, vs.
  en-dash `–` / `@bottom-center` Notes-only for the yearend statement — both deliberate
  per-family choices, confirmed not to be drift to reconcile.

## What genuinely is shared with financial-statement-yearend

Print-first single self-contained HTML + inline `<style>` (no framework/build),
WeasyPrint as the render target, `table-layout: fixed`, parenthetical negative
formatting, tabular-nums, and the single-rule-then-double-rule subtotal/total
convention (this family's statement theme: 0.75pt then 1pt+3pt-double; the yearend
statement: 0.5pt then 1pt+3pt-double) — modeled as the shared
`paper.primitive.rule.*` group both families draw from.

## Open items

The line-number gutter (32px, Courier New, JS-injected) is a dashboard/screen-only
feature — it does not render in WeasyPrint output and is entirely absent from the
statement theme; it is not a print-domain token, kept as a documented recipe variant
only. The statement theme's exact serif stack and column split remain provisional
until the proforma engine work referenced above actually lands.
