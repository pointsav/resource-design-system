# Component guide — org-chart-node-pill variants (teal, grey)

Modifier classes extending `.org-token-pill` for fund / flow-through and
placeholder entity roles. CSS lives in `components/nodes.css`.

## HTML recipe

```html
<!-- Teal pill — fund / flow-through entity -->
<div class="org-token-pill org-token-pill--teal">
  <div class="zone-top"><span class="t-title">Fund Name Ltd.</span></div>
  <div class="zone-mid"><span class="t-code">FND-001</span></div>
</div>

<!-- Grey pill — inactive / placeholder entity -->
<div class="org-token-pill org-token-pill--grey">
  <div class="zone-top"><span class="t-title">TBD Entity</span></div>
</div>
```

## CSS (in `components/nodes.css`)

```css
/* Teal pill — fund / flow-through entity role */
.org-token-pill--teal {
    background: var(--wf-teal-tint);
    border-color: var(--wf-teal);
    border-style: dotted;
}

/* Grey pill — placeholder / TBD entity */
.org-token-pill--grey {
    background: var(--wf-grey-tint);
    border-color: var(--wf-grey);
    border-style: dotted;
}
```

Token dependencies: `--wf-teal`, `--wf-teal-tint` (added `theme-woodfine.css` 2026-06-03),
`--wf-grey`, `--wf-grey-tint` (existing).

## ARIA notes

Pill nodes are display containers, not interactive controls. No additional ARIA
attributes beyond standard `.org-token` node patterns. Dotted border is purely
visual; chart authors should add an instance-level context label:

```html
<div class="org-token-pill org-token-pill--teal"
     aria-label="Flow-through entity: Fund Name Ltd.">
```

## When to use

| Pill type | Role | Border style |
|---|---|---|
| Base (amber) | Holding structure / SPV | dashed |
| `--teal` | Fund / flow-through entity | dotted |
| `--grey` | Placeholder / TBD | dotted |

Dotted vs dashed is a semantic distinction: dotted = relationship type not yet
finalized or a pass-through vehicle; dashed = direct-hold structure.

## Open questions

1. Is dotted (not dashed) the intended semantic distinction for teal/grey pills?
   Observed consistently across four Bencal charts — treat as confirmed until
   operator says otherwise.
2. `--sm` modifier for teal/grey (`org-token-pill--teal.org-token-pill--sm`)
   not observed in Bencal charts but may be needed for dense layouts.
