---
title: Tab Bar (Disclosure) — Style
---

# Style

Token references resolve from the active theme.

## Token mapping

| Element | Token |
|---|---|
| Active accent (selected tab, once JS-enhanced) | `{semantic.interactive-primary}` |
| Panel/summary background | `{semantic.surface-default}` |
| Dividers between tabs | `{semantic.border-subtle}` |
| Label text | `{semantic.ink-primary}` |

## Structure

- Root: `div.ps-tab-bar[role="tablist"]` (role added only once JS confirms
  it can coordinate the tabset — see Accessibility)
- Each tab: `details.ps-tab`
- Trigger: `summary.ps-tab__summary`
- Panel: `div.ps-tab__panel`

Compare against this site's own shipped `ps-tab` pattern — a plain
link-based nav, not `<details>`. The two components solve different
problems (see Usage) and are not meant to share a token namespace or
markup shape, even though both now draw from the same `--ps-*`
custom-property prefix.
