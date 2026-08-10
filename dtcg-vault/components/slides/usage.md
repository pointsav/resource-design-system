<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Full-screen slide-deck renderer for embedding a
presentation inside article prose, driven from a fenced <code>:::slides</code>
markdown block.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/slides/recipe.json</code></div>
</div>

## When to use In-article Slide Deck

Use when an article needs to embed a short slide presentation (a walkthrough, a
pitch excerpt) without leaving the page — authored via a fenced `:::slides` markdown
block, one `##` heading per slide. Root variables to set once per instance:
`--pds-slide-aspect: 16 / 9`, plus background/foreground/border/control colors.
Source: `app-mediakit-knowledge`, registered 2026-07-01 from the Sovereign Editorial
Phase 2→6 wiki redesign; live on all 3 wikis.

## When not to use

- **Long-form standalone presentations.** This is an in-article embed, not a
  presentation-authoring tool.

## Variants

| Variant | Behaviour |
|---|---|
| **Inline** | Default embedded state, aspect-ratio controlled viewport. |
| **Fullscreen** | `sd-fullscreen--active` — fixed `inset: 0` overlay, includes an iOS Safari CSS-fullscreen fallback since the native Fullscreen API is unreliable there. |

## Known follow-up work (not blocking this component landing)

Two items are tracked as separate follow-up rather than resolved in this recipe:

1. **Token-alias gap.** `--pds-slide-*` and several `--pds-space-*`/`--pds-radius-*`/
   `--pds-text-*` references in the CSS are engine-local tokens in
   `app-mediakit-knowledge/static/style.css`, not yet aliased to this design system's
   canonical primitives. Registering that alias chain is separate DESIGN-TOKEN-CHANGE
   work.
2. **`slide-deck.js` has no canonical design-system home yet.** The 90-line
   first-party controller (Left/Right/F/Esc keyboard nav, hash routing, fullscreen
   toggle with iOS fallback) is consumed directly from
   `app-mediakit-knowledge/static/slide-deck.js` until one exists.

## Tokens

| Token | Role in this component |
|---|---|
| `{semantic.border.subtle}` | Deck border, transcript top rule. |
| `{primitive.radius.md}` | Deck corner radius. |
| `{primitive.radius.sm}` | Control button corner radius. |
| `{primitive.space.1}`–`{primitive.space.10}` | Control/slide padding and gaps at various scales. |
| `{semantic.text.small}` | Control and transcript text size. |
| `{semantic.text.tertiary}` | Transcript label and summary colour. |

## Accessibility

The recipe targets WCAG 2.2 AA. A `<details>`/`<summary>` transcript renders
alongside the deck so screen readers get the full slide text without needing the
visual deck. The keyboard controller handles Left/Right/F/Esc navigation.

## Reference

Source: `app-mediakit-knowledge`, registered 2026-07-01.
