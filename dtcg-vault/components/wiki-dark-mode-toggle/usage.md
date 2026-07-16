<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A single toggle button that switches a documentation wiki between
its light and dark themes. It sets <code>data-theme='dark'</code> on the <code>&lt;html&gt;</code>
element, remembers the visitor's choice in <code>localStorage</code>, and falls back to the
operating-system <code>prefers-color-scheme</code> preference on a first visit.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-dark-mode-toggle/recipe.json</code></div>
</div>

## When to use Wiki Dark Mode Toggle

Use this toggle in the header or navigation chrome of a
Knowledge-Platform wiki to let a reader choose light or dark
theme and have that choice persist across pages and visits. It is
a theme control, not a general-purpose two-state switch: it does
one thing — flip `data-theme` on the document root and save the
result. For a control that submits, saves, or opens something, use
a [Button](/components/button/usage) instead.

The component originates in the Knowledge Platform surface (see
[Knowledge Platform overview](/products/knowledge-platform/overview))
and is theme-agnostic — it drives whatever light/dark token set the
consuming site has mounted. It is a distinct, standalone recipe;
it is not the same implementation as design.pointsav.com's own
`#theme-toggle` script, though the two share the same conceptual
model (persisted choice, `prefers-color-scheme` fallback).

## Variants

The recipe ships two variants. Both share one button, one CSS
class (`ps-wiki-dark-toggle`), and identical behaviour — they
differ only in whether the text label is visible.

| Variant | Renders | Use for |
|---|---|---|
| **icon-only** | Icon alone; the text label is present but screen-reader-only. | Compact chrome — a dense header or a narrow mobile nav bar where space is tight. |
| **icon-and-label** | Icon plus a visible text label (`Dark` / `Light`). | Roomier navigation where the affordance benefits from a written cue. |

In both variants the label text is always present in the markup —
the `icon-only` variant hides it visually but keeps it for assistive
technology, so the accessible name never depends on the icon alone.

## Anatomy

The button has two internal elements:

1. **Icon** (`.ps-wiki-dark-toggle__icon`) — a moon (`🌙`) in light
   mode, a sun (`☀`) in dark mode. It is decorative and marked
   `aria-hidden="true"`, so it is never announced.
2. **Label** (`.ps-wiki-dark-toggle__label`) — reads `Dark` in
   light mode and `Light` in dark mode. Visible in the
   `icon-and-label` variant, screen-reader-only in `icon-only`.

Both the icon glyph and the label text describe the *current*
theme's opposite — the destination the button will take you to —
which keeps them consistent with the action-oriented `aria-label`
described under [Accessibility](#accessibility).

## Behaviour

### Initialisation and flash prevention

On load, an inline init script reads `localStorage` key `ps-theme`.
If the stored value is `dark` — or if nothing is stored and the OS
reports `prefers-color-scheme: dark` — it sets
`data-theme='dark'` on `<html>`. Everything else stays in the
default light theme.

This script **must run before first paint**. Place it as an inline
script in `<head>`, ahead of stylesheet-dependent rendering, so the
correct theme is applied before the page is drawn. Deferring it —
loading it as an external module, or placing it at the end of
`<body>` — reintroduces the light-to-dark flash it exists to
prevent.

### Toggling and persistence

Clicking the button reads the current `data-theme`, flips it
(`dark` ↔ empty), and writes the new choice to `localStorage` under
`ps-theme`. The stored value outlives the session, so a reader who
chose dark once stays in dark on every later visit until they
choose otherwise — the OS preference is consulted only when no
stored choice exists.

## Tokens

Every colour, space, radius, and motion value comes from the token
substrate — the component hard-codes none of them. Swapping the
mounted theme restyles the toggle with no recipe change.

| Token | Role |
|---|---|
| [`semantic.surface.layer-hover`](/tokens#theme) | Hover background fill. |
| [`semantic.text.secondary`](/tokens#theme) | Default icon and label colour. |
| [`semantic.interactive.focus-ring`](/tokens#theme) | `:focus-visible` outline colour. |
| [`primitive.radius.sm`](/tokens#primitive) | Corner radius. |
| [`primitive.space.1`](/tokens#primitive) | Internal padding. |
| [`primitive.motion.duration.fast`](/tokens#primitive) | Hover background-colour transition duration. |

The hover transition collapses gracefully for readers who request
reduced motion when the mounted theme wires
`primitive.motion.duration.fast` to a reduced-motion-aware value.

## Accessibility

The toggle targets **WCAG 2.2 AA** and its ARIA contract is defined
by the recipe:

- **`aria-pressed`** carries the state as `true` or `false` —
  never `mixed`. The button is a genuine two-state toggle, so the
  binary pressed states are correct; a tri-state value would
  misrepresent it.
- **`aria-label` describes the action, not the state.** In light
  mode the label reads *"Switch to dark mode"*; in dark mode,
  *"Switch to light mode."* It updates on every toggle. This tells
  a screen-reader user what the button will *do*, which is more
  useful than restating the theme they are already in.
- **The icon is `aria-hidden="true"`.** The accessible name comes
  from `aria-label` and the always-present label text, so the emoji
  glyph is never read aloud.
- **Focus is visible.** `:focus-visible` draws a 2px
  `semantic.interactive.focus-ring` outline at 2px offset, so
  keyboard focus is unambiguous.

### Contrast

The component itself is chrome; the WCAG-critical question is
whether the dark theme it switches *to* stays legible. Per the
recipe's audit notes, the dark-mode colour pairs **pass AA**. One
of seven pairs narrowly misses the stricter AAA floor: the weakest,
`#4a9eff` on `#1a1a1a`, measures **6.32:1** — an AA pass that falls
just short of the 7.0:1 AAA threshold for normal-size text. Reserve
that exact pairing for large or bold text, or decorative use, if
you need it at that threshold; do not rely on it for small body
copy where AAA is required.

> An earlier revision of this recipe claimed all seven pairs passed
> AAA. That claim was self-contradictory and was corrected during a
> 2026-07-15 compliance audit — the honest status is AA, with the
> single near-miss noted above. The doc states only what the audit
> substantiated.

## When not to use

- **Not a settings switch.** For an on/off preference that saves a
  value on a form, use a switch or checkbox pattern, not this
  theme-scoped control.
- **Not a Button.** This does not submit, save, navigate, or open a
  dialog. If the control performs work, it is a
  [Button](/components/button/usage).
- **Not for per-component theming.** It flips the whole document via
  `data-theme` on `<html>`. It cannot theme one region in isolation.
- **Do not defer the init script.** Loading it late reintroduces the
  first-paint flash it exists to prevent.

<div class="doc-footer-meta">
<span>last changed</span> <a href="/releases/changelog/overview">2026-07-16</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>depends on:</span>
<a href="/tokens#theme">semantic.surface.layer-hover</a>,
<a href="/tokens#theme">semantic.text.secondary</a>,
<a href="/tokens#theme">semantic.interactive.focus-ring</a>,
<a href="/tokens#primitive">primitive.radius.sm</a>
</div>
