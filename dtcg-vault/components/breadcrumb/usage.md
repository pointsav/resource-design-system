<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AAA target</span>
</div>
<p class="doc-header__lead">Hierarchy trail to the current page — useful when nested
deeper than two levels.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/breadcrumb/recipe.json</code></div>
</div>

## When to use Breadcrumb

Use a breadcrumb when the user is more than two levels deep in
content hierarchy and the parent context is not visible elsewhere
(sidebar, page header). Skip the breadcrumb when the parent is
already in the sidebar — duplicating navigation surface adds cost
without adding clarity.

The current page is the last item, marked `aria-current="page"`,
and is not a link.
