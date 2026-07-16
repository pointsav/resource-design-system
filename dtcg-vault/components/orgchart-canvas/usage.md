<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">1 variant</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">The fixed-dimension print canvas that hosts all org
chart node boxes and SVG connector overlays. Sized exactly to US Letter
landscape at 96dpi (11in &times; 8.5in = 1056&times;816px) — it renders as a
white card on screen and fills the page edge-to-edge when printed.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/orgchart-canvas/recipe.json</code></div>
</div>

## When to use Org Chart Canvas

Use Org Chart Canvas as the single root container for a print-first
ownership/hierarchy diagram. Every
[Org Chart Node](/components/orgchart-node/usage) box is absolutely
positioned inside it, and every
[Org Chart Connector](/components/orgchart-connector/usage) line is
drawn on an SVG overlay it hosts — the canvas provides the
`position: relative` coordinate frame both depend on. It is not a
web-fluid layout container: the dimensions are fixed at
1056&times;816px so that on-screen pixel positions and the printed
page are the same coordinate system. See the
[Org Charts](/products/org-charts/overview) product page for how the
three components compose into a full diagram.

## Variants

| Variant | Description |
|---|---|
| **Default** | US Letter landscape at 96dpi, the only supported canvas size. |

There is deliberately no size modifier — a second page size would
fork every node position in a chart. Charts that need more room are
an open sizing question (see below), not a variant.

## Anatomy

- **Canvas** — a `.print-canvas` `div`, 1056&times;816px, filled
  with the surface-base token, `overflow: hidden`, with a soft
  drop shadow (`0 4px 6px rgba(0, 0, 0, 0.1)`) that presents it as
  a card against the surrounding page on screen.
- **Contents** — node boxes and the SVG connector overlay are
  children of the canvas; the canvas itself renders nothing else.

## Print behaviour

The recipe carries the full `@media print` block, so consumers get
correct print output without writing their own print CSS:

- `@page { size: landscape; margin: 0; }` — the canvas fills the
  US Letter page edge-to-edge.
- The on-screen box shadow is removed in print.
- `page-break-after: avoid` keeps the chart on one page.
- `print-color-adjust: exact` (with the `-webkit-` prefix) preserves
  the surface fill and node role colors in print output.

The recipe also sets SVG rendering hints for the connector overlay:
`shape-rendering: geometricPrecision` on the SVG root and on marker
paths (arrowheads), and `crispEdges` on connector paths — so
orthogonal connector lines print sharp while arrowheads stay smooth.

## Tokens

The canvas consumes one token:

| Token | Used for |
|---|---|
| `{semantic.surface-base}` (`--ps-surface-base`) | Canvas background — the white card fill on screen and the page fill in print |

See [Tokens](/tokens#theme) for the semantic layer this resolves
through. Node role colors and connector strokes are tokenized on
their own components, not on the canvas.

## Behaviour

Static, print-first component — no interaction states and no motion.
The canvas clips its contents (`overflow: hidden`); anything placed
outside the 1056&times;816px frame is cut off rather than reflowing,
which is the intended failure mode for a fixed print artifact.

## Accessibility

The canvas itself carries no ARIA role — semantics live on the node
boxes it contains. Each [Org Chart Node](/components/orgchart-node/usage)
provides its own `role="group"` and `aria-label`; the canvas is a
purely presentational positioning frame. Target: WCAG 2.2 AA, per
the recipe.

## Open questions

Node boxes and connectors must fit within the 816px height
constraint. If a chart approaches the limit, canvas height and the
SVG connector overlay's `viewBox` must be reduced together to match
the new content height — the two cannot be adjusted independently.
