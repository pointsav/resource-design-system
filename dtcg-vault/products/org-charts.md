<div class="page-intro">
<span class="eyebrow">Product line</span>
<p class="page-intro__lede">Print-first component set for entity/ownership hierarchy
diagrams — the newest of three product lines built on this design system's tokens,
landed this release.</p>

<div class="domain-stats">
<div class="domain-stat"><span class="domain-stat__value">3</span><span class="domain-stat__label">real components</span></div>
<div class="domain-stat"><span class="domain-stat__value">1</span><span class="domain-stat__label">rendered example — Org Chart Node</span></div>
<div class="domain-stat"><span class="domain-stat__value">1 / 6</span><span class="domain-stat__label">color with no Carbon equivalent at all</span></div>
</div>
</div>

<div class="domain-intro">
<p>Org chart diagrams are a print-first surface — every node renders at a fixed pixel
position on a 1056&times;816px canvas (US Letter landscape at 96dpi), not a fluid web
layout. That constraint, and the entity-role color system it needs, don't map cleanly
onto this design system's Carbon-derived primitives — see the gap analysis below.</p>
<p>The token registry reserves a 9-role entity-color palette
(<code>primitive.color.orgchart.*</code>, see <a href="/tokens#primitive">Tokens</a>)
— the shipped Org Chart Node component uses 6 of those 9 roles today (green, blue,
purple, orange, grey, yellow); the remaining 3 (two "legacy entity" colors plus an
extra grey variant) are reserved capacity, not yet wired into a component variant.</p>
</div>

<div class="gap-table-wrap">
<h2>Why org-chart tokens are their own namespace, not reused Carbon tokens</h2>
<p>From the real, ratified gap analysis
(<code>dtcg-vault/research/orgchart-carbon-token-map.md</code>): of the six entity-role
colors, one (Broker / Asset Manager, purple) has no Carbon equivalent at all — Carbon's
semantic system has nothing similar. Two more (Investment Vehicle's blue, Corporate
Holding's green) map to a same-intent Carbon token, but at a meaningfully different hex
value or semantic register (see the table). Reusing Carbon's <code>$support-*</code>
tokens for the remaining three would import status/alert semantics (success, caution,
warning) into what are structural, not evaluative, distinctions between entity types.
Box dimensions (110&ndash;250px, plus the 1056&times;816px canvas) don't derive from
Carbon's 8px spacing scale either — they're set by print legibility and the US Letter
page geometry. Typography runs 9&ndash;12px, below Carbon's 12px floor, because only
about five 210px-wide boxes fit across the 1056px canvas in one row, leaving little
room to spare at a larger type size.</p>

<div class="doc-table-scroll" role="region" tabindex="0" aria-label="Org chart to Carbon color mapping, scroll horizontally">
<table class="doc-table">
<thead><tr><th>Entity role</th><th>Our token</th><th>Carbon nearest</th><th>Assessment</th></tr></thead>
<tbody>
<tr><td>Corporate holding</td><td><code>primitive.color.orgchart.green</code></td><td><code>$support-success</code></td><td>Different hue — ours is lighter sage, Carbon is darker forest</td></tr>
<tr><td>Investment vehicle</td><td><code>primitive.color.orgchart.blue</code></td><td><code>$interactive</code></td><td>Different register — institutional navy vs. bright interactive blue</td></tr>
<tr><td>Broker / asset manager</td><td><code>primitive.color.orgchart.purple</code></td><td>none</td><td><strong>No Carbon equivalent at all</strong></td></tr>
<tr><td>Equity partner</td><td><code>primitive.color.orgchart.orange</code></td><td><code>$support-caution-major</code></td><td>Close visually, wrong semantic — caution implies a warning</td></tr>
<tr><td>Admin entity</td><td><code>primitive.color.orgchart.grey</code></td><td><code>$border-strong-01</code></td><td>Similar lightness, different use — border vs. entity fill</td></tr>
<tr><td>LP / fund vehicle</td><td><code>primitive.color.orgchart.yellow</code></td><td><code>$support-warning</code></td><td>Close visually, wrong semantic — warning implies an alert</td></tr>
</tbody>
</table>
</div>
</div>

<section class="card-grid" aria-label="Org Charts components">
<div class="card"><h3>Org Chart Node</h3>
<p>Absolutely-positioned entity box on the print canvas. Three shape families —
rectangle (operating entities), pill (fund vehicles, always dashed), ellipse
(cross-border flow-throughs).</p>
<div class="card__tags"><a href="/components/orgchart-node/usage" class="badge badge--brand">Live example &rarr;</a></div></div>

<div class="card"><h3>Org Chart Canvas</h3>
<p>The fixed-dimension print canvas hosting all node boxes and connector overlays —
exactly US Letter landscape at 96dpi (1056&times;816px), fills the page edge-to-edge
when printed.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Org Chart Connector</h3>
<p>SVG overlay of directed connection lines between nodes, beneath the node boxes.
Arrowhead fill matches the source box's border color.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>3 real components, the newest product line.</h3>
<p>Every card above is a real, registered component with its own recipe.json — get
the raw tokens or browse the full registry.</p></div>
<div class="closing-cta__actions"><a href="/tokens" class="btn btn--secondary">See the tokens</a></div>
</div>
