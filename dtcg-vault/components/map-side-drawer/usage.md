# When to use Map Side Drawer

Use Map Side Drawer to show detail for a single selected map feature
— a persistent right-side panel that slides in on click and stays
visible while the map underneath remains interactive. It replaces
the popup-on-marker pattern, which forces the map to lose context
every time a visitor inspects a feature.

Reference implementation: live at gis.woodfinegroup.com (v0.1.94).

## Variants

| Variant | Description |
|---|---|
| **Default** | Single-feature detail — the current, shipped GIS use. |
| **Comparison** | Split drawer showing two features side-by-side, for federated cluster comparison. Decision pending, not yet built. |

## Anatomy

- **Header** — brand-family badge, feature title, close button.
- **Facts list** — address, NAICS code, year opened (definition
  list: term/value pairs).
- **Cluster context** (hidden by default) — surfaces when the
  feature belongs to a retail cluster: cluster ID, anchor count,
  max radius.

## Behaviour

Slides in at 340px width from the inline-end edge, 250ms entrance
easing (collapses to a plain opacity fade under
`prefers-reduced-motion`). `role="complementary"` with
`aria-label` naming the feature type; `aria-modal="false"` since the
map stays interactive underneath. Tab cycles within the drawer while
open; Escape dismisses it and returns focus to the map canvas.

## Open questions

- Whether the drawer should expand to full width below 640px or
  keep its 340px overlay width on small viewports — not yet decided.
- Comparison variant's exact layout (two drawer columns vs.
  split-screen with the map between) is pending cluster-comparison
  feature work.

## When not to use

This is a map-context detail panel, not a generic modal or sidebar
— for those, see the substrate's Modal Dialog and TOC Sidebar
components.
