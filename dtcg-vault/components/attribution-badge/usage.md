<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Stub — pending verification</span>
</div>
<p class="doc-header__lead">Engine-family "Powered by" attribution mark. A two-line
stacked pill: an uppercase micro-label ("Powered by") over the engine-family
wordmark. Deliberately unthemed — a certification mark, not a themed UI component,
so it reads identically regardless of the hosting site's own color scheme.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/attribution-badge/recipe.json</code></div>
</div>

## When to use Attribution Badge

Use exactly one visible badge per engine **family** — `mediakit` or `privategit` —
never per specific engine variant. The specific variant a page actually runs
(`knowledge`/`marketing` under mediakit; `source`/`marketplace`/`bim` under
privategit) is exposed only through the badge's `title=` tooltip attribute, never
as a separate visible mark or an additional badge alongside the family one. A page
should never show two attribution badges.

## Status — real content, not yet pixel-verified

This recipe carries `"status": "stub"` in its own real `recipe.json` — it's a
formalization of a real design decision (from
`BRIEF-footer-badge-token-architecture.md`, project-editorial, 2026-07-10), not an
invented one, but its exact color/spacing values are a proposal derived from the
live `app-mediakit-marketing-2` implementation (`src/ui.rs:623-633`,
`static/app.css:735-772`), not yet a byte-exact transcription of it. The recipe's
own `open_questions` field flags this directly. Treat the values below as correct
in intent, pending a final pixel check against the deployed page.

## Data ownership

This component defines shape and CSS only. The actual label text and link
destination per family are **not** owned here — they live in
`factory-release-engineering/tokens/attribution-badges.yaml`
(`families.<name>.label` / `families.<name>.link` /
`families.<name>.variants.<variant>.tooltip`). A consuming page supplies
`{{link}}`, `{{tooltip}}`, and `{{familyName}}` at render time.

## Variants

| Variant | Family name | Tooltip carries |
|---|---|---|
| **mediakit** | MediaKit | The specific engine — Knowledge or Marketing |
| **privategit** | PrivateGit | The specific engine — Source, Marketplace, or BIM |

## Tokens

`semantic.surface-base`, `semantic.border-subtle`, `semantic.ink-disabled`,
`semantic.ink-secondary`, `primitive.border.corner-1`, `primitive.size.space-2`,
`primitive.size.space-3` — real border-radius scale is `border.corner-1/2/3`
(`corner-1` is the real "chip, badge" size in this vault's own `tokens.css`
comment); there is no `ink-tertiary` tier in this vault, `semantic.ink-disabled`
is the real most-muted tier available.

## Accessibility

Standard `<a href>` with a descriptive `title=` attribute carrying the
engine-variant tooltip (e.g. "MediaKit Knowledge Engine v0.3"). No additional ARIA
is needed — the visible label plus family name already convey the link's purpose;
`title=` is supplementary metadata, not the sole accessible name.
