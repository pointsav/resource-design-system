# Accessibility

The substrate targets WCAG 2.2 AAA. Every component recipe ships
conformant out of the box; tenants who fork the substrate inherit
the floor unless they deviate at the primitive layer.

## Conformance commitments

- **WCAG 2.2 AAA** for the canonical PointSav-brand theme on
  every shipped component recipe
- **WCAG 2.2 AA minimum** for any tenant theme that overrides
  primitives — the audit endpoint (subsequent milestone) flags
  drops below AA
- **EN 301 549** alignment for European public-sector tenants
- **Section 508** alignment for US public-sector tenants

## What every component carries

Every recipe in `dtcg-vault/components/` ships an
`accessibility.md` tab covering:

1. **Conformance status** — WCAG criterion-by-criterion table
2. **Keyboard interactions** — Tab, Shift+Tab, Space, Enter,
   arrow keys, Escape
3. **Screen reader behaviour** — announced role, name, value
4. **Reduced motion** — `prefers-reduced-motion: reduce` honoured
5. **Touch targets** — 44x44 minimum
6. **Colour independence** — no state communicated by colour
   alone
7. **Anti-patterns** — common deviations and why they break

## Recipe model is structurally accessible

The substrate's HTML+CSS+ARIA recipe model puts native elements
first, so keyboard and screen-reader behaviour comes straight from
the browser — no framework event layer sits between the user and
native browser events:

- **Native HTML elements first.** `<button>` instead of `<div
  role="button">`. The native element brings keyboard and
  screen-reader behaviour for free.
- **No JS required for activation.** Buttons, links, form
  controls work without JavaScript loaded — degrades gracefully
  on slow connections, ad blockers, JS errors.
- **No synthetic event layer.** The recipe doesn't capture the
  user's keyboard events through a framework's synthetic-event
  system; native browser events fire.

## Tenant override floor

A tenant who forks the substrate cannot unconfigure the
accessibility floor. Three commitments are enforced regardless
of theme overrides:

1. **Focus is always visible.** Component recipes never set
   `outline: none` without an alternative.
2. **Touch targets are never below 44x44.** Component recipes
   include the focus-ring offset in the activatable area.
3. **Motion respects `prefers-reduced-motion`.** Every recipe
   ships the media-query override.

The audit endpoint (subsequent milestone) flags violations of
these commitments.

## Audit endpoint (subsequent milestone)

`GET /api/audit/wcag?theme=<theme>` is planned to return
per-component WCAG conformance for the named theme — contrast
ratios, focus ring presence, touch target sizes, motion override
coverage.
The response is JSON suitable for CI/CD integration (`exit 1` on
fail) or AI-agent consumption.

Today this page is the canonical conformance statement; the
audit endpoint formalises what's already required.

## Where to look

- Each [component](/components/button/usage) carries its own
  Accessibility tab.
- [Color](/elements/color/overview) covers contrast at the
  primitive layer.
- [Motion](/elements/motion/overview) covers reduced-motion
  patterns.
- [Typography](/elements/typography/overview) covers heading
  hierarchy and screen-reader navigation.
