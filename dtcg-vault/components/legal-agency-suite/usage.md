<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">7 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print-first (WeasyPrint) MOU / Engagement Letter /
Schedules A&ndash;E document template family &mdash; the most readable-register of the
three legal-document families (11.5pt / 1.5 line-height, Tinos webfont), with
uniform 1in margins. One of six templates in the
<a href="/paper/paper/overview">Paper</a> document-family register.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/legal-agency-suite/recipe.json</code></div>
</div>

## What this template is

Legal Agency Suite is a **print document register**, not a screen widget. It
describes the page geometry, rule-weight usage, typography, and structural
elements of a real MOU / engagement-letter document suite &mdash; proposal letter,
memorandum of understanding, body clauses, allocation/fee table, signature
block, and Schedules A&ndash;E &mdash; as it prints through WeasyPrint to a portrait PDF.
Its CSS class is `paper-legal-agency`.

It is one of **three legal-document families** in the Paper register, and it is
deliberately the most readable of the three:

| Axis | Legal Agency Suite | [Subscription Agreement](/components/legal-subscription-agreement/usage) | [Prospectus](/components/legal-prospectus/usage) |
|---|---|---|---|
| **Body type** | Tinos, **11.5pt / 1.5** | Times New Roman / Liberation Serif, 9.5pt | Times New Roman / Liberation Serif, 10pt |
| **Page margin** | **Uniform 1in**, no binding asymmetry | 0.75in standard, 0.7&ndash;0.9in bind | 0.75in standard, 0.625in inline |

(Sibling values from the Paper pillar's
[document-families table](/paper/paper/overview).)

Reach for this template when the deliverable is a memorandum of understanding,
an engagement letter, or a proposal letter with lettered schedules &mdash; a
correspondence-adjacent legal register meant to be read comfortably, not a
dense fill-in booklet or a filing document. For those, use the subscription-
agreement or prospectus sibling instead.

## Variants

The register defines seven variants. Each is a real structural element of the
delivered document suite &mdash; never invent an eighth.

| Variant | Role |
|---|---|
| **`proposal-letter`** | Logo letterhead (inline SVG), sender address block, non-binding notice. |
| **`mou-engagement-letter`** | Text letterhead, addressee block, RE line, salutation. |
| **`body-clauses`** | Parties/recitals section, decimal `<ol>` clause numbering, indented sub-clauses. |
| **`alloc-fee-table`** | Allocation/fee table &mdash; 0.75pt cells, surface-tint header fill, subtotal/total rows. |
| **`signature-block`** | Table-based signature block (Word-export-safe layout), approved-connector notation. |
| **`schedule-cover`** | Page-break schedule cover pages, per-schedule named counters (`apage`&hellip;`epage`). |
| **`drafting-notes`** | Internal change-log page &mdash; intended as a **removable final page before distribution**, not part of the executed document. |

Two of these carry governance weight worth restating:

- **`drafting-notes` never ships.** It is an internal change-log page whose
  whole purpose is to be removed before the document is distributed. Any
  pipeline consuming this register must treat it as a pre-distribution
  artifact, not executed-document content.
- **`schedule-cover` owns pagination.** Each schedule restarts its own named
  page counter &mdash; `apage` through `epage`, one per Schedule A&ndash;E &mdash; behind a
  page break. This per-schedule named-counter pattern is shared with the
  [subscription-agreement](/components/legal-subscription-agreement/usage)
  family (see its token-map research).

## Page geometry

The family prints with a **uniform 1in margin on all four sides**, driven by a
single token:

- `{paper.semantic.agency-suite.page-margin}` &rarr;
  `{paper.primitive.page.margin-wide}` (1in).

There is no binding asymmetry &mdash; unlike the subscription-agreement family's
0.9in / 0.7in left/right split. This is the "wide" margin geometry in the
Paper pillar's [document-families table](/paper/paper/overview), and it is part
of what makes this the most readable of the three legal registers.

## Rule-weight ladder usage

Legal Agency Suite draws from the Paper pillar's four-step
[rule-weight ladder](/paper/paper/overview) &mdash; hairline 0.5pt &middot; light 0.75pt &middot;
standard 1pt &middot; emphasis 1.5pt &mdash; and extends it once:

- **`alloc-fee-table` cells** sit at **0.75pt** &mdash; the ladder's *light* step.
- **Signature lines** use `{paper.semantic.agency-suite.rule-signature}` &rarr;
  `{paper.primitive.rule.standard}` (1pt) &mdash; the ladder's *standard* step, the
  same weight the Paper pillar assigns to signature lines across families.
- **The form-note accent bar** uses
  `{paper.semantic.agency-suite.form-note-accent}` &rarr;
  `{paper.primitive.rule.accent}` (**3pt**) &mdash; a ladder extension unique to
  this family. It was deliberately kept as its own primitive rather than
  forced to reuse the prospectus's 2pt accounting-total rule: an accent bar
  and an accounting double-rule are visually and semantically different
  things, even at adjacent weights.

## Typography per section

The family is single-face by design &mdash; one serif stack for both body and
headings, differentiated by size and weight rather than by face:

| Section | Token | Face and metrics |
|---|---|---|
| Body text | `{paper.semantic.agency-suite.body-type}` | Tinos (webfont-first, falling back through Times New Roman / Liberation Serif / Times / serif), **11.5pt / 1.5 line-height**, weight 400. |
| Headings | `{paper.semantic.agency-suite.heading-type}` | Same Tinos stack, **18pt / 1.2 line-height**, weight 700. |

The 11.5pt / 1.5 body register is the most generous of the three legal
families &mdash; a genuinely distinct reading register from the subscription
agreement's dense fill-in-booklet setting (9.5pt) and the prospectus's
filing-document setting (10pt).

## Clause numbering

The `body-clauses` variant numbers clauses with **real decimal `<ol>`
elements, not visual-only numerals**, with indented sub-clauses beneath. This
is a semantic decision, not a styling one &mdash; see
[Accessibility](#accessibility) below.

## Accessibility

Because this is a print artifact, accessibility here means **document
semantics that survive into the tagged PDF**, not keyboard or focus
behaviour. The recipe carries two real `aria` positions:

- **Clause numbering is semantic.** Clauses use real `<ol>` markup (not
  visual-only numerals) so assistive technology can announce clause position
  within the agreement.
- **The signature table is presentational.** The signature block uses
  `<table>` only for print / Word-export layout fidelity; where the table
  conveys no relational data, it carries `role="presentation"` so it is not
  announced as a data table.

The recipe records a **WCAG 2.2 AA target**.

## Print output and motion

This is a **print-first static document** &mdash; no interaction states. It renders
to PDF via WeasyPrint.

## Open questions

Two items from the recipe must travel with anyone consuming this register:

- **`oq-1` &mdash; em-dash convention is unreconciled.** This family uses the
  `\2014` CSS escape; the
  [subscription-agreement](/components/legal-subscription-agreement/usage)
  family mandates a literal UTF-8 em-dash character (its source warns that
  `\2014` swallows the trailing space in WeasyPrint). This is a real,
  recorded inconsistency &mdash; not drift to silently fix. It must be reconciled
  before any shared draft-stamp component is built, and resolving it requires
  re-testing both families' actual WeasyPrint output.
- **`oq-2` &mdash; pdf-home-button geometry is out of scope here.** The
  `pdf-home-button` marker geometry referenced in the source draft is a
  tool-contract with `tool-pdf-interactive.py` &mdash; see the
  [Interactive PDF Binder](/components/interactive-pdf-binder/usage)
  component &mdash; not a token or recipe concern of this component.

## Related

- [Paper pillar &mdash; overview](/paper/paper/overview) &mdash; rule-weight ladder, geometry, and document-families table this register inherits.
- [Legal Subscription Agreement](/components/legal-subscription-agreement/usage) &mdash; the dense fill-in-booklet legal sibling whose token structure this family mirrors.
- [Legal Prospectus](/components/legal-prospectus/usage) &mdash; the filing-document legal sibling.
- [Financial Report Layout](/components/financial-report-layout/usage) &middot; [Financial Statement (year-end)](/components/financial-statement-yearend/usage) &mdash; the financial-document families in the Paper register.
- [Interactive PDF Binder](/components/interactive-pdf-binder/usage) &mdash; the navigation-overlay register (and the home of the `oq-2` tool-contract).
- [Tokens &mdash; Paper tier](/tokens#paper) &mdash; all five semantic tokens backing this template.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/legal-agency-suite/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/legal-agency-suite-token-map.md</a>
</div>
