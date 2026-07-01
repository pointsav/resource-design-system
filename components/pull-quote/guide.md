# Pull-quote

An editorial typographic device for setting off a notable passage inside
article prose. One CSS class, no markup dependencies beyond a `<blockquote>`.

## When to use

Use for a single sentence or short passage worth visually isolating inside
a long-form article — the editorial equivalent of a magazine pull-quote.
Do not use for regular blockquoted citations (use plain `<blockquote>`) or
for anything longer than a couple of sentences — length undermines the device.

## Complete CSS

```css
/* Pull-quote — editorial typographic device for notable passages */
.pull-quote {
  font-family: var(--font-display);
  font-size: 1.35em;
  font-weight: 400;
  font-style: italic;
  line-height: 1.35;
  color: var(--fg-2);
  border-left: 4px solid var(--s-accent);
  padding: 0.5em 1.2em;
  margin: 2em 0;
  text-wrap: pretty;
}
/* Dark mode: --fg-2 and --s-accent resolve correctly via dark-mode token cascade; no override needed. */
.pull-quote strong { font-weight: 400; }
```

`--fg-2` is `surface.fg-2` from `tokens/editorial-surface/editorial-surface.dtcg.json`.
`--s-accent` is the active `brand-accent.<tenant>` value (see that token group's
`$description` for the per-tenant `[data-instance]` pattern).

## Markup

```markdown
> **Pull quote text here**
```

Renders as `<blockquote class="pull-quote">`. `strong` inside the quote is
rendered at the same weight as the surrounding italic (`font-weight: 400`)
so emphasis reads as a design choice, not a weight jump.

## Source

Implemented in `app-mediakit-knowledge/static/style.css`; registered here
2026-07-01 from the Sovereign Editorial Phase 2→6 wiki redesign
(DESIGN-RESEARCH-sovereign-editorial-knowledge-wiki). Live on
documentation.pointsav.com, projects.woodfinegroup.com, corporate.woodfinegroup.com.
