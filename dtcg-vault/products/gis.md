<div class="page-intro">
<span class="eyebrow">Product line</span>
<p class="page-intro__lede">Component set for map-driven retail/portfolio analysis —
live in production at <strong>gis.woodfinegroup.com (v0.1.94)</strong>, one of three
product lines built on this design system's tokens.</p>

<div class="domain-stats">
<div class="domain-stat"><span class="domain-stat__value">4</span><span class="domain-stat__label">real components</span></div>
<div class="domain-stat"><span class="domain-stat__value">1</span><span class="domain-stat__label">rendered example — Map Side Drawer</span></div>
<div class="domain-stat"><span class="domain-stat__value">v0.1.94</span><span class="domain-stat__label">live reference implementation</span></div>
</div>
</div>

<div class="domain-intro">
<p>All four components below cite the same real, live reference implementation
directly in their registered recipe — this isn't a hypothetical component set built
ahead of a product; it documents one that's already running. The taxonomic swatch
component (Brand-Family Swatch) is deliberately <strong>taxonomy-agnostic</strong>:
the shipped defaults cover a Department / Hardware / Warehouse Club retail taxonomy,
but a customer extends the set via a runtime taxonomy file rather than a code change —
brand-family colors live outside the primitive token bundle for exactly this reason.</p>
</div>

<section class="card-grid" aria-label="GIS components">
<div class="card"><h3>Map Side Drawer</h3>
<p>Persistent right-side info drawer for map feature detail. Slides in on click;
replaces the popup-on-marker pattern so the map stays interactive underneath.</p>
<div class="card__tags"><a href="/components/map-side-drawer/usage" class="badge badge--brand">Live example &rarr;</a></div></div>

<div class="card"><h3>Map Stats Panel</h3>
<p>Floating aggregate-statistics panel for the current filtered map view. Updates
reactively on filter change; positioned top-right to avoid the zoom controls.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Brand-Family Swatch</h3>
<p>Taxonomic dot + label chip for the Department / Hardware / Warehouse Club retail
taxonomy. Taxonomy-agnostic — customers extend it via a runtime taxonomy file.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Country Filter Chips</h3>
<p>Horizontal radiogroup that filters map data and flies to the selected country's
bounds. Default state is ALL (world view); exclusive selection today.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>4 real components, already live.</h3>
<p>Every card above documents a component running in production today — get the raw
tokens or browse the full registry.</p></div>
<div class="closing-cta__actions"><a href="/tokens" class="btn btn--secondary">See the tokens</a></div>
</div>
