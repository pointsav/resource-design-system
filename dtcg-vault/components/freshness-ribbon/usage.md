<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">3 freshness stops</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Stub — pending verification</span>
</div>
<p class="doc-header__lead">Per-section last-content-review date badge, shown at the
right end of each wiki article section heading, after the [edit] pencil. A
three-stop colour scale answers "how current is this section?" at a glance: fresh
(green, ≤90 days), stale (amber, 91–365 days), archived (gray, &gt;365 days) — with
the review date itself always printed, so the colour is a reinforcement, never the
message.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/freshness-ribbon/recipe.json</code></div>
</div>

## When to use Freshness Ribbon

Use this component on the **section headings** of a
[Knowledge Platform](/products/knowledge-platform/overview) wiki article. Its
surface scope is deliberately narrow: `wiki-article-section-heading`. It is a
per-*section* signal, not a per-page one — a long reference article routinely has
a fresh "Current implementations" section sitting above an archived "Historical
context" section, and a single page-level date would flatten exactly that
distinction.

The ribbon is a read-only annotation. It is not a control, not a link, and not a
general-purpose date chip for use outside article section headings.

## Status — real design, two decisions not yet ratified

This recipe carries `"status": "stub"` in its own real `recipe.json`. It is a
formalization of a genuine design draft — `stub_source` points at
`component-freshness-ribbon.draft.md`, produced by **project-knowledge on
2026-04-30** — not an invented placeholder. The HTML shape, the three stops, the
thresholds, the token names, and the ARIA contract below are all transcribed from
that recipe.

What "stub" means here specifically is that two design decisions in the recipe's
own `open_questions` field remain open, pending ratification by the substrate:

1. **Reader-preference default.** Ribbons on by default, or off by default behind
   a toggle? The trade-off the recipe records: on-by-default adds visual weight to
   every heading; off-by-default hides the signal until a reader activates it.
   The toggle mechanism itself is already specified —
   `:root[data-freshness-display='off']` hides all ribbons — only the default is
   unresolved.
2. **Display format.** ISO `2026-03-15` versus relative `6 weeks ago` versus
   seasonal `Spring 2026`. The recipe's examples use the ISO form; the substrate
   ratifies the final choice.

There is also a hard scope boundary worth knowing: this recipe covers the visual
component only. Per its `engine_scope_note`, everything that *computes* the ribbon
— section-boundary detection, git-blame at section level, frontmatter
`content_reviewed_on` parsing, threshold computation, JSON-LD emission, and
ARIA-label generation — is engine work owned cluster-side by project-knowledge,
not by this vault. Treat the values below as correct in intent — real, sourced,
and internally consistent — but not yet a pixel-verified transcription of a
deployed page.

## The three freshness stops

The scale is closed and fixed at three stops. The stop is encoded as a class
modifier on the ribbon `<span>`, and the threshold boundaries are themselves
tokens, not magic numbers.

| Stop | Colour | Window | Class | Colour token |
|---|---|---|---|---|
| **Fresh** | Green | ≤90 days since last substantive content change | `ps-freshness-ribbon--fresh` | `--article-freshness-ribbon-color-fresh` |
| **Stale** | Amber | 91–365 days since last substantive content change | `ps-freshness-ribbon--stale` | `--article-freshness-ribbon-color-stale` |
| **Archived** | Gray | &gt;365 days since last substantive content change | `ps-freshness-ribbon--archived` | `--article-freshness-ribbon-color-archived` |

"Substantive" is doing real work in that table: the git-blame data source
explicitly excludes whitespace-only commits, so reformatting a section does not
reset its freshness clock.

## Data sources

Each ribbon declares where its date came from via a `data-source` attribute, with
two permitted values:

| `data-source` | Meaning |
|---|---|
| `git-blame` | Most recent commit touching content lines in the section — computed with `--ignore-all-space --ignore-blank-lines`, so whitespace-only changes never count as a review. |
| `frontmatter-review` | A per-section `content_reviewed_on` frontmatter field — a manual editor override for when a human has verified content that git history alone would mark stale. |

The machine-readable date always travels alongside the display string as
`data-iso="YYYY-MM-DD"`, regardless of which display format the substrate
ultimately ratifies.

## Markup shape

The ribbon is a `<span>` placed inside the section's `<h2>`, after the `[edit]`
link. One heading from the recipe's own HTML:

```html
<h2 class="ps-article__section-heading">
  Background
  <a class="ps-article__section-edit" href="?action=edit&section=2"
     aria-label="Edit section: Background">[edit]</a>
  <span class="ps-freshness-ribbon ps-freshness-ribbon--fresh"
        data-source="git-blame"
        data-iso="2026-03-15"
        aria-label="Last reviewed 2026-03-15 — fresh">
    2026-03-15
  </span>
</h2>
```

Because the ribbon lives *inside* the heading element rather than beside it, the
document outline stays clean — but note the constraint this imposes, covered under
Accessibility below.

## Tokens

The three stop colours and the two threshold boundaries are **component-layer
tokens** ([`/tokens#theme`](/tokens#theme)):

- `--article-freshness-ribbon-color-fresh` — aliases the theme's status-success
  colour in the canonical token bundle.
- `--article-freshness-ribbon-color-stale` — aliases the theme's status-warn
  colour.
- `--article-freshness-ribbon-color-archived` — a neutral gray; the bundle pins it
  to `neutral-70` with a documented 6.70:1 contrast ratio on the wiki's
  `neutral-20` background (a 2026-05-01 fix — the original `neutral-50` value was
  a 2.72:1 contrast defect).
- `--article-freshness-ribbon-threshold-fresh-days` — the number `90`. A
  per-deployment overrideable number token, per the bundle's own description.
- `--article-freshness-ribbon-threshold-stale-days` — the number `365`, same
  override rule.

Because the thresholds are tokens, a deployment with a faster or slower editorial
cadence can retune the scale without forking the component.

Sizing and type draw on five **primitive tokens**
([`/tokens#primitive`](/tokens#primitive)): `--font-family-mono` (dates are set in
the mono family), `--font-size-2`, `--radius-xs`, `--space-025`, and `--space-1`.

## Accessibility

The recipe's WCAG target is **2.2 AA**, and its ARIA contract is explicit:

- **The heading semantic is unbroken.** The ribbon is a `<span>` — not focusable,
  not a control — inside the `<h2>`. Screen-reader heading navigation still lands
  on a real section heading; the ribbon rides along as annotated content rather
  than fragmenting the heading into multiple elements.
- **The `aria-label` announces the date *and* the semantic class.** The pattern is
  `"Last reviewed YYYY-MM-DD — fresh"` (or `— stale, over a year ago` /
  `— archived, content under historical review only` in the recipe's examples), so
  a non-visual reader gets the classification the colour encodes, not just a bare
  date.
- **Colour is never the sole differentiator.** The date string is always visibly
  present inside the ribbon. A reader in grayscale, with colour-vision deficiency,
  or on a monochrome e-ink display still reads the actual review date and can
  judge freshness from it directly.
- **Reader opt-out is built in.** Setting `data-freshness-display='off'` on
  `:root` hides all ribbons — the hook for the reader-preference toggle whose
  default state is one of the two open questions above.

## Machine-readable surface

Per the recipe's `ai_hint`, the same freshness data the ribbon renders is emitted
as structured data: each section's `WebPageElement` JSON-LD node carries a
per-section `dateModified`, plus an `additionalType` of `FreshSection`,
`StaleSection`, or `ArchivedSection`. The threshold parameters are documented in
the wiki's `llms.txt`, so an external AI consumer knows what "fresh" means on this
substrate rather than guessing. (The emission itself is engine work —
project-knowledge scope, not this vault's.)

## Related

- [Citation Authority Ribbon](/components/citation-authority-ribbon/usage) — the
  sibling per-article annotation from the same project-knowledge draft series,
  classifying an article's references list.
- [Home Grid](/components/home-grid/usage) — the Knowledge Platform wiki's
  category-browse front door.
- [Knowledge Platform overview](/products/knowledge-platform/overview) — the
  product surface this component lives on.
