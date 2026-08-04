Print/document-formatting tokens for regulated documents — page geometry, a
four-step rule-weight ladder, two-tier typography, and pagination counters.
Consolidated from real, production-grounded drafts across three document
sub-domains: legal agreements, financial statements, and interactive PDF
navigation. Dimension values use pt/in/cm — this is the design system's first
print-native token domain. The DTCG 2025-10 draft documents its dimension unit set
as px/rem only, so pt/in/cm are a deliberate, documented print-domain extension
the print CSS these tokens drive genuinely needs.

## What Paper tokenizes

<div class="card-grid">
<div class="card"><span class="card__eyebrow eyebrow">Geometry</span><h3>Page geometry</h3>
<p>Letter-size dimensions, margins per document family (standard/narrow/wide/bind/cover),
header and footer distances — all real production values, not defaults.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Rules</span><h3>Rule-weight ladder</h3>
<p>A 4-step border-weight scale (0.5pt–1.5pt), shared identically across all five Paper
document families — three legal and both financial-statement families.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Typography</span><h3>Two-tier typography</h3>
<p>Each document family pairs a serif reading face for body/heading text with a distinct
sans face reserved for form-fill zones — never the same face for both roles.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Pagination</span><h3>Pagination counters</h3>
<p>Real coordinate primitives for the interactive PDF-binder's table-of-contents layer —
entry position, step, height, width — driving a real navigation overlay, not a mockup.</p></div>
</div>

## Rule-weight ladder

The core 4-step ladder, identical across every legal and financial-statement family:

<div class="rule-ladder">
<div class="rule-ladder__item"><span class="rule-ladder__label">hairline · 0.5pt</span><hr class="rule-ladder__sample" style="border-top-width: 0.5pt;"></div>
<div class="rule-ladder__item"><span class="rule-ladder__label">light · 0.75pt</span><hr class="rule-ladder__sample" style="border-top-width: 0.75pt;"></div>
<div class="rule-ladder__item"><span class="rule-ladder__label">standard · 1pt</span><hr class="rule-ladder__sample" style="border-top-width: 1pt;"></div>
<div class="rule-ladder__item"><span class="rule-ladder__label">emphasis · 1.5pt</span><hr class="rule-ladder__sample" style="border-top-width: 1.5pt;"></div>
</div>

Hairline: key-terms table borders, running-header rules, statutory subtotal
rules. Light: fill-line enclosures, financial-report subtotal rules.
Standard: form cells, signature lines, grand-total top rules. Emphasis:
warning boxes, cover rules, summary-page borders. Two families extend the
ladder further still — a prospectus data-table total row uses a 2pt double
rule, and an agency-suite form-note accent bar uses 3pt.

## Two-tier typography

Every document family keeps reading text and form-fill zones in
deliberately different faces — a fill-in field should never be mistaken
for printed body copy.

<div class="type-sample-grid">
<div class="type-sample"><div class="type-sample__label">Body text — subscription agreement</div>
<p class="type-sample__text" style="font-family: 'Times New Roman', 'Liberation Serif', Times, serif; font-size: 9.5pt; font-weight: 400; line-height: 1.28;">This Subscription Agreement is entered into as of the date set forth below, by and between the parties identified in the signature block, for the purpose of subscribing to the securities described herein.</p></div>
<div class="type-sample"><div class="type-sample__label">Fill-in label — subscription agreement</div>
<p class="type-sample__text" style="font-family: Verdana, Tahoma, 'DejaVu Sans', sans-serif; font-size: 10pt; font-weight: 400; line-height: 1.35;">Subscriber name: ______________________<br>Date: ____ / ____ / ______<br>Signature: ______________________</p></div>
</div>

## Document families

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Family</th><th>Page margin</th><th>Body face</th></tr></thead>
<tbody>
<tr><td>Legal agreement (subscription)</td><td>0.75in standard, 0.7–0.9in bind</td><td>Times New Roman / Liberation Serif, 9.5pt</td></tr>
<tr><td>Prospectus</td><td>0.75in standard, 0.625in inline</td><td>Times New Roman / Liberation Serif, 10pt</td></tr>
<tr><td>Agency suite</td><td>1in wide</td><td>Tinos / Times New Roman, 11.5pt</td></tr>
<tr><td>Financial statement (year-end)</td><td>1in wide</td><td>Calibri / Carlito, statutory sans</td></tr>
<tr><td>Financial report layout</td><td>2cm inline, 1.5cm block</td><td>system-ui (dashboard theme)</td></tr>
<tr><td>PDF binder navigation</td><td>72pt–540pt content zone (US Letter, 612×792pt)</td><td>Helvetica / Arial, core-14 PDF fonts</td></tr>
</tbody>
</table>
</div>

<p class="doc-footer-meta">Full token detail: <a href="/tokens#paper">Tokens — Paper tier</a> (164 real leaf tokens). Source research: <code>dtcg-vault/research/*-token-map.md</code> in the design-system repository.</p>
