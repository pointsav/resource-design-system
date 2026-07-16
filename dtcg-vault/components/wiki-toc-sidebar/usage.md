<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Sticky right-rail sidebar listing an article's headings
(H2/H3). The section currently in view is highlighted via IntersectionObserver;
on compact viewports the rail collapses to an inline toggle above the article
body.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-toc-sidebar/recipe.json</code></div>
</div>

## When to use Wiki Table of Contents Sidebar

Use the Wiki TOC Sidebar on long-form article pages in the
[Knowledge Platform](/products/knowledge-platform/overview) — any
wiki article whose body carries enough H2/H3 headings that a reader
benefits from a persistent map of where they are. It is an
article-scoped navigator: it lists the headings of *this page*, not
the site. For navigation between pages, that is a different surface
— this site's own left-rail component accordion is the closest
in-house parallel, but it is site chrome, not this component.

One instance per article. The component tracks scroll position and
marks exactly one section as current at a time; two competing TOC
rails on the same page would double the `aria-current` signal and
confuse both sighted readers and screen-reader users.

## When not to use

- **Short articles.** If the article has only one or two H2s, the
  rail adds chrome without aiding orientation — omit it.
- **Cross-page navigation.** The TOC lists this article's headings
  only. Category browsing belongs to
  [Home Grid](/components/home-grid/usage) and the wiki's own
  navigation surfaces.
- **Headings deeper than H3.** The recipe's list structure covers
  two levels (H2 items with an H3 sublist). H4+ headings are not
  represented — restructure the article rather than deepening the
  TOC.

## Variants

| Variant | Behaviour |
|---|---|
| **Desktop** | Sticky right-rail; `position: sticky; top: 1rem`. Stays alongside the article as the reader scrolls. |
| **Mobile** | Inline collapsible toggle above the article body; `<details>`/`<summary>` pattern. Below 800px the rail's `position` drops to `static`. |

## Anatomy

The component is a single `<nav>` landmark with three internal
elements:

1. **Heading** — a visible `Contents` label
   (`.ps-wiki-toc__heading`), uppercase, letter-spaced, set in
   `{semantic.text.secondary}`.
2. **List** — an ordered list (`.ps-wiki-toc__list`) of H2 links,
   each optionally carrying a nested `.ps-wiki-toc__sublist` of H3
   links. Nesting is conveyed structurally by an `<ol>` inside the
   `<li>`; sublists are indented with `{primitive.space.2}` of
   inline-start padding.
3. **Active indicator** — the link for the section currently in
   view gets `.ps-wiki-toc__link--active` plus `aria-current="true"`:
   a 2px inline-start border in
   `{semantic.interactive.button-primary}`, text promoted to
   `{semantic.text.primary}` at weight 600.

## Behaviour

### Scroll tracking

An IntersectionObserver watches the article's sections and moves the
`aria-current="true"` attribute (and the `--active` modifier class)
to the link whose section is in view. Exactly one link is current at
a time. The observer threshold is an open question in the recipe —
0.1 (section enters viewport) versus 0.5 (section majority visible)
— which affects feel at scroll boundaries; consumers should treat
the threshold as unratified until the recipe resolves it.

### Compact viewports

At `max-width: 799px` the CSS drops `position: sticky` to `static`.
The mobile variant then presents the same list as an inline
collapsible toggle above the article body using the native
`<details>`/`<summary>` pattern, so collapse/expand works without
component JavaScript.

### Link states

Links render in `{semantic.interactive.link}` and shift to
`{semantic.interactive.link-hover}` on hover. Sub-links
(`.ps-wiki-toc__link--sub`) are set a step smaller (0.8125rem) in
`{semantic.text.secondary}` to subordinate them visually to their
parent H2 entry.

## Tokens

The recipe consumes ten tokens — resolve them at
[/tokens#primitive](/tokens#primitive) and
[/tokens#theme](/tokens#theme):

| Token | Role in this component |
|---|---|
| `{primitive.font.family.body}` | Rail typography (`--pds-font-body`). |
| `{semantic.text.primary}` | Active link text colour. |
| `{semantic.text.secondary}` | `Contents` heading and sub-link colour. |
| `{semantic.interactive.link}` | Resting link colour. |
| `{semantic.interactive.link-hover}` | Link hover colour. |
| `{semantic.interactive.button-primary}` | Active-section indicator border. |
| `{semantic.surface.layer-accent}` | Rail background. |
| `{semantic.border.subtle}` | Rail border. |
| `{primitive.space.1}` | Heading margin; link inline-start padding. |
| `{primitive.space.2}` | Rail padding; sublist indent. |

## Accessibility

The recipe targets WCAG 2.2 AA.

- **Landmark.** The component is a `<nav aria-label="Table of
  contents">` — one named navigation landmark per article, so
  screen-reader users can jump straight to it or skip past it.
- **Current section.** The active link carries
  `aria-current="true"`, updated by the IntersectionObserver JS.
  Assistive technology announces which section the reader is in
  without relying on the visual border-and-weight treatment alone.
- **Structural nesting.** H3 sub-entries live in an `<ol>` nested
  inside the parent `<li>`. The list structure itself conveys the
  hierarchy — no extra ARIA is needed. Sublist items are indented
  visually with inline-start padding.
- **Visible heading.** The rail opens with a real `<h2>`
  (`Contents`), so the TOC appears in the page's own heading outline
  as well as in the landmark list.
