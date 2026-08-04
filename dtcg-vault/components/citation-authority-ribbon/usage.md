<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">6 source classes</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Stub — pending verification</span>
</div>
<p class="doc-header__lead">Source-type differentiation badges for a wiki article's
references list. Each citation entry carries a single-letter authority glyph — one
of six fixed classes — so a reader can tell an academic paper from a regulator
filing from an informal web link at a glance, instead of scanning a flat numbered
list where every source looks the same.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/citation-authority-ribbon/recipe.json</code></div>
</div>

## When to use Citation Authority Ribbon

Use this component on the **references section** of a
[Knowledge Platform](/products/knowledge-platform/overview) wiki article — the
ordered list at the foot of the page that each inline footnote links down to. Its
job is to replace a flat numbered list where every source looks the same — the
weakness the recipe explicitly names as its target — with one that encodes *what
kind of source* each entry is, right in the scan column.

The surface scope is deliberately narrow: `wiki-article-references`. This is not a
general-purpose badge for arbitrary links, and it is not a citation *formatter* —
it styles and classifies entries in a references `<ol>` whose text and hyperlinks
you supply. Every entry gets exactly one authority badge, keyed to its source
class.

## Status — real design, two decisions not yet ratified

This recipe carries `"status": "stub"` in its own real `recipe.json`. It is a
formalization of a genuine design draft — `stub_source` points at
`component-citation-authority-ribbon.draft.md`, drafted by the knowledge-platform
team, 2026-04-30 — not an invented placeholder. The HTML, the six source classes, the
token names, and the ARIA contract below are all transcribed from that recipe.

What "stub" means here specifically is that two design decisions in the recipe's
own `open_questions` field remain open, pending ratification by the substrate:

1. **Glyph form.** Single-letter glyphs (`A` / `R` / `I` / `D` / `N` / `W`) versus
   full-word tags (`Academic`, `Regulator`, …). The trade-off the recipe records:
   single letters keep the reference list as dense as a plain numbered list;
   full words are more accessible on first encounter. The examples below show the
   single-letter form the current HTML uses.
2. **Badge position.** Leading the entry text (denser) versus sitting in an
   outside-left gutter (creates a clean scan column). Unresolved.

Treat the values below as correct in intent — real, sourced, and internally
consistent — but not yet a pixel-verified transcription of a deployed page.

## Six source classes

The class set is closed and fixed at six. The class lives on each list item as
`data-source-authority`, and the visible badge is a `<span>` carrying the class
glyph plus an `aria-label`.

| Class | Glyph | `data-source-authority` | Badge background token |
|---|---|---|---|
| **Academic** | A | `academic` | `--article-references-citation-badge-academic-bg` (blue) |
| **Regulator** | R | `regulator` | `--article-references-citation-badge-regulator-bg` (green) |
| **Industry** | I | `industry` | `--article-references-citation-badge-industry-bg` (warm-gray) |
| **Direct source** | D | `direct-source` | `--article-references-citation-badge-direct-source-bg` (teal) |
| **News** | N | `news` | `--surface-layer-accent` (cool-gray) |
| **Web / informal** | W | `web-informal` | `transparent` — outline only |

Note the last two rows: **News** reuses the shared `--surface-layer-accent` token
rather than a bespoke citation-badge token, and **Web / informal** has no fill at
all — it is rendered as an outline-only badge. Only the first four classes have a
dedicated `--article-references-citation-badge-*-bg` token.

## Markup shape

The recipe's HTML is an `<ol class="ps-references">`. Each entry is:

```html
<li class="ps-references__entry" id="cite-1" data-source-authority="academic">
  <span class="ps-citation-badge ps-citation-badge--academic" aria-label="Academic source">A</span>
  <span class="ps-references__text">
    Klein, G. et al. seL4: Formal Verification of an OS Kernel. ACM SOSP 2009.
    <a href="https://sel4.systems/">sel4.systems</a>
  </span>
  <a class="ps-references__backref" href="#cite-ref-1" aria-label="Back to citation in body">↑</a>
</li>
```

Three parts per entry: the authority badge `<span>`, the reference text (with its
outbound source link), and a backref `<a>` — the `↑` arrow that returns the reader
to the inline footnote marker (`#cite-ref-N`) in the article body. The `data-source-authority`
attribute on the `<li>` is the machine-readable anchor; the visible badge class is
its presentational mirror.

## Tokens

The four per-class badge fills plus the backref color are **theme tokens**
([`/tokens#theme`](/tokens#theme)):

- `--article-references-citation-badge-academic-bg`
- `--article-references-citation-badge-regulator-bg`
- `--article-references-citation-badge-industry-bg`
- `--article-references-citation-badge-direct-source-bg`
- `--article-references-backlink-bracket-color` — colors the `↑` backref arrow

The News class draws its fill from the shared `--surface-layer-accent`; Web /
informal uses no fill token (outline only). Badge sizing draws on two **primitive
tokens** ([`/tokens#primitive`](/tokens#primitive)): `--font-size-3` for the glyph
and `--space-1` for its internal padding.

## Accessibility

The recipe's WCAG target is **2.2 AA**, and its ARIA contract is explicit:

- **The badge is informative, not decorative.** It is a `<span>` with an
  `aria-label` (`"Academic source"`, `"Regulator source"`, etc.) and is **never**
  `aria-hidden`. A screen-reader user hears the source class, not just the letter.
- **Colour is never the sole differentiator.** Each badge pairs a color with a
  single-letter glyph *and* the `aria-label`, so the classification survives
  color-blindness, grayscale, and non-visual reading. This is what lets the
  outline-only Web / informal badge and the two gray classes remain distinguishable
  without relying on hue.
- **Tab order is unchanged.** Only the citation's outbound hyperlink and the
  backref `↑` arrow are focusable; the badge itself is not a control. The backref
  `<a>` carries `aria-label="Back to citation in body"` and returns the reader to
  the inline footnote it came from.

## Machine-readable surface

Beyond the visible badge, `data-source-authority` on each `<li>` is the canonical
machine-readable surface. Per the recipe's `ai_hint`, a JSON-LD emission attaches a
`@type` refinement to each citation entry inside the article's `TechArticle`
schema — `AcademicSource`, `RegulatorSource`, `IndustrySource`, `DirectSource`,
`NewsSource`, `WebInformalSource` — so downstream consumers and crawlers can read
the same six-way classification that a human reads from the glyph.

## Related

- [Home Grid](/components/home-grid/usage) — the Knowledge Platform wiki's
  category-browse front door.
- [Attribution Badge](/components/attribution-badge/usage) — another
  single-purpose, tokens-backed mark from this vault.
- [Knowledge Platform overview](/products/knowledge-platform/overview) — the
  product surface this component lives on.
