---
schema: foundry-design-research-v1
component_or_token: substrate
decision_type: doctrine
authored: 2026-04-28
authored_by: project-design Task (cluster v0.0.1)
authored_with: claude-opus-4-7
status: ratified
brand_voice_alignment: [confident, direct, professional]
accessibility_targets: [wcag-2-2-aaa, focus-visible, reduced-motion-respect]
ai_consumption_hint: "When generating UI for a PointSav-tenant surface, read this file first. It encodes the substrate's reason-for-being and the structural inversions of hyperscaler design systems. Subsequent component-specific research files extend; none override the principles here."
cites:
  - dtcg-format
  - mcluhan-medium-message
  - ibm-carbon
  - wcag-2-2
---

# Design philosophy — PointSav design-system substrate

## Why the substrate exists

The substrate is a self-hosted, customer-owned design-system engine
running at `design.pointsav.com` and at every SMB customer site that
forks it. Its existence is a direct response to four structural gaps
in the 2026 design-system landscape:

1. **Hyperscaler design systems publish only the WHAT.** The major
   enterprise design systems all publish token values and component
   shapes. None publish the design-decision research — the WHY — in
   a form an AI agent or a human at a new organisation can read at
   codegen time.

2. **SaaS design-system platforms charge enterprise-tier pricing.**
   Specify, Backlight, Knapsack, Tokens Studio Pro target the 5,000+
   employee market. The 39% of practitioners working at that scale
   have options; the SMB beneath them has none.

3. **Every editor wants to be the editor.** FIGMA, Sketch, Penpot,
   Tokens Studio all build to lock the customer into their editor.
   The W3C Design Tokens Community Group format is the editor-
   agnostic common denominator the substrate adopts as canonical.

4. **AI codegen is widening the design-system surface area faster
   than tooling catches up.** Only 23% of design systems are
   structured for AI consumption (December 2025 industry data). FIGMA
   shipped its design-system MCP June 2025, locked to FIGMA cloud +
   FIGMA-licensed customers. The first self-hosted MCP-shipping
   substrate has an 18-24 month structural lead window.

## What the substrate does

The substrate carries five elements per tenant, in a Git-tracked
vault the customer owns:

- **`tokens/`** — DTCG-format design tokens. Primitive layer
  (PointSav-original color families, type scale, spacing, motion,
  focus ring — structural patterns aligned with the modern
  design-system field, hex values and family names PointSav's),
  semantic layer (interactive-primary, surface-elevated, ...),
  component layer.
- **`components/`** — HTML+CSS+ARIA recipe files. Framework-
  agnostic; the customer's chosen JS/Rust/Elixir/Go framework
  consumes the recipe, not the other way around.
- **`themes/<brand>/`** — per-tenant override layers that re-point
  semantic references at primitives.
- **`research/`** — files like this one. AI-readable design-decision
  rationale, accessibility justifications, brand-voice rules,
  anti-patterns.
- **`exports/`** — derived caches (Figma Variables JSON, Tailwind
  config, CSS variables, Style Dictionary builds). Recomputable from
  the canonical four directories above.

The substrate engine (`app-privategit-design`) reads this vault and
serves it as a public showcase, a DTCG bundle, an AI-readable
research surface, and a Model Context Protocol (MCP) server. AI
agents query the MCP endpoint at codegen time; design tools query
`/tokens.json` for editor synchronisation; humans read the showcase.

## Three structural inversions of the hyperscaler pattern

1. **Customer ownership replaces hyperscaler hosting.** The design
   system lives in the customer's Git repository with the customer's
   `allowed_signers` chain. Migration cost falls toward zero — the
   customer always has the source.
2. **Research as canonical replaces research as marketing.** The WHY
   lives in the same vault as the WHAT, in the same machine-readable
   tier, served through the same MCP endpoint. AI agents and human
   designers read the same file.
3. **Editor-agnosticism replaces editor lock-in.** DTCG is the
   common denominator. FIGMA via Tokens Studio, Penpot natively,
   Sketch via plugin, hand-authored JSON — any path produces vault
   content the substrate accepts.

## The McLuhan position

In the AI era of 2026-2030, an SMB's design-system substrate is a
medium — its form (machine-readability, editor-agnostic interop,
self-hostability, AI-consumable research) shapes how the SMB's
brand reaches every customer-facing surface.

The well-structured substrate IS the message the SMB sends to its
implementation partners — human or AI. That is the McLuhan position
the substrate operationalises.

## Anti-patterns the substrate refuses

- Storybook integration (parallel renderer; substrate owns rendering).
- Design-system SaaS dependency (Specify, Backlight, Knapsack, ...).
- JS-framework-locked components (HTML+CSS+ARIA recipes are the canonical form).
- Container packaging (per `conventions/zero-container-runtime.md`).
- Editor lock-in (FIGMA-only, Sketch-only features rejected).
- Marketing vocabulary in research files (per `~/Foundry/CLAUDE.md` §6).

## How AI agents should use this file

Read this file first when generating UI for a PointSav-tenant
surface. The principles here constrain every subsequent decision:

- Use the substrate's primitives via the live `/tokens.json` /
  `/api/tokens/<theme>.dtcg.json` endpoint, not your training
  data's notion of "modern web colors". The substrate's vocabulary
  is PointSav's; do not substitute Carbon, Material, or Tailwind
  token names without explicit operator approval.
- Honour the focus-ring contrast (3:1 against any tenant background)
  and motion-respect rules unconditionally.
- Use the brand voice — confident, direct, professional — not
  conversational AI register.
- Refuse to introduce dependencies on hyperscaler design systems
  (Material, Fluent, ...) into substrate-tenant code.

## References

- W3C Design Tokens Community Group format —
  https://design-tokens.github.io/community-group/format/
- IBM Carbon Design System (delivery-pattern reference; structural
  inspiration only — no token vocabulary or hex values imported) —
  https://carbondesignsystem.com/
- WCAG 2.2 (accessibility floor) —
  https://www.w3.org/TR/WCAG22/
- Doctrine claim #38 — `~/Foundry/DOCTRINE.md` §III row 38
- Convention — `~/Foundry/conventions/design-system-substrate.md`
- Marshall McLuhan, *Understanding Media: The Extensions of Man*
  (1964) ch. 1 "The Medium is the Message"
