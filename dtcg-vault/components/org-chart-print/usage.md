<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print/PDF-safe corporate-relationship diagram for
WeasyPrint-rendered securities documents — parent/subsidiary/affiliate boxes connected by
percentage-labeled edges, color-coded by entity role, on a fixed-pixel canvas forced onto
its own dedicated page. Generalized from the Mexico FIBRA prospectus org chart so any DHS
jurisdiction's chart can be authored from it without Mexico-specific content.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/org-chart-print/recipe.json</code></div>
</div>

## What this template is

`org-chart-print` is neither prose nor a table — it's an absolutely positioned
box-and-arrow diagram that has to survive one specific, unforgiving rendering path:
WeasyPrint → PDF, inside a house prospectus stylesheet it does not control. None of the
other Paper components describe a positioned-canvas figure, and every gotcha below is a
collision between a positioned SVG/box canvas and the surrounding print machinery —
invisible to a component that only ever emits flowing `<p>`/`<table>` content.

Reference implementation: the `.oc-figure` block in the Mexico FIBRA prospectus's
"Relaciones Intercorporativas" exhibit (project-documents, 2026-07-22/23). Every default
token value on this page is that reference's own real, delivered value — not invented.

## The core insight — author at final size, never `transform: scale()` a canvas

The tempting build is one oversized canvas at "screen" dimensions, shrunk to fit the print
column with `transform: scale(0.65)` on a `position: relative` container. **Don't.**

The Mexico chart's original defect looked like clipping or blur — it wasn't. At 300dpi the
scaled chart rendered crisply. The real defect was **fragile, non-deterministic page
placement**:

- A `transform: scale()`-ed, absolutely-positioned, fixed-height canvas enters page flow as
  one non-splittable block with no `break-before`/`break-after` control. Whether it fits
  below the preceding prose depends entirely on how much prose happens to precede it —
  edit the copy above it and placement changes.
- The scale factor couples two unrelated jobs — fitting the column width and choosing a
  readable type size — into one number. Shrinking the box for the column also shrinks the
  type; the Mexico embed authored at 12/10/9px printed at an effective ~7.8/6.5/5.85px.
- The coupled magic numbers (a scale factor, a canvas width, a column width) must be
  hand-edited together every time, and **had already drifted** in production before the
  fix — one embed used a different scale factor than the standalone snippet it was copied
  from.

**The pattern this component mandates instead:**

1. **Author every box at its final printed pixel size. No `transform: scale()` anywhere.**
   Nothing is scaled at render time, so there are no coupled numbers to keep in sync and
   font sizes mean what they say. `{paper.semantic.org-chart.canvas-width}` (680px in the
   reference) is a real fixed-pixel width, boxes sit at their true print coordinates, type
   is set at 11.5/9.5/8.5px — bigger and clearer than a scaled original would be.
2. **Force the figure onto its own dedicated page** with `break-before: page;
   page-break-before: always;` on the `<figure>` — reusing the house `.section-break`
   convention. Placement becomes deterministic and independent of preceding prose.
3. **`overflow: visible` on the canvas and every box.** `overflow: hidden` is a
   silent-clipping risk if any label runs a line long; with `visible`, an over-long label
   just makes its box slightly taller — it never silently disappears.

## Variants

| Variant | Role |
|---|---|
| **box-node** | `display:block .oc-box`, absolutely positioned at true print coordinates, up to five optional stacked zones (title/code/alias/legal/country). Never flexbox — WeasyPrint won't wrap long text inside a flex node whose overflow isn't a clipping value. |
| **role-band** | Modifier class selecting the role color: `role-green`/`role-blue`/`role-orange`/`role-grey` (solid-border square) or `role-vehicle` (dashed rounded oval, trust/SPV shape). Roles are consumer-defined per document. |
| **edge** | One `<svg class="oc-lines">` layer holding right-angle-routed `<path>` connectors with per-role arrowhead `<marker>` defs. |
| **edge-label** | A translate-centered box at each edge's midpoint, over a white background, carrying the relationship semantics (ownership %, admin/beneficiary role). |

## Geometry is generated, not hand-arithmetic'd

The reference implementation's box/edge coordinates were computed by a generator script
(`gen_orgchart.py` + `render_files.py` in project-documents), not authored by hand. For a
chart with a different node count, hand-placing absolute coordinates and SVG paths is the
hardest, most error-prone step — and exactly the kind of coupled-hand-maintained-numbers
problem the core insight above warns against elsewhere (the canvas dimensions already have
to agree across three places: the canvas container, the SVG layer, and the SVG `viewBox`).
**Start from a generator, not from hand-editing a delivered chart's HTML/CSS.**

## Three gotchas, named so they aren't rediscovered the hard way

**gotcha-flexbox-minwidth-nowrap.** A flex item's default `min-width: auto` resolves to its
content's intrinsic width whenever `overflow` is `visible`; combined with an
absolutely-positioned flex column, WeasyPrint let long entity titles overflow sideways
instead of wrapping. Fix: `display: block` boxes only, ordinary block `<p>` zones — never
flexbox for node content.

**gotcha-host-justify-override.** A global house rule like `p { text-align: justify }`
directly matches every `<p>` this component emits once embedded in a host stylesheet — a
direct match always beats a value merely *inherited* from a parent's `text-align: center`,
regardless of specificity. Fix: set `text-align: center` **explicitly on every text class**
(`.oc-title`, `.oc-legal`, `.oc-code`, `.oc-alias`, `.oc-country`) — never rely on
inheriting it. Any portable snippet dropped into a host document must not rely on inherited
values for anything a host generic selector might match.

**gotcha-canvas-width-vs-page-margin.** The canvas width must fit the host page's content
column, and the margin ceiling is a function of that width — not a fixed universal number:

```
required_content_column_width_in  ≥  canvas_width_px / 96
max_side_margin_in                ≈  (page_width_in − canvas_width_px / 96) / 2
```

For the Mexico geometry (680px canvas) that ceiling is ~0.7in — **0.625in is the house
value that happens to satisfy it, not a floor.** A chart with a wider or narrower canvas,
or a different page size, has a different ceiling; compute it from the actual canvas width
and `@page` geometry before assuming a chart fits.

## Role colors — consumer-assigned per document, not one fixed legend

`{paper.semantic.org-chart.role-green}` / `.role-blue` / `.role-orange` /
`.role-grey-border` + `.role-grey-edge` / `.role-vehicle` ship the Mexico FIBRA reference's
own real values as defaults, not a mandatory palette. A new jurisdiction's chart may assign
its own role-to-color mapping — the class names are structural (which role band a node
belongs to), not locked to these exact hexes.

**Deliberately distinct from `theme-woodfine.css`'s own `--wf-*` chart palette** (the
separate Client A org-chart family, its own real deliverable with its own
separately-approved role colors, e.g. `--wf-green: #198038` vs. this component's
`role-green: #54924E`) — confirmed during the 2026-07-30 chart-color reconciliation that
these are two different real charts with two different real color choices, not drift to
reconcile into one value.

**Grey is the one role whose border and edge-ink deliberately differ:**
`role-grey-border` (`#9CA3AF`) borders the box; `role-grey-edge` (`#374151`, noticeably
darker) fills the SVG arrowhead and edge stroke — a border-matched grey arrow reads too
faint against the page. Every other role's border color doubles as its own arrowhead fill
directly.

## Accessibility

- The `<figure>` carries a `<figcaption>` naming the exhibit ("Figura 1. Relaciones
  intercorporativas — …"). Node text is real text, not rasterized — selectable and
  screen-reader-legible in the PDF.
- The SVG edge layer is decorative relationship routing and may be `aria-hidden` — but the
  relationship semantics (who owns what %, who administers whom) must *also* be stated in
  the surrounding prospectus body prose. Never encode a legally required disclosure only in
  an arrow.
- WCAG 2.2 AA: role color is a secondary cue only — every node is independently identified
  by its own text (name + code + role alias), so the role banding never carries meaning by
  color alone. Verify node-text-vs-fill contrast for any new role color before adopting it.

## Print output and motion

Print-first static exhibit — no interaction states. Renders to PDF via
`bin/build-pdf.py` (WeasyPrint). `bin/build-docx.py` is out of scope: pandoc drops inline
SVG, so connector lines do not survive into Word (a pre-existing limitation, not a
regression) — the box zones degrade to plain paragraphs. Treat this component as
PDF-primary. Verify after any change by rebuilding the containing document and confirming
with `pdfplumber` that the figure occupies its own page with its caption, and that the
following top-level section still opens on its own fresh page immediately after.

(An interactive drag-and-drop chart *editor* exists separately in project-documents' IR
tooling — a distinct authoring artifact, not this component and not prospectus body
content.)

## Open questions

- **oq-2 — distribution shape.** This component's CSS is embedded inline in the host HTML
  (deliberately, so the portable snippet is self-contained and its scoped classes travel
  with it) — differing from `legal-prospectus`'s external-link convention. Same
  cross-cutting question already flagged in that component's own usage guide; not resolved
  here.
- **oq-3 — second-variant threshold.** A hierarchical, no-percentage layer-tree variant is
  not pre-defined. Recommend waiting until a real document needs one.
- **oq-5 — a third node shape.** A plain rounded-rectangle (`border-radius: 12px`) appeared
  once in the reference for a single node, distinct from both the square role bands and the
  dashed vehicle oval. Not yet promoted to a named modifier — treat as a one-off until a
  second real case justifies `.oc-rounded`.

## Related

- [Legal Prospectus](/components/legal-prospectus/usage) — the Canadian NI 41-101 sibling this exhibit type is most often embedded inside.
- [Mexico FIBRA Prospectus](/components/mx-fibra-prospectus/usage) — the delivering document this component's reference implementation was extracted from (Section 4.4).
- [Tokens — Paper tier](/tokens#paper) — the full leaf-token list backing this template.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/org-chart-print/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/org-chart-print-token-map.md</a>
</div>
