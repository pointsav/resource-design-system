---
title: Sidebar Accordion — Style
---

# Style

Token references resolve from the active theme.

## Token Mapping

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

This substrate's own live sidebar (`app-privategit-design/static/portal.css`)
implements a related but independently-evolved pattern
(`.nav-section`/`.nav-section-title`/`.sidebar li a.active`, plus a
`.nav-subgroup-label` extension for sub-grouping by origin) — the two are
not token-for-token identical; this recipe is the generic substrate form,
the app's own CSS is one concrete (and slightly extended) consumer of the
same idea.
