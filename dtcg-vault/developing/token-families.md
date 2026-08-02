<div class="page-intro">
<span class="eyebrow">Developing</span>
<p class="page-intro__lede">Every token in this system belongs to exactly one family — a
<code>pillar / layer / family</code> grouping, e.g.
<code>paper / semantic / financial-report-layout</code>. This page names the taxonomy so
a producer archive can find the right family before guessing a token name, instead of
drafting a near-duplicate because the real one wasn't easy to find.</p>

<div class="stat-panel">
<div class="stat-panel__item"><span class="stat-panel__value">41</span><span class="stat-panel__label">Token families</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">5</span><span class="stat-panel__label">Pillars</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">0</span><span class="stat-panel__label">Hand-maintained — generated from the same registry get_token reads</span></div>
</div>
</div>

<nav class="domain-jump" aria-label="Jump to section">
<a href="#shape">The shape: pillar / layer / family</a>
<a href="#pillars">The five pillars</a>
<a href="#finding">Finding the right family</a>
<a href="#mcp-tool">list_token_families()</a>
</nav>

<section class="doc-section" id="shape">
<h2>The shape: pillar / layer / family</h2>
<p class="doc-section__intro">A token's canonical id is its pillar and its full DTCG
path, joined verbatim — no translation layer between the id, the CSS custom property,
and what <code>get_token</code> matches on (see
<a href="/developing/mcp/overview">MCP &amp; machine API</a>). A family is the
grouping one level up: every token that shares the same pillar, layer, and top-level
name.</p>

<div class="card-grid">
<div class="card"><h3>Pillar</h3>
<p>The top-level tier: <code>primitive</code>, <code>theme</code>, <code>paper</code>,
<code>writing</code>, <code>wcp</code>.</p></div>
<div class="card"><h3>Layer</h3>
<p>Only <code>paper</code> and <code>writing</code> genuinely nest under a
<code>primitive</code>/<code>semantic</code> wrapper before their real groups start — so
only those two pillars carry a layer. Every other pillar's layer is <code>null</code>;
its first path segment is the family directly.</p></div>
<div class="card"><h3>Family</h3>
<p>The named group itself — a document family like
<code>financial-report-layout</code>, a craft group like <code>rhythm</code>, or a
primitive category like <code>color</code>. Every leaf token in a family shares the
same id prefix.</p></div>
</div>

<p class="doc-section__intro">Worked example: the token
<code>--ps-paper-semantic-financial-report-layout-header-rule</code> has pillar
<code>paper</code>, layer <code>semantic</code>, family
<code>financial-report-layout</code> — readable directly off the id string, since the
id <em>is</em> the pillar/layer/family path with no re-casing or re-delimiting.</p>
</section>

<section class="doc-section" id="pillars">
<h2>The five pillars</h2>
<p class="doc-section__intro">Each row is a real pillar in the current export, not an
aspirational list — counts are live, same source as the stat panel above.</p>

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Pillar</th><th>Layer</th><th>What it holds</th><th>Example families</th></tr></thead>
<tbody>
<tr><td><code>primitive</code></td><td>—</td><td>Raw, tenant-neutral values: color, spacing, typography, motion, borders, viewport, focus, duration.</td><td><code>color</code> (60), <code>typography</code> (14), <code>size</code> (13)</td></tr>
<tr><td><code>theme</code></td><td>—</td><td>PointSav's own default/reference theme — semantic-role mappings onto primitives, plus a dark-mode variant. The vendor's reference theme, not a tenant fork (see the pillar note below).</td><td><code>semantic</code> (53), <code>dark</code> (28), <code>accessibility</code> (5)</td></tr>
<tr><td><code>paper</code></td><td>primitive / semantic</td><td>Print/document-formatting substrate — page geometry, rule weights, type scales, and one semantic family per document register (legal agreements, financial reports, PDF-binder navigation, Mexico FIBRA trust/prospectus, org-chart print diagrams, …).</td><td><code>mx-fibra-prospectus</code> (49), <code>legal-subscription-agreement</code> (30), <code>financial-report-layout</code> (25)</td></tr>
<tr><td><code>writing</code></td><td>primitive / semantic</td><td>Prose-governance tokens — voice, rhythm, casing, register scale, disclaimer templates, and named content patterns for a specific document family.</td><td><code>register</code> (7), <code>rhythm</code> (7), <code>pattern</code> (4)</td></tr>
<tr><td><code>wcp</code></td><td>—</td><td>Engine-facing CSS custom-property namespaces — currently one family, a pure alias layer over an already-canonical Paper family, never a second literal-value store (see <a href="/tokens#paper">financial-report-layout</a>).</td><td><code>finance</code> (25, all aliases)</td></tr>
</tbody>
</table>
</div>

<div class="registry-note"><span aria-hidden="true">&#8618;</span>
<span>The <code>theme</code> pillar holds PointSav's own reference theme only — it is not
a multi-tenant fork target. An adopting tenant's own brand-specific token values (e.g.
Woodfine's palette) live in that tenant's own media-assets repo, layered on top via CSS
custom-property override, not inside this pillar. See
<code>.agent/rules/design-tokens.md</code> in the project-design archive for the full
rationale.</span>
</div>

<div class="registry-note"><span aria-hidden="true">&#8618;</span>
<span>A sixth and seventh pillar (org-chart color-extension tokens) were retired
2026-08-02 — their one real value is now <code>paper.primitive.color.org-chart-role-
warm-gray-*</code> / <code>paper.semantic.org-chart.role-warm-gray-*</code>, alongside
the rest of the org-chart document family's tokens. The retired pillars' names embedded
a third-party product's brand directly into shipped CSS custom-property names, which
this registry no longer does anywhere.</span>
</div>
</section>

<section class="doc-section" id="finding">
<h2>Finding the right family before drafting a new one</h2>
<p class="doc-section__intro">The failure mode this taxonomy exists to prevent: a
producer archive can't find an existing family, assumes one doesn't exist, and drafts a
near-duplicate under a new name. Two checks, in order:</p>

<div class="card-grid">
<div class="card"><h3>1. Is it a document-family variation?</h3>
<p>A new compliance document, print register, or legal instrument almost always composes
existing <code>paper.primitive.*</code> and adds one new
<code>paper.semantic.&lt;family&gt;.*</code> group — it very rarely needs new primitives.
Check the Paper families table above and on <a href="/tokens#paper">Tokens — Paper
tier</a> before assuming none of the ten existing document families are close
enough to extend from.</p></div>
<div class="card"><h3>2. Is it a genuinely new value, or a tenant's brand fork?</h3>
<p>A literal color/size/type value that's reusable across any adopting tenant belongs in
<code>primitive</code> or a Paper/Writing family. A value that encodes one specific
tenant's brand identity does not belong in this repository at all — see the pillar note
above.</p></div>
</div>
</section>

<section class="doc-section closing-note" id="mcp-tool">
<h2>list_token_families(pillar?)</h2>
<p class="doc-section__intro">The machine-readable form of this page. Returns every
family — the same rows as the table above — as JSON, optionally filtered to one pillar,
sourced from the same generated <code>token-families.json</code> registry
<code>get_token</code> and this page both read. See
<a href="/developing/mcp/overview">MCP &amp; machine API</a> for the full tool list and
call shape.</p>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Response</span><span>application/json</span></div>
<pre><code><span class="tok-attr">[</span>
  <span class="tok-attr">{</span> <span class="tok-attr">"pillar"</span>: <span class="tok-str">"paper"</span>, <span class="tok-attr">"layer"</span>: <span class="tok-str">"semantic"</span>, <span class="tok-attr">"family"</span>: <span class="tok-str">"financial-report-layout"</span>, <span class="tok-attr">"member_count"</span>: <span class="tok-str">25</span> <span class="tok-attr">}</span>,
  <span class="tok-attr">{</span> <span class="tok-attr">"pillar"</span>: <span class="tok-str">"wcp"</span>, <span class="tok-attr">"layer"</span>: <span class="tok-str">null</span>, <span class="tok-attr">"family"</span>: <span class="tok-str">"finance"</span>, <span class="tok-attr">"member_count"</span>: <span class="tok-str">25</span> <span class="tok-attr">}</span>
  <span class="tok-attr">// … 39 more</span>
<span class="tok-attr">]</span></code></pre>
</div>
</section>
