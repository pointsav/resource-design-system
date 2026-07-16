<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">5 slots</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Stub — pending verification</span>
</div>
<p class="doc-header__lead">Footer for customer/content-facing Woodfine and PointSav
sites. Composes a brand re-anchor block (top), a free-form context slot
(site-specific columns, hand-authored per site), a network slot, an optional
disclosure block driven by a named legal-tokens disclaimer profile, and a fixed
identity bar — locations, badge, copyright, disclaimer, trademark — byte-identical
across every site that uses it, except the two fields documented as expected to
vary.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/site-footer/recipe.json</code></div>
</div>

## When to use Site Footer

Use Site Footer on **customer/content-facing** Woodfine/PointSav sites — the sites
whose audience is reading content, not operating a developer tool. It is distinct
from [Machine Surface Footer](/components/machine-surface-footer/usage), which
serves developer-facing tool sites such as design.pointsav.com itself. The two are
not interchangeable: Site Footer carries the full corporate identity bar and an
optional legal-disclosure block; Machine Surface Footer does not. Whether
design.pointsav.com should adopt this component or deliberately stay on Machine
Surface Footer alone is an open question in the recipe — a developer-tool site may
legitimately not need the full customer-facing identity bar, though the recipe
recommends adding at minimum the identity bar's trademark notice there regardless,
since that specific omission was flagged in the 2026-07-10 research as a real gap,
not a stylistic choice.

## Status — real content, not yet finalized

This recipe carries `"status": "stub"` in its own real `recipe.json`. It
formalizes real research, not an invented pattern: it originates in the
project-editorial footer/badge architecture research
(`BRIEF-footer-badge-token-architecture.md`, 2026-07-10) and was **reconciled
2026-07-12, operator-approved,** against project-marketing's live mobile-audit
findings on home.woodfinegroup.com and home.pointsav.com. That reconciliation
changed the original draft in three ways, all grounded in already-shipped
live-site fixes: (1) section-heading casing moved from sentence-case-visual to
uppercase+tracked-visual; (2) a brand re-anchor block (site name + tagline) was
added at the top of the footer; (3) the attribution badge was repositioned from
inline-with-locations-and-copyright to right-aligned on its own locations row,
fixing a real mobile bug where the badge was buried under legal text. Token
references were also corrected from the draft's invented `--pds-*` prefix and
nonexistent token paths to this vault's real `--ps-*` prefix and real token names,
verified against `tokens/primitive.json` and `themes/pointsav-brand.json`.

Two questions remain open in the recipe: design.pointsav.com's adoption decision
(above), and the templating notation — the recipe uses Handlebars-style
placeholders for the design system's own documentation purposes, as existing
recipes do, but the consuming code (app-mediakit-shell) is maud/Rust and
translates the pattern rather than consuming this JSON literally.

## Anatomy — five slots in three layers

The recipe defines five slots, each tagged with the layer it belongs to and who
authors its content:

| Slot | Layer | Authored by |
|---|---|---|
| `siteName` / `tagline` | identity | Site's own brand name; tagline **reuses** the site's canonical SEO meta-description / JSON-LD description — deliberately not a second hand-authored copy, so it cannot drift out of sync |
| `contextColumns` | context | Per-site, hand-built — BIM spec numbers, GIS data credits, endpoint lists, version strings; the component provides only the layout container |
| `networkLinks` | grammar | Per-site data, shared structure — cross-links to sibling sites in the family |
| `disclosureProfile` / `disclosureStatements` | grammar | Selected from `legal-tokens-*.yaml` `disclaimers.profiles.<name>`; which statements render is data-driven, the section shape (heading + list + full-disclaimer link) is fixed |
| `locations` / `copyrightStatement` / `disclaimerOneLiner` / `trademarkStatement` / `attributionBadge` | identity | Byte-identical, sourced from `legal-tokens-*.yaml` + `attribution-badges.yaml` — **never hand-typed per site** |

The brand re-anchor block renders above everything else so brand identity is
re-established once the masthead has scrolled off-screen on a long page. The
disclosure block only renders when a `disclosureProfile` is supplied.

## The identity bar must never drift

The fixed bottom bar is the layer where every prior footer inconsistency found in
the 2026-07-10 research lived: a missing trademark notice on design.pointsav.com,
pipe-vs-middot separator drift, and section-heading synonyms. That is why its
content is sourced from token files rather than hand-typed. The
[Attribution Badge](/components/attribution-badge/usage) sits right-aligned on
the locations row, above its own copyright row — repositioned in the 2026-07-12
reconciliation for the mobile-legibility fix described above.

## Content conventions

- **Separator: middot (·) only.** Matches the family's existing convention
  ("v0.3.0 · live", "Apache-2.0 · platform code AGPL-3.0-or-later"). Do not use a
  pipe (|) — the live sites' "Vancouver | New York" is the one inconsistency this
  component corrects.
- **Link arrow: → (rightwards arrow)** — the only inline link-continuation glyph
  used in footer prose.
- **Fixed section-heading lexicon:** "Network", "Important information",
  "Machine surface", "Legal & attribution". Do not introduce a synonym for an
  existing heading — prior drift produced three names ("Family & Legal" /
  "Legal & Attribution" / "Corporate identity") for one drawer.
- **Casing:** headings are authored in sentence case and rendered uppercase with
  ~0.08em letter-spacing via CSS `text-transform` (`.ps-site-footer__heading`) —
  never as literal all-caps text, so screen readers don't risk reading a heading
  letter-by-letter as an acronym.

## Tokens

Five semantic and four primitive tokens:
[`semantic.surface-subtle`](/tokens#theme), `semantic.border-subtle`,
`semantic.ink-primary`, `semantic.ink-secondary`, `semantic.ink-disabled`, and
[`primitive.size.space-2`](/tokens#primitive), `space-3`, `space-4`, `space-6`.
The CSS consumes them as `--ps-*` custom properties (`var(--ps-surface-subtle)`,
`var(--ps-ink-disabled)`, `var(--ps-space-6)`, …) with pixel fallbacks on the
spacing values. There is no `ink-tertiary` tier in this vault —
`semantic.ink-disabled` is the real most-muted tier, used here for the
section-heading and muted identity rows.

## Accessibility

`<footer>` carries the `contentinfo` landmark role implicitly and should be the
last landmark on the page. Each column/block is labeled by an `<h2>` section
heading for screen-reader navigation. Heading uppercase styling is applied in CSS,
not in content, per the casing convention above. Target: **WCAG 2.2 AA** — a
target declared in the recipe, not yet a verified audit result, per the stub
status.
