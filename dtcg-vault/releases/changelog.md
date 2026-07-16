<div class="page-intro">
<span class="eyebrow">Releases</span>
<p class="page-intro__lede">Real, dated changes to this design system's server and
token graph. Unlike a version-numbered product changelog, this page tracks what
actually shipped and when — not an invented release-number history.</p>
</div>

<div class="release-list">
<div class="release-entry">
<div class="release-entry__head">
<span class="release-entry__date">2026-07-15</span>
</div>
<p class="release-entry__summary">Paper and Writing token pillars wired end-to-end;
Products/Releases/Install pages rebuilt to the current visual system; a real WCAG
contrast failure fixed on the Critical button.</p>
<ul class="release-notes">
<li><span class="release-notes__tag release-notes__tag--added">Added</span>Paper
and Writing token pillars wired into the token gallery (<code>/tokens</code>)
end-to-end: 185 &rarr; 381 tokens (Paper 164, Writing 32). Both now have real CSS
custom properties in <code>tokens.css</code> (276 variables, including decomposed
typography composites), not just JSON/gallery-only data.</li>
<li><span class="release-notes__tag release-notes__tag--added">Added</span>Real
Paper and Writing landing pages, rebuilt Knowledge Platform/GIS/Org Charts
product-line pages, and a rebuilt Install page — replacing plain markdown lists
with the current card/stat/comparison visual system.</li>
<li><span class="release-notes__tag release-notes__tag--fixed">Fixed</span>mobile
navigation previously disappeared entirely below 1300px viewport width with no
replacement. Ported a JS-free hamburger/drawer mechanism.</li>
<li><span class="release-notes__tag release-notes__tag--fixed">Fixed</span>a real
WCAG AA contrast failure on the Critical button's resting-state color (4.44:1,
below the 4.5:1 floor) — shifted to <code>color.critical-60</code> (7.33:1). See
<a href="/components/button/accessibility">Button — Accessibility</a> for the full
writeup.</li>
<li><span class="release-notes__tag release-notes__tag--changed">Changed</span>card
hover treatment now includes a lift (translateY + elevation shadow), not just a
border-color change.</li>
</ul>
</div>
</div>

<p class="doc-footer-meta">Real component and token history before this date lives
in each component's own recipe/changelog metadata
(<code>dtcg-vault/components/*/recipe.json</code>) and this repository's git
history — not duplicated here as an invented version-number timeline.</p>

<div class="closing-cta">
<div class="closing-cta__text"><h3>Get the current release</h3>
<p>Every token and component above is live in the registry today — download the
current bundle or browse the full token set.</p></div>
<div class="closing-cta__actions">
<a href="/bundles/tokens" class="btn btn--secondary">Download tokens</a>
<a href="/tokens" class="btn btn--primary">Browse the registry</a>
</div>
</div>
