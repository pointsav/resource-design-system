# Regional Market TOPIC — Page Template Design

**Origin:** project-gis (2026-05-30) · `language_protocol: DESIGN-RESEARCH`  
**Companion:** `components/regional-market-topic/guide.md`

A Regional Market (RM) TOPIC article is a wiki page archetype that profiles a single
human settlement containing one or more co-location clusters. It joins five data surfaces
— the cluster registry, the AEC overlays, the composite scoring output, civic-infrastructure
rosters, and Wikipedia summary content — into a single reader-facing article on the
knowledge wiki.

This document specifies the visual layout, the named CSS classes the template relies on,
and the HTML skeleton the wiki platform developer implements. Token values are drawn from
the existing design-system palette; no new tokens are added by this specification. If a
required token is absent, a separate DESIGN-TOKEN-CHANGE draft with Master co-sign is
opened before adding it.

---

## Layout overview

Two-column layout inside the existing `wiki_chrome()` shell. Right column: sticky infobox
card. Left column: article body. The existing TOC sidebar is shared with the chrome — the
infobox sits right of the article body, not in place of the TOC.

Column ratio: left ~65–70% of article content width, right ~30–35%. Infobox has
`position: sticky; top: var(--rm-infobox-sticky-top)`. Mobile (≤768 px, matching the
existing wiki chrome breakpoint): infobox flows above article body, full-width, sticky
dropped.

---

## Infobox card

Fields in display order:

| Field | Source | Treatment |
|---|---|---|
| **Rank** | `score-regional-markets.py` `rank` | "16 / 400" — position over total in same region |
| **Best Tier** | Highest tier in `cluster_ids` | Badge: T1 = gold, T2 = silver, T3 = bronze |
| **Cluster Count** | Length of `cluster_ids` | Integer |
| **Composite Score** | `score` | One decimal place |
| **ISO Country** | `country` | ISO 3166-1 alpha-2 |
| **Nearest Major Centre** | Derived metro + km | e.g. "Oklahoma City, 250 km SE" |
| **Centroid** | `centroid_lat`, `centroid_lon` | Decimal degrees, four places |

Optional: Wikipedia thumbnail below fields when `thumbnail.source` URL is available.
Width capped at infobox width; no crop. Caption: page title + link to Wikipedia article.

CSS classes: `.rm-infobox`, `.rm-infobox-fields`, `.rm-infobox-field`,
`.rm-infobox-field-label`, `.rm-infobox-field-value`, `.rm-rank-badge`,
`.rm-tier-badge` (modifiers: `--t1`, `--t2`, `--t3`), `.rm-wiki-thumb`,
`.rm-wiki-thumb-caption`.

---

## Co-location table

Columns: Cluster (link to `gis.woodfinegroup.com/?cluster=<id>`), Tier (badge), Anchor
Composition, Span (km, one decimal), Civic (Yes/No text label, not glyph).

Row background tint by tier (decorative — tier is also conveyed by the badge):
T1 → light gold (`#FFF8DC` reference; token-sourced), T2 → light blue (`#EEF4FF`),
T3 → light grey (`#F5F5F5`). All hex values are reference targets; actual rendered colours
come from the design-system token bundle.

CSS classes: `.rm-cluster-table`, `.rm-cluster-table tbody tr.tier-t1/t2/t3`,
`.rm-civic-yes`, `.rm-civic-no`.

---

## AEC data grid

CSS Grid `<dl>` (`grid-template-columns: max-content 1fr`). Fields: ASHRAE 169 Zone (US
only), EU Climate Zone (EU only), Köppen-Geiger Class, WWF Ecoregion, WWF Biome, Seismic
PGA 2%/50yr, Flood 100yr return period. Empty fields omitted — no "N/A" rows rendered.

CSS classes: `.rm-aec-grid`, `.rm-aec-grid-label`, `.rm-aec-grid-value`.

---

## Score breakdown

Two parts: (1) six-component table (Metric / Value / Weight), bold Total row; (2) optional
pure-CSS horizontal bar visualisation (`aria-hidden="true"`, `prefers-reduced-motion`
fallback drops to table-only). Bar fill uses a single neutral design-system colour, not tier
colours.

CSS classes: `.rm-score-table`, `.rm-score-total`, `.rm-score-bars`, `.rm-score-bar`,
`.rm-score-bar-fill` (width via `--rm-bar-pct` custom property), `.rm-score-bar-label`,
`.rm-score-bar-value`.

---

## Wikipedia attribution footer

Mandatory when the page embeds Wikipedia summary text or thumbnail. Sits at the bottom of
the article body, above the existing wiki article footer.

```html
<footer class="rm-wiki-attribution">
  Wikipedia content reproduced under
  <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC BY-SA 4.0</a>.
  Accessed <time datetime="YYYY-MM-DD">YYYY-MM-DD</time>.
  Original article(s):
  <a href="https://en.wikipedia.org/wiki/...">City Name</a>.
</footer>
```

CSS classes: `.rm-wiki-attribution`, `.rm-wiki-attribution a`. Visual: smaller type,
muted neutral foreground, top border.

---

## Open questions for implementation

1. **Tier badge tokens** — are gold/silver/bronze already in the token bundle? If not, a
   separate DESIGN-TOKEN-CHANGE draft is required before the template ships.
2. **Sticky offset** — `--rm-infobox-sticky-top` must be sourced from a design-system token
   (topnav height + any sticky breadcrumb), not hardcoded.
3. **Mobile breakpoint reuse** — confirm this template uses the existing 768 px wiki chrome
   breakpoint variable, not a new declaration.
4. **Civic badge style** — confirm Yes/No renders as chip or plain text against existing
   chip/pill patterns.
5. **Bar visualisation** — if the design-system has an existing data-bar pattern, use that
   rather than the `.rm-score-bar` pattern specified here.

---

## Research trail

**Done (4):**
1. Layout derived from existing `wiki_chrome()` server function patterns — two-column
   layout compatible with TOC sidebar; sticky infobox aligned with Wikipedia infobox convention.
2. CSS class namespace `rm-*` chosen to avoid collision with existing wiki chrome selectors;
   verified against `app-mediakit-knowledge/static/style.css`.
3. Score breakdown fields derived from `score-regional-markets.py` output schema — six
   component weights confirmed from Phase 22/23 cluster data shape.
4. Wikipedia CC BY-SA 4.0 attribution footer mandatory per Wikimedia reuse policy; structure
   mirrors standard academic/news reuse patterns.

**Suggested (3):**
1. WCAG 2.2 AA contrast audit on tier-tint row backgrounds with black body text.
2. Verify sticky infobox behaviour on iOS Safari (position:sticky + overflow:auto interaction).
3. Consider a `<details>/<summary>` progressive disclosure pattern for the score breakdown
   bars on mobile to reduce vertical footprint.
