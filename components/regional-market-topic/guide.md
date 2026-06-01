# Regional Market TOPIC — Component Guide

**Type:** Article template  
**Research:** `dtcg-vault/research/regional-market-topic.md`  
**Origin:** project-gis DESIGN-RESEARCH (2026-05-30)

Two-column wiki article template for Regional Market pages. Composes existing design-system
tokens; introduces the `rm-*` CSS class namespace.

---

## HTML skeleton

```html
<article class="rm-article">

  <!-- Two-column layout wrapper -->
  <div class="rm-layout">

    <!-- LEFT: article body -->
    <div class="rm-body">
      <h1 class="article__title">Wichita, Kansas — Regional Market</h1>

      <p class="rm-lead">Lead paragraph.</p>

      <section class="rm-overview">
        <h2 id="overview">Overview</h2>
        <p>Wikipedia summary extract, attributed.</p>
      </section>

      <section class="rm-colocation">
        <h2 id="co-location-profile">Co-location Profile</h2>
        <table class="rm-cluster-table">
          <thead>
            <tr>
              <th scope="col">Cluster</th>
              <th scope="col">Tier</th>
              <th scope="col">Anchor Composition</th>
              <th scope="col">Span (km)</th>
              <th scope="col">Civic</th>
            </tr>
          </thead>
          <tbody>
            <tr class="tier-t1">
              <td><a href="https://gis.woodfinegroup.com/?cluster=NA-12345">East Kellogg Hypermarket Belt</a></td>
              <td><span class="rm-tier-badge rm-tier-badge--t1">T1</span></td>
              <td>Hypermarket + Hardware</td>
              <td>2.1</td>
              <td><span class="rm-civic-yes">Yes</span></td>
            </tr>
          </tbody>
        </table>
      </section>

      <section class="rm-civic">
        <h2 id="civic-infrastructure">Civic Infrastructure</h2>
        <h3>Medical</h3>
        <ul><li>Ascension Via Christi St Francis</li></ul>
        <h3>Academic</h3>
        <ul><li>Wichita State University</li></ul>
      </section>

      <section class="rm-aec">
        <h2 id="aec-data">AEC Data</h2>
        <dl class="rm-aec-grid">
          <dt class="rm-aec-grid-label">ASHRAE 169 Zone</dt>
          <dd class="rm-aec-grid-value">4A — Mixed-Humid</dd>
          <dt class="rm-aec-grid-label">Köppen-Geiger Class</dt>
          <dd class="rm-aec-grid-value">Cfa — Humid subtropical</dd>
        </dl>
      </section>

      <section class="rm-score">
        <h2 id="composite-score">Composite Score</h2>
        <table class="rm-score-table">
          <thead>
            <tr><th scope="col">Metric</th><th scope="col">Value</th><th scope="col">Weight</th></tr>
          </thead>
          <tbody>
            <tr><td>Cluster count</td><td>12.0</td><td>3.0</td></tr>
            <tr><td>Best-tier weight</td><td>16.0</td><td>4.0</td></tr>
            <tr><td>Civic infrastructure</td><td>8.0</td><td>2.0</td></tr>
            <tr><td>AEC coverage</td><td>6.0</td><td>1.5</td></tr>
            <tr><td>Mobility coverage</td><td>4.0</td><td>1.0</td></tr>
            <tr><td>Span penalty</td><td>2.0</td><td>0.5</td></tr>
            <tr class="rm-score-total"><td>Total</td><td>48.0</td><td></td></tr>
          </tbody>
        </table>
        <!-- Optional bar visualisation (aria-hidden; prefers-reduced-motion: drops to table-only) -->
        <div class="rm-score-bars" aria-hidden="true">
          <div class="rm-score-bar">
            <span class="rm-score-bar-label">Best-tier weight</span>
            <span class="rm-score-bar-fill" style="--rm-bar-pct: 33%"></span>
            <span class="rm-score-bar-value">16.0</span>
          </div>
        </div>
      </section>

      <section class="rm-references">
        <h2 id="wikipedia-references">Wikipedia References</h2>
        <ul>
          <li><a href="https://en.wikipedia.org/wiki/Wichita,_Kansas">Wichita, Kansas</a></li>
        </ul>
      </section>

      <footer class="rm-wiki-attribution">
        Wikipedia content reproduced under
        <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC BY-SA 4.0</a>.
        Accessed <time datetime="YYYY-MM-DD">YYYY-MM-DD</time>.
        Original article(s): <a href="https://en.wikipedia.org/wiki/Wichita,_Kansas">Wichita, Kansas</a>.
      </footer>
    </div>

    <!-- RIGHT: infobox -->
    <aside class="rm-infobox" aria-labelledby="rm-infobox-heading">
      <h2 id="rm-infobox-heading" class="visually-hidden">Market Summary</h2>
      <dl class="rm-infobox-fields">
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Rank</dt>
          <dd class="rm-infobox-field-value"><span class="rm-rank-badge">16 / 400</span></dd>
        </div>
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Best Tier</dt>
          <dd class="rm-infobox-field-value"><span class="rm-tier-badge rm-tier-badge--t1">T1</span></dd>
        </div>
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Clusters</dt>
          <dd class="rm-infobox-field-value">4</dd>
        </div>
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Composite Score</dt>
          <dd class="rm-infobox-field-value">48.0</dd>
        </div>
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Country</dt>
          <dd class="rm-infobox-field-value">US</dd>
        </div>
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Nearest major centre</dt>
          <dd class="rm-infobox-field-value">Oklahoma City, 250 km SE</dd>
        </div>
        <div class="rm-infobox-field">
          <dt class="rm-infobox-field-label">Centroid</dt>
          <dd class="rm-infobox-field-value">37.6872, −97.3301</dd>
        </div>
      </dl>
      <!-- Wikipedia thumbnail (conditional on thumbnail.source availability) -->
      <figure class="rm-wiki-thumb">
        <img src="" alt="" loading="lazy">
        <figcaption class="rm-wiki-thumb-caption">
          <a href="">City Name (Wikipedia)</a>
        </figcaption>
      </figure>
    </aside>

  </div>
</article>
```

---

## CSS class reference

| Class | Element | Notes |
|---|---|---|
| `.rm-article` | Outer `<article>` | |
| `.rm-layout` | Two-column flex/grid wrapper | |
| `.rm-body` | Left column | |
| `.rm-infobox` | Right column `<aside>` | `position: sticky; top: var(--rm-infobox-sticky-top)` |
| `.rm-infobox-fields` | `<dl>` inside infobox | |
| `.rm-infobox-field` | One field div (dt+dd pair) | |
| `.rm-infobox-field-label` | `<dt>` | |
| `.rm-infobox-field-value` | `<dd>` | |
| `.rm-rank-badge` | Rank display | |
| `.rm-tier-badge` | Tier chip | Modifiers: `--t1` gold, `--t2` silver, `--t3` bronze |
| `.rm-wiki-thumb` | Wikipedia thumbnail `<figure>` | Conditional on API response |
| `.rm-wiki-thumb-caption` | `<figcaption>` | |
| `.rm-lead` | Lead paragraph | |
| `.rm-cluster-table` | Co-location `<table>` | |
| `.tier-t1/t2/t3` | Table row background | Decorative tint; tier also in badge |
| `.rm-civic-yes` | "Yes" civic badge cell | |
| `.rm-civic-no` | "No" civic badge cell | |
| `.rm-aec-grid` | AEC `<dl>` | `grid-template-columns: max-content 1fr` |
| `.rm-aec-grid-label` | AEC `<dt>` | |
| `.rm-aec-grid-value` | AEC `<dd>` | |
| `.rm-score-table` | Score `<table>` | |
| `.rm-score-total` | Bold total row | |
| `.rm-score-bars` | Bar visualisation container | `aria-hidden="true"` |
| `.rm-score-bar` | One bar row | |
| `.rm-score-bar-fill` | Bar fill | Width via `--rm-bar-pct` CSS custom property |
| `.rm-score-bar-label` | Bar label | |
| `.rm-score-bar-value` | Bar value | |
| `.rm-wiki-attribution` | Attribution `<footer>` | Mandatory when Wikipedia content is embedded |
| `.rm-wiki-attribution a` | Links inside footer | |

---

## ARIA

- Infobox `<aside>` labelled by hidden `<h2>` via `aria-labelledby="rm-infobox-heading"`.
- Tier row background is decorative — tier is also conveyed by the badge (not colour-only).
- Civic Yes/No is a text label (not a glyph).
- Score bar visualisation: `aria-hidden="true"` — data is in the table above.
- AEC grid uses `<dl>` for screen-reader term/definition pairing.

---

## Token dependencies

No new tokens required. Tier tint row colours reference design-system token bundle values;
if a tier-tint token is absent, open a separate DESIGN-TOKEN-CHANGE before implementing.
`--rm-infobox-sticky-top` must be set from an existing layout token (topnav height).
Mobile breakpoint inherits existing 768 px wiki chrome variable.
