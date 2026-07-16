<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">5 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A taxonomic swatch that renders a brand-family identifier as a
coloured dot plus a label chip. The visual primitive for the Department / Hardware /
Warehouse Club retail taxonomy — taxonomy-agnostic, so a deployment extends it through a
runtime taxonomy file rather than a code change.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/brand-family-swatch/recipe.json</code></div>
</div>

## When to use Brand-Family Swatch

Use a brand-family swatch wherever a retail anchor's *family* — Department, Hardware,
Warehouse Club, or a customer-defined family — needs a compact, consistent visual mark:
on a map marker, in a filter row, in a drawer header, or inline in running text. It is a
labelling primitive, not an interactive control: the swatch identifies which family a
feature belongs to; it does not, on its own, trigger an action.

The colour is deliberately supplementary. The label carries the meaning, so the swatch
remains legible for colour-blind visitors and under forced-colours mode. Reach for the
swatch when you need family identity to be scannable at a glance without relying on colour
alone.

Reference implementation: live at [gis.woodfinegroup.com](/products/gis/overview)
(v0.1.94). This component belongs to the map component line — see its sibling
[Map Side Drawer](/components/map-side-drawer/usage), whose header hosts the
`drawer-header-badge` variant below.

## Variants

The substrate ships five variants. Each targets one placement context; all share the same
dot-plus-label anatomy and the same per-family colour source.

| Variant | Description |
|---|---|
| **inline-chip** | Default. Dot + label chip, rendered inline. |
| **map-marker** | Large dot (24–32px); the label is suppressed and surfaced instead through the parent tooltip or drawer. |
| **cluster-centroid-ring** | A concentric arrangement of N family dots showing family distribution within a cluster. Renders at zoom &lt; 8.5 and crossfades to individual swatches above zoom 8. |
| **filter-row** | Paired with the checkbox primitive: `[✓] [●] Department`. |
| **drawer-header-badge** | The dot fills behind a brand short-code — e.g. `HD` for Home Depot. |

## Brand-family defaults

The recipe ships three baseline families. Each is a colour + human label pair; the colours
are the built-in CSS fallbacks used when a deployment has not supplied its own taxonomy.

| Family ID | Label | Default colour |
|---|---|---|
| `department` | Department | `#0B5FFF` |
| `hardware` | Hardware | `#FF6B00` |
| `warehouse-club` | Warehouse Club | `#00875A` |

These are defaults, not a closed set. The component is taxonomy-agnostic: a customer
extends the family list — Grocery, Pharmacy, or anything their portfolio requires —
through the runtime taxonomy file rather than by editing the component.

## Tokens

The swatch's structural styling — spacing, radius, and text colour — is drawn from the
design-token bundle:

| Token | Applied to |
|---|---|
| [`primitive.space.05`](/tokens#primitive) | Gap between the dot and the label |
| [`primitive.radius.sm`](/tokens#primitive) | Chip corner radius |
| [`semantic.text.primary`](/tokens#theme) | Label ink |
| [`semantic.text.secondary`](/tokens#theme) | Secondary/muted label contexts |

Brand-family **dot colours are not primitive tokens.** Per the recipe's own
`brand_family_token_note`, they are customer-taxonomy-specific and therefore live outside
the primitive bundle, expressed as CSS custom properties — `--ps-brand-family-department-color`,
`--ps-brand-family-hardware-color`, `--ps-brand-family-warehouse-club-color`, and the
generic `--ps-brand-family-color` — set per deployment by the runtime taxonomy file. Each
custom property falls back to its baseline default (or `currentColor` for the generic case)
when the deployment leaves it unset.

## Accessibility

The swatch targets **WCAG 2.2 AA**.

- The swatch element carries an `aria-label` stating the family name. The coloured dot is
  `aria-hidden="true"`, so assistive technology reads the family from the label, not the
  decoration.
- **Colour is supplementary; the label is the primary signifier.** A visitor who cannot
  distinguish the dot colours still gets the full meaning from the text label.
- Under `forced-colors: active`, the dots collapse to the user's link colour (`LinkText`)
  while the labels remain, so family identity survives high-contrast mode.

One consequence for the `map-marker` variant: because it suppresses the visible label
(clipping it for screen-reader-only access), the family name must be conveyed through the
marker's parent tooltip or the [Map Side Drawer](/components/map-side-drawer/usage) header —
the dot alone is not an accessible name.

## Open questions

Two decisions in the recipe remain open:

- **Default family IDs (oq-1).** Whether the component should ship a baseline family set
  (Department / Hardware / Warehouse Club / Grocery / Pharmacy / …) for customers to extend
  from, or ship empty so every deployment starts from scratch.
- **Cluster ring threshold (oq-2).** For the `cluster-centroid-ring` variant, whether a
  cluster with 10+ anchors of different families should transition the ring into a
  pie/donut at some threshold. Pending first banker-walkthrough feedback.

See the related design note on the zoom-tier reveal pattern
(`research/zoom-tier-reveal-pattern.md`) for the zoom-driven crossfade behaviour the
`map-marker` and `cluster-centroid-ring` variants share.

## When not to use

- Do not use a swatch as a button. It labels family identity; it does not perform an
  action. For triggers, use a [Button](/components/button/usage).
- Do not rely on the dot colour alone to convey family in a context where the label is
  hidden and no tooltip or drawer supplies it — that breaks the colour-supplementary
  contract.
