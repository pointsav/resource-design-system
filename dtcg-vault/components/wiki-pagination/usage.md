<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Prev/Next article navigation within a wiki category — a
three-column grid with the previous article on the left, a category link in the
centre, and the next article on the right. This is sequential article-to-article
navigation, not numbered-page pagination.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-pagination/recipe.json</code></div>
</div>

## When to use Wiki Pagination

Use Wiki Pagination at the foot of a wiki article to move the reader
to the previous or next article within the same category, with a
centre link back to the category itself. It is the article-level
navigation surface of the
[Knowledge Platform](/products/knowledge-platform/overview) — each
article ends with one, so a reader can walk a category front to back
without returning to the category index between articles.

## Not numbered-page pagination

The display name says "Prev/Next" deliberately. This component does
**not** render numbered page controls (`1 2 3 … 12`) for splitting a
long list across pages. It navigates between whole articles in a
category's sort order. If a future surface needs numbered result-list
pagination, that is a different component — do not overload this one.

## Variants

Four variants cover every position an article can occupy in its
category. The three-column grid geometry is identical in all four;
only which cells carry a link changes.

| Variant | Shows |
|---|---|
| **full** | Prev + category + next. |
| **first-article** | No prev; spacer holds left cell. |
| **last-article** | No next; spacer holds right cell. |
| **only-article** | Both edges empty; category link only. |

When an edge has no article, omit the `<a>` and render a spacer
`<span>` in its place so the grid columns hold — the category link
stays centred and the remaining edge link stays in its own column
rather than drifting.

## Anatomy

Each edge link is a stacked flex column with three internal elements:

1. **Arrow** — `←` / `→` glyph, `aria-hidden` (decorative; the
   accessible name carries the direction).
2. **Direction** — the word "Previous" or "Next" in small uppercase
   secondary text.
3. **Article title** — the destination article's title.

The next link right-aligns its content (`align-items: flex-end;
text-align: end`) so the two edges mirror each other. The centre cell
holds a single smaller link to the category index.

## Layout

`grid-template-columns: 1fr auto 1fr` — equal flexible edge columns
with an auto-sized centre. At the compact breakpoint (≤799px) the
grid stacks to a single column. A subtle top border
(`{semantic.border.subtle}`) separates the pagination block from the
article body, with block padding from `{primitive.space.4}`.

## Sort order

Prev/next targets come from the wiki engine's section sort order —
in Zola terms, `page.lower` (previous in sort order) and
`page.higher` (next in sort order), controlled by the `sort_by`
field in the category's `_index.md`. The recipe carries an open
question: which `sort_by` value the wiki engine uses for category
sections has not yet been confirmed against the project-knowledge
`_index.md` files, so editorial ordering assumptions should be
verified there before relying on them.

## Tokens

The recipe consumes seven tokens — no hard-coded colours, spacing,
or font stacks in the CSS.

| Token | CSS custom property | Used for |
|---|---|---|
| [`{semantic.interactive.link}`](/tokens#theme) | `--pds-link` | Prev/next and category link colour |
| [`{semantic.interactive.link-hover}`](/tokens#theme) | `--pds-link-hover` | Edge-link hover colour |
| [`{semantic.text.secondary}`](/tokens#theme) | `--pds-text-secondary` | "Previous" / "Next" direction labels |
| [`{semantic.border.subtle}`](/tokens#theme) | `--pds-border-subtle` | Top border separating from article body |
| [`{primitive.font.family.body}`](/tokens#primitive) | `--pds-font-body` | Component font family |
| [`{primitive.space.2}`](/tokens#primitive) | `--pds-space-2` | Grid gap |
| [`{primitive.space.4}`](/tokens#primitive) | `--pds-space-4` | Block padding |

## Accessibility

Target: **WCAG 2.2 AA** (per the recipe's `wcag` field).

- **Landmark.** The component is a `<nav>` with
  `aria-label="Articles in {{category-name}}"`, so assistive
  technology announces it as a distinct navigation region named for
  its category.
- **Full-context link names.** Each edge `<a>` carries an
  `aria-label` giving the complete context — `Previous article:
  {{title}}` / `Next article: {{title}}` — so the link is
  unambiguous when read out of visual context.
- **Decorative arrows hidden.** The `←` / `→` glyphs are
  `aria-hidden="true"`; direction is conveyed by the accessible name,
  not the glyph.
- **Sequence semantics.** Edge links carry `rel="prev"` /
  `rel="next"`. The engine also emits matching `<link rel>` elements
  in `<head>` — that part is the engine's responsibility, not the
  component's.
- **Keyboard.** Navigation uses native `<a>` elements, so it is
  keyboard navigable with no scripting: Tab reaches each link, Enter
  activates.

## When not to use

- Do not use it for numbered-page pagination of long lists or search
  results — it navigates between articles, not between pages of one
  list.
- Do not use it outside the wiki article surface. It assumes a
  category context (the centre link and the `nav` label both name the
  category).
- Do not render an edge `<a>` with no destination — use the spacer
  `<span>` variant behaviour instead, so there is never a focusable
  link that goes nowhere.
