# Org-chart tokens

A colour palette extension for Woodfine corporate hierarchy charts. Four IBM Carbon
colour families add to the existing Woodfine org-chart palette using the tinted
treatment: Carbon -70 border, Carbon -20 background fill.

## Tinted vs heavy treatment

The existing Woodfine palette uses the heavy treatment — dark border, very pale
background (e.g. `token-blue-solid`, `token-green`). The four IBM Carbon extensions
use the tinted treatment — mid-tone border, saturated tinted background. The visual
contrast between the two treatments is legible at a glance and survives greyscale print.

## Entity roles

| CSS class | Border | Background | Entity role |
|---|---|---|---|
| `token-magenta` | `#9F1853` | `#FFD6E8` | Promoter / management — warm distinction from `token-purple` |
| `token-teal` | `#005D5D` | `#9EF0F0` | SPV General Partner / Limited Partner (SPV-GP, SPV-LP) |
| `token-red` | `#A2191F` | `#FFB3B8` | SPV entities requiring red distinction (e.g. SPV-1 vs SPV-2) |
| `token-warm-gray` | `#565151` | `#E5E0DB` | Holding companies, passive entities above the management layer |

## Full org-chart palette

These four extend the complete palette. Bold rows are the IBM Carbon additions.

| CSS class | Border | Background | Treatment | Source |
|---|---|---|---|---|
| `token-orange-solid` | `#E65100` | `#FFF3E0` | Heavy solid | Material Deep Orange |
| `token-blue-solid` | `#1565C0` | `#E3F2FD` | Heavy solid | Material Blue |
| `token-blue-dashed` | `#1565C0` | `#E3F2FD` | Heavy dashed ellipse | Material Blue |
| `token-grey-solid` | `#757575` | `#EEEEEE` | Heavy solid | Material Grey |
| `token-grey-dashed` | `#94A3B8` | `#F8FAFC` | Dashed | Tailwind Slate |
| `token-green` | `#2E7D32` | `#F1F8E9` | Heavy solid | Material Green |
| `token-purple` | `#7B1FA2` | `#F3E5F5` | Heavy solid | Material Purple |
| `token-olive` | `#827717` | `#F9FBE7` | Heavy solid | Material Yellow dark |
| `token-yellow` | `#F57F17` | `#FFFDE7` | Dashed ellipse | Material Amber |
| **`token-magenta`** | **`#9F1853`** | **`#FFD6E8`** | **Tinted solid** | **IBM Carbon** |
| **`token-teal`** | **`#005D5D`** | **`#9EF0F0`** | **Tinted solid** | **IBM Carbon** |
| **`token-red`** | **`#A2191F`** | **`#FFB3B8`** | **Tinted solid** | **IBM Carbon** |
| **`token-warm-gray`** | **`#565151`** | **`#E5E0DB`** | **Tinted solid** | **IBM Carbon** |

## DTCG bundle

Machine-readable definitions are at [`/tokens.full.json`](/tokens.full.json) under
`ibm-carbon-org-chart` (primitive values) and `org-chart-extended` (semantic entries).
CSS class geometry (210×110 px, 10 px padding, solid border) is in `components/nodes.css`.
