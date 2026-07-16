<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AAA target</span>
</div>
<p class="doc-header__lead">Inline messaging — informational, positive, caution,
critical. Toast variant is subsequent-milestone work.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/notification/recipe.json</code></div>
</div>

## When to use Notification

Use a notification to surface system feedback after an action or
state change. Four variants — informational, positive, caution,
critical — communicate severity by colour AND icon AND framing.

| Variant | Use for |
|---|---|
| **Info** | Neutral context — "Your draft has been saved automatically." |
| **Positive** | Successful outcome — "Report exported." |
| **Caution** | Reversible problem — "Cannot connect to the network. Reconnecting…" |
| **Critical** | Failed action — "Could not save changes. Try again." |

Notifications never auto-dismiss without an undo affordance.
Time-sensitive critical notifications use `role="alert"` for
assertive announcement.

The substrate ships inline notifications today; toast (positioned)
notifications are subsequent-milestone work — most production
patterns use inline + a single toast slot at the page level.
