<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A trigger that initiates an action — submit a form, save
a record, open a dialog, delete something irreversible. Four variants map to four
emphasis levels, so a single surface never needs more than one way to signal what a
control will do.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/button/recipe.json</code></div>
</div>

## When to use Button

Use a button to trigger an action — submit a form, save a record,
open a dialog, dismiss a notification, navigate to a destination
that performs work on arrival. A button is for *doing*; for
*reading* (cross-references, navigation between pages without
state change) use a [Link](/components/link/usage/).

## Variants

The substrate ships four button variants. Each has one canonical
emphasis level and one canonical use context.

| Variant | Emphasis | Use for |
|---|---|---|
| **Primary** | Highest | The most important action on a surface. Form submit. Save. Confirm. Apply. One per surface. |
| **Secondary** | Lower | A complementary action paired with a primary. Cancel. Close. Back. |
| **Ghost** | Minimal | Inline actions in dense surfaces. Toolbar buttons. Row-level controls. Settings dropdowns. |
| **Critical** | High (destructive) | Destructive actions. Delete. Discard. Revoke. Always pair with a confirmation step. |

## When to use

- **Form submit.** Always Primary. Label with the action verb
  (`Save`, `Apply`, `Continue`) — never `Submit` (vague) or
  `OK` (banned in PointSav register).
- **Cancel a destructive flow.** Secondary. Label with the action
  the user is taking (`Discard changes`, `Cancel`).
- **Toolbar actions in a data grid.** Ghost. Icon + label, or
  icon-only with `aria-label`.
- **Delete a record.** Critical. Label specifies what is being
  deleted (`Delete account`, not `Delete`). Always opens a
  confirmation dialog.

## When not to use

- Do not use a button for navigation between pages without state
  change. That is a [Link](/components/link/usage/).
- Do not use a button to surface information that is already
  visible. The button label IS the action; if there is no action,
  there is no button.
- Do not use multiple primary buttons on the same surface — only
  one canonical action per context.
- Do not use Critical for non-destructive actions. The visual
  weight is reserved.

## Anatomy

A button is a single rectangular trigger with three internal
elements:

1. **Container** — background colour, border radius, focus ring.
2. **Label** — utility-4 typography (16/24, 600 weight).
3. **Optional icon** — leading or trailing the label, never both
   on the same button. Icon size matches the label cap height.

## Sizes

v0.0.2 ships one canonical size: 40px height (`min-height: 2.5rem`).
This satisfies the WCAG 2.2 minimum touch target (44x44 with
focus-ring offset). Larger and smaller sizes are subsequent-
milestone work; the dense-grid case currently uses Ghost.

## Live demo

Future: an interactive showcase here once the engine ships
`<ps-component-demo>` rendering. v0.0.2 ships the recipe;
contributors who consume the recipe render their own demo.

## Behaviour

### Focus

Buttons receive focus via Tab and Shift+Tab. The focus ring is
2px solid `{semantic.focus-ring}` with 2px offset, conformant to
WCAG 2.2 AAA against any tenant background.

### Activation

Space and Enter both activate. Clicked buttons fire on `pointerup`
within their bounds; pointer-down outside the button cancels
activation.

### Disabled

Disabled buttons render with `{semantic.interactive-primary-disabled}`
background and `{semantic.ink-disabled}` text. They are not
focusable. Avoid disabled states where possible — surface the
constraint near the trigger instead, so the user knows why they
cannot proceed.

### Loading

Subsequent milestone — a loading button shows a spinner alongside
the label and disables interaction without losing focus.

## Brand voice

Button labels follow the voice rules in the editorial style-guide
bundle (mounted at `/bundles/editorial-style-guide`):

- **Direct.** Action verb first. `Save changes`, not `Click here
  to save your changes`.
- **Specific.** What is being saved? `Save report`, `Save draft`.
- **Confident.** No hedging. `Continue`, not `Continue?`.
- **Professional.** No marketing register. `Get started`, not
  `Let's get started!`.

Banned vocabulary applies to button labels per the editorial
style-guide bundle (mounted at `/bundles/editorial-style-guide`),
not `themes/pointsav-brand.json` — the theme carries no voice data.

<div class="doc-footer-meta">
<span>last changed</span> <a href="/releases/changelog/overview">2026-07-15</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>depends on:</span>
<a href="/tokens#theme">theme.semantic.interactive-primary</a>,
<a href="/tokens#theme">theme.semantic.interactive-critical</a>,
<a href="/tokens#theme">theme.semantic.focus-ring</a>
</div>
