<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">1 variant</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A single external-egress navigation link rendered as an
icon + label pair — e.g. a repository or fleet-manifest link in site chrome.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/icon-tab/recipe.json</code></div>
</div>

## When to use Icon Tab

Use for a single external-egress link rendered as an icon + label pair — e.g. a
repository or fleet-manifest link in site chrome. One instance per destination.

## When not to use

- **In-page navigation.** That's a different semantic — see `docs-sidenav` and
  `wiki-toc-sidebar` for within-site and within-article navigation respectively.

## Variants

| Variant | Behaviour |
|---|---|
| **Filled-primary** | The primary egress tab — filled icon, no border treatment. Only variant committed in this release. |

A bordered, light-background ghost variant exists in source material
(`template-agnostic-ui.html`) but is deferred — see Open questions below.

## Icon mechanism — decided 2026-08-10

Inline SVG (`fill="currentColor"`), not a CSS `background-image` icon slot. Inline
SVG gives clean colour inheritance through `currentColor` with no separate
icon-color token needed; a background-image alternative would remove the HTML's
dependency on icon content but lose that inheritance, requiring a new `--icon-color`
token or a filter workaround. Kept simple for this release.

## Open questions (deferred, not blocking this release)

- **Ghost variant.** `template-agnostic-ui.html` uses a bordered, light-background
  `.btn` variant alongside the filled version. Deferred to a later milestone — commit
  only `filled-primary` now. Whether it eventually becomes a `wf-icon-tab--ghost`
  modifier of this same component, or a separate `icon-btn` component (different
  semantic emphasis: secondary/inline action vs. primary egress tab), is left open.
- **`--ps-font-display` token.** Not yet in `tokens/dtcg-bundle.json` — currently
  resolved via the Woodfine theme's `--display` custom property, which works today
  inside that theme. This component lands now with the gap flagged; formalizing
  `--ps-font-display` as a canonical token is separate follow-up DESIGN-TOKEN-CHANGE
  work, tracked but not blocking.

## Tokens

| Token | Role in this component |
|---|---|
| `{primitive.font.family.display}` | Label typeface (falls back to `--pds-font-display` until `--ps-font-display` is formalized — see Open questions). |
| `{semantic.text.primary}` | Resting icon/label colour. |
| `{semantic.interactive.link}` | Hover colour. |
| `{semantic.interactive.focus}` | Focus-visible outline colour. |

## Accessibility

The recipe targets WCAG 2.2 AA.

- **Native link semantics.** A plain `<a href>` — no `role="button"` override; this
  is navigation, not an action.
- **Named destination in the accessible name.** `aria-label` must name the
  destination clearly (e.g. "Fleet Manifest," never just the platform name like
  "GitHub") and end with the literal suffix "(opens in new tab)" per WCAG 2.4.4 Link
  Purpose (Level AA).
- **Icon never separately announced.** The SVG carries `aria-hidden="true"` and
  `focusable="false"` (the latter required for older SVG user agents); the label
  span carries the full accessible text.
- **`rel="noopener"`** is required alongside `target="_blank"`.
- Screen readers announce: "&lt;Destination name&gt; (opens in new tab), link."

## Reference

Source material: `template-agnostic-ui.html`.
