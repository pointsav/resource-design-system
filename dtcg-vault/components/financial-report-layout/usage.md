<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">8 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print-first (WeasyPrint) proforma / projection dashboard document
register — letter-landscape, dense, with tinted semantic-row fills and a single
navy section banner. Extracted verbatim from a delivered financial-report
deliverable, it lays out multi-period projections at up to eleven columns per
table. One of six templates in the <a href="/paper/paper/overview">Paper</a>
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
| **Tone** | Tinted semantic-row fills + navy banner | Pure black-on-white |

Reach for this template when the deliverable is a forward-looking projection
dashboard that must show many periods side by side. For a statutory,
compliance-register financial statement, use the year-end sibling instead.

## Two internal themes

The register ships two themes. They are **not** equally final — treat this
distinction as load-bearing.

- **`dashboard`** — the delivered, real theme. Tinted total/subtotal/banner
  rows, a navy section banner, `system-ui` type, and the on-screen line-number
  gutter. Every token value here is production-grounded.
- **`theme-statement`** — a **PROVISIONAL** classic-compliance theme: serif
  stack, no fills, a single-then-double rule convention. Its token values
  (`*-statement-theme`) are gated on not-yet-implemented proforma-engine work
  (`BRIEF-client-a-proforma-engine-recapitalization.md`). Do not treat the
  statement theme as final or commit its values as canonical without
  re-verifying against the engine once it lands. See
  [Provisional surfaces](#provisional-surfaces-and-open-questions) below.

## Variants

The register defines eight variants. Each is a real structural element of the
delivered document — never invent a ninth.

| Variant | Role |
|---|---|
| **`masthead`** | H1 + draft-status line + BCSC-compliance footer scaffold. |
| **`narrow-table`** | Input / summary-metric tables — few columns. |
| **`wide-table`** | Multi-period fixed-layout table — up to 11 data columns; label column 25% (dashboard) / 22% (statement-theme bundle, provisional). |
| **`section-banner`** | Full-width navy-ink section header row (`row-banner-bg` fill, `row-banner-ink` text — the only colored text in the family). |
| **`subtotal-row`** | Subtotal row — tinted fill + top hairline rule. |
| **`total-row`** | Total row — stronger tint + top standard rule. |
| **`line-gutter`** | JS-injected line-number gutter, Courier New, 32px — dashboard / screen only; absent from the print (WeasyPrint) output and from the statement theme entirely. |
| **`theme-statement`** | PROVISIONAL classic-compliance theme — serif stack, no fills, single-then-double rule convention. Gated; not equally final to `dashboard`. |

## Page geometry

The dashboard theme prints letter-landscape with margins driven by two tokens:

- `{paper.semantic.financial-report-layout.page-margin-inline}` — inline
  (left / right) margin.
- `{paper.semantic.financial-report-layout.page-margin-block}` — block
  (top / bottom) margin.

In the Paper pillar's [document-families table](/paper/paper/overview), this
register's margin is recorded as **2cm inline, 1.5cm block** — a landscape
geometry distinct from the year-end sibling's portrait page.

Page numbers run **`@bottom-right` as a standard running counter**. This is a
deliberate divergence from the year-end register's `@bottom-center`, Notes-only
convention — both are correct for their own family and are **not** drift to
reconcile (recipe `oq-2`).

## Rule-weight ladder usage

Financial Report Layout draws from the Paper pillar's four-step
[rule-weight ladder](/paper/paper/overview) — hairline 0.5pt · light 0.75pt ·
standard 1pt · emphasis 1.5pt — rather than defining its own weights. Its row
treatments map onto that ladder as follows:

- **`subtotal-row`** — tinted fill plus a **top hairline rule**
  (`{paper.semantic.financial-report-layout.row-subtotal-rule}`, dashboard
  theme).
- **`total-row`** — a stronger tint plus a **top standard rule**
  (`{paper.semantic.financial-report-layout.row-total-rule}`, dashboard theme).
- The shared **`hairline-rule`** token
  (`{paper.semantic.financial-report-layout.hairline-rule}`) carries key-line
  borders throughout.

The **statement theme** replaces these with its own single-then-double rule
convention through three provisional tokens —
`subtotal-rule-statement-theme`, `total-rule-statement-theme`, and
`total-rule-bottom-statement-theme` — whose values are gated (see below).

## Typography per section

| Section | Face | Notes |
|---|---|---|
| Body (dashboard theme) | `system-ui` | The register's default reading face; see the [Paper families table](/paper/paper/overview). |
| `section-banner` text | Navy banner ink | `{...row-banner-ink}` — the **only** colored text anywhere in the family. |
| `line-gutter` | Courier New, 32px | Monospaced line numbers; screen-only, `aria-hidden`. |
| Body (statement theme) | Serif stack — **PROVISIONAL** | Exact stack is gated on the proforma engine (`oq-1`). |

## Semantic-row fills and inks

The dashboard theme's colour is confined to a small, deliberate set of tokens.
Every fill is paired with a weight or rule treatment so colour is never the sole
signal (see [Accessibility](#accessibility)):

| Token | Applies to |
|---|---|
| `{...row-total-bg}` | Total-row fill (stronger tint). |
| `{...row-subtotal-bg}` | Subtotal-row fill (lighter tint). |
| `{...row-banner-bg}` | Section-banner fill (navy). |
| `{...row-banner-ink}` | Section-banner text — the family's only colored text. |
| `{...ink-primary}` | Primary body ink. |
| `{...ink-secondary}` | Secondary / supporting ink. |
| `{...ink-hairline}` | Hairline-rule ink. |
| `{...ink-gutter}` | Line-number gutter ink (screen only). |
| `{...column-label-width}` | Label column width — 25% dashboard / 22% statement (provisional). |

Full token detail for all seventeen leaf tokens: [Tokens — Paper tier](/tokens#paper).

## Accessibility

Because this is a print artifact, accessibility here means **tagged-PDF
structure and print contrast**, not keyboard or focus behaviour. The recipe
carries real `aria` and `wcag` guidance:

- **Table semantics.** Wide tables use `<table><caption>` naming the reporting
  period range, so a screen reader reading the tagged PDF announces the span a
  table covers. Section-banner rows use `<th scope="colgroup">` where they span
  the full table width.
- **Presentational gutter.** The line-number gutter is `aria-hidden` — it is
  decorative and carries no data relationship, so it is excluded from the
  accessibility tree.
- **WCAG 2.2 AA target.** The recipe records a `2.2 AA` target with the note
  that the dashboard theme's tinted semantic rows (total / subtotal / banner)
  are **never colour-only differentiators** — each also carries a distinct
  font-weight and rule treatment, so the total / subtotal / banner distinction
  survives greyscale printing and colour-vision differences.

## Print output and motion

This is a **print-first static document**. The `dashboard` theme also renders
on-screen, where the `line-gutter` feature appears; there are no interactive
states beyond that. The gutter is the one element that exists on screen but not
in the WeasyPrint PDF — everything else is identical between the two surfaces.

## Provisional surfaces and open questions

Two items from the recipe must travel with anyone consuming this register:

- **`oq-1` — statement theme is provisional.** The statement theme's serif font
  stack and exact column split (22% + 10 × 7.8%) are `wcp.finance.*` bundle
  values gated on unfinished proforma-engine Rust work. **Do not commit these as
  final** without re-verifying against the engine once it lands.
- **`oq-2` — page-number placement is intentional.** `@bottom-right` here vs.
  `@bottom-center` in the year-end register is a deliberate, correct divergence
  per family — not drift to reconcile.

## Related

- [Paper pillar — overview](/paper/paper/overview) — rule-weight ladder, geometry, and document-families table this register inherits.
- [Financial Statement (year-end)](/components/financial-statement-yearend/usage) — the portrait, black-on-white statutory sibling.
- [Legal Prospectus](/components/legal-prospectus/usage) · [Legal Subscription Agreement](/components/legal-subscription-agreement/usage) · [Legal Agency Suite](/components/legal-agency-suite/usage) — the legal-document families in the Paper register.
- [Interactive PDF Binder](/components/interactive-pdf-binder/usage) — the navigation-overlay register.
- [Tokens — Paper tier](/tokens#paper) — all seventeen leaf tokens backing this template.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/financial-report-layout/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/financial-report-layout-token-map.md</a>
</div>
