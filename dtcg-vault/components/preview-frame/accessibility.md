---
title: Preview Frame — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA.

## Conformance status

| Criterion | Level | Status |
|---|---|---|
| 4.1.2 Name, Role, Value | A | Pass — each toggle is a native `<button>` with `aria-pressed` reflecting state |
| 2.4.7 Focus Visible | AA | Pass — toggles inherit the substrate's standard focus ring |
| 1.4.11 Non-text Contrast | AA | Pass — border and toggle states meet 3:1 against both light and dark canvas surfaces |

## Keyboard interactions

| Key | Behaviour |
|---|---|
| Tab | Move focus between the two theme toggle buttons, then into the previewed canvas content |
| Space / Enter | Activate the focused toggle, switching the canvas theme |

## Screen reader behaviour

The frame itself is not a landmark — it is a visual container, per the
recipe's own `aria` note. Content placed inside `.ps-preview__canvas` must
carry its own appropriate landmark/heading structure; the frame does not
supply one. Each toggle announces as "Light, button, pressed" or "Dark,
button, not pressed" (or the reverse), so the active theme is discoverable
without relying on visual state alone.

## Notes if the canvas content is itself sandboxed (iframe)

If a consumer nests a sandboxed `<iframe>` inside the canvas (matching the
pattern this substrate's own live component preview uses — see Code tab),
ensure the iframe carries a descriptive `title` attribute and that keyboard
focus can both enter and exit the frame normally; never trap focus inside
it. `sandbox="allow-same-origin"` without `allow-scripts` (this substrate's
own choice) means the framed content cannot register its own focus traps,
which is the safer default.
