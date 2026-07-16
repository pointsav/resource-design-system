<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AAA target</span>
</div>
<p class="doc-header__lead">Page-level navigation header. Logo, primary nav, optional
actions, optional account menu.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/navigation-bar/recipe.json</code></div>
</div>

## When to use Navigation bar

Use the navigation bar for top-level page navigation. One per
application; appears at the top of every page.

The recipe ships a horizontal layout with logo + primary nav +
optional actions area. Mobile collapse (hamburger drawer pattern)
is subsequent-milestone work.

Mark the active page with `aria-current="page"`.
