<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Persistent left navigation column for product-documentation
surfaces — uppercase category headings as native <code>&lt;details&gt;</code> sections,
article links inside, active page highlighted by a border-left accent.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/docs-sidenav/recipe.json</code></div>
</div>

## When to use Documentation Left Navigation

Use `docs-sidenav` for cross-page category navigation on documentation-wiki
surfaces — lets a reader jump between categories without returning to a homepage, no
JS required for open/close. IBM Carbon's Side Nav was evaluated and rejected
(icon-slot overhead, no per-article icon assignments in this corpus); the adopted
pattern instead follows Stripe/Vercel/Cloudflare docs (uppercase category labels,
collapsible link lists), all surveyed 2026-06-01. Source: `app-mediakit-knowledge`
commit `914cd836`, originally a project-knowledge DESIGN-COMPONENT (2026-06-01).

## When not to use

- **Within-article table of contents.** Do not confuse with `wiki-toc-sidebar`
  (within-article H2/H3 contents, right rail) — the two solve different navigation
  problems and can coexist on the same page. `docs-sidenav` is cross-page; `wiki-toc-
  sidebar` is within-page.

## Variants

| Variant | Behaviour |
|---|---|
| **Desktop** | Sticky left rail, 256px, visible ≥ 1024px. |
| **Hidden-mobile** | `display: none` below 1024px; article reachable via breadcrumb. |

## Mobile behaviour and content depth — decided 2026-08-10

**No drawer.** Below 1024px the rail stays `display: none`; the breadcrumb (via
`doc-header`) remains the mobile navigation path. Not a placeholder pending a future
hamburger-triggered drawer — that alternative was considered and explicitly deferred,
since it would add a JS controller and a separate accessibility pass without a
demonstrated mobile-usage need.

**One level deep, locked.** The category → article-list hierarchy stays exactly one
level. Matches the Stripe/Vercel/Cloudflare pattern this component was modeled on and
keeps the component simple. Revisit only if a real category grows too large to browse
flat — not designed for section-level grouping up front.

## Anatomy

A single `<nav aria-label="Documentation navigation">` containing one or more
`<details class="docs-sidenav__cat">` category sections, each with a `<summary>`
category label and a `<ul>` of article links.

## Tokens

| Token | Role in this component |
|---|---|
| `{semantic.text.secondary}` | Category label and resting link colour. |
| `{semantic.text.primary}` | Link hover text colour. |
| `{semantic.text.tertiary}` | Category disclosure chevron colour. |
| `{semantic.interactive.link}` | Active-link text colour. |
| `{semantic.surface.hover}` | Link hover background. |
| `{semantic.surface.layer-accent}` | Active-link background. |
| `{semantic.border.subtle}` | Rail right-hand border. |
| `{primitive.font.family.display}` | Category label typeface. |

## Accessibility

The recipe targets WCAG 2.2 AA.

- **Landmark.** `<nav aria-label="Documentation navigation">`.
- **Current page.** Active link carries `aria-current="page"`.
- **Keyboard-operable disclosure.** Category open/close uses native
  `<details>`/`<summary>` — Enter/Space works without any JavaScript, and the browser
  manages `aria-expanded` implicitly and correctly.
- **Active state is never colour-only.** Border-left accent and `font-weight: 600`
  accompany the colour change.
- **Mobile removal, not hiding.** Below 1024px the rail is `display: none` — removed
  from the accessibility tree entirely, not just visually hidden. The article remains
  reachable via `doc-header`'s breadcrumb.

## Reference

Source: `app-mediakit-knowledge` commit `914cd836`. Research: `research/component-docs-
sidenav.md` (evaluated against Carbon, Stripe, Vercel, Cloudflare docs navigation).
