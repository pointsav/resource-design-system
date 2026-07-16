# Org Charts

Print-first component set for entity/ownership hierarchy diagrams —
the newest of three product lines built on this design system's
tokens.

Org chart diagrams are a print-first surface — every node renders at
a fixed pixel position on a 1056×816px canvas (US Letter landscape at
96dpi), not a fluid web layout. That constraint, and the entity-role
color system it needs, don't map cleanly onto this design system's
Carbon-derived primitives — see the gap analysis below.

The token registry reserves a 9-role entity-color palette
(`primitive.color.orgchart.*`, see [Tokens](/tokens#primitive)) — the
shipped Org Chart Node component uses 6 of those 9 roles today (green,
blue, purple, orange, grey, yellow); the remaining 3 (two "legacy
entity" colors plus an extra grey variant) are reserved capacity, not
yet wired into a component variant.

## Why org-chart tokens are their own namespace, not reused Carbon tokens

Of the six entity-role colors, one (Broker / Asset Manager, purple)
has no Carbon equivalent at all — Carbon's semantic system has
nothing similar. Two more (Investment Vehicle's blue, Corporate
Holding's green) map to a same-intent Carbon token, but at a
meaningfully different hex value or semantic register. Reusing
Carbon's `$support-*` tokens for the remaining three would import
status/alert semantics (success, caution, warning) into what are
structural, not evaluative, distinctions between entity types. Box
dimensions (110–250px, plus the 1056×816px canvas) don't derive from
Carbon's 8px spacing scale either — they're set by print legibility
and the US Letter page geometry. Typography runs 9–12px, below
Carbon's 12px floor, because only about five 210px-wide boxes fit
across the 1056px canvas in one row, leaving little room to spare at
a larger type size.

| Entity role | Our token | Carbon nearest | Assessment |
|---|---|---|---|
| Corporate holding | `primitive.color.orgchart.green` | `$support-success` | Different hue — ours is lighter sage, Carbon is darker forest |
| Investment vehicle | `primitive.color.orgchart.blue` | `$interactive` | Different register — institutional navy vs. bright interactive blue |
| Broker / asset manager | `primitive.color.orgchart.purple` | none | No Carbon equivalent at all |
| Equity partner | `primitive.color.orgchart.orange` | `$support-caution-major` | Close visually, wrong semantic — caution implies a warning |
| Admin entity | `primitive.color.orgchart.grey` | `$border-strong-01` | Similar lightness, different use — border vs. entity fill |
| LP / fund vehicle | `primitive.color.orgchart.yellow` | `$support-warning` | Close visually, wrong semantic — warning implies an alert |

3 real components, 1 rendered example (Org Chart Node), 1 of 6 colors
with no Carbon equivalent at all.
