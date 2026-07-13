---
schema: foundry-design-research-v1
component_or_token: legal-prospectus
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-documents DESIGN-TOKEN-CHANGE_prospectus-formatting_JW12.md — 17 research passes, cross-checked against 5 real Canadian securities law firms (Stikeman Elliott, Blake Cassels, McCarthy Tétrault, Osler Hoskin, Fasken), operator-iterated JW1 through JW12 (12 render passes)
ai_consumption_hint: "The most rigorously-vetted Paper source found in this consolidation pass. Confirms NI 41-101 prescribes no type sizes — the family's austere 10pt register is a deliberate Bay-Street filing-register choice. The red-herring #c00000 notice is a genuine BCSC/OSC statutory convention, not a brand color, and must stay brand-neutral for other design-system tenants."
---

# Legal Prospectus (NI 41-101) — token consolidation rationale

Of the three legal-agreement-family source drafts, this one is the most extensively
researched — 17 research passes, independently cross-checked against 5 real Canadian
IPO law firms' public guidance, refined across 12 operator-reviewed rounds (JW1-JW12).
Its underlying values were treated as highly reliable during consolidation.

## Key findings

- **Running header** (`"PRELIMINARY PROSPECTUS"`, 8.5pt, letter-spacing 0.5pt) is unique
  to this family among the three legal-document families — subscription-agreement and
  agency-suite have no running header.
- **Red-herring notice** (`#c00000`) is a real statutory filing convention (the
  "red herring" designation for a preliminary, unpriced prospectus), not brand-derived.
  Modeled as `paper.primitive.color.regulatory-red-herring` — deliberately outside any
  brand-color group, since this design system also ships to other tenants who must not
  inherit a securities-filing color as if it were a brand choice.
- **Distribution shape**: production convention for this family links CSS externally,
  differing from subscription-agreement's inline-CSS convention. Not yet normalized
  across the Paper pillar — flagged as an open question on the recipe, not resolved here.
- Shares the serif font stack byte-identically with legal-subscription-agreement; shares
  the rule ladder (with a `+2pt double` accounting-total extension) and the
  `"- " counter(page) " -"` footer format with the wider legal-agreement family.

## Terminology precision

Per `BRIEF-wcp-style-guide.md` (project-documents' authoritative defined-terms
glossary): "Agents"/"Agency Agreement" (never "Underwriters"/"Underwriting Agreement");
"CAD X" (never "$X"); "US" (never "U.S."); "Qualified Jurisdictions". Any exemplar copy
built from this component should nonetheless use neutral placeholder terms, not real
WCP-specific figures found in the source draft.
