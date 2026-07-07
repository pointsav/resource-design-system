# What is the PointSav Design System

The PointSav Design System is a self-hosted, customer-owned
substrate for SMBs who want to ship coherent, accessible,
AI-readable interfaces without paying enterprise SaaS pricing or
accepting hyperscaler brand voice.

The vendor showcase at `design.pointsav.com` is the canonical
instance. Each SMB customer who forks the substrate runs their
own instance at their own domain. Single codebase, single
deployment shape, two contexts.

## What it does

The substrate carries five elements per tenant, in a Git-tracked
vault the customer owns:

- **Tokens** in W3C Design Tokens Community Group format
  (DTCG 2025.10 stable spec) — primitive layer (color, type,
  spacing, motion, focus), semantic layer (interactive-primary,
  surface-elevated, ...), per-component scopes
- **Components** as HTML+CSS+ARIA recipe files — framework-
  agnostic; the customer's chosen JS framework consumes the
  recipe, not the other way around
- **Themes** — per-brand override layers that re-point semantic
  references at primitives
- **Research** — AI-readable design-decision rationale,
  accessibility justifications, brand-voice rules
- **Exports** — derived caches (Figma Variables JSON, Tailwind
  config, CSS variables, Style Dictionary builds)

The substrate engine reads the vault from disk and exposes:

- A public showcase (this site) with the structure design-system
  practitioners recognise from their previous role
- A downloadable token bundle via `/bundles/tokens/download`
- A Model Context Protocol JSON-RPC server at `POST /mcp` for AI
  agents querying tokens, components, and research at decode time
- Planned: a live DTCG token bundle at `/tokens.json`, a
  shadcn-compatible registry at `/r/registry.json` (v0, Cursor,
  Claude Code, Windsurf), and a DESIGN.md export at
  `/api/design-<theme>.md` (Google's April 2026 spec) — none of
  these three are implemented yet; do not cite them as shipped

## Three structural inversions

The substrate inverts the hyperscaler design-system pattern on
three structural axes:

1. **Customer ownership replaces hyperscaler hosting.** The
   design system lives in the customer's Git repository, signed
   by the customer's key, replayable into any tool. Migration
   cost falls toward zero.

2. **Research as canonical replaces research as marketing.** The
   *why* lives in the same vault as the *what*, in the same
   machine-readable tier, served through the same MCP endpoint.
   AI agents and human designers read the same files.

3. **Editor-agnosticism replaces editor lock-in.** DTCG is the
   common denominator. FIGMA via Tokens Studio plugin, Penpot
   natively, Sketch via plugin, hand-authored JSON — any path
   produces vault content the substrate accepts.

## Who uses the substrate

- **SMBs without an in-house design-system practitioner** — the
  substrate gives them Carbon-shape muscle memory without an
  agency engagement.
- **Holding companies, franchise operators, white-label
  resellers** — the multi-tenant theme model fans out a single
  substrate across many brands.
- **Regulated SMBs** (financial services, healthcare, legal) —
  the customer-rooted attestation pattern means the design system
  is part of the customer's audit surface, not the vendor's SaaS
  controls.
- **AI-codegen-aware teams** — every code generator (v0, Cursor,
  Claude Code, Windsurf) reads the substrate's MCP and registry
  endpoints at decode time. Generated UI matches the SMB's brand
  intent without re-deciding the same questions every session.

## How it relates to other design systems

The substrate's *delivery pattern* — sidebar navigation, four
canonical tabs per component (Usage / Style / Code /
Accessibility), live preview, Git-linked source — is recognisable
to anyone who has worked with a Carbon-influenced design system.
The cognitive on-ramp is intentional.

The substrate's *vocabulary* — token names, component recipes,
research files — is PointSav-original. No IBM trademarks, no
Carbon-derived hex values, no IBM Plex font binding (Inter ships
as the default; tenants substitute freely). The substrate is
inspired by Carbon's information architecture, not built on
Carbon's licensing surface.

## What the substrate is NOT

- **Not a Storybook replacement.** Storybook is a parallel
  renderer; the substrate owns its rendering.
- **Not a Figma / Penpot / Sketch competitor.** Those are design
  editors; the substrate is the canonical store the editors
  interop with via DTCG.
- **Not a SaaS platform.** It is self-hosted by design.
- **Not a JS-framework choice.** Components are HTML+CSS+ARIA
  recipes; the customer's chosen framework consumes the recipe.
- **Not a container artefact.** The substrate ships as native
  binaries deployed via systemd. No Docker, no Kubernetes, no
  OCI artefacts.

## Where to next

- [Components](/components/overview/) — the component recipe library
- [Color](/elements/color/overview/) — the color system
- [Typography](/elements/typography/overview/) — the type scales
- [GitHub](https://github.com/pointsav/pointsav-design-system) —
  fork the substrate, file an issue, contribute a recipe
