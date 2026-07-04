# When to use Sidebar Accordion

Use for a categorised left-rail navigation surface: sections labelled with
small monospace caps, items as horizontally-padded links, one active link
per view (2px left border in the brand accent, plus a soft accent-tint
background).

This substrate's own documentation site (design.pointsav.com) dogfoods a
close variant of this exact pattern in its live sidebar — see
`.nav-section` / `.nav-section-title` / `.sidebar li a.active` in
`app-privategit-design/static/portal.css`. That implementation additionally
supports nested sub-groups (`.nav-subgroup-label`) for grouping items by
origin within one section — a real-world extension beyond what this
component's current recipe covers (see "Status" below).

## When to use

- Multi-section in-app navigation where the current location needs a
  persistent, always-visible left rail (documentation portals, admin
  consoles, settings screens).
- Content organised into named categories where one item is active at a
  time and `aria-current="page"` communicates location.

## When not to use

- A small number of flat, unrelated links — use a plain link list instead
  of introducing section headings for one or two items.
- Primary top-level navigation on a marketing or public-facing page — this
  pattern is for in-app orientation, not acquisition surfaces.

## Status — recipe is a stub, not an accordion yet

Despite the component's name, the current `recipe.json` (`"status":
"stub"`, flowed back from project-bim's `design-generic-components-index.md`,
2026-04-29) contains a **static** categorised nav list — one section
heading, one active-link example — with no expand/collapse toggle, no
`aria-expanded` state, and no JS. There is exactly one variant ("default").
If accordion (collapsible-section) behavior is added in a future pass, it
must follow the disclosure pattern already established elsewhere in this
app (P1.7): a collapsed section is removed from the tab order via
`visibility:hidden`, not merely `max-height:0`, and the toggle carries
`aria-expanded`/`aria-controls`. Until then, treat this component as "named
sections + active-link indicator," not as a true accordion.
