<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Inline article header for product-documentation surfaces:
breadcrumb, article title, optional lede standfirst, last-edited date with history
link, and an auth-gated edit/view-source row.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/doc-header/recipe.json</code></div>
</div>

## When to use Documentation Article Header

Use `doc-header` on every documentation-wiki article page: breadcrumb, title, optional
lede, last-edited meta, and an edit/view-source row that only authenticated sessions
see. Live on documentation.pointsav.com, projects.woodfinegroup.com, and
corporate.woodfinegroup.com since the 2026-07-01 Sovereign Editorial Phase 2→6 wiki
redesign.

## When not to use

- **Wiki landing/category pages.** Those use their own hub template — `doc-header` is
  article-scoped, not a category index.
- **Non-wiki product pages.** Marketing/storefront pages don't carry an edit-row
  concept; see the [Storefront register](/editorial-style-guide/guide-storefront) for
  that surface's own voice guidance.

## Variants

| Variant | Behaviour |
|---|---|
| **Standard** | Breadcrumb + `<h1>` + meta row + auth-gated edit row. |
| **With-lede** | Adds a promoted standfirst paragraph between the titlewrap and meta row — render when frontmatter declares `content_type: guide` or `content_type: research`. |

## Anatomy

1. **Breadcrumb** — `<nav aria-label="Breadcrumb">` wrapping an `<ol>`: Home →
   category → current article (`aria-current="page"` on the final item).
2. **Title** — one `<h1 class="article__title">` per page.
3. **Meta row** — last-edited date, machine-readable via `<time datetime>`, linked to
   the article's history.
4. **Edit row** — Edit this page / View source links, present only for authenticated
   sessions.

## Attribution — decided 2026-08-10

No author-attribution field. The header stays impersonal, documentation-style:
breadcrumb + title + last-edited date only, no byline. Matches how the three live
wiki sites already read. (An earlier draft of this component used a real individual's
name as an example byline in its open question — genericized before this recipe was
drafted, and the question itself resolved to "no attribution" rather than a role-noun
byline, per house-core.md's Outside-voice rule either way.)

## Tokens

| Token | Role in this component |
|---|---|
| `{semantic.text.secondary}` | Meta row text, edit-row text and links (resting state). |
| `{semantic.interactive.link}` | Meta-row and edit-row link hover colour. |
| `{semantic.border.subtle}` | Edit-row top rule. |

## Accessibility

The recipe targets WCAG 2.2 AA.

- **Landmark.** `<nav aria-label="Breadcrumb">` is a named navigation landmark
  distinct from the article body.
- **Current page.** The breadcrumb's final `<li>` carries `aria-current="page"`.
- **Machine-readable date.** The last-edited date uses `<time datetime="{{iso-date}}">`
  so assistive technology and tooling get an unambiguous ISO date, not just the
  display string.
- **Auth-gated content removed, not hidden.** The edit/view-source row uses
  `display: none` under `html[data-auth="anon"]` — removed from the accessibility
  tree entirely for anonymous sessions, not just visually hidden, so screen-reader
  users on an anonymous session never encounter a dead-end edit link.

## Reference

Source: `app-mediakit-knowledge` commit `914cd836`. Research: `research/component-doc-
header.md` (evaluated against Carbon/Stripe/Vercel/Cloudflare documentation headers).
