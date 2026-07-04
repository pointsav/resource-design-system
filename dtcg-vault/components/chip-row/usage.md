# When to use Chip Row

Use a chip row for an inline group of small labelled values that share a
category — a label prefix (in monospace) followed by a value, rendered as a
constrained-height inline-flex element. It reads as metadata, not as an
action.

## When to use

- Metadata rows on a detail page: status, classification, mode — one chip
  per fact.
- Compact summaries in a list or table cell where a full field label would
  take too much horizontal space.

## When not to use

- Interactive filters the user can add/remove: build a real filter-chip
  component with `role="checkbox"`/`role="button"` and `aria-pressed` — chip
  row is presentational by default, not a control.
- A single standalone value: a chip only earns its keep as part of a *row*
  of related facts. One chip alone is just a badge.

## Variants

Six semantic variants, chosen by what the value means, not by preference:

| Variant | Use for |
|---|---|
| Default | Generic categorisation — no particular semantic weight |
| Primary | Primary semantic anchor for the row |
| Accent | Classification-domain chip (e.g. a taxonomy or category tag) |
| Neutral | Mode or state chip |
| Warning | Warning / regulation-attached chip |
| Success | Verified / pass state chip |
