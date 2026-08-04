<div class="page-intro">
<span class="eyebrow">Developing</span>
<p class="page-intro__lede">This server exposes a Model Context Protocol (MCP) JSON-RPC
endpoint alongside the pages you're reading right now. It also offers a small set of
plain GET endpoints for agents that don't need the full MCP envelope. Point an
MCP-capable agent at it and it can query components, tokens, and research notes
directly — no separate service to stand up, no copy of the registry to keep in sync by
hand.</p>

<div class="stat-panel">
<div class="stat-panel__item"><span class="stat-panel__value">5</span><span class="stat-panel__label">MCP tools</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">5</span><span class="stat-panel__label">Documented endpoints</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">1</span><span class="stat-panel__label">Token export format (DTCG)</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">0</span><span class="stat-panel__label">External network calls</span></div>
</div>
</div>

<nav class="domain-jump" aria-label="Jump to section">
<a href="#mcp">MCP endpoint</a>
<a href="#registry-api">Registry API</a>
<a href="#token-export">Token export</a>
<a href="#why-it-matters">One registry, no machine-only path</a>
</nav>

<section class="doc-section" id="mcp">
<h2>On-prem MCP endpoint</h2>
<p class="doc-section__intro">This same binary exposes a Model Context Protocol (MCP)
server alongside the pages you're reading right now. Point an MCP-capable agent at it
and it can query components, tokens, and research notes directly — no separate service
to stand up, no copy of the registry to keep in sync by hand.</p>

<div class="card onprem-callout">
<div class="onprem-callout__icon" aria-hidden="true">&#8962;</div>
<div>
<h3>Runs on your own infrastructure</h3>
<p>The MCP server ships inside the same binary as this documentation site. When you run
it on your own hardware, every tool call — from a single <code>get_token</code> lookup
to a full <code>list_components</code> sweep — is answered locally. Nothing about your
codebase, your prompts, or which components an agent is asking about is sent to any
third party; it never leaves your own network.</p>
<p>There is no hosted alternative — on-prem, as described on
<a href="/developing/install/overview">Self-host</a>, is the only way this surface is
offered.</p>
</div>
</div>

<div class="card-grid">
<div class="card"><h3><span class="mcp-tool__name">list_components(category?)</span></h3>
<p class="mcp-tool__desc">Returns every component the registry currently knows about,
optionally filtered by origin category (generic substrate, GIS-origin, wiki-engine-origin),
with a pointer to its full recipe.</p></div>
<div class="card"><h3><span class="mcp-tool__name">get_component_recipe(name)</span></h3>
<p class="mcp-tool__desc">Returns the HTML/CSS recipe, token dependencies, and
accessibility targets for one named component — the same data a human reads on its
Components page.</p></div>
<div class="card"><h3><span class="mcp-tool__name">get_token(name)</span></h3>
<p class="mcp-tool__desc">Resolves a single design token by its CSS custom property name
(<code>--ps-interactive</code>) or DTCG path (<code>semantic.interactive-primary</code>).</p></div>
<div class="card"><h3><span class="mcp-tool__name">search_design_system(query)</span></h3>
<p class="mcp-tool__desc">Full-text search across every indexed vault document —
components, tokens, research, guidelines, developing, designing, about — for an agent
that doesn't yet know the exact name of what it needs.</p></div>
<div class="card"><h3><span class="mcp-tool__name">list_token_families(pillar?)</span></h3>
<p class="mcp-tool__desc">Returns every token family (pillar/layer/family grouping,
e.g. <code>paper/semantic/financial-report-layout</code>) with its member count,
optionally filtered to one pillar. The taxonomy to check before guessing a token
group's name — see <a href="/developing/token-families/overview">Token families</a>.</p></div>
</div>
</section>

<section class="doc-section" id="registry-api">
<h2>Registry / machine API</h2>
<p class="doc-section__intro">There is no single aggregate registry file to fetch.
Component recipes, the token bundle, and full-text search are three separate real
endpoints — verified directly against the running server's own route table.</p>

<div class="endpoint-meta"><span class="badge badge--brand">POST</span><code>/mcp</code></div>
<p class="endpoint-meta__desc">JSON-RPC 2.0. Always returns HTTP 200 — check the response
body for an <code>error</code> key rather than the status code. Standard MCP envelope:
<code>tools/list</code> to enumerate the five tools above, <code>tools/call</code> to
invoke one.</p>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Request</span><span>Example</span></div>
<pre><code>curl -s https://design.pointsav.com/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_component_recipe","arguments":{"name":"button"}}}'</code></pre>
</div>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Response</span><span>application/json</span></div>
<pre><code><span class="tok-attr">{</span>
  <span class="tok-attr">"jsonrpc"</span>: <span class="tok-str">"2.0"</span>,
  <span class="tok-attr">"id"</span>: <span class="tok-str">1</span>,
  <span class="tok-attr">"result"</span>: <span class="tok-attr">{</span>
    <span class="tok-attr">"content"</span>: [<span class="tok-attr">{</span> <span class="tok-attr">"type"</span>: <span class="tok-str">"text"</span>, <span class="tok-attr">"text"</span>: <span class="tok-str">"{ ...recipe.json, as a string... }"</span> <span class="tok-attr">}</span>]
  <span class="tok-attr">}</span>
<span class="tok-attr">}</span></code></pre>
</div>
<p class="endpoint-meta__desc">The recipe travels inside
<code>result.content[0].text</code> as a JSON string, not as a top-level object — parse
it once more on your side. Reading
<code>dtcg-vault/components/button/recipe.json</code> directly is the file-system
alternative.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/components/:slug/recipe.json</code></div>
<p class="endpoint-meta__desc">A plain, curl-able GET for one component's recipe — no
JSON-RPC envelope. Reads <code>vault/components/&lt;slug&gt;/recipe.json</code> verbatim
and serves it as <code>application/json</code>.</p>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Request</span><span>Example</span></div>
<pre><code>curl -s https://design.pointsav.com/components/button/recipe.json</code></pre>
</div>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/tokens/search?q=...</code></div>
<p class="endpoint-meta__desc">Full-text search across components, tokens, and research
notes — the same index the <code>search_design_system</code> MCP tool queries. Response
is a JSON array of <code>{id, title, snippet, url}</code> objects, capped at 20 hits. An
empty or missing <code>q</code> returns <code>[]</code>.</p>

<div class="registry-note"><span aria-hidden="true">&#8618;</span>
<span><code>/mcp</code>, <code>/components/:slug/recipe.json</code>, and
<code>/tokens/search</code> all read the same vault files every human-facing page on
this site renders from. There is no second copy of this data to fall out of sync.</span>
</div>
</section>

<section class="doc-section" id="token-export">
<h2>DTCG token export</h2>
<p class="doc-section__intro">Agents that only need the token values — not full
component recipes — can pull the registry's DTCG-format export directly, without going
through <code>/mcp</code> at all.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/bundles/tokens/tokens.full.json</code></div>
<p class="endpoint-meta__desc">The full DTCG token bundle — every primitive and theme
token, real dotted paths and values, served as plain <code>application/json</code>.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/bundles/tokens/tokens.css</code></div>
<p class="endpoint-meta__desc">The same tokens compiled to CSS custom properties, served
as <code>text/css</code> — link it directly.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/bundles/tokens/download</code></div>
<p class="endpoint-meta__desc">Zips the current tokens bundle
(<code>tokens.full.json</code>, <code>tokens.css</code>, plus the bundle's
research/attribution files) for offline use.</p>
</section>

<section class="doc-section closing-note" id="why-it-matters">
<h2>Why this matters</h2>
<p class="doc-section__intro">Every endpoint on this page — <code>/mcp</code>,
<code>/components/:slug/recipe.json</code>, <code>/tokens/search</code>,
<code>/bundles/tokens/*</code> — reads from the same registry that drives every other
page on this site, including the token counts and swatches on
<a href="/tokens">Tokens</a>. There is no separate code path reserved for machines.</p>
</section>
