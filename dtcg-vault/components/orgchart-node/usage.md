# When to use Org Chart Node

Use Org Chart Node to represent one entity in a print-first
ownership/hierarchy diagram — an absolutely-positioned content box
on a fixed 1056×816px canvas (US Letter landscape). This is not a
web-fluid layout component; every node renders at a fixed pixel
position, matching how these diagrams are actually produced and
printed for regulatory/investor-relations use.

## Shape families

| Variant | Use for | Shape |
|---|---|---|
| **Rectangle** | Standard operating/holding entity | Solid border, one of 5 role colors |
| **Rectangle — tall** | Board-level or managing entity | 145px height |
| **Rectangle — short** | Asset or subsidiary entity | 80px height |
| **Rectangle — compact** | Dense-layout variant | 160×60px |
| **Pill** | Fund vehicle / limited partnership | Always dashed border, 250px wide, fully rounded |
| **Ellipse** | Cross-border flow-through entity | Dashed/dotted border, rounded |

## Entity-role colors

6 role colors are wired today (green/blue/purple/orange/grey/yellow)
from the registry's 9-role `primitive.color.orgchart.*` palette — see
[Tokens](/tokens#primitive) and the [Org Charts](/products/org-charts/overview)
product page for the real Carbon-token gap analysis behind this
color set. The remaining 3 reserved roles are not yet wired into a
node variant.

## Anatomy

- **Title** — entity name, 12px bold.
- **Alias** (optional) — italic secondary line, e.g. a trade name.
- **Node number** — bottom-of-box reference number tying the node to
  a supporting schedule.

## Behaviour

Print-first, static component — no interaction states, no motion.
Each node carries `role="group"` with `aria-label` naming the entity
and its node number; the SVG connector layer between nodes is
`pointer-events: none` and needs no ARIA annotation of its own.

## Open questions

Whether the short-radius and rounded administrative-entity variants
should consolidate into one modifier, or stay distinct for different
subcategories — not yet decided.
