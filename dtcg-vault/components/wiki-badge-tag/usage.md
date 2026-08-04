<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A dual-purpose inline chip for the documentation wiki:
as a quality-grade badge it announces an article's assessment tier
(Featured/Good/A/B/C/Stub); as a category tag it links to a category page. Pill-shaped,
inline-flex, and small enough to sit inside a heading row or footer without breaking
line rhythm.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-badge-tag/recipe.json</code></div>
</div>

## When to use Wiki Badge / Tag

Use Wiki Badge / Tag inside the
[Knowledge Platform](/products/knowledge-platform/overview) article
chrome, in exactly two places:

- **Quality-grade badge** — rendered by
  [Wiki Article Header](/components/wiki-article-header/usage) to
  announce the article's assessment tier at the top of the page.
- **Category tag** — rendered by
  [Wiki Article Footer](/components/wiki-article-footer/usage) as a
  row of links to the category pages the article belongs to.

The two uses share one visual language — same padding, same
`{primitive.radius.xs}` pill corner — so a reader learns the chip
shape once and recognises it in both positions.

## Variants

| Variant | Element | Behaviour |
|---|---|---|
| **Quality grade** | Non-interactive `<span>` | Grade colour plus an `aria-label` carrying the full grade name. Announces status; does nothing on click. |
| **Category tag** | Interactive `<a>` | Links to the category page (`/category/{slug}`). Standard link semantics; bordered, link-coloured text. |

The distinction is load-bearing: a quality badge is a statement, a
category tag is a destination. Never make a quality badge clickable,
and never render a category tag as a plain `<span>` — the border and
link colour are the affordance that separates the two at a glance.

## Quality grades

The quality-grade variant ships six grade modifiers. Each maps one
modifier class to one colour token:

| Grade | Modifier class | Colour token | Reading |
|---|---|---|---|
| **Featured article** | `--featured` | `{primitive.color.status.warn}` | Gold/amber — highest quality tier |
| **Good article** | `--good` | `{primitive.color.status.success}` | Green — second tier |
| **A-class** | `--a-class` | `{primitive.color.brand.blue.60}` | Blue — third tier |
| **B-class** | `--b-class` | `{primitive.color.brand.blue.50}` | Light blue — fourth tier |
| **C-class** | `--c-class` | `{semantic.surface.layer-accent}` | Muted surface — developing |
| **Stub** | `--stub` | `{semantic.surface.layer-accent}` | Muted surface — minimal content |

The scale is intentionally top-heavy in colour: the two muted grades
(C-class, Stub) share one quiet surface token, so only articles that
have earned a tier draw the eye. Featured through B-class each carry
`{semantic.text.on-color}` text on their filled background; the muted
grades use `{semantic.text.secondary}`.

## When not to use

- Do not use the quality badge as a general-purpose status chip
  outside wiki article chrome. The six grades are an editorial
  assessment scale, not a generic severity palette.
- Do not use a category tag for navigation that is not a category
  page. It is a link to `/category/{slug}` — other destinations
  belong to ordinary links.
- Do not stack a quality badge inside body copy. It belongs in the
  article header, placed by
  [Wiki Article Header](/components/wiki-article-header/usage).

## Anatomy

Both variants are a single inline-flex pill:

1. **Container** — `0.1em` vertical padding, `{primitive.space.1}`
   horizontal padding, `{primitive.radius.xs}` corner radius,
   `white-space: nowrap` so a chip never wraps mid-label.
2. **Label** — 0.75rem at weight 600 for the quality badge;
   0.8125rem for the category tag.
3. **Border** — category tag only: 1px solid
   `{semantic.border.subtle}`, with `{semantic.interactive.link}`
   text colour and no underline.

## Tokens

The recipe consumes these tokens — primitives from
[/tokens#primitive](/tokens#primitive), semantics from
[/tokens#theme](/tokens#theme):

| Token | Role |
|---|---|
| `{primitive.color.status.warn}` | Featured badge background |
| `{primitive.color.status.success}` | Good badge background |
| `{primitive.color.brand.blue.60}` | A-class badge background |
| `{primitive.color.brand.blue.50}` | B-class badge background |
| `{semantic.surface.layer-accent}` | C-class and Stub badge background |
| `{semantic.text.primary}` | Text on unfilled surfaces |
| `{semantic.text.secondary}` | Text on the muted C-class/Stub badges |
| `{semantic.text.on-color}` | Text on filled grade backgrounds |
| `{semantic.interactive.link}` | Category tag text colour |
| `{semantic.border.subtle}` | Category tag border |
| `{primitive.radius.xs}` | Pill corner radius (both variants) |
| `{primitive.space.05}`, `{primitive.space.1}` | Chip padding scale |

## Accessibility

Target: **WCAG 2.2 AA**, per the recipe's `wcag` field.

### Quality badge

The badge is a non-interactive `<span>` carrying an `aria-label` with
the full grade name — `Article quality: Featured article`. This means
the visible text may be abbreviated (e.g. `FA`) without losing
meaning for screen-reader users: the `aria-label` supplies the full
name regardless of what is painted.

### Category tag

A standard `<a href>` — no additional ARIA is needed or wanted. Link
semantics, focus behaviour, and announcement all come from the native
element.

### Known open question

The recipe carries one unresolved contrast check: the Featured badge
uses amber/gold (`{primitive.color.status.warn}`), verified in the
contrast audit as passing on a dark surface (`#f5cd7a` on dark), but the
light-mode combination for this specific badge has not yet been
separately verified. Treat light-mode Featured-badge contrast as
pending verification, not as a confirmed pass.
