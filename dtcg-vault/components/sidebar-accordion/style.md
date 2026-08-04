---
title: Sidebar Accordion — Style
---

# Style

Token references resolve from the active theme.

## Token mapping

- Section heading / secondary text: `{semantic.ink-secondary}`
- Link text (default): `{semantic.ink-primary}`
- Active link background: `{semantic.surface-raised}`
- Active link indicator / active state: `{semantic.interactive-primary}`

## Structure

- Root element: `nav.ps-sidebar`
- Section: `section.ps-sidebar__section`
- Section heading: `h2.ps-sidebar__heading`
- Item list: `ul.ps-sidebar__list`
- Link: `a.ps-sidebar__link`, active state adds `ps-sidebar__link--active`

This substrate's own live sidebar implements a related but
independently-evolved pattern — a categorised nav with section titles, an
active-link indicator, and a sub-group label for grouping items by origin —
the two are not token-for-token identical; this recipe is the generic
substrate form, and this site's own CSS is one concrete (and slightly
extended) consumer of the same idea.
