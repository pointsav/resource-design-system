---
title: Tab Bar (Disclosure) — Code
---

# Code

## Dependencies

- Primitives: color, spacing, border
- Assets: none (zero-JS baseline works without a script; JS is a
  progressive enhancement layer, not a requirement)

## HTML recipe (zero-JS baseline)

```html
<div class="ps-tab-bar" role="tablist">
  <details class="ps-tab" open>
    <summary class="ps-tab__summary">{{tabLabel}}</summary>
    <div class="ps-tab__panel">{{content}}</div>
  </details>
  <!-- repeat one <details class="ps-tab"> per tab; only ONE should carry
       the `open` attribute in the zero-JS default state -->
</div>
```

Every panel is independently expandable via native `<details>` behavior
with no script at all — this is the fallback, not a degraded state.

## JS coordination layer

Per the recipe's own `js_notes`: on open, close sibling `<details>`
elements so only one panel is expanded at a time (true tab behavior).
Deep-linking: read `window.location.hash` on `DOMContentLoaded`, open the
`<details>` whose id matches, and scroll it into view.

```js
document.querySelectorAll('.ps-tab-bar .ps-tab').forEach((detail) => {
  detail.addEventListener('toggle', () => {
    if (!detail.open) return;
    document.querySelectorAll('.ps-tab-bar .ps-tab').forEach((sibling) => {
      if (sibling !== detail) sibling.open = false;
    });
  });
});

const hash = window.location.hash.slice(1);
if (hash) {
  const target = document.getElementById(hash);
  if (target && target.matches('.ps-tab')) {
    target.open = true;
    target.scrollIntoView();
  }
}
```

**Only after this script runs successfully** should `role="tablist"` /
`role="tab"` / `role="tabpanel"` / `aria-selected` / `aria-controls` be
applied (see Accessibility) — synthesising tab roles before the
coordinating JS is present breaks screen readers, since the native
`<details>` semantics would then be masked by roles the markup doesn't
actually behave like yet.
