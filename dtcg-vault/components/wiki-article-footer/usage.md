<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Bottom-of-article surface for the documentation wiki:
category tags, a references/citations section, and an edit-on-GitHub link. It
separates editorial metadata from the article body, so the reading surface ends
where the article ends and everything after the rule is about the article rather
than of it.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-article-footer/recipe.json</code></div>
</div>

## When to use Wiki Article Footer

Use Wiki Article Footer as the closing surface of every article on a
[Knowledge Platform](/products/knowledge-platform/overview) wiki. It
renders after the article body, above the site chrome, and carries the
three pieces of editorial metadata a wiki article accumulates: which
categories it belongs to, which sources it cites, and where a
contributor goes to change it. A `1px` top border in
`{semantic.border.subtle}` draws the line between content and
metadata — the footer is *about* the article, not part of it.

It is a per-article surface, not a site footer. One instance per
article, always last in the article's `<article>` region.

## Variants

| Variant | Shows |
|---|---|
| **standard** | Categories + references + edit link. |
| **no-references** | Categories + edit link; references section omitted. |

Use **no-references** only when the article genuinely cites nothing —
omit the References section entirely rather than rendering an empty
heading over an empty list. The categories section and the edit link
are present in both variants: every wiki article belongs to at least
one category and every wiki article is editable.

## Anatomy

The footer is a `<footer class="ps-wiki-article-footer">` with up to
three regions, in fixed order:

1. **Categories** — a `<section>` with a visible `Categories`
   heading and an unstyled, wrap-friendly `<ul>` of category tags.
   Each tag is a [Wiki Badge Tag](/components/wiki-badge-tag/usage)
   in its `category` form (`ps-wiki-badge ps-wiki-badge--category`),
   linking to that category's browse page.
2. **References** — a `<section>` with a visible `References`
   heading and an `<ol>` of citations. Each list item carries
   `id="ref-N"` and wraps its citation text in `<cite>`, so
   in-article superscript links can target `#ref-N` directly.
   Omitted in the **no-references** variant.
3. **Actions** — an end-aligned `Edit on GitHub` link opening the
   article's source file in a new tab (`rel="noopener"`,
   `target="_blank"`).

Section headings render at `1.25rem` / `600` weight — visually
subordinate to the article's own headings, since the footer is
metadata, not content.

## Registry dependencies

The recipe declares two registry dependencies: `wiki-badge-tag`
(category tags reuse [Wiki Badge Tag](/components/wiki-badge-tag/usage)
rather than defining their own pill styles) and `edit-on-github-link`
(the actions row's edit affordance). Consumers pulling this recipe
from the registry receive both.

## Tokens

All colour, typography, and spacing values resolve through the token
pipeline — nothing is hard-coded except the two structural sizes
(section-heading `font-size` and reference-list indent).

| Token | Role |
|---|---|
| [`{primitive.font.family.body}`](/tokens#primitive) | Footer text family |
| [`{semantic.text.primary}`](/tokens#theme) | Default footer text colour |
| [`{semantic.text.secondary}`](/tokens#theme) | Reference-list text — de-emphasised relative to body copy |
| [`{semantic.interactive.link}`](/tokens#theme) | Edit-on-GitHub link colour |
| [`{semantic.border.subtle}`](/tokens#theme) | Top border separating footer from article body |
| [`{primitive.space.2}`](/tokens#primitive) | Block padding and inter-section spacing |
| [`{primitive.space.4}`](/tokens#primitive) | Spacing scale — declared in the recipe's token set |

Because the three text roles are semantic tokens, the footer re-themes
per tenant with no component-level overrides.

## Accessibility

The recipe targets **WCAG 2.2 AA** and bakes the structure in rather
than leaving it to the consumer:

- **Labelled landmarks.** The two `<section>` elements each carry
  `aria-labelledby` pointing to their own visible `<h2>` — screen
  readers announce "Categories" and "References" as named regions
  without a duplicate hidden label.
- **Addressable citations.** References render as an `<ol>` whose
  items carry `id="ref-N"`, so in-article back-links
  (`<a href="#ref-N">`) land on the exact citation. Citation text is
  wrapped in `<cite>`.
- **New-tab disclosure.** The edit link uses `rel="noopener"` with
  `target="_blank"`, and must include visually hidden
  *"(opens in new tab)"* text so screen-reader users are told the
  context switch before it happens.
- **Heading hierarchy.** The footer's section headings are `<h2>`
  elements — same level as the article's own top sections, since the
  footer sits directly inside the article's document outline.

## When not to use

- Not a site footer. Legal links, navigation, and brand marks belong
  to the page shell, not to the article.
- Not a tag cloud or general badge row. The categories list is
  specifically the article's category memberships; for badges
  elsewhere, use [Wiki Badge Tag](/components/wiki-badge-tag/usage)
  directly.
- Not a bibliography page. The references section holds the citations
  *this* article makes; a standalone reference index is a different
  surface.
