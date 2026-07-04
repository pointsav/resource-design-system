---
title: Tab Bar (Disclosure) — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA, focus-visible required (per the recipe's own
`wcag` field).

## Conformance notes — two distinct accessible states

**Without JS (baseline):** the native `<details>`/`<summary>` interaction
is accessible to every screen reader and keyboard user with zero
additional ARIA. Each panel is independently expandable. Do not add
`role="tablist"`/`role="tab"` in this state — a tablist role implies
exactly one panel is ever visible and that arrow keys move between tabs,
neither of which is true yet without the coordinating script.

**With JS (enhanced):** once the coordination script (see Code) has
confirmed it's running, synthesise the real tabs pattern:
`role="tablist"` on the container, `role="tab"` + `aria-selected` on each
`summary`, `role="tabpanel"` + `aria-controls` linking each panel back to
its trigger. At that point arrow-key navigation between tabs (Left/Right)
should be added to match the WAI-ARIA APG tabs pattern — this is
additional behavior a `<details>` element doesn't provide natively, so
it must be implemented in the same script that adds the roles.

## Keyboard

- **Baseline (no JS):** Tab/Shift+Tab moves between `summary` triggers;
  Enter/Space toggles the native `<details>` open state. This works with
  zero script.
- **Enhanced (JS active):** add Left/Right arrow-key movement between
  tabs once `role="tab"` is applied, per the APG tabs pattern.

## Why this matters more than the always-JS `ps-tab` alternative

This component's entire reason to exist is resilience: if the
coordinating script fails to load (network issue, CSP block, JS disabled),
the content is still fully navigable — nothing is hidden behind a broken
script. `ps-tab` (this app's own shipped pattern) doesn't have this
concern since it's plain server-rendered links with no JS dependency at
all; `ps-tab-bar-disclosure` earns its complexity specifically for
single-page contexts where `ps-tab`'s URL-per-tab model isn't available.
