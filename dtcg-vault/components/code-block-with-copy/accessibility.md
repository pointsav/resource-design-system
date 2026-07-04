---
title: Code Block With Copy — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA.

## Conformance status

| Criterion | Level | Status |
|---|---|---|
| 2.1.1 Keyboard | A | Pass — copy button is a native `<button>`, reachable via Tab |
| 2.4.7 Focus Visible | AA | Pass — copy button carries the substrate's standard focus ring |
| 4.1.2 Name, Role, Value | A | Pass — `aria-label="Copy to clipboard"` on the button |
| 4.1.3 Status Messages | AA | Pass, when implemented per below — the "Copied" state change must be announced without moving focus |

## Screen reader behaviour

The copy button's `aria-label` updates from "Copy to clipboard" to "Copied
to clipboard" for the 1.4-second confirmation window, then reverts. This
label swap is sufficient for the state change to be announced on next focus,
but because the button doesn't move focus itself, a screen reader user who
isn't currently focused on the button won't hear the confirmation — pair the
label swap with `aria-live="polite"` on a visually-hidden status node if the
copy action needs to be confirmed to a user who triggered it via a
non-focus-moving method (unlikely here, since activation requires focus,
but worth stating explicitly since the underlying `aria` guidance in this
component's own recipe flags it).

## Reduced motion

The visible/fade-in-on-hover transition for the copy button should respect
`prefers-reduced-motion: reduce` by resolving to an instant show/hide rather
than a fade, consistent with the substrate's motion-respect commitment.

## Anti-patterns

- **Button never receives visible focus.** If the fade-in-on-hover
  treatment is implemented as `opacity: 0` with no `:focus-within` rule on
  the parent block, a keyboard user tabbing through the page cannot see
  where focus is. The button must become visible on focus, not just hover.
- **No fallback for restricted clipboard contexts.** Some embedded/sandboxed
  iframe contexts block `navigator.clipboard`; silently failing with no
  fallback and no error state leaves the user unsure whether the copy
  worked.
