# When to use Tab Bar (Disclosure)

Use for in-page tabbed content where all panels should remain reachable
even if JavaScript never loads: tabs are native `<details>`/`<summary>`
elements, progressively enhanced by JS to coordinate "opening one closes
the others" and deep-link via `#fragment`. Without JS, every panel is
still independently expandable — nothing is inaccessible.

**This is not the same component as the tab bar this substrate's own
documentation site already ships.** This site's shipped tab bar implements
the *other* pattern this recipe's own `comparison` field names — `ps-tab`:
real URL-reflected navigation, one
route per tab (`/{section}/{slug}/{tab}`), rendered as plain `<a href>`
links. Use `ps-tab` (the existing, shipped pattern) for multi-page
documentation where each tab is genuinely a separate page worth its own
URL and browser-history entry — exactly what this app's own Usage/
Style/Code/Accessibility tabs need. Use `ps-tab-bar-disclosure` (this
component) instead when the content lives on one page and there's no
routing layer to reflect tab state into a URL.

## When to use

- In-page sections that read acceptably as sequential `<details>` blocks
  even before JS runs (FAQ-style panels, a settings page's grouped
  sections).
- Contexts where a URL-per-tab isn't available or desirable (an embedded
  widget, a single static page with no router).

## When not to use

- Multi-page documentation where each tab is a real, separately
  linkable/bookmarkable page — use `ps-tab` instead (this substrate's own
  component pages are the reference example).
- Content where losing tab state on page reload would be confusing —
  `ps-tab-bar-disclosure`'s state lives in the DOM, not the URL, so a
  reload resets to the zero-JS default (all panels independently
  expandable, not necessarily "tab 1 selected").
