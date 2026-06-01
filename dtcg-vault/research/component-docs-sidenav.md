# component-docs-sidenav — Design Rationale

**ai_consumption_hint:** Left navigation sidebar for product-documentation pages.
Use `class="docs-sidenav"` on the `<nav>` element with `aria-label="Documentation navigation"`.
Category sections use native `<details>`/`<summary>` — no JS needed for expand/collapse.
Active link: add `class="docs-sidenav__link is-active"` and `aria-current="page"`.
Server must set `open` attribute on the `<details>` whose category contains the active page.
Width token: `--sidenav-w: 256px`. Hidden below 1024px via `display: none`.

**Origin:** project-knowledge DESIGN-COMPONENT (2026-06-01) · `source_commit: 914cd836`  
**Recipe:** `components/docs-sidenav/guide.md`

---

## What problem this solves

Product-documentation surfaces need persistent left navigation that shows the full
content hierarchy at a glance, lets readers jump across categories without returning
to a homepage, and does not require JavaScript for basic open/close behaviour.

IBM Carbon's Side Nav was evaluated and rejected: it carries icon slots, multi-level
nesting, and 256px fixed-rail width designed for enterprise app shells. The corpus is
a documentation wiki without per-article icon assignments. Carbon's pattern would
impose icon maintenance overhead for no reader benefit.

The pattern observed across Stripe docs, Vercel docs, and Cloudflare docs (all surveyed
2026-06-01) is: uppercase category labels with article link lists inside collapsible
sections. The implementation at `app-mediakit-knowledge` commit `914cd836` follows
this pattern.

---

## Key decisions

**`<details>`/`<summary>` over JS accordion.** Native elements work without JS,
are keyboard-navigable by default (Enter/Space), and carry correct implicit ARIA
semantics (`aria-expanded` is managed by the browser). The chevron animation is
CSS-only via the `[open]` attribute selector — no state management code.

**`--sidenav-w: 256px` as a CSS token.** Width extracted to a custom property so
the shell grid and any future sidenav-aware components (mobile drawer, etc.) share
the same measurement without hardcoding.

**Active category auto-expanded server-side.** Server adds `open` attribute on
the `<details>` whose category matches the current article's category slug. Avoids
the flash-of-collapsed-nav that JS-based lazy expansion causes on initial page load.

**No icons.** Stripe, Vercel, and Cloudflare docs all include icon slots for brand
identity. Omitted here: content corpus is a documentation wiki; icons would require
per-article assignments not in the current content schema.

**`display: none` below 1024px, not a drawer.** No sidenav-exclusive content —
all articles are reachable via breadcrumb. Hiding rather than collapsing to a
drawer keeps the mobile layout simple. A drawer pattern is a future option if
content volume grows past breadcrumb navigability.

---

## Token dependencies

- `--sidenav-w` — column width (defined in this component; consumed by `.shell` grid)
- `--header-h` — sticky top offset (defined in wiki chrome)
- `--fg-1`, `--fg-2`, `--fg-3`, `--fg-4` — foreground scale
- `--link` / `--navy` fallback — active link and border accent
- `--bg-hover`, `--bg-subtle` — hover and active backgrounds
- `--rule` — right-border and divider
- `--font-display` / `--font-body` fallback — category label typeface

---

## Open questions

1. **Mobile drawer.** `display: none` below 1024px is the current decision.
   A hamburger-triggered drawer would require an additional component and JS state.
   Deferred pending content volume.
2. **Hierarchy depth.** One category level is the current maximum. Nested categories
   would require a different pattern (recursive `<details>` or a new component).
   Deferred pending content structure decision.
