---
title: Empty State Card — Code
---

# Code

```html
<div class="ps-empty-state">
  <h2 class="ps-empty-state__title">{{title}}</h2>
  <p class="ps-empty-state__body">{{body}}</p>
  <div class="ps-empty-state__links">{{links}}</div>
</div>
```

## Dependencies

- Primitives: color, typography (display + body), spacing, border
- Assets: none
- No JavaScript — the card is a static container. If it replaces a live
  region on state change, the surrounding page owns the `aria-live` wiring
  (see Accessibility).
