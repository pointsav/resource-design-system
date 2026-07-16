<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A horizontal radiogroup of country chips that filter map
data and fly the viewport to the selected country's bounds. Default state is ALL —
no filter, world view. Selection is single and exclusive; a multi-select variant is
planned but pending its first real use-case.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/country-filter-chips/recipe.json</code></div>
</div>

## When to use Country Filter Chips

Use Country Filter Chips when a map surface offers a small, fixed set
of country scopes and choosing one should do two things at once:
filter the visible map data to that country, and `flyTo` the country's
bounds. The chip row always leads with an **ALL** chip — the default,
unfiltered world view — so there is never a hidden filter state a
visitor cannot see or escape.

This is a [GIS product-line](/products/gis/overview) component.
Reference implementation: live at gis.woodfinegroup.com (v0.1.94). It
pairs naturally with [Map Side Drawer](/components/map-side-drawer/usage),
the other half of the shipped GIS map-interaction pattern.

## Variants

| Variant | Description |
|---|---|
| **Default** | Exclusive selection (radiogroup). The current GIS use. |
| **Multi-select** | Multiple chips active simultaneously. `role="group"` + `aria-pressed` replaces `radiogroup` + `aria-checked`. Decision pending first multi-select use-case — not yet built. |

## Anatomy

- **Container** — a flex row (`.ps-country-chips`) with
  `role="radiogroup"` and an `aria-label` ("Filter by country"),
  wrapping onto multiple lines when the chip set outgrows the width.
- **ALL chip** — first in the row; the default active state,
  meaning no filter applied.
- **Country chips** — one per country, rendered as flag emoji plus
  ISO country code (🇺🇸 US, 🇨🇦 CA, 🇲🇽 MX, 🇪🇸 ES in the reference
  implementation). The flag emoji is supplementary; the ISO code is
  always rendered as the text fallback.

Each chip is a pill-shaped `<button type="button">` — 2.25rem tall
with a 1.125rem radius and a `min-height` of 44px.

## Behaviour

### Selection

Exclusive: activating a chip deactivates the previous one, filters
the map data to that country, and flies the viewport to the country's
bounds. Activating **ALL** clears the filter and returns to the world
view. The selected chip signals state through background, border,
*and* `aria-checked` — never colour alone.

### Keyboard

Tab focuses the group; arrow keys move between chips; Space or Enter
activates. Focus is indicated by a 2px `{semantic.interactive.focus-ring}`
outline with 2px offset.

### Motion

Background and border colour transition over
`{primitive.motion.duration.base}`; under `prefers-reduced-motion:
reduce` the transition is removed entirely.

## Tokens

The recipe consumes six theme-layer and four primitive-layer tokens
— see [theme tokens](/tokens#theme) and
[primitive tokens](/tokens#primitive):

| Token | Role |
|---|---|
| `{semantic.surface.layer}` | Chip resting background |
| `{semantic.surface.layer-hover}` | Chip hover background |
| `{semantic.text.primary}` | Chip label, resting |
| `{semantic.text.on-color}` | Chip label, selected |
| `{semantic.border.subtle}` | Chip border, resting |
| `{semantic.interactive.focus-ring}` | Focus outline |
| `{primitive.color.brand.blue.60}` | Selected background and border |
| `{primitive.space.1}` | Gap between chips |
| `{primitive.space.2}` | Chip horizontal padding |
| `{primitive.motion.duration.base}` | Hover/selection transition |

## Accessibility

The recipe targets WCAG 2.2 AA.

- **Radiogroup semantics.** The container carries `role="radiogroup"`
  with an `aria-label`; each chip carries `role="radio"` and
  `aria-checked` — not `aria-pressed`, because selection is exclusive.
  (The planned multi-select variant is where `aria-pressed` takes
  over.)
- **Not colour alone.** Selected state is conveyed by background,
  border, and `aria-checked` together.
- **Text fallback for flags.** The flag emoji is supplementary; the
  ISO code is always rendered as text, so the chip is legible where
  flag emoji do not render.
- **Touch target.** Every chip has a minimum height of 44px — the
  recipe notes this meets the WCAG 2.2 AAA target-size level, ahead
  of the component's overall AA target.
- **Focus visibility.** `:focus-visible` draws a 2px
  `{semantic.interactive.focus-ring}` outline with 2px offset.

## Open questions

- **oq-1 — Multi-select and the ALL chip.** When the multi-select
  variant is activated, does ALL become disabled or act as
  "clear all"? Decision pending the first multi-select use-case.

Related research: `dtcg-vault/research/zoom-tier-reveal-pattern.md`.

## When not to use

- Do not use for long or open-ended country lists — the chip row is
  a small, fixed scope set, not a search. Beyond a handful of
  countries, a select or type-ahead pattern fits better.
- Do not use for non-exclusive filtering today. The shipped variant
  is a radiogroup; multiple simultaneous selections are the pending
  multi-select variant, not something to improvise with the default.
- Do not use outside a map context. The component's contract couples
  filtering with a `flyTo` viewport change; a plain data-table filter
  has no viewport to fly.
