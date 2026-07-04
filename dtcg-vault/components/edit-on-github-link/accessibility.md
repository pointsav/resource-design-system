---
title: Edit On Github Link — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA.

## Conformance notes

- A real `<a>` element, not a styled `<div>` or `<span>` with a click handler
  — keyboard-focusable and correctly announced as a link by default.
- Link text is a full, descriptive phrase ("Edit this page on GitHub"), never
  a bare "click here" or "edit" — meets 2.4.4 Link Purpose (In Context) and
  reads correctly out of context in a screen-reader links list.
- If a decorative icon is added, it must carry `aria-hidden="true"` so it
  isn't announced separately from the link text.
- Opens in a new tab (`target="_blank"`) — consider pairing with visually
  hidden text or an icon indicating "opens in a new window," since 3.2.5
  (Change on Request, AAA) recommends warning users before a context change
  they didn't request.
