---
schema: foundry-design-research-v1
component_or_token: org-chart-print
decision_type: token-consolidation
authored: 2026-07-30
authored_by: totebox@project-design
authored_with: claude-opus (project-documents' original draft), claude-fable-5 (project-documents' independent coverage review), claude-sonnet-5 (landing synthesis)
status: ratified
source: project-documents DESIGN-COMPONENT_org-chart-print.md (2026-07-22, coverage-reviewed same day)
ai_consumption_hint: "org-chart-print's token values are the Mexico FIBRA prospectus reference implementation's own real, delivered values — not invented, not yet exercised by a second jurisdiction. A generation agent authoring a new DHS jurisdiction's org chart should read the component's own usage.md (the three named gotchas, the geometry-generator guidance, the canvas-width/page-margin relationship) before assuming these exact hex values are mandatory — role colors are consumer-assigned per document."
---

# org-chart-print — landing notes (2026-07-30)

## Why this landed now, not when the draft first arrived (2026-07-22)

The draft's own `oq-1` left the token namespace undecided ("should the role-band fills
promote as a new `paper.semantic.org-chart.*` family, or reuse an existing paper
palette?"). project-design resolved the namespace question quickly (`paper.semantic.org-chart.*`,
matching every other document family's own convention) and told project-documents so — but
held the actual landing, because the draft's role-color values (`role-green: #54924E`,
`role-blue: #164679`, `role-orange: #F15F22`, `role-vehicle`/amber `#EAB308`) are the exact
same hex values caught up in a real, unrelated governance conflict discovered the same
session: `theme-woodfine.css`'s own chart palette had a stale `--wf-amber` (`#F57F17`,
abandoned by org-chart itself back on 2026-06-06 in favor of `#EAB308`) and a genuine
green-name collision with `woodfine-media-assets`' separate AEC-compliance palette.
Landing `org-chart-print` before that resolved risked baking in a value that would need
correcting out from under it within the same session.

## What the 2026-07-30 chart-color reconciliation actually found (resolving this draft's oq-4)

Two real, independently-approved chart families exist, not one:

1. **The Client A org-chart family** (`theme-woodfine.css`'s own `--wf-*` variables) —
   green `#198038` (IBM Carbon Green 70, operator-approved 2026-06-03), amber-turned-yellow
   `#EAB308` (corrected 2026-07-30 from a stale `#F57F17` theme-woodfine.css never picked up
   after org-chart's own 2026-06-06 rename).
2. **The Mexico FIBRA prospectus org chart** (this component's reference implementation) —
   green `#54924E`, blue `#164679`, orange `#F15F22`, vehicle/amber `#EAB308`.

These are **not the same palette drifting apart** — they're two separately-delivered real
documents that each made their own real, defensible role-color choice, confirmed by reading
both source files directly rather than assuming one is stale because it differs from the
other. `org-chart-print`'s token defaults are the Mexico FIBRA values specifically (the only
values this component's *own* reference implementation actually uses); a future Client-A-style
chart built on this component would supply its own role-color set, not silently inherit
Mexico's.

This also resolves the draft's own `oq-4` ("should project-design ratify one canonical
role-color legend across all DHS jurisdictions, or leave it per-document?"): **per-document.**
The draft's own body text already argued for this ("Roles are consumer-defined... A
different jurisdiction assigns its own role→color mapping; the class names carry no
Mexico-specific meaning") — landing confirms that architecture rather than overriding it
with a forced single legend.

## What landed vs. what stayed exactly as drafted

Landed close to verbatim — the draft's own research (2 independent AI passes, one a
dedicated coverage-review pass that caught and corrected a real token error, an
undocumented third node shape, an omitted geometry-generator reference, and an
unparameterized hardcoded width) needed no further correction. The three named gotchas,
the `transform: scale()` anti-pattern analysis, and the canvas-width/page-margin
relationship all landed as written.

**Not landed, per the draft's own explicit scoping:**
- A hierarchical no-percentage layer-tree variant (oq-3) — draft recommended waiting for a
  real second-variant need; still waiting.
- A named modifier for the third "Edificios Woodfine" rounded-rectangle shape (oq-5) — one
  real instance is not enough evidence to promote a one-off into a named pattern.
- The inline-CSS-vs-external-link distribution question (oq-2) — a cross-cutting Paper
  pillar question already open on `legal-prospectus`, not decided per-component.

## Research trail

### Done (5)
- Confirmed no `paper.semantic.org-chart` namespace collision existed before this landing.
- Confirmed `paper.primitive.font.serif-legal` (the Times/Liberation-Serif/Times stack)
  already exists and is the correct reuse target for the org-chart title/legal/alias/country
  type zones, rather than defining a new font primitive.
- Read both real source files directly (`theme-woodfine.css`, this draft's role-color
  values) rather than assuming the collision found during the chart-color reconciliation
  extended to this component's own values — confirmed it does not; Mexico's green/#54924E
  is a real, separate, correctly-attributed value, not the same drift.
- Verified the draft's own coverage-review corrections (grey border-vs-edge-ink split,
  the third undocumented node shape, the geometry-generator authoring path, the
  unparameterized `label-max-width`) all still held and needed no further correction at
  landing time.
- Cross-checked the amber/yellow correction made during the 2026-07-30 chart-color
  reconciliation (`theme-woodfine.css`) against this component's own `role-vehicle` value
  (`#EAB308`) — confirmed they now coincidentally match (both trace to the same real
  org-chart yellow decision), not a forced alias.

### Open questions (3, all carried from the original draft, unresolved by design)
- oq-2: inline-CSS distribution vs. `legal-prospectus`'s external-link convention — a
  cross-cutting Paper pillar question, tracked on `legal-prospectus`, not here.
- oq-3: second (hierarchical) variant threshold — wait for a real second use case.
- oq-5: third node shape (`border-radius: 12px` rounded-rectangle) — wait for a second real
  instance before naming a modifier class.
