---
title: Sidebar Accordion — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA (per the recipe's own `wcag.target`).

## Conformance notes

- **Landmark:** the whole tree is wrapped in `<nav aria-label="…">` so
  screen-reader users can jump straight to section navigation. Do not nest
  a second `<nav>` inside it — the recipe's own guidance is explicit on
  this point.
- **Current location:** `aria-current="page"` marks the active link. Only
  one link in the entire tree should carry it at a time.
- **Keyboard:** every link is a native `<a>`, so Tab/Shift+Tab and Enter
  work with no additional scripting.
- **Color independence:** the active state is communicated by background
  fill *and* the left-border indicator *and* `aria-current`, not by color
  alone.

## If a future pass adds real accordion (collapse) behavior

The current recipe has no expand/collapse mechanism — it's a static list
(see Usage). If that's added later, follow the pattern this app itself
already established (P1.7 fix, `app-privategit-design`): a collapsed
section must be removed from the tab order (`visibility:hidden`), not just
visually hidden with `max-height:0` — the earlier version of this app's own
sidebar had exactly this bug (collapsed links stayed focusable). The toggle
control needs `aria-expanded` reflecting current state and
`aria-controls` pointing at the id of the region it opens (the
`ul.ps-sidebar__list` for that section).

Keyboard for the disclosure trigger follows the standard WAI-ARIA
disclosure pattern: Tab/Shift+Tab moves focus to the trigger like any
other focusable control; Enter and Space both toggle it (expand if
collapsed, collapse if expanded). Panel content — the links inside
`ul.ps-sidebar__list` — joins the page's normal Tab order only while
`aria-expanded="true"`; while collapsed, those links must not be
reachable by Tab at all (this is the `visibility:hidden` requirement
above, not `display:none`, so the region can still be targeted by
`aria-controls` and measured for animation without exposing its
contents to keyboard or assistive-technology traversal).
