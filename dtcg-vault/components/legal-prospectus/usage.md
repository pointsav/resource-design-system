<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">7 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Print-first · WeasyPrint</span>
</div>
<p class="doc-header__lead">A print-first document template for a Canadian NI 41-101 preliminary
(&ldquo;red-herring&rdquo;) prospectus. Seven page variants carry one filing from cover to
glossary in an austere Bay-Street register: a serif reading face, a four-step rule-weight
ladder, a running header, and the statutory red-herring notice. This is a page-geometry and
typography template rendered to PDF, not an interactive UI control.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/legal-prospectus/recipe.json</code></div>
</div>

## What this template is

`legal-prospectus` describes the layout of a Canadian preliminary prospectus filed under
**National Instrument 41-101, *General Prospectus Requirements***. A preliminary prospectus
is the unpriced, pre-final document a securities regulator reviews before a distribution is
qualified; its cover carries the statutory *red-herring* notice from which the document takes
its informal name. This page documents how the design system renders that document — page
geometry, the rule-weight ladder, and per-section typography — drawn from a real delivered
filing and iterated across twelve operator-reviewed render passes.

It is a member of the [Paper](/paper/paper/overview) print-token pillar. Where a UI component
documents when to click a control, a Paper template documents how a page is set: margins,
rule weights, type sizes, and the order of sections down the page. There are no interaction
states — the template renders to a fixed PDF through WeasyPrint.

It shares the Paper pillar with five sibling document families, each documented separately:
[legal-subscription-agreement](/components/legal-subscription-agreement/usage),
[legal-agency-suite](/components/legal-agency-suite/usage),
[financial-report-layout](/components/financial-report-layout/usage),
[financial-statement-yearend](/components/financial-statement-yearend/usage), and
[interactive-pdf-binder](/components/interactive-pdf-binder/usage). The prospectus is a
*distinct register* from the subscription-agreement family it sits closest to: it adds a
running header and the red-herring notice, and it links its CSS externally rather than inline.

## When to use

Use this template when the deliverable is a preliminary prospectus or a document of the same
regulatory register — a long-form, statutorily-structured filing that opens with a cover and
red-herring notice, carries a table of contents and a summary, and closes with financial
tables and a defined-terms glossary. The seven variants below are the canonical page types;
a filing is assembled by selecting the variant appropriate to each section.

Do not reach for this template for a subscription agreement or an agency (underwriting)
agreement — those are the [legal-subscription-agreement](/components/legal-subscription-agreement/usage)
and [legal-agency-suite](/components/legal-agency-suite/usage) families, which have no running
header and a different type scale. Do not use it for financial statements presented on their
own; those are the two `financial-*` families.

## Variants

The template ships seven page variants. Each is one section of the filing, set to its own
local conventions but sharing the family's geometry, rule ladder, and serif reading face.

| Variant | Section | Layout notes |
|---|---|---|
| **cover-page** | Cover | Red-herring notice; cover-title hierarchy (issuer = offering 14pt &gt; doc-type 12pt &gt; 10pt); 15pt price headline; offering table; price-to-public data table. |
| **toc** | Table of contents | All-caps entries, spaced dot-leader (CSS `leader('. ')`), right-aligned folio. |
| **prospectus-summary** | Summary | 28/72 two-column summary table; `rule.emphasis` page border; dilution-sensitivity (DHS) sub-tables. |
| **section1-preamble** | Front matter | Header-free front matter — Eligibility for Investment, Forward-Looking Information, Non-IFRS Measures. |
| **body-section** | Body | `"PRELIMINARY PROSPECTUS"` running header (GCPM `running()`/`element()`) + folio, hairline border beneath. |
| **financials** | Financial tables | Data table with subtotal (hairline) / total (accounting-total double rule) distinction, footnotes, sup/sub numerals. |
| **glossary** | Defined terms | Definition-list glossary (`dl`/`dt`/`dd`). |

## Page geometry

Geometry resolves to the Paper pillar's primitive page dimensions. All three values are real
production settings, not defaults:

| Token | Resolves to | Applies to |
|---|---|---|
| `paper.semantic.prospectus.page-margin-top` | `0.75in` (`page.margin-standard`) | Top and bottom margins, body pages |
| `paper.semantic.prospectus.page-margin-inline` | `0.625in` (`page.margin-narrow`) | Left and right margins |
| `paper.semantic.prospectus.cover-margin-top` | `0.375in` (`page.margin-cover-top`) | Cover page top margin only |

This matches the Prospectus row of the Paper pillar's [document-families table](/paper/paper/overview):
0.75in standard, 0.625in inline, on letter-size stock.

## Rule-weight ladder

The prospectus draws on the Paper pillar's four-step [rule-weight ladder](/paper/paper/overview)
— hairline 0.5pt, light 0.75pt, standard 1pt, emphasis 1.5pt — and extends it by one rung for
one specific job. Three semantic tokens pin the family's rule usage:

| Token | Rung | Weight | Job |
|---|---|---|---|
| `paper.semantic.prospectus.running-header-border` | hairline | `0.5pt` | Rule beneath the running header on body pages |
| `paper.semantic.prospectus.summary-page-border` | emphasis | `1.5pt` | Full page border on the summary variant |
| `paper.semantic.prospectus.total-row-rule` | accounting-total | `2pt` | Double rule beneath a financial-table total row |

The `2pt` accounting-total is the family's one extension beyond the base ladder — the same
double-rule convention the Paper pillar notes for a prospectus data-table total row. Within
the `financials` variant this rule carries meaning: a *subtotal* is set with the hairline,
a *total* with the accounting-total double rule, so the two are distinguishable without a
label.

## Typography

Two tiers, both set in the family's serif reading face — `serif-legal`
(`Times New Roman, Liberation Serif, Times, serif`). The prospectus uses no separate form-fill
sans face; unlike the subscription-agreement family, it has no fill-in fields.

| Token | Size / weight | Detail |
|---|---|---|
| `paper.semantic.prospectus.body-type` | 10pt / 400 | Line-height 1.35. Reading text. |
| `paper.semantic.prospectus.heading-type` | 12pt / 700 | Line-height 1.2. Section headings. |
| `paper.semantic.prospectus.running-header-type` | 8.5pt / 400 | Letter-spacing 0.5pt. `"PRELIMINARY PROSPECTUS"` running header. |

The `cover-page` variant sets its own local hierarchy above the body scale — issuer name at
the offering size of 14pt, document type at 12pt, a supporting line at 10pt, and a 15pt price
headline. That cover hierarchy is specific to the cover; body pages return to the 10pt / 12pt
pairing above.

The 10pt body and the austere heading treatment are a deliberate Bay-Street *filing register*
choice — not a regulatory requirement. NI 41-101 prescribes no type sizes; the register is a
house decision and should be described as such, never attributed to the regulation.

## The running header

The `"PRELIMINARY PROSPECTUS"` running header is unique to this family among the three
legal-document families — subscription-agreement and agency-suite have none. It is set through
Generated Content for Paged Media (`running()` / `element()`), paired with the page folio, and
underlined by the hairline `running-header-border`. Front matter is deliberately header-free:
the `section1-preamble` variant carries no running header, matching the filing convention that
the eligibility and forward-looking front matter runs clean before the numbered body begins.

## The red-herring notice

The cover carries the statutory red-herring notice set in `paper.semantic.prospectus.red-herring-ink`,
which resolves to `paper.primitive.color.regulatory-red-herring` — `#c00000`. This is a genuine
BCSC/OSC filing convention (the &ldquo;red herring&rdquo; designation for a preliminary, unpriced
prospectus), **not a brand color**. It is modeled deliberately outside every brand-color group so
that other design-system tenants do not inherit a securities-filing color as if it were a brand
choice. Do not fold this token into a brand palette in any future review.

## Accessibility

This is a print document rendered to PDF, so the interaction concerns of a UI control —
keyboard focus, activation, disabled states — do not apply. Print-accessibility for the
generated PDF rests on document structure:

- **TOC entries are real anchor links** with descriptive text, never &ldquo;click here.&rdquo;
  The dot-leader is CSS-generated and decorative; the accessible name is the section title.
- **Financial tables use `<table><caption>`** plus `<th scope>` so that a total or a
  price-to-public figure is announced with its row and column headers rather than read as a
  loose number.
- **The red-herring notice stays in the accessibility tree.** It is required statutory
  disclosure, not decoration, and must remain reachable — it is never rendered as a background
  image or presentational-only element.

The recipe declares a WCAG 2.2 AA target for the generated document. The recipe does not
specify PDF/UA tagging beyond the structural requirements above; that is not claimed here.

## Rendering

Print-first and static. The template renders to PDF through WeasyPrint and has no interaction
states, hover, focus, or motion. Page furniture — running header, folio, page borders — is
produced through paged-media CSS (`@page`, `running()`/`element()`, `leader()`, `counter(page)`),
not through client-side script.

## Open questions

Carried from the recipe, unresolved here:

- **Red-herring token scope.** `#c00000` is a confirmed brand-neutral, standalone regulatory
  token (BCSC/OSC convention). It must not be folded into any brand palette during future review.
- **Distribution shape.** This family links its CSS externally, differing from the
  subscription-agreement family's inline-CSS convention. This is a cross-cutting Paper-pillar
  question, not resolved at the component level.
- **Type-scale attribution.** NI 41-101 prescribes no type sizes. The 10pt / austere-heading
  register is a deliberate Bay-Street filing-register choice; do not cite the regulation as the
  reason for the type scale in any exemplar copy.

<div class="doc-footer-meta">
<span>part of</span> <a href="/paper/paper/overview">Paper — print-token pillar</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>tokens:</span> <a href="/tokens#paper">Tokens — Paper tier</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>research:</span> <code>research/legal-prospectus-token-map.md</code>
</div>
