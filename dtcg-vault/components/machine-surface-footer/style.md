---
title: Machine Surface Footer — Style
---

# Style

Token references resolve from the active theme. The component never hardcodes a colour,
font, or spacing value.

## Token mapping

| Element | Token |
|---|---|
| Footer background | `{semantic.surface-default}` |
| Column/base-bar divider | `{semantic.border-subtle}` |
| Body link text | `{semantic.ink-secondary}` |
| Base-bar canonical-URL text | `{semantic.ink-tertiary}` |
| Link hover / active state | `{semantic.interactive-primary}` |

## Typography

Three distinct sizes carry the "this row is for machines" signal, from the recipe's own
description: small monospace section headings (11px, uppercase), body links at 14px, and
a muted monospace canonical-URL base bar at 12px. The monospace treatment is deliberate —
it's the same visual cue a code block gives, applied to a whole footer band rather than
an inline snippet.

## Structure

Three columns (brand identity, machine surface, substrate provenance), each with an `h2`
heading and a plain link list, sitting above a single-line base bar carrying the
canonical URL. No card, shadow, or border treatment on the columns themselves — the
divider is the only visual separation from the rest of the page.

Not yet specified at this stub stage: `recipe.json` carries no spacing, border-radius, or
motion tokens, and no explicit hover/pressed color table beyond the single
`interactive-primary` link-state token above. A future non-stub revision should add these
before the recipe is promoted out of `status: "stub"`.

## Live production reference

`design.pointsav.com`'s own footer (`app-privategit-design/templates/footer.html` +
`static/tokens.css`) implements the same three-part idea today, but with its own local
naming: `.ds-footer__col--mono` / `.ds-footer__col-title` classes and `--ps-footer-bg`,
`--ps-footer-ink`, `--ps-footer-ink-muted`, `--ps-footer-link`,
`--ps-footer-heading-size` (0.6875rem = 11px, matching this recipe's heading size)
custom properties — rather than this recipe's `ps-machine-footer` classes and
`{semantic.*}` token references. It is evidence the pattern works in production; it is
not itself an instance of this recipe. Reconciling the two — retrofitting the live footer
onto this recipe, or vice versa — is open work.
