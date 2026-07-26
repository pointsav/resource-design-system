---
schema: foundry-design-research-v1
component_or_token: financial-statement-yearend
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-proforma DESIGN-COMPONENT-financial-statement-yearend-bundle.draft.md (6 refinement phases) + BRIEF-bencal-financial-statements-yearend.md
ai_consumption_hint: "Fully real and finalized per its own BRIEF — deep-extracted from a real private compilation-template docx and a genuine PwC-audited PDF sample, reconciled against real Shareholders' Agreements. Deliberately adopted the '- N -' bottom-center page-numbering convention FROM this workspace's legal-agreement family rather than the PwC sample's own bare-digit/bottom-right style — a real, intentional cross-family consistency choice already made upstream of this consolidation, not invented here."
---

# Financial Statement — Year-End — token consolidation rationale

Of every Paper source consolidated in this pass, this is the most rigorously verified:
deep-extracted from a real private compilation-template docx and a genuine
PwC-audited PDF sample, cross-checked against real public-company SEC EDGAR
conventions (WELL Health Technologies Corp.), reconciled against real Client A-entity
Shareholders' Agreements across 6 refinement phases. Its own BRIEF records the
operator considering the formatting genuinely finalized.

## Key findings

- Portrait letter, symmetric 1in margins, pure black-on-white — the audited Big-Four
  look, with zero fills or tints anywhere (a hard contrast with the sibling
  `financial-report-layout` register's tinted semantic rows).
- Running-header typography (GCPM `running()`/`element()`, 12/11/9pt bold/regular/
  bold-italic) was deliberately tuned DOWN from the PwC-measured 14/12/10pt reference
  proportions after the larger sizes read too large in this bundle's own layout — a
  documented, deliberate refinement, not an inconsistency with the PwC source.
- Grand-total rule was deliberately upgraded from the source docx's single 1.5pt rule to
  a genuine double rule (1pt top + 3pt double bottom) — modeled as
  `paper.primitive.rule.total-double`, distinct from the source's original weight.
- Page-numbering convention (`@bottom-center "- N -"`, Notes section only) was
  deliberately adopted FROM this workspace's legal-agreement family, not from the PwC
  sample (which uses bare-digit/bottom-right) — confirms this is genuinely the strongest
  shared-primitive candidate across the whole Paper pillar, not a coincidence.
- 10pt body size is inferred, not explicitly present in the source docx's style
  definitions (no `w:sz` on the relevant style) — carried as an open question on the
  recipe, not silently presented as definitively extracted.

## Publication-gate note

This component's own BRIEF originally recorded an explicit operator publication gate
("NOT yet routed to project-design — operator-explicit publication gate"). That gate
was explicitly lifted by the operator during this consolidation initiative's planning
conversation (2026-07-13) — recorded here for the record, since the gate's existence
was real and load-bearing until that decision.
