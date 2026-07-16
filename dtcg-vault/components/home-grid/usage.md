<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">9-card responsive category-browse grid for the
documentation wiki home page. Always renders all 9 ratified categories regardless of
article count — an empty category reads as "in preparation," never as a missing
page.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/home-grid/recipe.json</code></div>
</div>

## When to use Home Grid

Use Home Grid as the category-browse entry point on a documentation
wiki's home page — a 9-card grid, one card per ratified content
category, each showing an article count and a short preview list.
It is the front door to the wiki, not a general-purpose card grid.

## The 9-category set

The category set is closed and operator-ratified (per
`naming-convention.md` §10 Q5-A): Architecture, Services, Systems,
Applications, Governance, Infrastructure, Company, Reference, Help.
Do not alphabetize or reorder this list, and do not suppress empty
categories — every deployment renders all 9, always. An empty
category shows `0 articles — in preparation` rather than being
hidden, so a visitor never wonders whether a category exists.

## Variants

| Variant | Shows |
|---|---|
| **Populated** | Article count, top-3 child links, a `More →` link to the full category. |
| **Empty** | `0 articles — in preparation` only — no child list, no `More` link. |

## Layout

3 columns at ≥960px, 2 columns from 640–959px, 1 column below 640px.

## Behaviour

Each card has a hover border-color transition (collapses under
`prefers-reduced-motion`). Card titles and child links carry a
`:focus-visible` ring. Heading hierarchy: `h2` for the section
heading ("Browse by category"), `h3` per card title — screen readers
get one section landmark via `aria-label`, not a redundant visible
heading duplicate.

## When not to use

This is not a generic content card grid — it is specifically the
9-category wiki home-page browse surface. For a general card layout
elsewhere on the site, use the substrate's generic `.card`/`.card-grid`
classes instead.
