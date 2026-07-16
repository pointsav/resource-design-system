<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">3 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">An SVG overlay layer that draws the directed connection lines
between org chart nodes. It sits beneath the node boxes on the canvas and carries no
semantic content of its own — every line ends in an arrowhead whose fill matches the
source box's border colour, so the diagram reads correctly in print without relying on
the connector to convey meaning.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/orgchart-connector/recipe.json</code></div>
</div>

## When to use Org Chart Connector

Use Org Chart Connector to draw the relationship lines in a print-first
ownership/hierarchy diagram. It is a single absolutely-positioned `<svg class="svg-layer">`
that overlays the [Org Chart Canvas](/components/orgchart-canvas/usage) and renders directed
paths from one [Org Chart Node](/components/orgchart-node/usage) to another. The connector is
`pointer-events: none` and `z-index: 1` — it draws beneath the node boxes, not over them, so
the labelled boxes always stay legible where a line meets a box.

This is not a general-purpose diagramming primitive. It exists to serve the fixed
1056&times;816px (US Letter landscape) org-chart layout described on the
[Org Charts](/products/org-charts/overview) product page. Node positions are authored at
fixed pixel coordinates; the connector paths are drawn to match.

## Variants

The connector ships three path shapes. Each is one SVG `<path d="…">` string; the variant is
determined entirely by the path geometry, not by a CSS class.

| Variant | Path form | Use for |
|---|---|---|
| **Vertical drop** | `M x1 y1 L x1 y2` — same x, different y | A straight parent-to-child line where both boxes share a horizontal centre. |
| **Horizontal run** | `M x1 y1 L x2 y1` — different x, same y | A straight sibling-to-sibling or side link where both boxes share a baseline. |
| **L-shape** | `M x1 y1 L x1 ymid L x2 ymid L x2 y2` — two legs with a shared midpoint | An offset parent-to-child line that steps across before dropping down. |

All three are static geometry. This is a **static, print-first component with no interaction
states** and no motion — there is nothing to hover, focus, or animate.

## Tokens

The connector is tokens-backed: stroke and arrowhead-marker fill are driven by the
`primitive.color.orgchart.*` role palette rather than hard-coded colours. The recipe wires six
role colours:

- `{primitive.color.orgchart.green}`
- `{primitive.color.orgchart.blue}`
- `{primitive.color.orgchart.purple}`
- `{primitive.color.orgchart.orange}`
- `{primitive.color.orgchart.grey}`
- `{primitive.color.orgchart.yellow}`

Each connection's `stroke` and its `marker-end` arrowhead `fill` are set to the **source
box's border colour** — the same role colour the originating node carries — so a line reads as
belonging to its parent entity. In CSS these resolve to the `var(--ps-orgchart-*)` custom
properties (for example, `var(--ps-orgchart-green)` in the reference recipe). See
[Tokens](/tokens#primitive) for the primitive palette and the
[Org Charts](/products/org-charts/overview) product page for the role-colour mapping shared
with [Org Chart Node](/components/orgchart-node/usage).

## Anatomy

- **`<svg class="svg-layer">`** — one absolutely-positioned overlay per canvas, sized to the
  full 1056&times;816px canvas, `pointer-events: none`, `z-index: 1`.
- **`<defs>` / `<marker>`** — one arrowhead marker definition per role colour in use. The
  reference recipe defines `arrow-green` with a triangle `path` filled by the matching role
  token; a connection references it via `marker-end="url(#arrow-green)"`.
- **`<path>`** — one path element per connection, `fill="none"`, `stroke-width="2"`, coloured
  by the source box's role token, ending in the matching arrowhead marker.

Rendering fidelity is tuned for print: the SVG uses `shape-rendering: geometricPrecision`, the
straight connector `path` elements use `crispEdges`, and marker paths return to
`geometricPrecision` so arrowheads stay smooth.

## Accessibility

The connector overlay carries **no semantic information** and is marked `aria-hidden="true"` on
the `<svg>` element. The hierarchy of the chart is conveyed through the spatial layout of the
labelled [node boxes](/components/orgchart-node/usage) — each of which names its entity and node
number — not through the connector lines. Because the lines are decorative reinforcement of a
structure already stated by the boxes, hiding them from assistive technology is correct: it
avoids announcing meaningless path geometry.

Colour is never the sole carrier of meaning here. A connector's colour echoes its source box's
role colour, but the relationship itself is expressed by the geometric connection between two
labelled boxes, and the box labels state the entities in text. The component targets
**WCAG 2.2 AA**.

## Dependencies

Org Chart Connector depends on [Org Chart Node](/components/orgchart-node/usage) (its
`registry_dependencies`) for the box positions and role colours it draws between and inherits
its stroke colours from, and is composed onto the
[Org Chart Canvas](/components/orgchart-canvas/usage) as the underlying overlay layer.

## Open questions

None recorded in the recipe at this time.
