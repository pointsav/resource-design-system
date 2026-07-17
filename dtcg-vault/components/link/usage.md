# When to use Link

Use a link to navigate to a destination. Links are for *reading*;
[buttons](/components/button/usage) are for *doing*. The
distinction is invariant.

## When to use

- Cross-references between pages, articles, or sections.
- External resources (with `target="_blank"` and `rel="noopener
  noreferrer"`).
- Inline navigation within prose.

## When not to use

- For actions — even visually styled as a link. Buttons handle
  actions; links handle navigation. The distinction matters for
  keyboard users (Space activates a button, Enter activates a
  link), screen readers (different roles), and the user's mental
  model (links don't perform work).

## Underlines are non-negotiable

PointSav links carry an underline at all times. Hover does not
add the underline; it changes colour. Removing the underline is
an anti-pattern that depends on colour alone (WCAG 1.4.1) — links
indistinguishable from prose without the underline fail
accessibility.

## Visited state

Visited links shift to `interactive-primary-pressed`. This is
optional in the substrate's recipe (some surfaces — search
results, navigation toolbars — should not differentiate visited).
The recipe ships with visited styling on; remove via
`.ps-link:not(.ps-link--no-visited):visited` in customer themes.
