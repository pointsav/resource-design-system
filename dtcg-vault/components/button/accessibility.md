# Button — Accessibility

Target: WCAG 2.2 AA, AAA where achievable. Corrected 2026-07-15 — this
file previously claimed a blanket AAA target and false contrast numbers
(recomputed directly from the real shipped hex values, not carried
forward from an earlier, unverified draft).

## Conformance status

| Criterion | Level | Status |
|---|---|---|
| 1.4.3 Contrast (Minimum) — text vs background | AA | Pass — primary variant 6.66:1; critical variant (resting) 7.33:1 as of the 2026-07-15 `interactive-critical` fix (previously 4.44:1, a real AA failure — see Fixed defects below) |
| 1.4.6 Contrast (Enhanced) | AAA | Partial — critical variant (7.33:1) passes; primary variant (6.66:1) does not meet the 7:1 AAA floor, AA only |
| 1.4.11 Non-text Contrast — focus ring | AA | Pass — 3:1 minimum against any tenant background |
| 2.1.1 Keyboard | A | Pass — Tab to focus, Space/Enter to activate |
| 2.4.7 Focus Visible | AA | Pass — 2px ring, 2px offset |
| 2.5.5 Target Size — 44x44 minimum | AAA | Pass — 40px height + 2px ring + 2px offset = 44px |
| 4.1.2 Name, Role, Value | A | Pass — native `<button>` element |

## Fixed defects

**2026-07-15 — Critical variant resting-state contrast, real AA failure.**
`theme.semantic.interactive-critical` resolved to `{color.critical-50}`
(`#d24747`), which computes to **4.44:1 against white** — below the 4.5:1
AA floor for normal text, a real defect (this recipe's white
`ink-on-critical` text was genuinely under-contrasted, not just a
documentation error). Found during the v3 design.pointsav.com mockup's
factual-grounding audit (round 11, 2026-07-11), flagged rather than
silently patched at the time since the fix belongs in the token layer,
not the mockup. Fixed here: `interactive-critical` moved to
`{color.critical-60}` (7.33:1, matching the resting-state color this
component's own hover state already used), `interactive-critical-hover`
moved to `{color.critical-70}` (10.59:1) to preserve a distinct hover
step; `interactive-critical-pressed` unchanged (`{color.critical-70}` —
now identical to hover, since the primitive scale has no darker step
below `critical-70`; accepted rather than inventing an unratified value).

## Keyboard interactions

| Key | Behaviour |
|---|---|
| Tab | Move focus to the button |
| Shift + Tab | Move focus to the previous focusable element |
| Space | Activate the button |
| Enter | Activate the button |
| Escape (in dialog context) | Cancel the dialog without activating |

## Screen reader behaviour

The native `<button>` element is announced as "button" with the
visible label. For icon-only buttons, set `aria-label` with the
action description. The substrate's recipe never overrides the
native role with `role="button"` on a non-button element; that
pattern is an anti-pattern that breaks keyboard activation.

When a button enters a loading state (subsequent milestone),
`aria-busy="true"` and `aria-disabled="true"` are set; the visible
label updates to reflect the in-flight state.

## Reduced motion

Buttons respect `prefers-reduced-motion: reduce` automatically —
the CSS transition-duration value resolves to 0 when the media
query matches. No code change required at the consumer level.

```css
@media (prefers-reduced-motion: reduce) {
  .ps-btn { transition: none; }
}
```

## Touch targets

All button variants meet the 44x44 minimum touch target. The
component renders at 40px height; the focus ring offset adds 4px
on each side, bringing the activatable area to 44px+. Dense-grid
contexts that need smaller buttons should use the Ghost variant
in a context that does not require touch — Ghost in a toolbar
above a keyboard-focused work surface is acceptable; Ghost in a
mobile-first form is not.

## Colour independence

No button state is communicated by colour alone. Hover adds a
darker background tone; pressed adds a darker still; disabled
changes both background AND text colour AND removes the focus
ring. Critical variants are marked by colour AND by their
positioning (always paired with a confirmation step) AND by their
label semantics (`Delete account`, `Discard changes`).

## Anti-patterns

- **`<div onclick>`** instead of `<button>`. Loses keyboard
  activation, screen-reader role, focus management. Always use
  `<button>`.
- **Disabled without explanation.** The user has no way to know
  what would unlock the action. Surface the constraint near the
  trigger instead.
- **Critical variants with non-destructive labels.** The visual
  weight is reserved for destructive actions. Don't use Critical
  for "Submit" or "Apply".
- **Focus ring removed.** `outline: none` without an alternative
  breaks 2.4.7. The recipe never removes the ring.

## Compliance audit endpoint

Intended for v0.0.3 — the substrate is planned to expose
`GET /api/audit/wcag?theme=<theme>` returning a per-component
WCAG conformance report. Today, this page is the canonical
conformance statement.
