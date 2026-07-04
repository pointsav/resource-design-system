---
title: Code Block With Copy — Style
---

# Style

Token references resolve from the active theme. The component never
hardcodes a colour, font, or spacing value.

## Token Mapping

| Element | Token |
|---|---|
| Block background / text | `{semantic.surface-code}` / `{semantic.ink-code}` |
| Copy button hover state | `{semantic.interactive-ghost-hover}` |

## Structure

The copy button (`.ps-code-block__copy`) is positioned inset within the
block and fades in on hover/focus rather than persisting at full opacity —
this keeps dense pages of stacked code blocks from feeling button-heavy
while still surfacing the affordance the moment a reader's attention (mouse
or keyboard focus) lands on a given block.
