<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">5 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AAA target</span>
</div>
<p class="doc-header__lead">A small, inline status indicator. Carries a short label
and a tone — five tones cover the canonical state patterns.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/badge/recipe.json</code></div>
</div>

## When to use Badge

Use a badge to mark a record's state inline — `Active`, `Draft`,
`Archived`, `Pending review`. Five tones cover the canonical state
patterns.

| Variant | Use for |
|---|---|
| Neutral | Default state, no urgency |
| Primary | Active, in-progress |
| Positive | Completed, verified, approved |
| Caution | Needs attention, expiring soon |
| Critical | Failed, expired, requires action |

A badge is decorative — wrap with screen-reader-friendly context
when the badge IS the only signal of state.
