# GIS

Component set for map-driven retail/portfolio analysis — live in
production at gis.woodfinegroup.com (v0.1.94), one of three product
lines built on this design system's tokens.

## Components

- **Map Side Drawer** — persistent right-side info drawer for map
  feature detail. Slides in on click; replaces the popup-on-marker
  pattern so the map stays interactive underneath.
- **Map Stats Panel** — floating aggregate-statistics panel for the
  current filtered map view. Updates reactively on filter change;
  positioned top-right to avoid the zoom controls.
- **Brand-Family Swatch** — taxonomic dot + label chip for the
  Department / Hardware / Warehouse Club retail taxonomy.
  Taxonomy-agnostic — customers extend it via a runtime taxonomy file.
- **Country Filter Chips** — horizontal radiogroup that filters map
  data and flies to the selected country's bounds. Default state is
  ALL (world view); exclusive selection today.

4 real components, already live at gis.woodfinegroup.com; 1 rendered
example (Map Side Drawer) — see Components.
