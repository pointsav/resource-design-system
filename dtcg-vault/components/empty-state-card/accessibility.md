---
title: Empty State Card — Accessibility
---

# Accessibility

Target: WCAG 2.2 AA.

## Conformance notes

The card itself is a purely visual container — the title and body are
standard heading and paragraph text, so they inherit conformance from the
page's own heading order and text-contrast tokens.

**If the card replaces a live region** (for example, a search-result list
that becomes empty after a filter is applied), wrap the card in an
`aria-live="polite"` container so screen reader users are told the state
changed, rather than silently seeing nothing update:

```html
<div aria-live="polite">
  <!-- empty state card renders here on zero results -->
</div>
```

Without this, a sighted user sees the empty state appear immediately;
a screen reader user gets no equivalent signal that their search actually
ran and returned zero matches.

## Heading level

`<h2>` is the recipe's default — confirm it matches the surrounding
page's actual heading hierarchy rather than assuming `<h2>` is always
correct (an empty state nested inside a `<h2>`-titled panel should use
`<h3>`). "The state is empty" is not a reason to skip a level — a
`<h2>` empty state inside an `<h2>`-titled parent still needs to drop
to `<h3>`, exactly as a populated equivalent would.

## Decorative icon or illustration

The shipped recipe has no icon or illustration slot, but implementations
commonly add one above the title. Any such icon or illustration is
decorative — it restates what the title already says in words — and must
carry `aria-hidden="true"` (or be a CSS background image) so it is not
announced as an unlabelled image or an empty link. Do not give it an
`alt` attribute with descriptive text; that duplicates the heading.

## CTA in `ps-empty-state__links`

`{{links}}` is free-form template content, which makes it easy to ship
as a styled `<div>` with a click handler instead of a real control. Any
call-to-action inside `ps-empty-state__links` — "Create your first
record," "Clear filters" — must render as an `<a href>` or `<button>`,
never a `<div>` or `<span>` with a click listener. A styled div is
invisible to keyboard navigation and to assistive-technology users who
tab through interactive elements; it also fails the WCAG 2.2 AA
"Name, Role, Value" criterion (4.1.2) because it has no accessible role
or keyboard operability.
