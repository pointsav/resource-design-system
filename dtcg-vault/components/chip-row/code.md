---
title: Chip Row — Code
---

# Code

## Dependencies

- Primitives: color, spacing, corner-radius, typography (mono face for the
  label prefix)
- Assets: none

## HTML + CSS recipe

```html
<div class="ps-chip-row">
  <span class="ps-chip"><span class="ps-chip__label">{{label}}</span>{{value}}</span>
</div>
```

Variant modifiers append to the base `ps-chip` class: `ps-chip--primary`,
`ps-chip--accent`, `ps-chip--neutral`, `ps-chip--warning`, `ps-chip--success`.
The default variant uses the bare `ps-chip` class with no modifier.

## Provenance

This component originated during the BIM showcase build (2026-04-29): discovered
to be domain-agnostic while building it, then generalized into the shared
substrate rather than staying BIM-specific.
