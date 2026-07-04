---
title: Preview Frame — Style
---

# Style

Token references resolve from the active theme; the frame never hardcodes a
colour value directly.

## Token Mapping

| Element | Token |
|---|---|
| Canvas surface (light) | `{semantic.surface-default}` |
| Border | `{semantic.border-subtle}` |
| Canvas surface (dark) | `{semantic.surface-inverse}` |
| Canvas text (dark) | `{semantic.ink-on-inverse}` |

## Structure

The container carries `data-theme="light"` or `data-theme="dark"`; CSS rules
scoped to `[data-theme='dark']` override the surface-palette tokens on the
canvas. The toolbar sits top-right, above the canvas, and does not scroll
with previewed content.
