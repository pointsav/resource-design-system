---
title: Chip Row — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA.

## Semantic variant meaning

No variant conveys its meaning through color alone: every chip carries a
visible text label prefix (`{{label}}`) ahead of its value, so a warning or
success chip reads correctly even to a user who cannot perceive the accent
color.

## Role

Chips are presentational by default — inline text, no role override. If a
consuming context makes a chip interactive (e.g. a toggleable filter), it
must add `role="checkbox"` or `role="button"` with `aria-pressed`; the base
recipe does not assume interactivity and must not have a role forced onto
static usage.

## Contrast

Label and value text resolve from `{semantic.ink-secondary}` /
`{semantic.ink-primary}` against `{semantic.surface-raised}` — both meet the
AA 4.5:1 minimum against the tenant surface.
