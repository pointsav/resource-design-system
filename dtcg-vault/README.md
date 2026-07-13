# dtcg-vault — vault template

[ 🇪🇸 Leer este documento en Español ](./README.es.md)

This directory is the **canonical template** for a per-tenant
vault under Doctrine claim #38 (Design System Substrate). It is
the content `app-privategit-design` reads from disk at runtime —
distinguished here from the existing top-level `tokens/`,
`components/`, `themes/`, `templates/`, `guidelines/`, `docs/`
trees which carry the prior YAML-canonical layer consumed by
sibling clusters (`project-orgcharts`).

## How it is used

| Context | Path |
|---|---|
| Vendor showcase | `~/Foundry/deployments/vault-privategit-design-1/` (this content seeds it) |
| SMB customer fork | `<their-clone>/dtcg-vault/` → bootstrap copies into their `vault-privategit-design-N/` |

## Layout

```
dtcg-vault/
├── tokens/
│   ├── primitive.json              — DTCG primitive layer
│   └── dtcg-bundle.json            — deprecated stub (2026-07-10); superseded
│                                      by repo-root tokens/dtcg-bundle.json, see below
├── themes/
│   └── pointsav-brand.json         — semantic-layer override + voice + a11y commitments
├── components/
│   ├── button/                     — fully populated
│   │   ├── recipe.json             — DTCG component recipe (4 variants)
│   │   ├── usage.md                — Usage tab
│   │   ├── style.md                — Style tab
│   │   ├── code.md                 — Code tab (incl. shadcn/MCP/HTTP/Git fetch paths)
│   │   └── accessibility.md        — Accessibility tab
│   ├── input-text/                 — recipe + usage tab
│   ├── link/
│   ├── surface/
│   ├── navigation-bar/
│   ├── notification/
│   ├── badge/
│   └── breadcrumb/
├── elements/
│   ├── color/
│   │   ├── overview.md
│   │   └── tokens.md
│   ├── typography/
│   │   └── overview.md
│   ├── spacing/
│   │   └── overview.md
│   └── motion/
│       └── overview.md
├── about/
│   └── what-is-pointsav-design.md
├── guidelines/
│   └── accessibility/
│       └── overview.md
├── research/
│   ├── design-philosophy.md
│   └── primitive-vocabulary-rationale.md
└── exports/                        — derived caches (built at runtime)
```

`tokens/`, `themes/`, `components/`, `elements/`, `about/`,
`guidelines/`, `research/`, `exports/`, `paper/`, `writing/` are the
ten canonical top-level layers the substrate engine reads. `paper/`
(document/print-format tokens: legal agreements, financial
statements, interactive PDF navigation) and `writing/` (content/voice
tokens: register scale, lexicon structure, disclaimer templates)
were added 2026-07-13, consolidating design-token content that had
previously been scattered across several `project-*` archives —
see `research/legal-*-token-map.md`, `research/financial-*-token-map.md`,
`research/interactive-pdf-binder-token-map.md`, and
`research/writing-token-consolidation.md` for the full rationale.

## v0.0.2 contents

### Primitive vocabulary (PointSav-original)

- `tokens/primitive.json` — Color: `neutral / primary / positive
  / caution / critical` numeric scales (10–100/90/70). Spacing:
  `space-1..13`. Type: `utility-1..4` + `display-1..4`. Motion:
  `ease-utility / ease-display / ease-enter / ease-exit`.
  Duration: `speed-1..6`. Border: `corner-1..3` + `stroke-1..2`.
  Focus ring (WCAG 2.2 AAA conformant).

### Theme

- `themes/pointsav-brand.json` — semantic-layer override +
  accessibility commitments (WCAG 2.2 AAA, 7:1 text contrast,
  3:1 focus-ring contrast, 44px min touch target). Voice, register,
  and vocabulary discipline live in the editorial style-guide bundle
  (mounted at `/bundles/editorial-style-guide`), not this theme.

### Components (8)

| Component | Tabs populated |
|---|---|
| `button` | recipe + usage + style + code + accessibility (FULL) |
| `input-text` | recipe + usage |
| `link` | recipe + usage |
| `surface` | recipe + usage |
| `navigation-bar` | recipe + usage |
| `notification` | recipe + usage |
| `badge` | recipe + usage |
| `breadcrumb` | recipe + usage |

### Elements (foundations)

- `color/overview.md` + `color/tokens.md`
- `typography/overview.md`
- `spacing/overview.md`
- `motion/overview.md`

### About + guidelines

- `about/what-is-pointsav-design.md`
- `guidelines/accessibility/overview.md`

### Research

- `research/design-philosophy.md` — substrate doctrine narrative
- `research/primitive-vocabulary-rationale.md` — why PointSav
  vocabulary instead of Carbon vocabulary (the structural
  patterns are field-shared; the literal tokens are not)

## Why this directory exists separately from `tokens/`, `themes/`, `components/` at repo root

The repo root carries the prior YAML-canonical layer consumed by
project-orgcharts as its DOWNSTREAM input. The substrate cluster
(`project-design`) introduces DTCG as the new canonical form per
claim #38; the two coexist during the migration window.

`dtcg-vault/` is the substrate-canonical form. Migration of the
prior YAML layer into DTCG happens in subsequent milestones,
coordinated with project-orgcharts.

## A note on `dtcg-bundle.json` (not part of this vault's own served tokens)

`design.pointsav.com`'s own served token data (`/tokens.json`, `/api/tokens/<theme>.dtcg.json`,
`exports/tokens.full.json`) is built **exclusively** from `tokens/primitive.json` +
`themes/pointsav-brand.json` in this directory. It has never included either copy of
`dtcg-bundle.json` — `sync-design-tokens.sh` (the script that populates a deployed
vault's `exports/`) explicitly skips that filename when merging extension token files.

Repo-root `tokens/dtcg-bundle.json` is a separate, actively-maintained, cross-domain
DTCG bundle — wiki/article-domain components, `app-workplace-*` products, and a set of
shared numeric primitives — consumed directly by those downstream apps, not through
this substrate's own HTTP surface. It is routed through this repo per
`token-intake-checklist.md`'s "generic design token" rule, not because it feeds
`design.pointsav.com` itself. This vault's own former copy of the same file
(`tokens/dtcg-bundle.json`, now a deprecation stub) was a smaller, pre-refactor
duplicate of that bundle — reconciled into the root copy 2026-07-10 (see
`.agent/briefs/BRIEF-design-pointsav-v3-ground-up-rethink.md` Phase 4a.8/4a.9).

## Delivery surface (what `app-privategit-design` exposes)

The substrate engine reads this vault and serves:

| Surface | URL pattern |
|---|---|
| HTML showcase (Carbon-shape sidebar + 4 tabs per component) | `/`, `/components/<name>/<tab>`, `/elements/<slug>/<tab>` |
| Live DTCG token bundle | `/tokens.json`, `/api/tokens/<theme>.dtcg.json` (Content-Type: `application/design-tokens+json`) |
| shadcn-compatible registry | `/r/registry.json`, `/r/<component>.json` |
| DESIGN.md export (Google's Apr 2026 spec) | `/api/design-<theme>.md` |
| MCP JSON-RPC server | `POST /mcp` |
| Machine-readable JSON | `/api/components.json`, `/api/components/<name>.json` |

The four leapfrog API endpoints (DTCG live API, shadcn registry,
DESIGN.md export, expanded MCP) are documented in Doctrine claim
#38 leapfrog targets L1, L3, L4, and L2 respectively.
