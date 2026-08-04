---
title: Edit On Github Link — Style
---

# Style

Visual design rationale for the edit-on-github-link component.

## Token mapping

- Link text: `{semantic.interactive-primary}`
- Visited/secondary state: `{semantic.ink-secondary}`

## Structure

A single inline `<a>` element (`ps-edit-link` class) — no container, no icon
by default. If an icon is added later, it renders before the label and is
sized to the label's cap height, matching the pattern used elsewhere in the
substrate (e.g. Button's optional leading icon).
