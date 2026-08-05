<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">6 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print-first (WeasyPrint) proforma / projection dashboard document
register — letter-landscape, dense, horizontal-rules-only, with a single filled
section-banner row. Lays out multi-period projections at up to eleven columns
per table. One of six templates in the <a href="/paper/paper/overview">Paper</a>
document-family register.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/financial-report-layout/recipe.json</code></div>
</div>

## What this template is

Financial Report Layout is a **print document register**, not a screen widget.
It describes the page geometry, rule-weight usage, typography, and semantic-row
treatment of a real proforma / projection dashboard as it prints through
[WeasyPrint](/paper/paper/overview) to a letter-landscape PDF.

It is a **sibling of, not a synonym for,**
[Financial Statement (year-end)](/components/financial-statement-yearend/usage).
The two share the Paper pillar's rule-weight ladder and pagination discipline
but diverge deliberately on three axes recorded in the recipe:

| Axis | Financial Report Layout | Financial Statement (year-end) |
|---|---|---|
| **Page geometry** | Letter **landscape** | Portrait |
| **Density** | Up to **11 period columns** per wide table | Up to 3 |
| **Tone** | Horizontal rules only; one filled section-banner row | Pure black-on-white |

Reach for this template when the deliverable is a forward-looking projection
dashboard that must show many periods side by side. For a statutory,
compliance-register financial statement, use the year-end sibling instead.

## V5 canonical spec — one applied system, not a provisional second theme

Earlier drafts of this register described a real "dashboard" theme alongside a
provisional "statement" theme gated on unfinished engine work. A 2026-07-16
design audit corrected and unified both into the single system documented
below, applied to and verified against the live proforma engine's canonical
renderer across the whole document family. Treat every value
on this page as final, not provisional.

## Variants

The register defines six variants — each a real structural mechanism of the
canonical spec, not a stylistic grouping.

| Variant | Role |
|---|---|
| **`masthead`** | `position:relative` masthead with an absolutely-pinned draft stamp (never floated — a floated stamp lets long description text wrap under it). `h1` carries `string-set:doctitle` for the running header. A single "All amounts CAD" line is the document's only currency mention. |
| **`wide-table-alignment`** | `table.wide` + `table-layout:fixed`, label column pinned to 24%, restated inside `@media print`. Alignment is scoped to a *group* of same-shaped tables, not the whole document — a document may hold more than one aligned group. `tabular-nums lining-nums` mandatory on every cell. |
| **`semantic-rows`** | Horizontal-rules-only: header = 1.5px bottom rule, subtotal = 1px top rule, total = 2px top+bottom rule — none filled. `tr.section-banner` is the **only** filled row. |
| **`line-number-gutter`** | Server-rendered at generation time — **not** JavaScript-injected (WeasyPrint does not execute JS, so a client-side gutter never reaches the primary PDF target). |
| **`section-block-pagination`** | `section.block{break-inside:avoid}` wraps every heading+note+table+footnote group. One tallest statement per document may flow instead, so a short section's page fills rather than stranding white space. Running header/footer via `@top-left`/`@top-right`/`@bottom-center`. |
| **`chart-beside-table`** | `table.layout` for any chart-beside-table or two-up band — never flexbox (WeasyPrint overlaps nested flex onto adjacent content). |

## Page geometry

Four independent margins — not a symmetric inline/block pair:

- `{paper.semantic.financial-report-layout.page-margin-top}` — 1.05cm
- `{paper.semantic.financial-report-layout.page-margin-right}` — 1.1cm
- `{paper.semantic.financial-report-layout.page-margin-bottom}` — 1.2cm (kept larger for the `@bottom-center` page-number line)
- `{paper.semantic.financial-report-layout.page-margin-left}` — 1.1cm

Page numbers run **`@bottom-center`** as `counter(page) " / " counter(pages)`,
suppressed on `@page :first`. This is a deliberate divergence from the
year-end register's own `@bottom-center` Notes-only convention in content, not
placement — both are correct for their own family (recipe `oq-2` in the prior
draft is now resolved: V5 settled on `@bottom-center` for this family too, with
a running header carrying the doctitle/draftstamp instead of a right-aligned
counter).

## Rule-weight ladder usage

Financial Report Layout draws from the Paper pillar's rule-weight ladder rather
than defining its own weights:

- **`header-rule`** — `{...header-rule}` → `emphasis` (1.5pt) — `th` bottom rule, no fill.
- **`subtotal-rule`** — `{...subtotal-rule}` → `standard` (1pt) — `tr.subtotal` top rule, no fill.
- **`total-rule-top`** / **`total-rule-bottom`** — both → `accounting-total` (2pt) — `tr.total` top **and** bottom rule, no fill.
- **`hairline-rule`** — `{...hairline-rule}` → `hairline` (0.5pt) — interior dividers.
- **`cell-divider-color`** — the faint `#e3e3e3` default `th`/`td` border-bottom underlying every cell.

## Typography

Explicit px scale, no rem/px mixture, all on the Carlito stack
(`{paper.primitive.font.proforma-sans}` — Calibri-metric; the render host needs
`fonts-crosextra-carlito` installed):

| Token | Size | Notes |
|---|---|---|
| `h1-type` | 17px | Document title; carries `string-set:doctitle`. |
| `h2-type` | 13px | Statement section. |
| `h3-type` | 11.5px | Sub-section. |
| `h4-type` | 10.5px | Sub-sub-section. |
| `body-type` | 10px | Narrative prose. |
| `note-type` | 9.5px italic | Inline caveats / basis-of-preparation notes. |
| `table-type` | 10px | Table cells — `tabular-nums lining-nums` mandatory. |

## Semantic-row fills and inks

Colour is confined to a small, deliberate set of tokens. Every emphasised row
is paired with a weight or rule treatment so colour is never the sole signal
(see [Accessibility](#accessibility)):

| Token | Applies to |
|---|---|
| `{...row-banner-bg}` | Section-banner fill — the **only** filled row (`#f2f4f7`). Ink is plain `ink-primary`, not a dedicated navy. |
| `{...row-total-rule}` | Total-row top/bottom rule colour. |
| `{...row-subtotal-rule}` | Subtotal-row top rule colour. |
| `{...ink-primary}` | Primary body ink. |
| `{...ink-secondary}` | Secondary / supporting ink. |
| `{...ink-hairline}` | Hairline-rule ink. |
| `{...ink-gutter}` | Line-number gutter ink (screen only). |
| `{...column-label-width}` | Label column width — 25%. |

Full token detail: [Tokens — Paper tier](/tokens#paper).

## Accounting formatting (not CSS)

Negatives render in parentheses — `($1.54M)`, `(19K)`, `$(0.77)` — a
formatter-level rule (`fmt_*` helpers), not a token. Nil renders as an
em-dash `—`, never blank or `0`. Currency is a plain `$`, stated exactly once
near the title (a single "All amounts CAD" masthead line) — not per-figure,
not in table titles.

## Content patterns (composition, not tokens)

Three reusable prose/composition patterns, applied as recipe guidance rather
than DTCG tokens (they are compositional signals specific to a document's
content, not visual constants):

- **Optional-overlay section spacing** — an optional/alternate-scenario
  section gets an inline `style="margin-top:14px"` on its own `section.block`.
- **External-reference note** — one `p.note` after a table, naming the source
  document and giving only the one-sentence consequence; never re-derive the
  source document's own figures inline.
- **Forward-computed fixed-sum disclosure** — when a figure is a fixed gross
  sum rather than solved backward from a net target, state that explicitly and
  what it is not conditioned on.

Full rationale: [Research — Financial Report Layout](/tokens#paper) §9.

## Accessibility

Because this is a print artifact, accessibility here means **tagged-PDF
structure and print contrast**, not keyboard or focus behaviour:

- **Table semantics.** Wide tables use `<table><caption>` naming the reporting
  period range, plus `scope="col"` on column headers and `scope="row"` on
  `td.lbl` cells.
- **Presentational gutter.** The line-number gutter is `aria-hidden` —
  decorative, carries no data relationship.
- **WCAG 2.2 AA target.** Horizontal-rules-only theme is pure black-on-white
  except the single section-banner fill; total/subtotal/section-banner roles
  are never colour-only — each also carries a distinct border weight and
  font-weight.

## Print output and motion

Print-first static document — no interactive states. Renders via WeasyPrint
(`fonts-crosextra-carlito` required on the render host) or Chromium
print-to-PDF.

## Open questions and known live defect

- **oq-1 — six sibling renderers still ship the pre-V5 defect.** A 2026-07-23
  audit of the proforma engine's report-rendering family found the canonical
  CSS applied to only one of nine report-rendering renderers. Six others
  still ship the exact bug V5 fixed. In those files, `system-ui` silently falls back to DejaVu Sans
  under WeasyPrint, and the JS-injected line-number gutter never reaches a
  WeasyPrint PDF at all. **This is a live defect in compliance documents
  currently being generated.** It is not fixed in this token landing, which
  was scoped to the design artifact only — see
  [Research — Financial Report Layout](/tokens#paper) §10 for the full table.
- **oq-2 — deep-linkable line numbers.** Still open; the gutter is currently
  presentational only.
- **oq-3 / oq-4 — two files confirmed correctly out of scope.**
  `d1_dev_classes_v2.rs` is a structural variant, not a drifted copy.
  `forecast_statements.rs` (a separate proforma-engine report renderer) is a
  legitimately distinct classic-statement family aligned with the year-end
  sibling, not this component.

## Related

- [Paper pillar — overview](/paper/paper/overview) — rule-weight ladder, geometry, and document-families table this register inherits.
- [Financial Statement (year-end)](/components/financial-statement-yearend/usage) — the portrait, black-on-white statutory sibling.
- [Proforma Vehicle Layout](/components/proforma-vehicle-layout/usage) — the composition pattern built on this register.
- [Legal Prospectus](/components/legal-prospectus/usage) · [Legal Subscription Agreement](/components/legal-subscription-agreement/usage) · [Legal Agency Suite](/components/legal-agency-suite/usage) — the legal-document families in the Paper register.
- [Interactive PDF Binder](/components/interactive-pdf-binder/usage) — the navigation-overlay register.
- [Tokens — Paper tier](/tokens#paper) — all leaf tokens backing this template.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/financial-report-layout/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/component-financial-report-layout.md</a>
</div>
