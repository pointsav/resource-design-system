---
title: Sidebar Accordion — Code
---

# Code

## Dependencies

- Primitives: color, spacing
- Assets: none
- No JavaScript required for the current (static) recipe — a future
  accordion/collapse variant would add a toggle script.

## HTML recipe

```html
<nav class="ps-sidebar" aria-label="Section navigation">
  <section class="ps-sidebar__section">
    <h2 class="ps-sidebar__heading">{{sectionLabel}}</h2>
    <ul class="ps-sidebar__list">
      <li>
        <a class="ps-sidebar__link ps-sidebar__link--active" aria-current="page" href="{{href}}">
          {{label}}
        </a>
      </li>
    </ul>
  </section>
</nav>
```

Repeat the `section.ps-sidebar__section` block once per named category.
Only one link across the whole tree should carry `aria-current="page"` at
a time — the currently active view.

## Notes on nesting

Wrap the whole tree in a single `<nav aria-label="…">` landmark. Do not
nest additional `<nav>` elements inside — sub-groupings should be plain
`<section>`/`<ul>` structure, matching the flat recipe above, not a second
navigation landmark.
