---
schema: foundry-design-research-v1
component_or_token: browser-tab-title
decision_type: cross-site-convention
authored: 2026-07-12
authored_by: totebox@project-design
authored_with: claude-sonnet-5
status: ratified
source: direct-observation (relayed from project-marketing, ratified by command@claude-code 2026-07-12) + cited external precedent
ai_consumption_hint: "Browser-tab title formatting convention for every Woodfine/PointSav property: home page renders the brand token alone (no separator, no page word); sub-pages render '{Page Title} — {brand token}' using an em dash, not a pipe. The brand token keeps the property descriptor (e.g. 'PointSav Design System', 'PointSav Software'), never a bare company name, since several family tabs may be open at once. A real SVG favicon is part of the same standard on every page. This is a naming/string convention, not a visual component — no recipe.json/CSS exists for it."
---

# Browser Tab Title Convention

Cross-site convention for `<title>` formatting and favicon presence across every
Woodfine/PointSav property. Ratified 2026-07-12 (`command@claude-code`, following a
proposal from `project-marketing`'s mobile audit of home.woodfinegroup.com /
home.pointsav.com). Captured here because it is a real, reusable pattern any site in
the family can reference from one canonical source instead of re-deriving it — but it
is a naming convention, not a themed UI component, so it has no `recipe.json`/CSS
counterpart the way `site-footer` or `attribution-badge` do.

## The rule

- **Home page:** brand token alone. No separator, no page word.
  Example: `PointSav Software`
- **Sub-page:** `{Page Title} — {brand token}`, using an **em dash** (—), not a pipe (|)
  or hyphen (-).
  Example: `Products — PointSav Software`
- **Brand token** keeps the property descriptor, not a bare company name —
  `PointSav Design System`, `PointSav Software`, `PointSav Documentation`, etc. With
  several family tabs open at once, a bare company name on every tab is undiscriminating.
- **Real SVG favicon** (`<link rel="icon" type="image/svg+xml" href="...">`) is part of
  the same standard on every page — do not assume it is already present; verify.

Drop-in template for any `render_page()`-equivalent head-builder:

```
title = page_title ? f"{page_title} — {brand_token}" : brand_token
```

## Why an em dash, not a pipe

Sourced from real precedent (GitHub Docs, Stripe, Google Docs, Apple, Microsoft Learn)
plus SEO data: Google rewrites pipe separators in search-result titles roughly 41% of
the time, versus roughly 20% for dashes. A Semrush A/B test found dash-separated titles
drove roughly 9% more organic clicks than pipe-separated ones. (Figures as relayed in
the ratifying message — re-verify against the original sources before citing externally
in a public-facing document; this file records the design decision and its rationale,
it is not itself the primary source.)

## Verification against this codebase

`app-privategit-design`'s own `render::shell()` (`templates/shell.html` +
`src/routes/browse.rs`) already implements this pattern: sub-page titles render as
`{label} — PointSav Design System` (em dash, real token), the home page renders the
bare brand token (`PointSav Design System`), and a real SVG favicon
(`/static/favicon.svg`) is already wired on every page. No change was needed on
design.pointsav.com's own implementation when this convention was ratified — confirmed
by direct inspection, 2026-07-12.

## Reference implementations

- `home.pointsav.com`, `software.pointsav.com` — cited by the ratifying message as
  live reference implementations of this exact pattern.
- `design.pointsav.com` (`app-privategit-design`) — independently already compliant
  (see above).

## Scope note

This is deliberately not a `recipe.json` component: it has no markup shape or CSS to
formalize, only a string-formatting rule and a favicon presence requirement. Sites
adopting it should implement the drop-in template directly in their own head-builder,
citing this file as the canonical source of the convention.
