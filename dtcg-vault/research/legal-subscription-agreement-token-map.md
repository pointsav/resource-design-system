---
schema: foundry-design-research-v1
component_or_token: legal-subscription-agreement
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-documents DESIGN-TOKEN-legal-subscription-agreement.md + 6 DESIGN-COMPONENT drafts (subscription-form, subscription-form-template, subscription-form-familyandfriends-template)
ai_consumption_hint: "Subscription-agreement page geometry, rule ladder, and page-numbering convention are shared with legal-prospectus and legal-agency-suite (see paper/primitive.json's cross-family rule/page groups); type ladder and margins are genuinely family-specific, driven by document register (dense fill-in booklet), not by any securities regulation. The tier-2 sans-fill register exists specifically for accessible form completion — do not treat it as a stylistic choice."
---

# Legal Subscription Agreement — token consolidation rationale

Source drafts used a wrong `$schema` URL (`tr.designtokens.org/format/` instead of this
repo's real `schemas.designtokens.org/2025-10-01/draft.json`) and invalid `$type` usage
(`string`/`number`/`spacing`, `dimension:"letter"`). Every value was re-verified against
the source and re-enveloped in `paper/primitive.json` and `paper/semantic.json` — the
numbers are sound, only the DTCG wrapper needed correction.

## Shared vs. family-specific findings

- **Shared across all three legal families**: US Letter page size; the 0.5/0.75/1/1.5pt
  rule ladder; the `"- " counter(page) " -"` footer format; `#000` ink; the serif
  font stack (byte-identical to legal-prospectus); the per-schedule named-counter
  page-numbering pattern (shared with legal-agency-suite); the page-1-only draft stamp.
- **Genuinely family-specific**: page margins (0.75/0.7/0.75/0.9in — binding-asymmetric,
  left wider for the scan/bind edge) and the 9.5pt/1.28 type ladder. The type-ladder
  divergence across all three legal families is a deliberate document-register choice
  (dense fill-in booklet vs. Bay-Street filing vs. readable letter), confirmed **not**
  driven by any regulation (NI 41-101 prescribes no type sizes) — do not cite regulation
  as the reason for this family's type scale in any exemplar copy.

## Real bugs found in the source drafts (fixed, not silently propagated)

- `#C00000`-style regulatory colors and `letter`-as-dimension abuse — corrected.
- An em-dash-vs-`\2014` inconsistency exists between this family (mandates literal
  UTF-8 em-dash) and legal-agency-suite (uses `\2014`) — flagged as an open question,
  not silently reconciled to one convention.
- Dead CSS in the source (`.schedule-b .definitions-section p` selector that never
  matches a real element) was excluded from token promotion.

## Brand-neutrality note

The source drafts embed real Woodfine asset paths and real deal economics (Client A, WCP
deal figures). Per this archive's own asset-routing convention, Woodfine-specific brand
assets route to `woodfine-media-assets`, not the generic design system — any public
exemplar built from this component must use neutral placeholder copy and assets, not the
real figures found in the source drafts.
