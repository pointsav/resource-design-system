<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">6 variants</span>
<span class="badge badge--brand">Composition pattern</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">The section order, prose conventions, and vehicle-specific mechanics a
single-entity investment-vehicle compliance proforma follows. Sits inside
<a href="/components/financial-report-layout/usage">Financial Report Layout</a>
(V5 canonical), which supplies every visual rule — this component never
restates fonts, colors, or print rules, only composition.</p>
<div class="registry-note"><span>Rendered from</span> <code>dtcg-vault/components/proforma-vehicle-layout/recipe.json</code></div>
</div>

## What this template is

`financial-report-layout` specifies the shell — fonts, table borders, page
geometry, the line-number gutter. It does not say what a **single-entity
investment-vehicle proforma** — a Club Deal, a Private SPV, or a comparable
corporation raising capital to acquire units of one underlying investment —
actually contains, in what order, or how its prose connects the tables. Three
reference documents (Club Deal Inc., Private SPV Inc., Commission Paths) converged
on the same composition independently, without a shared spec. This component
extracts that pattern so the next vehicle proforma starts from it instead of
re-deriving it.

Always use this **together with** `financial-report-layout` — this component
has no CSS of its own.

## When to use

Use this composition when the document is a **single-entity,
single-investment-vehicle** compliance proforma.

Do **not** use this for:
- A cross-vehicle comparison document with no single issuer — such a document
  legitimately uses only the `capital-structure` and `commission-waterfall`
  variants per vehicle/path, not the full six-section composition (see
  Commission Paths below).
- A statutory year-end financial statement — use
  [Financial Statement (year-end)](/components/financial-statement-yearend/usage)
  instead (serif, portrait, no line-number gutter, a different family
  entirely).
- An interactive sensitivity/scenario tool — that is a screen-first dashboard,
  out of scope for both this component and its parent shell.

## Section order

A single-entity vehicle proforma is five sections, in this fixed order — skip
a section only if it genuinely doesn't apply (e.g. a formation-only,
no-forecast document has no Income Statement or Return Summary); never
reorder:

| # | Variant | Role |
|---|---|---|
| 1 | **`capital-structure`** | The raise, any carried-interest share class, the underlying units held. The only section naming share counts and prices directly. |
| 2 | **`commission-waterfall`** | Formation-time cash waterfall, followed by one governance `p.note`. |
| 3 | **`income-statement`** | `table.wide`, Y0–Y10, ending in the fixed per-share rows. |
| 4 | **`return-summary`** | Y10-endpoint aggregate return metrics — never restates the annual rows. |
| 5 | **`basis-of-preparation`** | One closing `p.note` covering issuer, security, holdings, cost-recovery, tax treatment, cash-flow caveats. |

An optional sixth, **`form-note-overlay`**, follows the base sections when a
genuine alternate scenario exists.

The BCSC forward-looking-information footer (`financial-report-layout`'s
mandatory footer) follows section 5, outside this component's own sections.

## Per-share convention

The Income Statement's last two rows are always:

```
Distributions per share (per $100[, fully diluted][, after tax])
Value (NAV) per share (per $100[, fully diluted])
```

- **`per $100`** — always stated explicitly; never a bare "per share" with an
  implied $100 par.
- **`fully diluted`** — present only when the vehicle has a carried-interest
  share class. Apply the dilution factor (`investor_shares / diluted_shares`)
  to both rows so they tie to the Investment Return Summary's post-carry
  total. Absent entirely for a single-investor vehicle with no carry.
- **`after tax`** — present when the row reflects post-corporate-tax cash (it
  always does in this family). State it once in the row label, not per cell.

## Governance note

After the Commission Waterfall table, one `p.note` states, in order: the
cost-recovery relationship (what the Commission Rebate funds, capped with no
gross-up on the vehicle's own-cost piece), board composition (director count
and fee — state the *actual* relationship between vehicles once their rates
can diverge; never claim "same rate as X" once that can silently go stale),
then whether the vehicle carries a Programme Participant / carried interest.

## Optional — Form Note overlay

When a base document has a genuine alternate scenario (e.g. an Offering Cost
Fee overlay for a Programme-Participant-arranged deal), add it as a **separate
section after the base sections**, not interleaved:

```html
<section class="block" style="margin-top:14px">
  <h2>Form Note — <Scenario Name> (Optional Overlay; <who it applies to> Only)</h2>
  <p><!-- one paragraph: what triggers this scenario, what changes, what stays the same --></p>
  <h3><Entity> — Alternate Breakdown (<Scenario Name> Overlay)</h3>
  <table><!-- restate ONLY the waterfall table, on the new basis --></table>
</section>
```

Uses `financial-report-layout`'s V8 optional-overlay spacing (the
`margin-top:14px` inline style) to separate it from the base sections. Restate
only the table(s) that actually change.

## Worked example — five-section vehicle proforma

```html
<h1>Club Deals — Multi-Investor Proforma</h1>
<p>DRAFT — YYYY-MM-DD — Vn · All amounts CAD. <one-line description>.</p>

<h2>Capital Structure &amp; Investment Position</h2>
<table><!-- Item / Shares / Price / Capital --></table>

<h2>Commission Waterfall at Formation</h2>
<table><!-- Item / Note / Amount --></table>
<p class="note"><!-- governance note --></p>

<h2>10-Year Income Statement</h2>
<table class="wide"><!-- Y0..Y10, ending in the per-share rows --></table>
<p class="note"><!-- external-reference note, if applicable --></p>

<h2>Investment Return Summary (Y10 endpoint)</h2>
<table><!-- Metric / Aggregate [/ Per Share] --></table>

<p class="note"><strong>Basis.</strong> <!-- basis-of-preparation paragraph --></p>
<p class="footer"><!-- BCSC forward-looking footer, from financial-report-layout --></p>
```

## Worked example — formation-only, no-forecast variant

A cross-vehicle comparison document (no single issuer, no forecast) uses only
`capital-structure` and `commission-waterfall` per offering path — a narrow
waterfall table per path, each followed by its own one-line governance note,
plus the optional Form Note overlay when an alternate scenario exists. This is
a legitimate partial application, not a document forced into the full
five-section shape.

## Basis-of-preparation checklist

Every "Basis" paragraph covers, in order: issuer type → security issued →
what it holds and its carrying basis → cost-recovery mechanism (capped, no
gross-up) → tax treatment (rate, what's taxable now vs. deferred, pointer to
an external tax-treatment document if one exists) → any structural caveat
about early-year cash flow. Omit a clause only if it doesn't apply to the
vehicle, rather than stating "none."

## Accessibility and print output

Inherits `financial-report-layout` entirely — table semantics, WCAG 2.2 AA
target, print/motion behaviour. This component adds no new visual structure,
only section order and prose.

## Open questions

- **oq-1** — should the per-share row's `fully diluted` / `after tax`
  qualifier list be a fixed enum, or addable per-vehicle as new dilution/tax
  mechanics appear? Deferred — no second carried-interest class exists yet to
  design against.
- **oq-2** (suggested) — once a fourth vehicle type is built, re-verify this
  five-section composition against it before treating the order as fully
  locked — three data points is a reasonable start, not exhaustive.

## Related

- [Financial Report Layout](/components/financial-report-layout/usage) — the required parent shell (V5 canonical CSS, page geometry, line-number gutter).
- [Financial Statement (year-end)](/components/financial-statement-yearend/usage) — the statutory, portrait sibling; not a substitute for this composition.
- [Tokens — Paper tier](/tokens#paper) — this component defines no tokens of its own; all values come from financial-report-layout.

<div class="doc-footer-meta">
<span>rendered from</span> <code>dtcg-vault/components/proforma-vehicle-layout/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/proforma-reproducibility.md</a>
</div>
