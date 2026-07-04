# When to use Machine Surface Footer

Use this footer on a PointSav machine surface — a showcase/reference instance built on
the substrate, a documentation hub, an API status page — where a real audience of the
page is codegen agents and tooling, not only human visitors. It exists alongside (not
instead of) a normal human-facing footer nav: a three-column band — brand identity,
machine surface links (`/tokens.json`, `/components`, `/research`, `/healthz`), and
substrate provenance (Doctrine claims, standards floor) — set in small monospace type to
visually signal "this row is for machines" the same way a code block signals "this is
literal," distinct from the prose column beside it.

This is not a speculative pattern. `design.pointsav.com` itself already ships the same
idea in production: its footer carries a dedicated "Machine surface" column
(`/tokens/search`, `/bundles/:name`, `/bundles/:name/download`, `/healthz`) in monospace,
visually separated from the family-link row above it
(`app-privategit-design/templates/footer.html`, `.ds-footer__col--mono`). That deployment
is the proof of concept for the pattern and predates this recipe — but it uses its own
local class names and `--cds-footer-*` custom properties, not this recipe's
`ps-machine-footer` classes or `{semantic.*}` token references. Treat it as evidence the
pattern earns its place on a real page, not as a literal instance of this recipe; see
Style for the naming divergence.

## When to use

- The footer of any substrate showcase or reference site that exposes a machine-readable
  surface (a `/tokens.json` endpoint, an MCP server, a component registry) and wants that
  surface to be discoverable, not just documented in prose elsewhere on the page.
- Sites where the operator wants to signal "this is self-hostable, inspectable
  infrastructure" — the machine-surface column is itself evidence of that claim, not just
  a description of it.

## When not to use

- A page with no real machine-readable endpoints to list. An empty or aspirational
  machine-surface column undercuts the exact credibility signal it's meant to provide —
  don't ship this component until the endpoints it lists actually resolve.
- Marketing pages aimed at a purely human audience (e.g. a landing page with no
  developer/agent-facing surface). Use a conventional footer there instead.
- As a substitute for real API documentation. The footer is a discoverability aid — "here
  is where the machine-readable material lives" — not the documentation itself. Pair each
  linked endpoint with its own proper reference.

## Status note

The recipe currently ships as a single, fixed composition — one column count, one heading
size, one machine-surface link set — recorded as `"status": "stub"` in `recipe.json`
(`stub_source: project-bim flowback — design-generic-components-index.md, 2026-04-29`).
There is no variant switch yet (unlike, for example, Button's four emphasis levels).
Treat additions — a two-column compact variant, a mobile-collapsed variant, per-tenant
machine-surface link overrides — as forward work, not as something already shipped.
