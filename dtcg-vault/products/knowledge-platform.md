# Knowledge Platform

Component set powering PointSav's own wiki engine — the same
documentation.pointsav.com / projects.woodfinegroup.com /
corporate.woodfinegroup.com "leapfrog 2030" wiki family, one of three
product lines built on this design system's tokens.

Wiki article content reads in IBM Plex Sans and IBM Plex Mono, distinct
from the Inter/mono pairing the rest of this design system uses for UI
chrome — a deliberate register shift for long-form reading (see the
`primitive.typography.wiki-h1` token on [Tokens](/tokens)). The home
page's category-browse grid extends IBM's Carbon Tile pattern with a
ratified, always-render-all-nine-categories rule, so an empty category
reads as "in preparation," never as a missing page. Search results are
backed by a real Tantivy full-text index served over the same `/mcp`
JSON-RPC endpoint documented under Agents.

## Components

- **Home Grid** — 9-card responsive category-browse grid for the wiki
  home page. Always renders all 9 ratified categories, including empty
  ones ("0 articles — in preparation") rather than hiding them.
- **Search Results** — ordered list of search hits with a plain-text
  excerpt. Backed by the Tantivy JSON-RPC endpoint at `/mcp` (method
  `search`).
- **TOC Sidebar** — sticky right-rail heading list with active-section
  highlighting; collapses to an inline toggle on compact viewports.
- **Article Header** — breadcrumb, H1 from frontmatter, quality badge,
  and byline. Maps Wikipedia article-header muscle memory using IBM
  Plex Sans at 2.25rem.
- **Article Footer** — bottom-of-article surface: category tags,
  references/citations section, and an edit-on-GitHub link.
- **Badge/Tag** — dual-purpose chip: article quality grade
  (Featured/Good/A/B/C/Stub) or a category-tag link.
- **Citation Source Badge** — source-type differentiation badges for
  references — six fixed source classes (academic, regulator,
  industry, and others), each its own color.
- **Review-Freshness Badge** — per-section last-content-review date
  badge, shown after the section's edit pencil. Three-stop color scale
  from fresh to stale.
- **Research-Trail Footer** — collapsible bottom-of-article disclosure
  with three fixed subsections: Research done, Suggested research,
  Open questions — the epistemic-frontier record for a wiki article.
- **Article Prev/Next** — prev/next article navigation within a
  category. Three-column grid: previous article, category link, next
  article.
- **Modal Dialog** — native `<dialog>` element with `showModal()`
  focus trap. Used for image lightbox, search overlay, and
  confirmation prompts.
- **Dark-Mode Toggle** — toggles `data-theme="dark"` on `<html>` and
  persists the choice in `localStorage`.
- **Drawer Mobile Nav** — slide-in overlay navigation for compact
  (≤799px) viewports.

13 real components documented; 1 rendered example (Home Grid) — see
Components.
