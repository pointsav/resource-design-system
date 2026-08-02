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

- IBM Plex Sans (open-source)
- Source Sans 3 (Adobe, open-source)
- Public Sans (public domain)
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
