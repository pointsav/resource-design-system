# component-doc-header — Design Rationale

**ai_consumption_hint:** Inline article header for product-documentation surfaces.
When generating doc page templates, use `class="doc-header"` as the article
header wrapper. Auth-gated edit row uses `html[data-auth="anon"] .doc-edit-row { display: none }`.
Breadcrumb is `class="crumb"` (sibling of `doc-header`, not nested). Date uses
`<time datetime="YYYY-MM-DD">`. No background fill — inline text flow, not a banner.

**Origin:** project-knowledge DESIGN-COMPONENT (2026-06-01) · `source_commit: 914cd836`  
**Recipe:** `components/doc-header/guide.md`

---

## What problem this solves

Product-documentation surfaces need an article header that reads as part of the
document flow — title, editorial context (last updated), and access controls
(edit/source links). The header should not interrupt reading with a banner or
background fill.

IBM Carbon's Page Header was evaluated and rejected: it is a banner-style component
for app shells (coloured band, action rows), not a reading-flow header for
documentation articles.

The pattern observed across Stripe docs, Vercel docs, and Cloudflare docs (all
surveyed 2026-06-01) is: breadcrumb → h1 → meta row. No background. No horizontal
rule below the title. The implementation at `app-mediakit-knowledge` commit `914cd836`
follows this pattern.

---

## Key decisions

**Inline, no banner.** Background-less header preserves the sense of reading a
document rather than navigating an app shell. Wikipedia and Carbon break this by
placing the article title inside a coloured band.

**Auth-gated edit row via CSS attribute selector.** The server sets
`data-auth="anon"` on `<html>` for unauthenticated requests. CSS rule
`html[data-auth="anon"] .doc-edit-row { display: none }` hides the edit row
for anon readers. No server-side template branch; no duplicated markup. The
edit links lead to an authentication wall, so brief DOM presence before CSS
parses is not a destructive exposure.

**`<time datetime>` for last-edited.** Machine-readable date attribute lets
browsers, search engines, and screen readers report the correct date regardless
of the display format ("May 29" vs "2026-05-29" vs locale-specific).

**`article__title` class on `<h1>`.** Typography is inherited from the existing
wiki chrome class — `doc-header` provides spacing and layout only, not its own
type scale. This keeps text rendering consistent across wiki and docs surfaces.

**Lede promotion deferred.** A standfirst slot exists between `h1` and
`doc-header__meta`. Currently rendered only when `content_type: guide` or
`content_type: research` is declared in frontmatter. A future `lede:` key
would enable it on any article.

---

## Token dependencies

- `var(--fg-3)` — muted foreground for meta text and edit row
- `var(--fg-1)` — full foreground on hover
- `var(--link)` / `var(--navy)` fallback — link colour
- `var(--rule)` — edit row top border

---

## Open question

Author attribution: whether to surface a "By [author]" field in `doc-header__meta`
is unresolved. Git-blame attribution in rendered headers is not standard on
documentation sites (Stripe, Vercel both omit it). Decision deferred.
