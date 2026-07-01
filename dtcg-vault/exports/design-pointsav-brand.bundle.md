---
name: pointsav-brand
schema: design.md/v1
source: https://design.pointsav.com/
generated_by: app-privategit-design
doctrine_claim: 38
tokens:
  border:
    corner-1: "0.125rem"
    corner-2: "0.25rem"
    corner-3: "0.5rem"
    stroke-1: "1px"
    stroke-2: "2px"
  color:
    black: "#000000"
    caution-10: "#fff5e1"
    caution-30: "#f5cd7a"
    caution-50: "#d49b1f"
    caution-60: "#a87514"
    caution-70: "#7a520a"
    critical-10: "#fceaea"
    critical-30: "#f0a3a3"
    critical-50: "#d24747"
    critical-60: "#a52323"
    critical-70: "#7d1414"
    neutral-10: "#f5f6f8"
    neutral-100: "#0e0f12"
    neutral-20: "#e6e8ec"
    neutral-30: "#cdd1d8"
    neutral-40: "#aab0bb"
    neutral-50: "#878d99"
    neutral-60: "#666c78"
    neutral-70: "#4a4f59"
    neutral-80: "#33373e"
    neutral-90: "#1f2125"
    positive-10: "#e8f6ed"
    positive-30: "#9fdaae"
    positive-50: "#3fa55c"
    positive-60: "#26823f"
    positive-70: "#16602b"
    primary-10: "#eef3ff"
    primary-20: "#d3deff"
    primary-30: "#a6bcff"
    primary-40: "#7392ff"
    primary-50: "#3f6cf2"
    primary-60: "#234ed8"
    primary-70: "#173ab1"
    primary-80: "#0c2785"
    primary-90: "#04165a"
    white: "#ffffff"
  duration:
    speed-1: "70ms"
    speed-2: "120ms"
    speed-3: "200ms"
    speed-4: "320ms"
    speed-5: "480ms"
    speed-6: "720ms"
  focus:
    ring: {"color":"{color.primary-60}","offset":"2px","style":"solid","width":"{border.stroke-2}"}
  motion:
    ease-display: [0.4, 0.14, 0.3, 1.0]
    ease-enter: [0.0, 0.0, 0.4, 1.0]
    ease-exit: [0.2, 0.0, 1.0, 1.0]
    ease-utility: [0.2, 0, 0.4, 1.0]
  size:
    space-1: "0.125rem"
    space-10: "4rem"
    space-11: "5rem"
    space-12: "6rem"
    space-13: "10rem"
    space-2: "0.25rem"
    space-3: "0.5rem"
    space-4: "0.75rem"
    space-5: "1rem"
    space-6: "1.5rem"
    space-7: "2rem"
    space-8: "2.5rem"
    space-9: "3rem"
  typography:
    display-1: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"1.25rem","fontWeight":500,"letterSpacing":"-0.01em","lineHeight":1.4}
    display-2: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"1.5rem","fontWeight":500,"letterSpacing":"-0.01em","lineHeight":1.34}
    display-3: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"2rem","fontWeight":400,"letterSpacing":"-0.015em","lineHeight":1.25}
    display-4: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"2.625rem","fontWeight":300,"letterSpacing":"-0.02em","lineHeight":1.2}
    utility-1: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"0.75rem","fontWeight":400,"letterSpacing":"0.16px","lineHeight":1.34}
    utility-2: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"0.875rem","fontWeight":400,"letterSpacing":"0.16px","lineHeight":1.43}
    utility-3: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"1rem","fontWeight":400,"letterSpacing":"0px","lineHeight":1.5}
    utility-4: {"fontFamily":"'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif","fontSize":"1rem","fontWeight":600,"letterSpacing":"0px","lineHeight":1.5}
---

# PointSav Design System — DESIGN.md export

Theme: `pointsav-brand`. Auto-generated from the live vault at <https://design.pointsav.com>.

## Overview

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
- A live DTCG token bundle at `/tokens.json`
- A shadcn-compatible registry at `/r/registry.json` (works with
  v0, Cursor, Claude Code, Windsurf out of the box)
- A DESIGN.md export at `/api/design-<theme>.md` (Google's April
  2026 spec — the substrate is among the first non-Google
  implementations)
- A Model Context Protocol JSON-RPC server at `POST /mcp` for AI
  agents querying tokens, components, and research at decode time

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


## Colors

# Color

The substrate's color system has three layers — primitive,
semantic, and component. Each tenant's brand lives at the
semantic layer; primitives are stable across tenants; components
reference semantics, never primitives directly.

## Three-layer model

```
   primitive    color.primary-60  →  #234ed8
        ↓
   semantic     interactive-primary  →  {color.primary-60}
        ↓
   component    button.background-default  →  {semantic.interactive-primary}
```

A tenant who wants their primary action to be teal instead of
blue overrides only the semantic layer:

```json
"interactive-primary": { "$value": "{color.brand-teal-60}" }
```

Components don't change. Primitives don't change. The override
ripples through every consumer of `interactive-primary`.

## Primitive families

The substrate ships five color families at the primitive layer.
Names are generic — they describe role, not business meaning.

| Family | Use for | Steps |
|---|---|---|
| **Neutral** | Backgrounds, borders, ink, dividers | 10–100 (10 steps) |
| **Primary** | The tenant's most prominent interactive color | 10–90 |
| **Positive** | Successful state, positive feedback | 10–70 |
| **Caution** | Reversible problems, expiring states | 10–70 |
| **Critical** | Failures, destructive actions, errors | 10–70 |

Numbers indicate lightness — `10` is lightest, `90`/`100` is darkest.
A designer arriving from a Carbon-influenced system recognises the
scale immediately; the muscle memory is intentional. Hex values
are PointSav's, not Carbon's.

## Semantic roles

The semantic layer maps roles onto primitives. PointSav-brand
ships one canonical mapping; SMB customers fork it.

### Ink (text)

| Token | Use for |
|---|---|
| `ink-primary` | Body text, headings on default surface |
| `ink-secondary` | Captions, helper text, supporting copy |
| `ink-on-interactive` | Text on interactive backgrounds |
| `ink-on-positive` / `-caution` / `-critical` | Text on support backgrounds |
| `ink-disabled` | Disabled controls |
| `ink-placeholder` | Input placeholder text |

### Surface (background)

| Token | Use for |
|---|---|
| `surface-base` | Default page background |
| `surface-subtle` | Backgrounded panels, sidebars |
| `surface-elevated` | Modals, popovers, layers above the page |
| `surface-inverse` | High-emphasis inversions |

### Border

| Token | Use for |
|---|---|
| `border-subtle` | Default border between sections, cards |
| `border-strong` | Emphasised divider, input border |
| `border-interactive` | Focus / active state |

### Interactive (background)

| Token | Use for |
|---|---|
| `interactive-primary` (+ hover, pressed, disabled) | Primary buttons, primary links |
| `interactive-secondary` (+ hover, pressed) | Secondary buttons |
| `interactive-ghost` (+ hover, pressed) | Ghost buttons |
| `interactive-critical` (+ hover, pressed) | Critical / destructive actions |

### Support (status feedback)

| Token | Use for |
|---|---|
| `support-positive` (+ -bg) | Successful state |
| `support-caution` (+ -bg) | Reversible problem |
| `support-critical` (+ -bg) | Failure |
| `support-info` (+ -bg) | Neutral context |

## Themes

A tenant theme is a `themes/<tenant>.json` file that overrides
the semantic layer. The substrate ships `pointsav-brand.json`;
SMB customers fork.

A tenant can ship multiple themes:

- `<tenant>-light.json` and `<tenant>-dark.json` for theme switching
- `<tenant>-seasonal-2026-q4.json` for time-bounded campaigns
- `<tenant>-acquisition-x.json` for sub-brand fan-outs

The future theme-composition endpoint
(`GET /api/themes/compose?base=...&override=...`) lets multiple
themes resolve into one DTCG bundle at request time — see Doctrine
claim #38 leapfrog target L8.

## WCAG contrast floor

The substrate's primitive choices guarantee WCAG 2.2 AAA contrast
(7:1) for the canonical text-on-surface pairs:

- `ink-primary` on `surface-base`: 14.7:1
- `ink-on-interactive` on `interactive-primary`: 7.4:1
- `ink-secondary` on `surface-base`: 8.9:1

A tenant theme that overrides primitives below the WCAG 2.2 AA
floor (4.5:1 normal text, 3:1 large text) fails the audit
endpoint (subsequent milestone). The substrate enforces the floor;
the tenant chooses everything above it.


## Typography

# Typography

Two type scales — Utility and Display — split the typographic
load between functional UI text and expressive surfaces.

## The two scales

| Scale | Use for | Sizes |
|---|---|---|
| **Utility** | UI text — body, labels, captions, table cells, button labels | 4 steps (12/14/16/16-bold) |
| **Display** | Expressive type — sub-headings, section headings, page titles, hero | 4 steps (20/24/32/42) |

The split is structural, not decorative. Utility text uses
optimised letter-spacing for screen-readability at small sizes;
Display text uses negative letter-spacing for a tighter, more
confident heading rhythm. Mixing scales (Utility-3 used as a
heading, Display-1 used for a button label) breaks the system's
visual hierarchy.

## Font stack

The substrate ships Inter as the canonical sans-serif, with a
system-stack fallback chain:

```
'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
```

Inter is a modern, open-source workhorse face (SIL OFL 1.1),
optimised for UI rendering at small sizes. The system stack
fallback ensures the substrate is fully functional even if the
Inter binary is not loaded — degradation is graceful.

A tenant theme can substitute any font family at the primitive
layer. Common substitutions:

- IBM Plex Sans (open-source, Carbon's canonical face)
- Source Sans 3 (Adobe, open-source)
- Public Sans (USWDS, public domain)
- A tenant's own brand face

Self-hosting the font binary is the customer's responsibility;
the substrate references the family by name.

## The scale

### Utility

| Token | Size / Line / Weight | Use for |
|---|---|---|
| `typography.utility-1` | 12 / 16 / 400 | Caption, label, table cell |
| `typography.utility-2` | 14 / 20 / 400 | Secondary body, helper text |
| `typography.utility-3` | 16 / 24 / 400 | Primary body floor |
| `typography.utility-4` | 16 / 24 / 600 | UI heading, button label |

### Display

| Token | Size / Line / Weight | Use for |
|---|---|---|
| `typography.display-1` | 20 / 28 / 500 | Sub-heading |
| `typography.display-2` | 24 / 32 / 500 | Section heading |
| `typography.display-3` | 32 / 40 / 400 | Page title |
| `typography.display-4` | 42 / 50 / 300 | Hero / landing |

## Heading hierarchy

| HTML | Token |
|---|---|
| `<h1>` | `display-3` |
| `<h2>` | `display-2` |
| `<h3>` | `display-1` |
| `<h4>` | `utility-4` |
| Body `<p>` | `utility-3` |
| `<small>`, helper, caption | `utility-2` |

A heading-level skip (h1 → h3 with no h2 between) breaks
accessibility — screen readers rely on the hierarchy to navigate.
The substrate enforces this in subsequent-milestone audit work.

## Brand voice

Voice, register, and vocabulary discipline are governed by the editorial
style-guide bundle (mounted at `/bundles/editorial-style-guide`), not by
this theme. The brand theme carries only visual, token, and accessibility
data.


## Spacing

# Spacing

A 13-step spacing scale on a 16px base. Numeric — `space-1` through
`space-13` — gives one canonical answer per layout decision.

## Scale

| Token | Value | Common use |
|---|---|---|
| `space-1` | 2px | Hairline gutter (rare; usually borders only) |
| `space-2` | 4px | Inline element gap |
| `space-3` | 8px | Paragraph rhythm floor; icon-label gap |
| `space-4` | 12px | Form field padding |
| `space-5` | 16px | Body grid unit; default container padding |
| `space-6` | 24px | Card padding; vertical rhythm between sections |
| `space-7` | 32px | Section gutter |
| `space-8` | 40px | Wider section gap |
| `space-9` | 48px | Major section break |
| `space-10` | 64px | Page-level section |
| `space-11` | 80px | Page-level section (looser) |
| `space-12` | 96px | Page-level section (loosest) |
| `space-13` | 160px | Hero / landing-page-only spacing |

## Composition

Compose larger spacing from the scale, never invent off-scale
values:

- 4px + 12px + 4px = `space-2 + space-4 + space-2` for a labelled
  field
- Card with 24px padding: `space-6`
- Section break with title above and content below at 32px each:
  `space-7` × 2

Off-scale values (5px, 14px, 22px) break the rhythm and accumulate
as drift. The 13-step scale is dense enough to cover every layout
need without resorting to off-scale.

## Layout floor

The substrate uses a 16px (`space-5`) baseline grid. Body text and
headings align to multiples of 16px in their line-height
calculation; container padding aligns to multiples of 16px in the
inline axis. This is structural — it ensures vertical rhythm
remains consistent across surfaces.


## Motion

# Motion

Motion communicates causation. The substrate ships four easing
curves and six duration steps. Combine them per interaction
class.

## Easing curves

| Token | Curve | Use for |
|---|---|---|
| `motion.ease-utility` | `cubic-bezier(.2, 0, .4, 1)` | Productive interactions — buttons, inputs, tabs |
| `motion.ease-display` | `cubic-bezier(.4, .14, .3, 1)` | Expressive interactions — toasts, modals, hero |
| `motion.ease-enter` | `cubic-bezier(0, 0, .4, 1)` | Element appearing |
| `motion.ease-exit` | `cubic-bezier(.2, 0, 1, 1)` | Element disappearing |

Productive curves are designed for short durations (≤200ms);
expressive curves work at longer durations (≥320ms) where the
extra weight is perceptible.

## Duration steps

| Token | Value | Use for |
|---|---|---|
| `duration.speed-1` | 70ms | Imperceptible — color hover |
| `duration.speed-2` | 120ms | Quick — button press, focus ring |
| `duration.speed-3` | 200ms | Snappy — tab switch |
| `duration.speed-4` | 320ms | Smooth — toast appearance, drawer slide |
| `duration.speed-5` | 480ms | Considered — modal entrance |
| `duration.speed-6` | 720ms | Deliberate — hero animation |

## Reduced motion

`prefers-reduced-motion: reduce` is honoured at all interaction
layers. Component recipes ship with the media-query override
included; consumers inherit. Do not bypass the override —
motion-sensitive users have explicitly opted out.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Anti-patterns

- Animations that block user input (modals fading in for 700ms
  while the focus is unfocusable). Modal entrance is `speed-5`
  for the visual; focus moves immediately at duration 0.
- Decorative motion that adds time to a productive task. Save
  expressive motion for moments that warrant the user's attention.
- Off-scale durations (350ms, 500ms). The 6-step scale covers
  every interaction class.


## Components

### Badge (`badge`)

A small, inline status indicator. Carries a short label and a tone.

[Recipe](https://design.pointsav.com/api/components/badge.json) · [Registry](https://design.pointsav.com/r/badge.json)

### Breadcrumb (`breadcrumb`)

Hierarchy trail to the current page. Useful when nested deeper than two levels.

[Recipe](https://design.pointsav.com/api/components/breadcrumb.json) · [Registry](https://design.pointsav.com/r/breadcrumb.json)

### Button (`button`)

A trigger that initiates an action. Five variants — primary, secondary, ghost, critical, link — each with its own emphasis and use context.

[Recipe](https://design.pointsav.com/api/components/button.json) · [Registry](https://design.pointsav.com/r/button.json)

### Checkbox (`checkbox`)

Boolean choice. Use when each option is independent of the others.

[Recipe](https://design.pointsav.com/api/components/checkbox.json) · [Registry](https://design.pointsav.com/r/checkbox.json)

### Citation Authority Ribbon (`citation-authority-ribbon`)

A leading source-classification badge in a references list. Six source types — Academic (A), Regulator (R), Industry (I), Direct source (D), News (N), Web-informal (W) — each with a distinct colour and single-letter glyph. Colour is never the sole differentiator; each badge carries a letter glyph and an aria-label with the full class name. Designed for Wikipedia-style references sections.

[Recipe](https://design.pointsav.com/api/components/citation-authority-ribbon.json) · [Registry](https://design.pointsav.com/r/citation-authority-ribbon.json)

### Freshness Ribbon (`freshness-ribbon`)

A per-section date badge that signals content review currency. Three semantic stops: fresh (≤90 days, green), stale (91–365 days, amber), archived (>365 days, muted). ISO date (YYYY-MM-DD) displayed in monospace — datestamp register. Attaches to <h2>/<h3> section headings via flex layout. On by default; toggle off globally via :root[data-freshness-display='off']. All three variants pass WCAG 2.2 AA contrast.

[Recipe](https://design.pointsav.com/api/components/freshness-ribbon.json) · [Registry](https://design.pointsav.com/r/freshness-ribbon.json)

### Home Grid (`home-grid`)

A 3-column responsive category-browse grid for knowledge-wiki home pages. Shows all 9 operator-ratified categories with article count, top-3 child links, and a More → entry point. Collapses to 2-col at 960px, 1-col at 640px. Empty categories always rendered with empty-state copy.

[Recipe](https://design.pointsav.com/api/components/home-grid.json) · [Registry](https://design.pointsav.com/r/home-grid.json)

### Text input (`input-text`)

Single-line text entry with label, helper text, and error state.

[Recipe](https://design.pointsav.com/api/components/input-text.json) · [Registry](https://design.pointsav.com/r/input-text.json)

### Link (`link`)

A navigation primitive — moves the user to a destination without state change.

[Recipe](https://design.pointsav.com/api/components/link.json) · [Registry](https://design.pointsav.com/r/link.json)

### Navigation bar (`navigation-bar`)

Page-level navigation header. Logo, primary nav, optional actions, optional account menu.

[Recipe](https://design.pointsav.com/api/components/navigation-bar.json) · [Registry](https://design.pointsav.com/r/navigation-bar.json)

### Notification (`notification`)

Inline messaging — informational, positive, caution, critical. Toast variant subsequent milestone.

[Recipe](https://design.pointsav.com/api/components/notification.json) · [Registry](https://design.pointsav.com/r/notification.json)

### Research Trail Footer (`research-trail-footer`)

A collapsible disclosure at article foot showing the research pipeline trail — Done, Suggested, and Open questions subsections. Collapsed by default (chrome posture). Uses native <details>/<summary> — no JavaScript required. Placed after 'See also', before 'References'. Only rendered for articles with research_trail: true frontmatter and non-zero counts.

[Recipe](https://design.pointsav.com/api/components/research-trail-footer.json) · [Registry](https://design.pointsav.com/r/research-trail-footer.json)

### Select (`select`)

Single-choice picker from a known list. Native <select> element for keyboard + screen-reader behaviour out of the box.

[Recipe](https://design.pointsav.com/api/components/select.json) · [Registry](https://design.pointsav.com/r/select.json)

### Surface (`surface`)

A container that groups related content. Three elevation levels — subtle, base, elevated — communicate visual hierarchy without coupling to specific use cases.

[Recipe](https://design.pointsav.com/api/components/surface.json) · [Registry](https://design.pointsav.com/r/surface.json)

### Switch (`switch`)

On/off toggle for settings that take effect immediately. Use when the action is reversible and binary.

[Recipe](https://design.pointsav.com/api/components/switch.json) · [Registry](https://design.pointsav.com/r/switch.json)

### Tab (`tab`)

URL-reflected page-section navigation. Each tab is a separate route; state lives in the URL, not in client memory.

[Recipe](https://design.pointsav.com/api/components/tab.json) · [Registry](https://design.pointsav.com/r/tab.json)

## Do's and Don'ts

See [`/guidelines/accessibility/overview/`](/guidelines/accessibility/overview/) and per-component anti-pattern sections.

## References

- W3C DTCG: https://design-tokens.github.io/community-group/format/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Source: https://github.com/pointsav/pointsav-design-system
