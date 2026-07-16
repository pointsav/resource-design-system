<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">The top-of-article surface for a Knowledge Platform wiki page: a slug
breadcrumb, the H1 title drawn from article frontmatter, a quality-grade badge, and a
byline carrying the last-edited date, the editor, and a link to page history. It maps
Wikipedia article-header muscle memory using IBM Plex Sans at a 2.25rem heading.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-article-header/recipe.json</code></div>
</div>

## When to use Wiki Article Header

Use Wiki Article Header once, at the very top of a wiki article, as
the first thing below the site chrome. It is the article's masthead:
it tells a reader where they are (breadcrumb), what they are reading
(title), how far the article can be trusted (quality badge), and who
last touched it and when (byline). It is produced from article
frontmatter, so every article on a [Knowledge
Platform](/products/knowledge-platform/overview) deployment gets a
consistent header without per-page authoring.

Use it only for editorial wiki articles. It is not a generic page
header, a hero, or a section title — those surfaces do not carry a
quality grade or an edit history, and reusing this component for them
would imply an editorial provenance that does not exist.

## Anatomy

The header is a single `<header class="ps-wiki-article-header">`
landmark composed of three stacked rows:

1. **Breadcrumb** — a `<nav aria-label="Article location">` wrapping
   an `<ol>` of category crumbs. It locates the article inside the
   wiki's category tree and links back up to the category.
2. **Title row** — the article `<h1>` alongside a quality badge. The
   `<h1>` is the article title from frontmatter; the badge reflects
   the article's editorial grade.
3. **Byline** (`role="doc-subtitle"`) — the last-edited date in a
   machine-readable `<time>` element, the editor's display name, and a
   `View history` link, separated by decorative `·` dividers.

The quality badge is the [Wiki Badge / Tag](/components/wiki-badge-tag/usage)
component; this header declares it as a registry dependency and reuses
it rather than restyling a grade pill of its own.

## Variants

The recipe ships four variants. Each is the same three-row header with
one deliberate change; there is no size or density axis.

| Variant | Description |
|---|---|
| **Standard** | Breadcrumb + title row (H1 + badge) + byline. The default article header. |
| **With lead image** | Standard, plus a right-floated `<figure>` for a lead image beside the opening prose. |
| **With infobox** | Standard, plus a right-floated `<aside class="ps-wiki-infobox">` for a structured summary panel. |
| **Ungraded** | Badge omitted; the title row is the H1 only. Use for articles that carry no editorial grade. |

Choose **Ungraded** when an article has not been graded — do not
render a placeholder or "unrated" badge in its place. An absent badge
reads as "not yet graded," which is the honest state; a placeholder
badge would imply a grade was assigned.

## When not to use

- Do not use it for a non-article page (a category index, a search
  result, a landing surface). Those carry no quality grade or edit
  history.
- Do not add a second `<h1>` elsewhere on the article — this header
  owns the page's single top-level heading.
- Do not hand-author the badge markup. Reuse [Wiki Badge /
  Tag](/components/wiki-badge-tag/usage) so grade styling stays
  consistent across the platform.

## Tokens

The header is fully tokens-backed — every colour, space, and type
value resolves through a DTCG token, so it re-themes per tenant with
no per-component overrides.

| Token | Role |
|---|---|
| [`primitive.font.family.body`](/tokens#primitive) | Heading and text family (IBM Plex Sans). |
| [`primitive.font.size.10`](/tokens#primitive) | H1 title size (2.25rem). |
| [`primitive.space.1`](/tokens#primitive) | Title-row and byline gaps; vertical rhythm around the title row. |
| [`primitive.space.2`](/tokens#primitive) | Padding below the header, above its bottom border. |
| [`primitive.space.4`](/tokens#primitive) | Larger spacing primitive available to the floated `figure`/`aside` variants. |
| [`semantic.text.primary`](/tokens#theme) | Title colour. |
| [`semantic.text.secondary`](/tokens#theme) | Breadcrumb and byline colour. |
| [`semantic.interactive.link`](/tokens#theme) | History link colour. |
| [`semantic.border.subtle`](/tokens#theme) | The 1px rule separating the header from article body. |

## Accessibility

Target: **WCAG 2.2 AA**.

- **Breadcrumb landmark.** The breadcrumb is a `<nav>` with
  `aria-label="Article location"`, so assistive technology announces
  it as a distinct navigation region and can list it separately from
  the main navigation.
- **Current page.** The last breadcrumb item carries
  `aria-current="page"`, marking the reader's location within the
  category trail.
- **Quality badge.** The badge exposes its grade to screen readers via
  `aria-label="Article quality: <grade label>"`, so the grade is
  announced as words rather than inferred from colour alone.
- **Machine-readable date.** The last-edited date is wrapped in a
  `<time datetime="…">` element carrying an ISO 8601 value, so the
  date is available to machines and assistive technology independent
  of its human-readable display form.
- **Byline role.** The byline row uses `role="doc-subtitle"` to
  associate it with the article title as subordinate metadata.
- **Decorative dividers.** The `·` separators are marked
  `aria-hidden="true"` so they are not announced.

## Related

- [Knowledge Platform overview](/products/knowledge-platform/overview) — the product this header ships with.
- [Wiki Badge / Tag](/components/wiki-badge-tag/usage) — the quality-grade badge reused in the title row.

<div class="doc-footer-meta">
<span>depends on:</span>
<a href="/components/wiki-badge-tag/usage">wiki-badge-tag</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>tokens:</span>
<a href="/tokens#primitive">primitive.font.size.10</a>,
<a href="/tokens#theme">semantic.text.primary</a>,
<a href="/tokens#theme">semantic.border.subtle</a>
</div>
