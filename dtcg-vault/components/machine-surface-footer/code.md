---
title: Machine Surface Footer — Code
---

# Code

The substrate's component recipes are framework-agnostic HTML+CSS+ARIA bundles.

## Dependencies

- Primitives: color, typography (monospace variant)
- Assets: none
- Content: three link lists supplied by the consuming page (`brandLinks`, the fixed
  machine-surface list, `provenanceLinks`) plus a `canonicalUrl` string for the base bar

## HTML recipe

```html
<footer class="ps-machine-footer">
  <div class="ps-machine-footer__inner">
    <div class="ps-machine-footer__col">
      <h2 class="ps-machine-footer__heading">{{brandLabel}}</h2>
      <ul class="ps-machine-footer__list">{{brandLinks}}</ul>
    </div>
    <div class="ps-machine-footer__col">
      <h2 class="ps-machine-footer__heading">Machine surface</h2>
      <ul class="ps-machine-footer__list">
        <li><a href="/tokens.json">/tokens.json</a></li>
        <li><a href="/components">/components</a></li>
        <li><a href="/research">/research</a></li>
        <li><a href="/healthz">/healthz</a></li>
      </ul>
    </div>
    <div class="ps-machine-footer__col">
      <h2 class="ps-machine-footer__heading">Substrate</h2>
      <ul class="ps-machine-footer__list">{{provenanceLinks}}</ul>
    </div>
  </div>
  <div class="ps-machine-footer__base">{{canonicalUrl}}</div>
</footer>
```

The "Machine surface" column's four links are fixed by the recipe — they name the actual
endpoints a substrate instance exposes. `brandLinks` and `provenanceLinks` are supplied by
the consuming page (brand identity links; Doctrine claims and standards-floor citations).

## Get the recipe

Via the substrate's registry endpoint (`https://design.pointsav.com/r/machine-surface-footer.json`)
or Git — customers running their own substrate fork the
`dtcg-vault/components/machine-surface-footer/` directory in
[`pointsav-design-system`](https://github.com/pointsav/pointsav-design-system).
