<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A floating data-display panel that shows aggregate statistics for the
current filtered map view. Always visible, it updates reactively as filters change —
country chips, family checkboxes — and sits top-right so it never collides with the
map's zoom controls.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/map-stats-panel/recipe.json</code></div>
</div>

## When to use Map Stats Panel

Use Map Stats Panel to keep a running summary of *what the map currently
shows* in view at all times. As a visitor narrows the map with filters,
the panel's counts recompute in place — so the answer to "how much of the
data am I looking at right now?" is always on screen, without a click.

It is a read-only aggregate for the whole filtered view. For detail on a
single selected feature, use the [Map Side Drawer](/components/map-side-drawer/usage)
instead — that panel answers "tell me about *this* one," this panel answers
"tell me about *all* of these."

Reference implementation: live at gis.woodfinegroup.com (v0.1.94). Both
components belong to the GIS product line — see the
[GIS overview](/products/gis/overview) for how they compose on the map surface.

## Variants

The substrate ships four panel variants. All share the same definition-list
grid; they differ only in how many stat cells they carry and how those cells
are arranged.

| Variant | Layout | Use for |
|---|---|---|
| **Default** | 4 cells, 2×2 grid | The current GIS use — Corridors, Anchors, Countries, and Avg cluster grade. |
| **Compact** | 2 cells, horizontal | Single-axis stat dashboards where only two figures matter. |
| **Wide** | 6 cells, 3×2 grid | Federated cluster comparison, where more aggregate dimensions are shown at once. |
| **With sparkline** | Each cell carries a small inline sparkline | Phase-2 use — trend context alongside each figure. |

## Anatomy

The panel is an `<aside>` landmark wrapping a single definition list:

- **Grid** (`.ps-map-stats__grid`) — a two-column CSS grid of stat cells.
- **Cell** (`.ps-map-stats__cell`) — one `<dt>`/`<dd>` pair per statistic.
- **Label** (`.ps-map-stats__label`, the `<dt>`) — an uppercase micro-label
  naming the figure (e.g. *Corridors*, *Anchors*, *Countries*, *Avg cluster grade*).
- **Value** (`.ps-map-stats__value`, the `<dd>`) — the figure itself, in
  large bold type, with a `color` transition so a changed value reads as
  a deliberate update rather than a flicker.

## Positioning

The panel is absolutely positioned over the map container at `top: 16px;
right: 16px` (`top: 1rem; right: 1rem` in the recipe CSS), on `z-index: 5`.
Top-right placement is intentional: it keeps the panel clear of the map's
zoom controls. It has a `min-width` of 160px so counts do not reflow the
grid as their digit-width changes.

## Tokens

Every colour, radius, and spacing value in the recipe resolves through the
token substrate — the panel carries no hard-coded design values except its
drop shadow. From `recipe.json`:

| Token | Tier | Drives |
|---|---|---|
| `semantic.surface.layer` | [theme](/tokens#theme) | Panel background (`--pds-surface-layer`) |
| `semantic.text.primary` | [theme](/tokens#theme) | Stat value colour (`--pds-text-primary`) |
| `semantic.text.secondary` | [theme](/tokens#theme) | Stat label colour (`--pds-text-secondary`) |
| `semantic.border.subtle` | [theme](/tokens#theme) | Panel border (`--pds-border-subtle`) |
| `primitive.radius.sm` | [primitive](/tokens#primitive) | Corner radius (`--pds-radius-sm`) |
| `primitive.space.2` | [primitive](/tokens#primitive) | Panel padding, grid row gap (`--pds-space-2`) |
| `primitive.space.4` | [primitive](/tokens#primitive) | Grid column gap (`--pds-space-4`) |
| `primitive.motion.duration.base` | [primitive](/tokens#primitive) | Value colour-change transition (`--pds-duration-base`) |

Because the surface, text, and border values are semantic (theme-tier), the
panel re-skins with the hosting tenant's theme without any component-level
change. The `box-shadow` (`0 2px 8px rgba(0,0,0,0.15)`) is the one literal
value in the recipe — it is not yet tokenised.

## Accessibility

The panel is grounded in the recipe's own `aria` and `wcag` fields:

- **Landmark.** The container is `role="region"` with `aria-label="Map
  statistics"`, so assistive technology can jump to it as a named region.
- **Live updates.** `aria-live="polite"` announces filter-driven count
  changes without interrupting speech already in progress — the visitor
  hears the new figures at the next natural pause rather than being cut off.
- **Semantic pairing.** Each statistic is a `<dt>`/`<dd>` term/value pair
  inside the definition list, so the label and its figure are programmatically
  associated.
- **Spelled-out units.** Where a unit is not implicit, the value carries an
  explicit `aria-label` (e.g. `aria-label="N corridors"`) so a screen reader
  announces "42 corridors," not a bare number.
- **Contrast.** Labels meet 4.5:1 (WCAG 2.2 AA) and values meet 7:1 (AAA)
  against the panel surface. WCAG target for the component is **2.2 AA**.

## Open questions

- Whether the panel should auto-collapse on small viewports (mobile
  &lt;640px) and expand on tap, or always stay visible. Decision pending
  mobile usage telemetry (recipe `oq-1`).

## When not to use

- Do not use this panel for single-feature detail — that is the
  [Map Side Drawer](/components/map-side-drawer/usage).
- Do not use it for figures unrelated to the current map view. The panel's
  contract is that its counts reflect exactly what the filtered map shows;
  putting static or off-view numbers in it breaks that expectation.
