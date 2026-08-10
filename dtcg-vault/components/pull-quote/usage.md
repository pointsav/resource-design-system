<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">1 variant</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">Editorial typographic device for setting off a notable
passage inside article prose. One CSS class, no markup dependencies beyond a
<code>&lt;blockquote&gt;</code>.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/pull-quote/recipe.json</code></div>
</div>

## When to use Pull-quote

Use for a single sentence or short passage worth visually isolating inside a
long-form article — the editorial equivalent of a magazine pull-quote. Source:
`app-mediakit-knowledge/static/style.css`, registered 2026-07-01 from the Sovereign
Editorial Phase 2→6 wiki redesign; live on all 3 wikis.

## When not to use

- **Regular citations.** Use a plain `<blockquote>` instead — `pull-quote` is a
  typographic emphasis device, not a citation format.
- **Long passages.** Anything longer than a couple of sentences undermines the
  device — restructure or use a plain blockquote instead.

## Anatomy

A single `<blockquote class="pull-quote">` wrapping a `<strong>` element. The
`<strong>` renders at the same weight as the surrounding italic text so emphasis
reads as a design choice, not a weight jump.

## Behaviour

Dark mode needs no override — both tokens resolve correctly through the existing
dark-mode cascade.

## Tokens

| Token | Role in this component |
|---|---|
| `{primitive.font.family.display}` | Quote typeface. |
| `{semantic.text.secondary}` | Quote text colour. |
| `{semantic.brand-accent}` | Left border accent. |

## Accessibility

The recipe targets WCAG 2.2 AA. No ARIA is needed — a styled `<blockquote>` carries
correct implicit semantics on its own.

## Reference

Source: `app-mediakit-knowledge/static/style.css`, registered 2026-07-01.
