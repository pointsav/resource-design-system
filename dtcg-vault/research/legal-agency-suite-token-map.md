---
schema: foundry-design-research-v1
component_or_token: legal-agency-suite
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-documents DESIGN-TOKEN-legal-agency-suite.md (explicitly mirrors legal-subscription-agreement's structure) + DESIGN-COMPONENT_agency-form.md
ai_consumption_hint: "The most readable-register of the three legal-agreement families (11.5pt/1.5 line-height, Tinos webfont) — uniform 1in margins, no binding asymmetry. Shares the rule ladder and per-schedule named-counter page-numbering pattern with legal-subscription-agreement; uses the \\2014 em-dash escape where subscription-agreement mandates a literal em-dash character — a real, unreconciled inconsistency, not drift to silently fix."
---

# Legal Agency Suite — token consolidation rationale

This family (MOU / Engagement Letter / Schedules A-E) was the thinnest of the three
legal-agreement source drafts — its own frontmatter states it "mirrors the token
structure of DESIGN-TOKEN-legal-subscription-agreement.md," and it was developed less
independently than the prospectus or subscription-agreement families.

## Key findings

- Uniform 1in margin on all four sides (no binding asymmetry, unlike
  legal-subscription-agreement's 0.9in/0.7in left/right split).
- Body type is the most generously readable of the three families: 11.5pt / 1.5
  line-height, Tinos webfont-first stack (`Tinos, Times New Roman, Liberation Serif,
  Times, serif`) — a genuinely distinct register from the other two families' dense
  fill-in-booklet or filing-document registers.
- Adds a 3pt "accent" rule weight (form-note left accent bar) not present in the other
  two families — kept as its own primitive rather than forced to reuse the prospectus's
  2pt accounting-total rule, since the two serve visually and semantically different
  purposes (an accent bar vs. an accounting double-rule).
- **Real, unreconciled inconsistency**: this family uses the `\2014` em-dash escape,
  while legal-subscription-agreement's source explicitly warns that `\2014` swallows the
  trailing space in WeasyPrint and mandates a literal UTF-8 em-dash character instead.
  Flagged on the recipe as an open question — not resolved here, since resolving it
  would require re-testing both families' actual WeasyPrint output.
- `pdf-home-button` marker geometry referenced in the source draft is a tool-contract
  with `tool-pdf-interactive.py` (see the `interactive-pdf-binder` component's own
  research file) — not a token or recipe concern of this component.
