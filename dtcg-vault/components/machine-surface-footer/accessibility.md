---
title: Machine Surface Footer — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA.

## Landmarks

`<footer>` at the page's outermost scope is an implicit `contentinfo` landmark — it must
be the last landmark on the page. The three columns are visually labelled with real `h2`
headings, which is sufficient structure; no additional ARIA landmarks are needed inside
the footer itself.

## Not decorative — these are real links

The monospace styling signals "machine-readable surface," but every link in the
machine-surface column (`/tokens.json`, `/components`, `/research`, `/healthz`) is a
genuine, navigable link for sighted keyboard users and screen-reader users alike — not a
visual flourish. Treat them exactly like the human-facing links beside them: real
`<a href>` elements, included in tab order, with link text that stands on its own when
read out of context (a screen reader announces "/healthz link," which is already
self-describing — no additional `aria-label` needed here). None are placeholder `#`
targets — an endpoint listed here that does not resolve is a violation of the pattern's
own purpose (see Usage, When not to use), independent of any WCAG criterion.

## Monospace is not the semantic signal — use `<code>`

Font-family alone must never be the thing that tells an assistive-technology user "this
text is an endpoint/code token, not prose." A visual monospace typeface applied only via
CSS (as the recipe's `html` currently does — `<a href="/tokens.json">/tokens.json</a>`
with no inline semantic wrapper) is announced by a screen reader identically to any other
link text; the "this is code" meaning is lost entirely for non-sighted users, and is lost
for sighted users too under any stylesheet override or reader-mode extension that strips
font-family. Each endpoint string should be wrapped in a `<code>` element inside the
anchor — `<a href="/tokens.json"><code>/tokens.json</code></a>` — so the semantic is
carried in markup, with the monospace *look* then simply following from the browser's
default `<code>` styling (or the recipe's own CSS keyed off the element, not a class-only
convention). This is a real gap in the recipe as currently authored, consistent with its
`status: "stub"`; it should be closed before promotion out of stub.

## Contrast

`{semantic.ink-secondary}` (link/body text) and `{semantic.ink-tertiary}` (base-bar text)
must each resolve to at least 4.5:1 against `{semantic.surface-default}` at whatever size
the theme renders them (WCAG 1.4.3, AA — the recipe's stated target). `recipe.json` does
not carry resolved color values, so no specific ratio can be asserted here without
checking the active theme's token output; verify per-theme at token-resolution time,
particularly for the 12px base bar, which is both the smallest text in the component and
the one token (`ink-tertiary`) deliberately chosen to read as de-emphasized — de-emphasis
must not be allowed to cross the line into failing contrast.

## Keyboard interactions

| Key | Behaviour |
|---|---|
| Tab | Move focus through brand, machine-surface, and provenance links in column order |
| Shift + Tab | Move focus to the previous focusable element |
| Enter | Follow the focused link |

## Colour independence

Link state (hover/active) is communicated by the `interactive-primary` colour change
alone in the base recipe — consuming pages that need a non-colour signal (e.g. for a
`forced-colors` media query) should add an underline-on-hover fallback, consistent with
how the rest of the substrate handles `forced-colors` elsewhere.
