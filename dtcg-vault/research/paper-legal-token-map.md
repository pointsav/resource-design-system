---
schema: foundry-design-research-v1
component_or_token: paper-legal
decision_type: new-component-taxonomy
authored: 2026-07-17
authored_by: totebox@project-design
authored_with: claude-sonnet-5
status: draft-pending-css-delivery
source: project-documents-20260717-consolidated-paper-legal-design-componen (supersedes project-documents-20260716-paper-legal-design-components-5-category and project-documents-20260717-commercial-variant-drafting-convention-r)
ai_consumption_hint: "This is a CONVENTION register, not a rendering stylesheet. A codegen agent asked to draft or reformat a legal document should first classify it into one of the 5 categories (commercial-agreement / constitutional-agreement / schedule-exhibit / letter / preliminary-instrument), then apply that category's heading form, 'Section'/'Article' presence rule, and cross-reference capitalization from the recipe's paper-legal-conventions token block — before touching any CSS. Two variants (schedule-exhibit, letter) overlap with the already-shipped legal-agency-suite component and are NOT yet reconciled — check both registers, do not assume this one is authoritative."
---

# Paper Legal — component taxonomy rationale

## Why this component exists

Every prior legal-document component in this vault (`legal-agency-suite`,
`legal-prospectus`, `legal-subscription-agreement`) is a *concrete* register:
real CSS backing a specific document type, built from a specific source draft.
None of them separately captures the *drafting convention* — heading form,
numbering scheme, cross-reference grammar — as a reusable rule set that
downstream authors (human or AI) can apply to a *new* document type without
re-deriving it from scratch or copying an existing register that may not
actually fit.

`paper-legal` is the first component built specifically to hold that
convention layer. It was requested by project-documents after a blind
two-reviewer (Opus + Fable) research pass grounded in filed-exhibit evidence
(EDGAR full-text search) and standard drafting-style authorities (Adams/MSCD,
Weagree, Canada Justice *Legistics*, US House *Manual on Drafting Style*),
cross-checked against a real pilot document (the Master Engagement Agreement,
JW8/JW9).

## Key findings from this session's build

- **The 5-category split is evidence-backed, not house style.** The
  commercial-vs-constitutional heading split (flat `Section` vs. `ARTICLE`)
  maps cleanly onto a real, observable pattern in filed agency/underwriting
  agreements vs. filed shareholder/LP agreements — see the citations list in
  the recipe and usage.md. This is a genuine reason to keep them as separate
  variants rather than collapsing to one generic "legal document" heading
  rule.
- **Real naming collision found, not silently resolved.** project-documents'
  own request refers to their local `templates/legal-agreement.css` as the
  Constitutional/Shareholder-Agreement base. This vault already has
  `paper.semantic.legal-agreement.*` tokens — but they back the *unrelated*
  `legal-subscription-agreement` component (accredited-investor fill-in
  booklets). Same name, two different document families, two different
  archives' independent naming choices colliding by coincidence. This
  component's `constitutional-agreement` variant deliberately does not bind
  to the pre-existing `legal-agreement.*` tokens for this reason — see `oq-1`
  on the recipe.
- **Two real overlaps with `legal-agency-suite`, flagged not merged.** That
  component's `schedule-cover` variant and its `proposal-letter` /
  `mou-engagement-letter` variants cover essentially the same ground as this
  component's `schedule-exhibit` and `letter` variants. Both components are
  now live with overlapping scope — this needs a reconciliation decision
  (which register is authoritative, or do they merge) that neither this
  session nor project-documents' original request resolved. Recorded as
  `oq-2`/`oq-3`.
- **Most token values are provisional by design, not by omission.**
  project-documents' own request explicitly defers CSS delivery ("Commercial
  first, from JW9... [others] to follow as we work each type"). This
  component's `paper.semantic.paper-legal.*` DTCG tokens therefore only bind
  the one thing stated with confidence (Tinos font family) plus generic rule
  weights already proven safe to reuse across the Paper pillar; every
  variant's heading-form/numbering/cross-ref rule lives instead in the
  separate `paper-legal-conventions` block, which is deliberately
  non-DTCG-typed string data (mirroring the existing `number-format` block's
  own precedent for the same kind of non-measurement convention data).
- **`preliminary-instrument` is genuinely new ground.** Unlike the other four
  variants, no existing component in this vault covers MOU/LOI/term-sheet
  documents at all — no reconciliation question needed there.

## What a downstream consumer should do

1. Classify the document into one of the 5 categories using the recipe's
   `variants` array descriptions.
2. Pull that category's heading-form / article-word / cross-ref-capitalization
   rule from `paper.semantic.paper-legal-conventions.<variant>`.
3. Apply the 9 family-wide drafting rules
   (`paper.semantic.paper-legal-conventions.drafting-rules-family-wide`)
   regardless of category.
4. For CSS: check whether project-documents has delivered the category's
   `templates/<name>.css` yet (only commercial-agreement is in progress as of
   this writing); if not, the convention rules above still apply even before
   CSS exists — draft to the rule, not to a stylesheet that doesn't exist yet.
5. If the category is `schedule-exhibit` or `letter`, also check
   `legal-agency-suite`'s `schedule-cover` / `proposal-letter` /
   `mou-engagement-letter` variants before building anything net-new — the
   overlap is unresolved, and building against both independently would
   create a third, worse inconsistency.
