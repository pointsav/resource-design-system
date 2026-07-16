<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Slide-in overlay navigation for compact (≤799px)
viewports. A hamburger trigger opens a full-height left drawer containing the
wiki site nav, and the HTML <code>inert</code> attribute locks the background
DOM while it is open — Tab cannot escape the drawer.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-drawer-mobile-nav/recipe.json</code></div>
</div>

## When to use Wiki Drawer

Use Wiki Drawer as the compact-viewport navigation surface for a
[Knowledge Platform](/products/knowledge-platform/overview) wiki
deployment. At ≤799px the persistent site nav gives way to a
hamburger trigger; activating it slides a full-height drawer in from
the inline-start edge, dims the page behind a backdrop, and renders
the rest of the document inert until the drawer closes. Desktop
users never see it — the trigger is `display: none` above the
compact breakpoint, so there is no desktop variant to design for.

This component is the *wiki engine's* drawer. This documentation
site's own top-nav hamburger (`.nav-toggle`/`.site-nav` in the site
shell) is a conceptually parallel but separate implementation — do
not reach for this recipe to style the design-system site's chrome,
and do not assume the two share markup or class names.

## When not to use

- Do not use it at wide viewports. The drawer only exists at
  ≤799px; a persistent sidebar or top nav is the wide-viewport
  pattern.
- Do not use it as a general-purpose modal or sheet. It is a
  navigation landmark (`<nav aria-label="Site navigation">`), not a
  dialog container for arbitrary content.
- Do not fake the background lock with CSS. `pointer-events: none`
  plus `user-select: none` blocks the mouse but **not** the
  keyboard — it is not a substitute for `inert` (see
  Accessibility below).

## Variants

The drawer has exactly two states, and the recipe treats them as
its two variants:

| Variant | Description |
|---|---|
| **Closed** | Hamburger button only; drawer and backdrop `[hidden]`. |
| **Open** | Drawer slides in; backdrop dims; main content inert. |

There are no size, placement, or emphasis variants — one drawer,
two states.

## Anatomy

Three sibling elements make up the component:

1. **Trigger** — `.ps-wiki-drawer-trigger`, a `<button>` carrying
   `aria-expanded`, `aria-controls="wiki-drawer"`, and a state-aware
   `aria-label` (`Open navigation` / `Close navigation`). Hidden
   above 799px, `display: flex` below.
2. **Backdrop** — `.ps-wiki-drawer-backdrop`, a fixed full-viewport
   scrim (`rgba(0,0,0,0.5)`, `z-index: 100`) that is always
   `aria-hidden="true"` and `[hidden]` while closed.
3. **Drawer panel** — `#wiki-drawer`, a `<nav>` with
   `class="ps-wiki-drawer"` and `aria-label="Site navigation"`,
   fixed to the inline-start edge at `width: min(80vw, 20rem)`,
   `z-index: 101`, vertically scrollable. It holds a
   `.ps-wiki-drawer__list` of `.ps-wiki-drawer__link` items; the
   current page's link carries `aria-current="page"`.

## Behaviour

The recipe's JS contract is deliberately small:

- **On open** — remove `[hidden]` from the drawer and backdrop; set
  `inert` on `#wiki-main-content` and `#wiki-header`; update the
  trigger's `aria-expanded`.
- **On close** — add `[hidden]` back; remove `inert` from
  main/header.
- **Escape key closes. Backdrop click closes.**

The slide is pure CSS: the panel rests at
`transform: translateX(-100%)` and transitions to `translateX(0)`
when `[hidden]` is removed, using
`var(--pds-duration-slow)` with `var(--pds-easing-decelerate)`.
Logical properties (`inset-inline-start`, `border-inline-end`)
keep the drawer on the correct edge in RTL locales.

## Tokens

The recipe binds to these DTCG token paths — semantic surfaces and
text resolve per tenant theme, primitives are shared substrate
values:

| Token | Role |
|---|---|
| [`{semantic.surface.background}`](/tokens#theme) | Page surface behind the backdrop |
| [`{semantic.surface.layer}`](/tokens#theme) | Drawer panel background |
| [`{semantic.surface.layer-hover}`](/tokens#theme) | Link hover background |
| [`{semantic.text.primary}`](/tokens#theme) | Trigger icon colour |
| [`{semantic.interactive.link}`](/tokens#theme) | Drawer link colour |
| [`{semantic.border.subtle}`](/tokens#theme) | Drawer inline-end border |
| [`{primitive.space.2}`](/tokens#primitive) | Trigger/link padding |
| [`{primitive.space.4}`](/tokens#primitive) | Drawer panel padding |
| [`{primitive.motion.duration.slow}`](/tokens#primitive) | Slide-in transition duration |
| [`{primitive.motion.easing.decelerate}`](/tokens#primitive) | Slide-in easing curve |

The backdrop scrim (`rgba(0,0,0,0.5)`) is currently a literal in
the recipe CSS, not a token.

## Accessibility

WCAG target: **2.2 AA** (per the recipe's `wcag` field).

### Trigger semantics

The trigger is a real `<button>` with `aria-expanded` reflecting
state, `aria-controls="wiki-drawer"` naming the panel it controls,
and an `aria-label` that flips between `Open navigation` and
`Close navigation`. The hamburger glyph itself is
`aria-hidden="true"` — the label does the announcing.

### Background lock via `inert`

While open, `inert` is applied to `#wiki-main-content`,
`#wiki-header`, and any other focusable regions. This prevents Tab
from escaping the drawer without a hand-rolled focus trap. Notes
from the recipe's research trail:

- Native `inert` support is ~94% global (as of Aug 2025); iOS
  Safari has it from 15.5+.
- Strategy is **native-first with a conditional WICG polyfill**:
  `if (!('inert' in HTMLElement.prototype))` load the polyfill
  (~3KB gzipped; in maintenance mode since late 2023 but
  functional).
- The CSS-only partial (`pointer-events: none` +
  `user-select: none`) blocks mouse interaction but **not**
  keyboard focus — never use it as an `inert` substitute.

### Landmarks and current page

The drawer is a `<nav aria-label="Site navigation">` landmark. The
backdrop is permanently `aria-hidden="true"` — it is a visual scrim
only. The active page's link carries `aria-current="page"`.

### Keyboard dismissal

Escape closes the drawer, satisfying keyboard users who opened it
by accident; backdrop click covers pointer users.

## Related

- [Knowledge Platform overview](/products/knowledge-platform/overview)
  — the product this component ships in.
- [Home Grid](/components/home-grid/usage) — the wiki home page's
  category-browse surface, from the same Knowledge Platform
  component family.
