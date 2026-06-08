---
schema: foundry-design-research-v1
component_or_token: orgchart
decision_type: color-system
authored: 2026-06-06
authored_by: totebox@project-orgcharts
authored_with: claude-sonnet-4-6
status: ratified
source: 9 production HTML org charts (commit dabe5000 and prior; 15 JW iterations)
ai_consumption_hint: "When generating HTML org chart CSS for Woodfine entities, read this file to understand the three-axis model (color/shape/size) and the nine entity-role color assignments. The token-base class and color modifier pattern (token-base token-[color] for rectangles; token-[color]-pill-dashed for fund vehicles) is defined here. Yellow updated 2026-06-06 from #F57F17 to #EAB308."
---

# Org Chart Token System — Design Rationale

## Three-axis token model

Every node in the org chart system is defined by three independent axes:

**Axis 1 — Color (entity role):** Nine semantic colors, each mapped to a corporate entity type. Color communicates *who this entity is* in the ownership structure, not its status or health.

**Axis 2 — Shape (entity class):** Three base shapes. Rectangle = operating or holding company. Pill = fund vehicle or limited partnership. Ellipse = cross-border flow-through entity or access fund.

**Axis 3 — Size (hierarchy weight):** Four heights. Standard 110px = majority of entities. Tall 145px = Board-level or managing entity. Short 80px = asset or subsidiary. Compact 60px = service provider or secondary role. Ellipse 90px = cross-border vehicles.

Axes are composited via CSS class stacking: `token-base token-[color]` for rectangles; `token-[color]-pill-dashed` for fund vehicles; `token-[color]-ellipse-dashed` or `token-[color]-ellipse-dotted` for cross-border entities.

## Color semantics — nine entity roles

| Token | Border | Surface | Entity role |
|---|---|---|---|
| token-green | `#54924E` | `#EEF6EC` | Corporate holding company; primary group entity |
| token-blue | `#164679` | `#E8EFF7` | Investment vehicle; investor units |
| token-purple | `#7C468C` | `#EEE6F1` | Broker-dealer; asset manager; regulatory intermediary |
| token-orange | `#F15F22` | `#FDE8DD` | Equity partner; named individual; Bencal-group entity |
| token-grey | `#9CA3AF` | `#E6E7E8` | Administrative entity; titleco; support company |
| token-yellow | `#EAB308` | `#FFFDE7` | Fund vehicle (LP, limited partnership, fideicomiso) — always dashed pill |
| token-magenta | `#9F1853` | `#FFD6E8` | Legacy corporate (Bencal Corporation pre-reorganization) |
| token-teal | `#005D5D` | `#9EF0F0` | Legacy asset company (Bencal Real Assets pre-reorganization) |
| token-grey-dashed | `#9CA3AF` | `#F7F9FA` | Service provider; independent dealer; placeholder |

## Color decision log

**Yellow update 2026-06-06:** `#F57F17` → `#EAB308`. Original amber was at hue ~30° (too close to orange `#F15F22` at hue ~15°). Replacement `#EAB308` is at hue ~45°, reading clearly as yellow/gold in both screen and print contexts. Applied across all 9 production charts in commit `dabe5000`.

**Bencal green 2026-06-03:** `#198038` (design-system green) → `#54924E` (WCP canonical green). The darker Carbon-style green failed at 9–10px font weights against the `#EEF6EC` background. Operator decision ratified (commit `57960322`).

## Why `orgchart.*` semantic namespace

The PointSav design system already uses `$support-success`, `$support-warning`, etc. for operational status. These tokens carry the wrong semantic load for org charts: a green node is not "successful" — it identifies a corporate holding company. Reusing status tokens would pollute downstream consumers (dashboards, alerts) with entity-role color meanings.

The `orgchart.*` semantic namespace (parallel to the existing `wiki.*` namespace) encapsulates these entity-role colors without cross-contaminating the status semantic layer.

## Shape border styles

**Solid 2px:** All rectangles — operating companies, holding entities, investor boxes.
**Dashed 2px:** All pills and ellipses representing fund vehicles and cross-border structures. Dashed communicates contingency, flow-through nature, or indirect ownership.
**Dotted 2px:** External cross-border vehicles (purple-ellipse-dotted) — signals third-party or externally-managed entity.

## Open questions

1. Should the grey-dashed token (service providers) be promoted to a named semantic role, or remain as a catch-all? Current usage is inconsistent across charts — some independent dealers are grey-dashed, others are plain grey.
