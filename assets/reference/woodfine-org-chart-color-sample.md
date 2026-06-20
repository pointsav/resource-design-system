---
schema: foundry-design-research-v1
title: "Woodfine Org Chart Color Sample — Palette Reference"
decision_type: asset-reference
authored: 2026-05-28
authored_by: totebox@project-orgcharts
authored_with: claude-sonnet-4-6
status: ratified
source: "Production org-chart files (project-orgcharts/current-org-chart-html/color-sample.html)"
ai_consumption_hint: "Visual reference for the complete Woodfine org-chart token palette. Three sections: (1) 7 core token classes used across 3+ charts; (2) 6 additional existing colors; (3) 6 proposed IBM Carbon tokens not yet deployed. Source HTML file: clones/project-orgcharts/current-org-chart-html/color-sample.html"
---

# ASSET — Woodfine Org Chart Color Sample (Palette Reference)

Visual reference file showing the complete Woodfine org-chart token
palette across three sections. Produced during `project-orgcharts`
session 2026-05-28 as a design decision aid.

Source file: `clones/project-orgcharts/current-org-chart-html/color-sample.html`

---

## Purpose

A standalone HTML file that renders every org-chart token class as a
labelled box swatch, organized into three sections:

1. **Core token classes** — 7 named tokens used across 3+ org charts,
   including both dashed and dotted ellipse variants of `token-blue`.
2. **Additional existing colors** — 6 tokens found in some charts but
   not universally applied: green, purple, purple-ellipse-dotted,
   olive, gray-dark, gray-light.
3. **Proposed new colors** — 6 net-new IBM Carbon tokens not yet used
   in any chart: crimson, magenta, cyan, slate, deep-violet, navy.

Each swatch shows: token class name, border hex, background hex, and
border style (solid / dashed / dotted ellipse).

---

## Color Inventory

### Core token classes (7)

| Token Class | Border | Background | Style |
|---|---|---|---|
| `token-green` | `#54924E` | `#EEF6EC` | solid |
| `token-blue` | `#164679` | `#E8EFF7` | solid |
| `token-blue-ellipse-dotted` | `#164679` | `#E8EFF7` | dotted ellipse |
| `token-orange` | `#F15F22` | `#FDE8DD` | solid |
| `token-grey` | `#9CA3AF` | `#E6E7E8` | dashed |
| `token-grey-light-dashed` | `#9CA3AF` | `#F7F9FA` | dashed |
| `token-yellow` | `#EAB308` | `#FFFDE7` | dashed |

### Additional existing colors (6)

| Token Class | Border | Background | Style |
|---|---|---|---|
| `token-purple` | `#7C468C` | `#EEE6F1` | solid |
| `token-purple-ellipse-dotted` | `#7C468C` | `#EEE6F1` | dotted ellipse |
| `token-olive` | `#6B7C3A` | `#F0F3E6` | solid |
| `token-gray-dark` | `#374151` | `#E6E7E8` | solid |
| `token-gray-light` | `#9CA3AF` | `#F7F9FA` | solid |

### Proposed IBM Carbon tokens (6, not yet deployed)

| Token Class | Proposed hex | IBM Carbon source |
|---|---|---|
| `token-crimson` | `#A2191F` | Red 70 |
| `token-cyan` | `#00539A` | Cyan 70 |
| `token-slate` | `#697077` | Cool Gray 60 |
| `token-deep-violet` | `#4D2D68` | Purple 70 |
| `token-navy` | `#003A6D` | Blue 80 |

---

## Notes

- All hex values are verified against production chart files as of 2026-05-28.
- `token-magenta` and `token-teal` were removed from the canonical palette (commit `1b0db90`) — omitted from this reference.
- The source HTML color-sample.html renders each swatch interactively with token class labels.
