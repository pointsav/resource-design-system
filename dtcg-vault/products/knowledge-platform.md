<div class="page-intro">
<span class="eyebrow">Product line</span>
<p class="page-intro__lede">Component set powering PointSav's own wiki engine — the same
documentation.pointsav.com / projects.woodfinegroup.com / corporate.woodfinegroup.com
"leapfrog 2030" wiki family, one of three product lines built on this design system's
tokens.</p>

<div class="domain-stats">
<div class="domain-stat"><span class="domain-stat__value">13</span><span class="domain-stat__label">real components</span></div>
<div class="domain-stat"><span class="domain-stat__value">1</span><span class="domain-stat__label">rendered example — Home Grid</span></div>
<div class="domain-stat"><span class="domain-stat__value">IBM Plex Sans / Mono</span><span class="domain-stat__label">article typography (see Tokens)</span></div>
</div>
</div>

<div class="domain-intro">
<p>Wiki article content reads in <strong>IBM Plex Sans</strong> and
<strong>IBM Plex Mono</strong>, distinct from the Inter/mono pairing the rest of this
design system uses for UI chrome — a deliberate register shift for long-form reading
(see the <code>primitive.typography.wiki-h1</code> token on <a href="/tokens">Tokens</a>).
The home page's category-browse grid (Home Grid, below) extends the standard tile-grid
browse pattern with a ratified, always-render-all-nine-categories rule, so an empty category
reads as "in preparation," never as a missing page. Search results are backed by a real
Tantivy full-text index served over the same <code>/mcp</code> JSON-RPC endpoint
documented on <a href="/developing/mcp/overview">Developing</a>.</p>
</div>

<section class="card-grid" aria-label="Knowledge Platform components">
<div class="card"><h3>Home Grid</h3>
<p>9-card responsive category-browse grid for the wiki home page. Always renders all 9
ratified categories, including empty ones ("0 articles — in preparation") rather than
hiding them.</p>
<div class="card__tags"><a href="/components/home-grid/usage" class="badge badge--brand">Live example &rarr;</a></div></div>

<div class="card"><h3>Wiki Search Results</h3>
<p>Ordered list of search hits with a plain-text excerpt. Backed by the Tantivy
JSON-RPC endpoint at <code>/mcp</code> (method <code>search</code>).</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki TOC Sidebar</h3>
<p>Sticky right-rail heading list with active-section highlighting; collapses to an
inline toggle on compact viewports.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Article Header</h3>
<p>Breadcrumb, H1 from frontmatter, quality badge, and byline. Maps Wikipedia
article-header muscle memory using IBM Plex Sans at 2.25rem.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Article Footer</h3>
<p>Bottom-of-article surface: category tags, references/citations section, and an
edit-on-GitHub link — separates editorial metadata from article prose.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Badge / Tag</h3>
<p>Dual-purpose chip: article quality grade (Featured/Good/A/B/C/Stub) or a
category-tag link. Inline, pill-shaped.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Citation Authority Ribbon</h3>
<p>Source-type differentiation badges for references — six fixed source classes
(academic, regulator, industry, and others), each its own color.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Freshness Ribbon</h3>
<p>Per-section last-content-review date badge, shown after the section's [edit]
pencil. Three-stop color scale from fresh to stale.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Research Trail Footer</h3>
<p>Collapsible bottom-of-article disclosure with three fixed subsections: Research
done, Suggested research, Open questions — the epistemic-frontier record for a wiki
article.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Pagination</h3>
<p>Prev/Next article navigation within a category. Three-column grid: previous
article, category link, next article.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Modal Dialog</h3>
<p>Native <code>&lt;dialog&gt;</code> element with <code>showModal()</code> focus
trap. Used for image lightbox, search overlay, and confirmation prompts.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Dark Mode Toggle</h3>
<p>Toggles <code>data-theme="dark"</code> on <code>&lt;html&gt;</code> and persists
the choice in <code>localStorage</code>, initialising from it on load.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>

<div class="card"><h3>Wiki Drawer (Mobile Navigation)</h3>
<p>Slide-in overlay navigation for compact (&le;799px) viewports. Hamburger trigger
opens a full-height left drawer with the wiki site nav.</p>
<div class="card__tags"><span class="badge">Recipe documented</span></div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>13 real components, one rendered so far.</h3>
<p>Every card above is a real, registered component with a genuine recipe.json
behind it — the ones without a rendered page yet are documented, not fictional. Get
the raw tokens or browse the full registry.</p></div>
<div class="closing-cta__actions"><a href="/tokens" class="btn btn--secondary">See the tokens</a></div>
</div>
