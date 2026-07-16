<div class="doc-header">
<span class="eyebrow">Components &middot; Paper</span>
<div class="doc-header__badges">
<span class="badge">6 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print-first (WeasyPrint) securities
subscription-agreement document template for accredited-investor and
Family &amp; Friends offerings. One recipe covers both structural
variants of the offering type — they differ only in which schedule
variants and per-schedule named page counters are present, not in base
geometry or type.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/legal-subscription-agreement/recipe.json</code></div>
</div>

## What this template is

Legal Subscription Agreement is a **paper**-category registry entry: a
document layout, not a UI widget. It was extracted from real delivered
subscription-agreement documents and renders to PDF via WeasyPrint —
there are no interaction states, no hover, no focus rings. What the
system specifies instead is page geometry, a rule-weight ladder, a
two-tier typography contract, and the anatomy of the fill zones a
subscriber completes by hand or on screen before printing.

This family is the reference implementation of the Paper pillar's core
primitives. The two-tier typography samples on the
[Paper overview](/paper/paper/overview) — 9.5pt Times New Roman /
Liberation Serif body against 10pt Verdana / Tahoma fill-labels — are
drawn from this exact family, and the four-step rule-weight ladder
documented there (hairline 0.5pt &rarr; light 0.75pt &rarr; standard
1pt &rarr; emphasis 1.5pt) maps directly onto this template's
key-terms tables, fill lines, form cells, and warning boxes.

## When to use

- **A securities subscription agreement** for an accredited-investor
  offering or a Family &amp; Friends offering. The template's two
  structural shapes cover both; select by including the schedule
  variants the offering type requires.
- **Any legal-agreement document that pairs dense serif body text with
  subscriber-completed fill zones** — the tier-2 sans-fill register and
  the fill-label / fill-line / fill-hint anatomy generalize within the
  legal-agreement token family.
- **Prescribed-form write-in schedules** in the consolidated
  NI 45-106 family, via the `prescribed-form-writein` variant's fixed
  write-in cell heights.

## When not to use

- **Not for a prospectus.** The cover variant carries an explicit
  "not a prospectus" warning box; prospectus-register documents use
  [Legal Prospectus](/components/legal-prospectus/usage), which has its
  own margins, 10pt body size, and distribution convention.
- **Not for agency or engagement letters.** That register is
  [Legal Agency Suite](/components/legal-agency-suite/usage) — wider
  1in margins, larger 11.5pt body, and a different em-dash convention
  (see open question oq-2 below).
- **Not for financial reporting.** Statement and report layouts live in
  [Financial Statement — Year-End](/components/financial-statement-yearend/usage)
  and [Financial Report Layout](/components/financial-report-layout/usage).
- **Not for screen-first surfaces.** This is a static print document.
  If the output is an interactive PDF with a navigation layer, see
  [Interactive PDF Binder](/components/interactive-pdf-binder/usage).

## Variants

The recipe ships six variants. Together they compose a complete
subscription-agreement document: a cover, two execution blocks, two
schedules, and a prescribed-form write-in register.

| Variant | Role in the document | Description |
|---|---|---|
| **cover-key-terms** | Cover page | H1 + subtitle, key-terms table, completion checklist, "not a prospectus" warning box (`rule.emphasis` border). |
| **subscriber-execution** | Subscriber signing | Tier-2 accessible fill-section: fill-label / fill-line / fill-hint pairs in fill-cols layout, sans-fill font for legibility. |
| **corporate-acceptance** | Issuer acceptance | Full-width fill-label-sm &rarr; fill-line &rarr; signature-attribution block (not fill-cols). |
| **schedule-a-usa-joinder** | Schedule A | US-accredited-investor joinder schedule — DATED-AT hand-blank spans, party execution. |
| **schedule-b-category** | Schedule B | Accredited-investor category schedule — category letter / description / initials-box table. |
| **prescribed-form-writein** | Prescribed form | Consolidated NI 45-106-family prescribed-form write-in cells (`f9-writein` 0.5in, `f9-sign` 0.62in, `f9-writein-lg` 0.92in, `initials-head`) — the cell border doubles as the write line. |

The offering-type split is structural, not stylistic: an
accredited-investor package and a Family &amp; Friends package assemble
different subsets of the schedule variants and carry per-schedule named
page counters accordingly. Base geometry and type are identical in both
shapes — one `css_class` (`paper-legal-subscription`), one token set.

## Page geometry

The legal-agreement family renders on Letter at **0.75in standard
margins**, with a **0.7–0.9in bind** margin variant for documents bound
along one edge (values per the
[Paper document-families table](/paper/paper/overview)). Margins are
tokenized per edge:

- `{paper.semantic.legal-agreement.page-margin-top}`
- `{paper.semantic.legal-agreement.page-margin-right}`
- `{paper.semantic.legal-agreement.page-margin-bottom}`
- `{paper.semantic.legal-agreement.page-margin-left}`

Dimension values in the Paper tier use pt/in/cm — a deliberate,
documented print-domain extension of the DTCG dimension unit set (see
the [Paper overview](/paper/paper/overview) for the rationale).

## Rule-weight ladder in this family

Three of the ladder's four steps are tokenized for this family, each
with one canonical role:

| Token | Ladder step | Used for |
|---|---|---|
| `{paper.semantic.legal-agreement.rule-fill-line}` | Light | Fill-line enclosures — the blank a subscriber writes on. |
| `{paper.semantic.legal-agreement.rule-form-cell}` | Standard | Form cells and signature lines, including the prescribed-form write-in cells where the cell border doubles as the write line. |
| `{paper.semantic.legal-agreement.rule-warning-box}` | Emphasis | The cover's "not a prospectus" warning box (`rule.emphasis` border). |

The hairline step (0.5pt) serves the family's key-terms table borders
and running-header rules per the shared ladder on the
[Paper overview](/paper/paper/overview); it is consumed from the shared
ladder rather than aliased into this family's semantic set.

## Typography — the two-tier contract

Reading text and fill zones never share a face. This is the rule the
whole Paper pillar's two-tier typography principle was grounded in, and
this family supplies the reference values:

| Tier | Token | Face and size |
|---|---|---|
| **Body** | `{paper.semantic.legal-agreement.body-type}` | Times New Roman / Liberation Serif, 9.5pt — dense agreement prose. |
| **Headings** | `{paper.semantic.legal-agreement.heading-type}` | Serif heading register paired with the body face. |
| **Fill labels** | `{paper.semantic.legal-agreement.fill-label-type}` | Verdana / Tahoma sans stack, 10pt — every fill zone, deliberately larger and sans-serif. |

Ink and placeholder marking are tokenized alongside:
`{paper.semantic.legal-agreement.ink}` and
`{paper.semantic.legal-agreement.placeholder-mark}`.

The rationale: a fill-in field should never be mistaken for printed
body copy, and the person completing the form — often reading at arm's
length, pen in hand — gets the more legible face. Live samples of both
tiers, set in this family's real values, are on the
[Paper overview](/paper/paper/overview).

## Anatomy of a fill zone

The execution variants compose fill zones from three parts:

1. **Fill label** — sans-fill face (`fill-label-type`), naming what
   goes in the blank. The corporate-acceptance variant uses the
   smaller `fill-label-sm` register.
2. **Fill line** — the rule the subscriber writes on
   (`rule-fill-line`), or, in the prescribed-form variant, a fixed-
   height cell whose border doubles as the write line.
3. **Fill hint** — supplementary guidance paired with the label in the
   subscriber-execution variant.

Two layout modes exist: **fill-cols** (paired columns, used by
subscriber-execution) and **full-width** (label &rarr; line &rarr;
signature-attribution stack, used by corporate-acceptance). The
schedule-a-usa-joinder variant additionally uses DATED-AT hand-blank
spans for date-and-place execution lines.

## Accessibility

The WCAG target is **2.2 AA**, and for a print document the
accessibility surface is specific: **the fill zones**. Per the recipe:

- Fill-in form fields use real `<label>`/`<input>` or
  contenteditable-safe markup with associated labels — not
  placeholder-only text. The tier-2 sans-fill register exists
  specifically for completion accessibility: 10pt Verdana / Tahoma
  against the 9.5pt serif body.
- Schedule tables use `<table>` with `<th scope="col">`, so the
  category-letter / description / initials-box structure of Schedule B
  survives into assistive contexts.

Interaction-state accessibility (focus order, keyboard activation)
does not apply — this is a static document rendered to PDF. The recipe
makes no claims about tagged-PDF output from WeasyPrint, and none are
made here.

## Rendering

Print-first static document — no interaction states; renders to PDF
via WeasyPrint. The WeasyPrint dependency is load-bearing, not
incidental: see oq-1 below.

## Open questions

Carried verbatim from the recipe's `open_questions`; these gate reuse
decisions, so they are published rather than buried:

- **oq-1** — F9/F12 prescribed-form cell height-as-minimum only holds
  in WeasyPrint's table model; it would need re-verification if a
  browser-print distribution path is ever added.
- **oq-2** — em-dash convention: this family mandates a literal UTF-8
  em-dash (and warns that `\2014` eats the trailing space in
  WeasyPrint); this must be reconciled against
  [Legal Agency Suite](/components/legal-agency-suite/usage), which
  uses `\2014`, before any shared draft-stamp recipe is built.
- **oq-3** — distribution shape (inline vs. externally-linked CSS)
  differs from the
  [Legal Prospectus](/components/legal-prospectus/usage) family's own
  convention; not yet normalized across Paper.

## Related

- [Paper overview](/paper/paper/overview) — pillar landing page; its
  rule-weight ladder and two-tier typography samples are grounded in
  this family.
- [Tokens — Paper tier](/tokens#paper) — full leaf-token detail for
  `paper.semantic.legal-agreement.*`.
- Sibling document families:
  [Legal Prospectus](/components/legal-prospectus/usage),
  [Legal Agency Suite](/components/legal-agency-suite/usage),
  [Financial Statement — Year-End](/components/financial-statement-yearend/usage),
  [Financial Report Layout](/components/financial-report-layout/usage),
  [Interactive PDF Binder](/components/interactive-pdf-binder/usage).
- Source research: <code>dtcg-vault/research/legal-subscription-agreement-token-map.md</code>.

<div class="doc-footer-meta">
<span>depends on:</span>
<a href="/tokens#paper">paper.semantic.legal-agreement.page-margin-*</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.rule-form-cell</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.rule-fill-line</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.rule-warning-box</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.body-type</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.heading-type</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.fill-label-type</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.ink</a>,
<a href="/tokens#paper">paper.semantic.legal-agreement.placeholder-mark</a>
</div>
