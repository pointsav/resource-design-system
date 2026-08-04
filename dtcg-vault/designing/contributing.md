# Contributing

This substrate is built to receive real proposals from other product clusters, not
just from the team that maintains it directly. The process below isn't a hypothetical
— it's the exact path a real contribution took, from a domain-specific product build to
eight components now documented in the [component library](/components/chip-row/usage).

## Two ways in

**You're building something domain-specific and think part of it is generic.** This is
the common path — a product team (GIS, BIM, the wiki engine, or a future cluster) builds
UI for its own domain, notices a pattern that isn't domain-specific at all, and proposes
it for the shared substrate. The worked example below follows this path exactly.

**You want to change an existing token or component.** Open an issue on
[GitHub](https://github.com/pointsav/pointsav-design-system) with the label `design`,
including a screenshot and the affected component or token name. Token changes
specifically require an additional maintainer sign-off before they land — see the note
on that below.

## Process, worked from a real example

In April–May 2026, the BIM product team was mid-build on its own AEC-domain UI. Along
the way, it had assembled nine component patterns. Some were genuinely BIM-specific — a
3D viewport, a spatial tree browser, an IFC properties panel. Others weren't
domain-specific at all: a copy-to-clipboard code block, a semantic chip row, a
categorised sidebar. The team proposed the second group back to this substrate.

**Step 1 — draft, don't just paste code.** The proposal wasn't a pull request of raw
markup. It was a `DESIGN-RESEARCH` draft — `design-generic-components-index.md` — naming
each candidate component, its structural shape, and one genuinely open question: should
the generic versions inherit BIM's own `.bim-*` class-naming convention, or use this
substrate's existing `ps-*` prefix?

**Step 2 — submit it, addressed to this substrate.** The proposal was submitted through
the standard design-contribution pipeline and then waited in a queue. Nothing moved
automatically until a maintainer here picked it up.

**Step 3 — review resolves naming, scope, and licensing — explicitly, in writing.** This
is the part worth reading closely, because the reasoning is what makes a review real
rather than rubber-stamped:

- *Naming*: `ps-*` won, not `.bim-*` — because a tenant surface that consumes both
  BIM-specific and generic components needs a coherent vocabulary. BIM's own internal
  classes stay `.bim-*` in the BIM product's own codebase; only the generic forms
  crossing into this substrate take the `ps-*` prefix.
- *Scope — what actually crossed over*: eight of the nine proposed patterns were accepted
  as generic stubs (`chip-row`, `code-block-with-copy`, `edit-on-github-link`,
  `empty-state-card`, `machine-surface-footer`, `preview-frame`, `sidebar-accordion`,
  `tab-bar-disclosure` — the same eight now fully documented in this library). The ninth,
  a breadcrumb pattern, was **not** added. This substrate already shipped an equivalent
  `breadcrumb` component, so the review pointed the BIM team at reusing it instead of
  forking a near-duplicate. Seven further patterns (a 3D viewport, spatial tree,
  properties panel, and four more AEC-specific components) were explicitly **excluded**
  as too domain-specific for a generic substrate. Those stayed in the BIM product's own
  component set rather than crossing into the generic library.
- *Licensing, forwarded rather than decided unilaterally*: the same review cycle surfaced
  that one BIM-specific component (a 3D viewport built on an AGPL-3.0-licensed rendering
  library) changes the licensing posture of the app that ships it. This substrate doesn't
  make licensing calls on another team's behalf. The finding was written down and
  forwarded for governance review rather than acted on locally.

**Step 4 — acceptance is a committed, git-tracked decision record**, not a verbal
agreement. Two research files carry the full reasoning: one records the structural
acceptance (path conventions, token taxonomy, what's in vs. out), the other records the
component flowback itself (naming resolution, the accepted/rejected list, and what each
stub still needs before it's a complete recipe). Both live in `research/` in this vault,
readable by anyone — human or AI agent — deciding whether to build on this pattern.

**Step 5 — a stub becomes a real component over time, not all at once.** Landing as a
`recipe.json` stub is the start, not the finish. Each of those eight components needed a
follow-up pass — `usage.md`, `style.md`, `code.md`, `accessibility.md` — written against
the stub's actual structure. That pass honestly notes where the recipe still falls short
of its name. One of the eight, for instance, is still a static list rather than a true
accordion, and says so on its own usage page rather than pretending otherwise.

## What this means if you're proposing something

- Write down *why* a pattern is generic, not just that it exists — the review needs a
  reason to say yes, and a reason to say no to the parts that should stay domain-specific.
- Expect naming and scope questions to get resolved in writing, with a stated rationale —
  not silently deferred and not decided by whoever writes the most code first.
- If your proposal touches licensing (a dependency with a viral license, a token that
  crosses a compliance boundary), say so explicitly rather than letting it surface later.
- A stub is an honest starting point. Don't promise complete behavior in a component's own
  docs that the recipe doesn't actually implement yet.

## Token changes need a co-sign

Any change to `tokens/dtcg-bundle.json` or a token file requires an additional
maintainer sign-off before it can be committed here — this is a harder gate than
component proposals, since a token change can silently shift color, spacing, or type
across every consuming surface at once.
