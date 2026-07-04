# Design research — wiki institutional redesign brief

Registers the 2026-06-03 institutional redesign audit for the three-wiki portfolio
(documentation.pointsav.com, projects.woodfinegroup.com, corporate.woodfinegroup.com),
from project-knowledge (a 9-agent Opus browser audit — 5 live sites, 7 institutional
comparators, 143 tool uses, 502 seconds wall-clock). Source:
`DESIGN-wiki-institutional-redesign.draft.md` (totebox@project-knowledge, 2026-06-03).
**Decision 5** (below) is the one design-system token change in scope here — master-cosigned
by command@claude-code, 2026-06-03 — everything else in §2 and §6 is template/code work
for project-knowledge, included for context.

*(This file previously landed as an 8-line frontmatter stub with no body — the real
content below was recovered from the original source draft, still present at
`project-software`/`project-proforma`'s `drafts-outbound/`, 2026-07-03.)*

## §1 Executive summary

The three-wiki portfolio rates C-minus / 3.6 out of 10 on an institutional credibility
scale. The foundations are strong — self-hosted Source Serif 4 + Inter, navy #164679 +
gold #C7A961, a DTCG token system, and WCAG 2.2 AAA structure — but they are consistently
undercut by prototype-grade finish: dead links in global chrome, empty structural
scaffolding rendered to customer-facing surfaces, vendor brand leaking onto customer
sites, and layouts that leave 40% of a 27-inch monitor empty on every sparse page.

The single biggest systemic problem is that all three wiki properties were built for the
dense-article case and never finished for the common sparse case — empty TOC rails,
single-item categories adrift in 3-column shells, blank right columns, and exposed
internal taxonomy. This is the textbook startup-vs-institution tell: institutions never
expose raw empty scaffolding.

The one decision with the largest positive impact is adopting per-surface,
content-aware layout governance: listing/category/home templates collapse to a
content-filling grid with designed empty states, while only dense article pages retain
the 3-column reading shell. Make that structural decision correctly and roughly
two-thirds of the P0/P1 findings dissolve — they are all symptoms of a single layout
system applied indiscriminately.

## §2 Ranked audit findings

**P0 — must fix before any institutional demo:** a category-template TOC rail renders a
permanent dead "Contents" column on ~35 documentation.pointsav.com category pages; sparse
categories sit adrift in a fixed 3-column shell; two design generations (legacy `wiki-*`
CSS vs. the unused modern shell markup) ship in one 4,200-line stylesheet; the
projects.woodfinegroup.com global footer 404s on Disclaimer/Contact across 44+ pages;
vendor pointsav.com branding and a "PointSav Knowledge" login title leak onto the Woodfine
customer site; the corporate.woodfinegroup.com home page links two featured articles to
404ing slugs; and category templates across all three sites render vast blank expanses
with no empty-state design.

**P1 — must fix before public launch:** non-canonical links missing the `/wiki/` prefix;
a footer category count that doesn't match the real total; unbranded 404 pages; internal
ops taxonomy (`cluster-totebox-*`, `fleet-infrastructure-*`, etc.) published to a public
customer surface; a public editor login exposed in the masthead; dead-empty right rails
on non-TOC templates; a consumer-grade "Wiki" home page title burying strong quantified
proof points; and corporate.woodfinegroup.com's sidenav disappearing on every template
except articles — exactly where new visitors need orientation most.

**P2 — polish:** TOC disappearing below 1100px with no fallback; an inconsistent body-type
step-up; inconsistent category list card treatments; Wikipedia-style "Last edited"
metadata instead of institutional citation; unverified ES-toggle siblings; utility pages
mixed into substantive topic lists; and a "Recently updated" block where every article
shares the same bulk-import date.

## §3 Institutional comparator lessons

Twelve concrete patterns from Bloomberg, BlackRock, Stripe, Cloudflare, Palantir, IBM
Carbon, and Atlassian: editorial weighting over uniform grids (importance expressed
through size, not position); an intent-first home with taxonomy demoted to "browse all";
hiding empty categories from navigation entirely rather than exposing dead nav nodes;
designed three-part empty states (positive-action title, one explanatory line, at most
one stable-position CTA); "invisible UI" restraint reading as confidence; a single
interactive color discipline (one blue for all links/actions/focus, not a palette of
accents); a fluid `clamp()` type scale constrained to a 65–80ch reading measure even on
wide viewports; hierarchy carried through weight *and* size, not size alone; a 3-column
shell reserved only for genuinely dense reference content; breadcrumbs plus a visible
changelog/freshness signal as non-negotiable trust markers; navigation capped at two
nesting levels with a quiet left selection indicator; and accessibility/trust
infrastructure (WCAG AA minimum, CVD-safe status colors, visible timestamps and version
attribution) treated as a credibility signal, not an afterthought.

## §4 Redesign decision — wiki home page

Two-column desktop layout (≥1280px): a 280px fixed left nav rail, content filling the
remainder up to a 1200px max width, no right column on the home page (it is a listing
surface, never a TOC-bearing one). The auto-generated category list is replaced by three
stacked zones: **Zone A** (editorial-weighted Featured — one large slot at 2/3 width plus
two secondary slots), **Zone B** (a hand-curated "Start here / Most popular" intent list
of 5–7 links), and **Zone C** (a populated-category card grid, minimum 3 articles to
qualify — internal ops taxonomy excluded entirely). An empty category reached by direct
URL gets a designed empty state (a quiet line-art glyph, a positive-action title, and
related-category cross-links) rather than a blank page. Typography: Source Serif 4 body
at 18px/1.6 line-height (raised from 17px, the 17→19px responsive step-up removed),
paired with Inter for all UI/nav/labels — H1 `clamp(34px,4vw,44px)`/600, H2 28px/600, H3
20px/600, nav labels 14px/500.

**Decision 5 — color (the design-system token change, master-cosigned 2026-06-03):**
`--color-interactive` → **#0E3A66** (darkened navy; single link/focus/primary-action
color, Carbon-style one-blue discipline); `--color-brand-surface` retained at **#164679**
for masthead fills and large brand moments; `--color-accent` → **#C7A961** gold, sparing
use only (rules, active indicators, key metrics — never a text-background fill).

## §5 Redesign decision — wiki article page

Three columns only when an article has ≥3 H2/H3 headings *and* viewport ≥1100px (left
256px sidenav + a reading column now `clamp(62ch, 70vw, 80ch)` wide, up from a fixed 68ch
that left wide viewports half-empty + a 248px right TOC rail); below that threshold the
layout collapses to two columns with the TOC as a collapsible inline disclosure — the
rail is never rendered empty. The sidenav renders only populated public categories
(zero-article nodes are never emitted, filtered at template render time via an
`article_count > 0` guard), capped at two nesting levels, with a `3px solid #C7A961` left
selection indicator rather than a color fill. Article headers get a real hierarchy:
breadcrumb (with JSON-LD `BreadcrumbList`) → clamp-scaled H1 → an institutional metadata
row ("Methodology · Woodfine Management Corp. · Revised `<date>`", replacing Wikipedia-
style "Last edited" chrome) → a horizontal rule before prose. A build-time internal
link-checker runs against the rendered sitemap before every deploy and blocks the build
outright on any unresolved internal link, any chrome 404, a non-canonical alias missing
the `/wiki/` prefix, or an ES-toggle target with no live sibling.

## §6 Implementation priority order

The first five items are blocking for any institutional demo: a build-time link-checker
that blocks deploy on chrome/featured-slot 404s; removing the vendor-brand leak from
projects.woodfinegroup.com; authoring real Disclaimer/Contact pages; the category-template
redesign (drop empty TOC rails, content-filling grid, designed empty states); and fixing
corporate.woodfinegroup.com's two 404ing featured-article slugs. P1 items (migrating
documentation.pointsav.com off legacy `wiki-*` CSS, splitting public docs from internal
ops taxonomy, normalizing internal routing, the Decision-5 token change, the home-page
zone restructure, and the article-header redesign) and one P2 polish item (collapsible
inline TOC below 1100px) round out the full punch list — all owned by project-knowledge
except the token change itself, which was project-design's to commit.
