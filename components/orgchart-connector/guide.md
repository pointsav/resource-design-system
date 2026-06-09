---
schema: foundry-doc-v1
title: "Component Guide — Org Chart Connector"
slug: guide-component-orgchart-connector
category: design-system
type: reference
quality: complete
status: active
audience: internal
bcsc_class: internal-only
language_protocol: DESIGN-COMPONENT
carbon_baseline: none
accessibility_targets: [wcag-2-2-aa, pointer-events-none]
last_edited: 2026-06-06
editor: project-orgcharts
source_commit: dabe5000
---

An SVG overlay layer that renders directed connection lines between org chart nodes. Sits at `z-index: 1` beneath node boxes. Each connection ends with an arrowhead marker whose fill matches the source box's border color.

## HTML Recipe

```html
<!-- SVG overlay — full canvas size, zero pointer events -->
<svg class="svg-layer" xmlns="http://www.w3.org/2000/svg"
     width="1056" height="816" viewBox="0 0 1056 816"
     aria-hidden="true">
  <defs>
    <!-- One marker per color in use on this canvas -->
    <marker id="arrow-green"
            viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#54924E"/>
    </marker>
    <marker id="arrow-blue"
            viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#164679"/>
    </marker>
    <marker id="arrow-purple"
            viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#7C468C"/>
    </marker>
    <marker id="arrow-orange"
            viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#F15F22"/>
    </marker>
    <marker id="arrow-grey"
            viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#9CA3AF"/>
    </marker>
    <marker id="arrow-yellow"
            viewBox="0 0 10 10" refX="10" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#EAB308"/>
    </marker>
  </defs>

  <!-- Straight vertical connector from green source box -->
  <path d="M 528 350 L 528 464"
        fill="none" stroke="#54924E" stroke-width="2"
        marker-end="url(#arrow-green)"/>

  <!-- L-shaped connector (horizontal then vertical) from green source -->
  <path d="M 175 350 L 175 420 L 528 420 L 528 464"
        fill="none" stroke="#54924E" stroke-width="2"
        marker-end="url(#arrow-green)"/>
</svg>
```

## CSS Recipe

```css
/* SVG connector overlay — covers entire canvas */
.svg-layer {
  position: absolute;
  top: 1px;          /* empirical subpixel alignment correction — do not remove */
  left: 3px;
  width: 1056px;
  height: 816px;
  pointer-events: none;   /* clicks pass through to node boxes beneath */
  z-index: 1;
}

/* SVG render quality — critical for print sharpness */
svg          { shape-rendering: geometricPrecision; }
path         { shape-rendering: crispEdges; }
marker path  { shape-rendering: geometricPrecision; }
```

## Connector authoring rules

**Color rule:** Connector stroke and arrowhead fill = border color of the **source** box (the box the connection originates from), not the destination. This makes connection ownership immediately readable at a glance.

**Marker naming:** `arrow-[color-name]` — one marker per color in use on the canvas. Declare only the markers you use; unused markers add no visual overhead but clutter the SVG.

**Path routing:**
- Vertical drop: `M x1 y1 L x1 y2` — same x, different y
- Horizontal run: `M x1 y1 L x2 y1` — different x, same y
- L-shape: `M x1 y1 L x1 ymid L x2 ymid L x2 y2` — two legs with shared midpoint
- All coordinates are in canvas coordinate space (0,0 = top-left of `.print-canvas`)

**Attachment points:**
- Top center: `(left + width/2, top)`
- Bottom center: `(left + width/2, top + height)`
- Left center: `(left, top + height/2)`
- Right center: `(left + width, top + height/2)`
- Pill attachment uses the same center points — the visual border curves but the geometry is rectangular

**Hit-detection padding:** If implementing interactive connector selection, use `PAD = 30` — a 30px proximity threshold to the path geometry.

## Accessibility

The SVG overlay carries no semantic information. Add `aria-hidden="true"` to the `<svg>` element. The structural hierarchy is conveyed through the spatial layout of labelled node boxes, not the connector lines.
