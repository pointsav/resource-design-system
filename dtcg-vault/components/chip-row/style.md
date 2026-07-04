---
title: Chip Row — Style
---

# Style

Visual design rationale for the chip row component.

## Token mapping

| Element | Token |
|---|---|
| Chip surface | `{semantic.surface-raised}` |
| Label prefix text | `{semantic.ink-secondary}` |
| Value text | `{semantic.ink-primary}` |
| Primary variant accent | `{semantic.interactive-primary}` |
| Warning variant accent | `{semantic.status-warning}` |
| Success variant accent | `{semantic.status-success}` |

## Structure

Each chip is `inline-flex`, constrained height, consistent border-radius —
the label prefix renders in the monospace face to visually distinguish it
from the value it precedes.
