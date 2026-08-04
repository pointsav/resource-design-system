---
title: Empty State Card — Style
---

# Style

Visual design rationale for the empty state card component.

## Token mapping

| Element | Token |
|---|---|
| Border | `{semantic.border-subtle}` |
| Background | `{semantic.surface-default}` |
| Title text | `{semantic.ink-primary}` |
| Body text | `{semantic.ink-secondary}` |
| Inline links | `{semantic.interactive-primary}` |

## Structure

The card border is dashed, not solid — a deliberate visual signal that
distinguishes "empty by design" from a normal bordered surface (e.g.
[Surface](/components/surface/usage)), which uses a solid border.
