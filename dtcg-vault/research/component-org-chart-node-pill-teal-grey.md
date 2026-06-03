# DESIGN-RESEARCH — org-chart-node-pill teal + grey modifier variants

> Source: project-orgcharts session 2026-06-01. Committed to design-system 2026-06-03.
> ai_consumption_hint: rationale for two new pill modifier classes in nodes.css.
> carbon_baseline: Carbon Tag component (pill shape semantics).

## Context

`nodes.css` has one pill shape — `.org-token-pill` (amber, dashed border, direct-hold /
SPV role). The Bencal Organization_JW2 and SPV2_JW2 org charts introduced two
additional pill uses with inline ad-hoc classes (`.token-teal-pill`, `.token-grey-pill`).
This research record formalises those patterns as canonical design-system modifier classes.

## Component

- **Base class:** `.org-token-pill` (existing — amber, dashed)
- **New modifiers:** `.org-token-pill--teal`, `.org-token-pill--grey`
- **Location:** `components/nodes.css`
- **Guide:** `components/org-chart-node-pill/guide.md`

Both modifiers override only `background`, `border-color`, and `border-style`.
All dimensions, border-radius, padding, and interior zone structure are inherited
from the base `.org-token-pill`.

## Design decisions

**Dotted vs dashed border:** The existing amber pill uses `dashed`. The two new
variants use `dotted`. This is a semantic distinction observed across all four
Bencal charts: `dotted` signals a pass-through or unresolved relationship;
`dashed` signals a direct-hold structure. Encoding the distinction in border-style
(not just color) provides a second visual channel that survives greyscale print.

**Token values:**
- Teal: `--wf-teal: #005D5D` (IBM Carbon Teal 70), `--wf-teal-tint: #9EF0F0` (Carbon Teal 20)
- Grey: `--wf-grey: #6B7280` (existing), `--wf-grey-tint: #e9ecef` (existing)

Teal tokens were added to `theme-woodfine.css` in the same session (2026-06-03).
Grey tokens were pre-existing.

**Contrast ratios (estimated):**
- Teal `#005D5D` on white: ~7.5:1 (WCAG AA large text)
- Grey `#6B7280` on white: ~4.6:1 (WCAG AA)
Both meet WCAG 2.2 AA for border/visual indicator purposes.

## Research trail

### Done

1. Confirmed `nodes.css` had no teal or grey pill modifiers before this commit.
2. Confirmed `--wf-grey` / `--wf-grey-tint` already existed in `theme-woodfine.css`
   — grey pill ships without any token dependency.
3. Confirmed Bencal charts use the same dotted style consistently for both
   teal and grey variants — treated as intentional semantic differentiation.

### Suggested

1. Verify dotted / dashed semantic encoding is documented in org-chart authoring
   guide when that guide is produced.
2. Evaluate whether `--sm` modifier is needed for teal/grey pills in dense layouts.

### Open questions

None blocking. Token dependency (teal) resolved in same session.
