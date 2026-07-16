<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AAA target</span>
<span class="badge">Focus-visible</span>
</div>
<p class="doc-header__lead">Boolean choice. Use when each option is independent of
the others.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/checkbox/recipe.json</code></div>
</div>

## When to use Checkbox

Use a checkbox for boolean choices where each option is
independent of the others ("Email me when a report finishes",
"Include archived records").

For mutually-exclusive choices from a fixed set, use radio
buttons (subsequent milestone) or a select.

For binary on/off settings that take effect immediately, prefer
a switch — the visual semantics communicate "this is live" better
than a checkbox does.

The native `<input type="checkbox">` is hidden visually but kept
in the accessibility tree; the styled `<span>` is decorative.
This pattern preserves keyboard activation (Space toggles) and
screen-reader announcement.
