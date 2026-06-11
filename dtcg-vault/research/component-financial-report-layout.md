# Research — Financial Report Layout

This file records why each decision in the financial-report-layout component
was made. A generation agent producing a proforma, income statement, book
valuation, or summary sheet should read this, then emit HTML/CSS that honours
the constraints.

## 1. Why `table-layout:fixed` + explicit label `width:25%`

**Problem:** A compliance financial report is several separate `<table>`
elements (Revenue, Costs, Capital, Returns), each with its own section heading
and page-break behaviour. With default `table-layout:auto`, each table sizes
columns to its own content, so "Y3" in the Revenue table lands at a different
x-position than "Y3" in the Costs table. The period alignment — the entire
point of a multi-year statement — is lost.

`table-layout:fixed` makes column widths a function of CSS rules, not cell
contents. Every `table.wide` resolves the same widths: label at 25%, the
remaining 75% divided across 11 data columns. Because the rule set is shared,
every wide table gets identical geometry and columns align without per-table
tuning.

The rule is **restated inside `@media print`** because some print engines
re-resolve table layout at print time and would otherwise revert to auto,
breaking alignment in the PDF.

**Codegen rule:** keep column count and label/data split identical across every
`table.wide` in a document.

## 2. Why `tr.total` / `tr.subtotal` / `tr.section-banner` as semantic classes

These are **roles**, not styles. Encoding them as classes (not inline):

1. Single source of visual truth — one edit changes every total.
2. Machine-readable — a tool can find every total with `tr.total`.
3. Non-colour differentiation — roles escalate by border weight and
   font-weight, not just fill, surviving greyscale print and colour vision
   deficiency.

**Codegen rule:** apply exactly one role class per emphasised row, on the
`<tr>`. Banner rows use `colspan="12"` over the 12 authored content columns.

## 3. Why `td.lnum` is injected by JS, not server-rendered

Line numbers are a property of the *rendered document*, not the *data*. Baking
them into source rows requires recomputation every time a row is added, removed,
or reordered. Client-side injection after layout means the number is always
correct for the document as rendered, continuous across all tables.

The `!important` flags on `.lnum` exist solely to win against the inherited
`tr.total` / `tr.subtotal` / `th` backgrounds and weights — the gutter must
read as a margin rule, not as a figure.

**Codegen rule:** emit data rows only. Append the injection script once at the
end of `<body>`. Do not author `.lnum` cells. Do not count the gutter in your
`colspan` values.

## 4. Why letter-landscape `@page`

A label plus 11 periods does not fit portrait at a legible size. Landscape is
the compliance print standard for multi-year statements. **Letter** (not A4)
because the audience is a North American securities context (BCSC); the
regulator and filers print on letter stock.

Margins `1.5cm 2cm 1.5cm 1.5cm` — the wider value on the bound/punch edge
leaves room for holes without eating the gutter or first data column.

**Codegen rule:** do not change `@page` for a compliance financial report.

## 5. Colour tokens and semantic meaning

| Value | Used by | Meaning |
|---|---|---|
| `#111` | body text | Primary ink |
| `#555` | `p`, `p.note` | Secondary ink — narrative subordinate to tables |
| `#333` | `h3` | Sub-heading ink |
| `#ccc` | borders, `h2` rule | Hairline grid |
| `#f5f5f5` | `th` background | Header band |
| `#aaa` / `#bbb` | `td.lnum` ink (screen / print) | Gutter numerals — faint, recedes |
| `#d0d0d0` / `#ccc` | gutter right border | Boundary: gutter / content |
| `#eef2f7` | `tr.total` fill | Heaviest emphasis. Bottom line |
| `#f5f7fa` | `tr.subtotal` fill | Lighter emphasis. Intermediate sum |
| `#e3edf7` | `tr.section-banner` fill | Most saturated. Names a block |
| `#1a2a44` | `tr.section-banner` ink | Dark navy — the only coloured text |
| `#888` | `tr.total` top border | Heavy rule above bottom line |
| `#aaa` | `tr.subtotal` top border | Lighter rule above intermediate sum |
| `#666` / `#ddd` | `.footer` ink / rule | Compliance notice, quietest block |

The three emphasis fills are one cool-blue family at three saturations — the
hierarchy reads as one coherent system. All three clear WCAG contrast against
`#111` / `#1a2a44` in print.

**Codegen rule:** do not recolour a role. If a brand theme overrides, keep the
three-saturation relationship intact.

## 6. Typography scale

| Element | Size | Rationale |
|---|---|---|
| `body` | 13px (11px print) | Base; steps down in print to fit landscape |
| `h1` | 1.25rem | Document title; one per document |
| `h2` | 1rem + hairline rule | Statement section |
| `h3` | 0.9rem | Sub-section, no rule |
| `p` | 0.82rem | Narrative — smaller than base, subordinate to tables |
| `p.note` | 0.78rem italic | Inline caveat |
| `table` | 0.76rem (10px print wide) | Smallest legible; maximises columns per page |
| `tr.section-banner` | 0.74rem uppercase | Header read at low height via uppercase + letter-spacing |
| `td.lnum` | 9px monospace | Below data size; reads as metadata |
| `.footer` | 0.72rem | Required but visually deprioritised |

`system-ui` throughout (no web-font dependency); `'Courier New'` monospace
on the gutter reads as a ruled margin.

**Codegen rule:** do not enlarge `p`; do not shrink table type below 0.76rem
screen / 10px print — figures clip below that with 13 columns on letter landscape.

## Research trail

### Done (6)
- Extracted CSS, line-number JS, and HTML patterns verbatim from the delivered
  WCP V2 proforma (primary source; polished over two sessions).
- Verified cross-table alignment depends on `table-layout:fixed` + shared 25%
  label width, and that the rule must be restated in `@media print`.
- Confirmed `!important` on `.lnum` is required to override inherited
  total/subtotal/header backgrounds.
- Confirmed the three emphasis fills are one blue family at three saturations
  and clear WCAG contrast against their text in print.
- Confirmed `print-color-adjust:exact` is required for gutter and fills to
  survive print.
- Confirmed colspan accounting: 12 authored content columns; gutter inserted
  by script outside the authored colspan.

### Suggested (2)
- Validate the letter-landscape margin asymmetry against a real binding/
  hole-punch sample.
- Test in at least one non-Chromium print engine to confirm fixed-layout
  alignment holds.

### Open questions (2)
- Should `td.lnum` be semantically addressable (e.g. an `id` per line) so a
  reviewer's "line 42" can deep-link, or does it remain purely decorative?
- For tables taller than one printed page: should we introduce repeating
  `<thead>` so the period header reprints on each page? Repeating headers
  would interact with the line-number injector (header rows would re-number).
