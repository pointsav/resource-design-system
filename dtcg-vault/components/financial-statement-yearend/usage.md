<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">7 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Print-first · WeasyPrint</span>
</div>
<p class="doc-header__lead">A print-first statutory year-end financial-statement
template — the Notice to Reader / compilation register (CSRS 4200) —
deep-extracted from a real private compilation-template docx and a real
audited financial-statement PDF from a major firm. Portrait letter,
symmetric 1in margins, pure black-on-white: the restrained, dense
audited-statement register. A sibling of
<a href="/components/financial-report-layout/usage">financial-report-layout</a>,
not the same register — different geometry, density, and tone.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/financial-statement-yearend/recipe.json</code></div>
</div>

## What this template is

This is not a UI widget. It is a page template in the
[Paper](/paper/paper/overview) document family — a WeasyPrint print
stylesheet (`paper-financial-yearend`) that renders a complete set of
statutory year-end financial statements to PDF. Its layout decisions were
deep-extracted from two real sources: a private compilation-engagement
template (docx) and a real audited financial-statement PDF from a major
firm. Every
geometry value, rule weight, and column ratio below traces to one of those
two documents, via the token map in
`research/financial-statement-yearend-token-map.md`.

The register it reproduces is the Canadian compilation-engagement register
— statements issued under CSRS 4200, historically titled "Notice to
Reader." The template reproduces that register's *visual* conventions;
whether a given document satisfies the standard is an engagement question
for the practitioner, not a property of the stylesheet.

## When to use

- **A statutory year-end statement set.** Balance sheet, income statement,
  changes in equity, cash flows, and accompanying notes, assembled into
  one bound PDF with a cover.
- **The compilation / audited look.** Symmetric 1in margins, portrait
  letter, pure black ink on white. If the document needs the restrained,
  dense, pure-black-on-white audited-statement register, this is the
  family.

## When not to use

- **Management-reporting or dashboard-style financial documents.** That is
  [financial-report-layout](/components/financial-report-layout/usage) —
  a sibling family, deliberately *not* the same register. The two differ
  in geometry, density, and tone; do not mix conventions between them.
- **Legal instruments with fill-in zones.** Signature-and-form documents
  belong to the legal families:
  [legal-subscription-agreement](/components/legal-subscription-agreement/usage),
  [legal-prospectus](/components/legal-prospectus/usage),
  [legal-agency-suite](/components/legal-agency-suite/usage).
- **Multi-document navigation shells.** Assembling several documents
  behind a clickable table of contents is
  [interactive-pdf-binder](/components/interactive-pdf-binder/usage).

## Variants

Seven variants cover the full statement set, from cover page to signature
block. Names and descriptions below are the recipe's own.

| Variant | What it renders |
|---|---|
| **cover** | Title block (entity 16pt / "FINANCIAL STATEMENTS" 14pt / period), currency line, assurance-caveat box, draft/version stamp in a `@top-right` margin box on a named cover page (page-1 only). |
| **statement-financial-position** | Balance sheet — one continuous 3-column table (label 55% / value 22.5% / 22.5%, equal value-column widths). |
| **statement-income** | Statement of income/loss — same 3-column convention. |
| **statement-equity** | Statement of changes in equity/partners' capital — 4- or 5-column stacked roll-forward (40/20&times;3 or 36/16&times;4). |
| **statement-cash-flow** | Statement of cash flows — same 3-column convention as financial-position. |
| **notes** | Note blocks (h4 10pt bold); the ONLY section carrying page numbers (`@bottom-center` "- N -"), per this bundle's own adopted-from-legal-agreements convention. |
| **signature-block** | Side-by-side drawn-rule signature table (hairline bottom border, not underscores), cells 44% / 12% / 44%. |

## Page geometry

Portrait letter with symmetric 1in margins — the widest standard margin in
the Paper family table (compare the legal-agreement family's 0.75in). Three
tokens carry the geometry:

- `{paper.semantic.financial-statement-yearend.page-margin}`
- `{paper.semantic.financial-statement-yearend.header-distance}`
- `{paper.semantic.financial-statement-yearend.footer-distance}`

The cover renders as a *named* page-1-only page: the draft/version stamp
lives in a `@top-right` margin box that exists on that page alone, so a
final render drops the stamp without touching content flow.

## Rule-weight ladder

Financial statements speak in rules — a subtotal, a column header, and a
grand total are distinguished by border weight, not by color or fill. This
family draws its rules from the Paper pillar's shared
[4-step rule-weight ladder](/paper/paper/overview) (hairline 0.5pt / light
0.75pt / standard 1pt / emphasis 1.5pt), through six dedicated semantic
tokens:

| Token | Role |
|---|---|
| `…running-header-rule-width` | Rule under the running page header |
| `…header-row-rule` | Column-header row in statement tables |
| `…subtotal-rule` | Section subtotals within a statement |
| `…grand-total-rule-top` | Rule above a statement's grand total |
| `…grand-total-rule-bottom` | Rule below a statement's grand total |
| `…signature-rule` | Drawn signature line in the signature-block variant |

Grand totals carry *separate* top and bottom rule tokens — the top and
bottom weights of a total row are independently addressable rather than
one shared border value. The signature rule is a drawn hairline bottom
border on the table cell — explicitly *not* a run of underscore
characters, which reflow unpredictably and read as fill-in blanks rather
than a rule.

All six tokens resolve at [Tokens — Paper tier](/tokens#paper).

## Typography

Two zones carry dedicated type tokens: the cover title block and the
running page header.

**Title block (cover).** Entity name at 16pt, the "FINANCIAL STATEMENTS"
report heading at 14pt, and the period line — via
`…title-entity-type`, `…title-report-heading-type`, and
`…title-subtitle-type`.

**Running header.** Every content page repeats entity, statement title,
and currency line through three running-header type tokens —
`…running-header-entity-type`, `…running-header-statement-type`,
`…running-header-currency-type` — implemented with CSS GCPM
`running()`/`element()` so the header content is lifted from the page's
own heading structure rather than duplicated by hand.

**Notes.** Note headings are h4, 10pt bold. The 10pt body size is
*inferred* from the source docx rather than explicitly extracted (the
relevant style carries no `w:sz`) — see open question oq-1 below before
treating it as final.

Ink is a single token — `…ink` — pure black-on-white, no tints. The Paper
pillar's [document-families table](/paper/paper/overview) records this
family's body face as Calibri / Carlito, the statutory sans.

## Statement tables

The three flow statements (financial position, income, cash flow) share
one convention: a single continuous 3-column table — label 55%, two
equal value columns at 22.5% each (current and comparative period). The
equity statement is the exception: a stacked roll-forward at 4 or 5
columns (40/20&times;3 or 36/16&times;4).

Seven tokens parameterize table internals:

- `…column-label-width`, `…column-value-width` — the 55 / 22.5 / 22.5 split
- `…cell-pad-x`, `…cell-pad-y` — cell padding
- `…num-min-width` — minimum width of numeric cells (105px), so a narrow
  render cannot reflow a figure into a misreadable wrap
- `…indent-1`, `…indent-2` — the two line-item indent levels
  (sub-account and sub-sub-account nesting)

Numeric cells are right-aligned with `tabular-nums`, so digits align in
columns regardless of the figures rendered.

## Pagination and running headers

Only the **notes** section carries page numbers — `@bottom-center`,
rendered as "- N -". This is a deliberate adoption *from* this workspace's
legal-agreement family rather than the audited sample's own bare-digit /
bottom-right convention — an intentional cross-family consistency choice,
recorded as open question oq-2 so the trade-off stays visible. The
statements themselves are unnumbered, matching the source register's
convention of numbering only the notes.

## Accessibility in print

This is a static print document — no interaction states, no focus order,
no keyboard behaviour. It renders to PDF via WeasyPrint. The recipe's
accessibility posture (WCAG 2.2 AA target) is about the *structure and
legibility* of the rendered document:

- **Statement tables are real tables.** Each uses `<table><caption>`
  naming the statement and period, so the table's identity survives into
  the PDF's structure rather than living only in visual layout.
- **Numbers cannot misread under reflow.** Numeric cells are
  right-aligned with `tabular-nums` and a 105px minimum width, preventing
  reflow-induced misreading of figures.
- **Running headers are decorative to assistive tech — correctly.** They
  are implemented via CSS GCPM `running()`/`element()`; the
  entity/statement/currency information is already present in the page's
  own heading structure, so the print engine's exclusion of the running
  header from the accessibility tree removes duplication rather than
  information.

Claims beyond these — screen-reader behaviour in specific PDF viewers,
tagged-PDF conformance levels — are not made by the recipe and are not
made here.

## Open questions

Carried verbatim from the recipe so consumers can weigh them:

- **oq-1** — The 10pt body size is inferred from the source docx, not
  explicitly extracted (no `w:sz` on the relevant style). Verify against
  a future source revision before treating it as definitively final.
- **oq-2** — The page-number convention (`@bottom-center` "- N -", Notes
  section only) was deliberately adopted from this workspace's
  legal-agreement family rather than the audited sample's own
  bare-digit/bottom-right convention — an intentional cross-family
  consistency choice, not an oversight.

## Related

- [Paper — the print token pillar](/paper/paper/overview) — rule-weight
  ladder, two-tier typography, page geometry across all document families
- [financial-report-layout](/components/financial-report-layout/usage) —
  the sibling financial family in the management-reporting register
- [legal-subscription-agreement](/components/legal-subscription-agreement/usage),
  [legal-prospectus](/components/legal-prospectus/usage),
  [legal-agency-suite](/components/legal-agency-suite/usage) — the legal
  document families
- [interactive-pdf-binder](/components/interactive-pdf-binder/usage) —
  multi-document PDF navigation
- [Tokens — Paper tier](/tokens#paper) — all 23
  `paper.semantic.financial-statement-yearend.*` tokens resolved

<div class="doc-footer-meta">
<span>last changed</span> <a href="/releases/changelog/overview">2026-07-16</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>depends on:</span>
<a href="/tokens#paper">paper.semantic.financial-statement-yearend.*</a> (23 tokens)
<span class="doc-footer-meta__sep">&middot;</span>
<span>research:</span> <code>research/financial-statement-yearend-token-map.md</code>
</div>
