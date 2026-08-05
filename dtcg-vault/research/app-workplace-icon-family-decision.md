---
schema: foundry-design-research-v1
component_or_token: app-workplace-icon-family
decision_type: brand-voice-decision
authored: 2026-07-30
authored_by: totebox@project-design
status: ratified
source: asset-app-workplace-icons-v1.draft.md (totebox@project-workplace, 2026-07-13)
ai_consumption_hint: "Decision record for the app-workplace-* desktop icon family. No
  artwork exists yet -- this file records the brand-voice call (differentiated family,
  not a uniform mark) and the concrete anchors a future image-generation pass should
  use. Do not treat this as a finished asset; it is the design brief."
---

# app-workplace-* icon family — decision (2026-07-30)

## The ask

project-workplace's draft (`asset-app-workplace-icons-v1.draft.md`) found the seven
`app-workplace-*` Tauri apps have no consistent icon source: one app (presentation) has
a genuine finished set, two (memo, proforma) have only unexecuted generation
instructions, three (workbench, gis, pdf) have nothing and a broken "copy from memo"
config reference that points at a source with nothing to copy. It asked project-design
to decide: one shared mark applied uniformly across all seven apps, or a differentiated
family (one shared style treatment, distinct per-app subject).

## Decision — differentiated family

Not a uniform mark. Precedent: PointSav's own home-page icon strip
(`ASSET-pointsav-icon-strip-redraw.draft.md`, project-marketing, 2026-07-11) was
corrected specifically *toward* Woodfine's 4-icon family model — one shared silhouette
treatment (solid black/near-black, `#231F20`, no outline/isometric styles, single blue
accent used consistently) but a **different subject per icon** (building skyline,
ledger/document motif, etc.), not the same icon four times. That's the established house
convention for an icon family in this design system, and it directly answers this
question the same way: shared treatment, differentiated subject.

Practically, it's also the right call independent of precedent — these are seven
distinct native desktop apps that will sit side by side in a dock/taskbar/Alt-Tab
switcher. A literally uniform icon makes the apps indistinguishable at the one moment
icon recognition actually matters. Marketing iconography (the product homepage
strips) doesn't have that constraint; app icons do.

## Anchors for the shared treatment

- **Style:** solid silhouette, not outline — matching the corrected
  house convention above, not memo's originally-proposed glyph-on-flat-background
  approach (a workable starting point, but predates the house silhouette convention
  being established).
- **Base color — graphite bronze `#c89a4a`, the already-ratified `--wp-accent` token**
  (`workplace-tokens-2026-06-02.md`), not memo's independently-proposed `#c8a96e`. The
  two values are nearly identical (both warm bronze/gold) — memo's instinct was
  directionally right and confirms the family already has a coherent identity, but the
  icon family should use the canonical token value, not a second, slightly-drifted one
  invented separately for icons alone. Same "one value, one source" discipline applied
  everywhere else in this vault.
- **Crop / silhouette weight discipline:** presentation's existing set is the only
  genuinely finished, distributable artifact in the family — use its proportions and
  crop as the shared frame's technical reference (it already survived a real `tauri
  icon` generation pass end to end), not its specific glyph.
- **Per-app subject (glyph inside the shared frame):**
  - `presentation` — keep its current mark; it becomes the reference implementation for
    the shared frame, not a redraw.
  - `memo` — the documented ✦ (U+2726) star glyph is a real, considered choice; keep it
    as memo's differentiator, re-rendered in the corrected bronze/silhouette treatment
    rather than invented fresh.
  - `proforma`, `workbench`, `gis`, `pdf`, `bim` (once activated) — each needs its own
    glyph reading as its function (e.g. a chart/ledger mark for proforma, a tool/wrench
    motif for workbench, a map-pin for gis, a document-page mark for pdf) — not decided
    here; a future image-generation pass should propose one candidate per app for
    review, not invent and ship in one step.

## What this is not

No artwork is attached or produced here — this session has no image-generation
capability, same limitation project-workplace's own draft already flagged. This is the
brand-voice decision the draft asked for, plus concrete anchors (style, color source,
crop reference) so a future pass with real generation capability doesn't have to
re-derive them. The three broken `tauri.conf.json` `_notes.icons` references and
proforma's mislabeled README stay unfixed until real per-app files exist, matching the
draft's own explicit scoping.

## Research trail

### Done (3)
- Confirmed the Woodfine/PointSav icon-strip precedent uses shared-treatment +
  differentiated-subject, not a uniform mark, resolving the open question by direct
  analogy rather than a fresh judgment call.
- Confirmed `--wp-accent` (`#c89a4a`) already exists as a ratified token
  (`workplace-tokens-2026-06-02.md`) and is close enough to memo's independently-proposed
  `#c8a96e` to treat as the same design intent, not a second competing value.
- Confirmed presentation's icon set is the only genuinely complete, tested artifact in
  the family — verified directly (its own draft already did this; re-confirmed the
  finding still held, no new file appeared since).

### Open questions (1, carried forward — not resolved here)
- Per-app glyph choices for proforma/workbench/gis/pdf/bim — a future
  image-generation-capable pass should propose candidates for review, not decided in
  this brief.
