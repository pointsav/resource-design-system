<div class="page-intro">
<span class="eyebrow">Self-host</span>
<p class="page-intro__lede"><code>app-privategit-design</code> is the same engine that
runs design.pointsav.com. Build the binary and point it at your own vault directory.
It then serves your design system's token gallery, component docs, Writing/Paper
content, and an on-prem MCP endpoint directly from your own infrastructure. Your
tokens, your change history, your perimeter — a small VM, a spare rack unit, or a
laptop repurposed as a server. No cloud dependency, no managed database, no account rep
to call.</p>
</div>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">Quickstart</span></div>
<h2>Build the binary, point it at a vault directory, and it's running.</h2>
<p class="install-block__intro">There is no installer wizard and no license-key
activation step. The binary reads three environment variables and starts serving.</p>

<div class="doc-code-block">
<div class="doc-code-block__label"><span>Terminal</span><span>bash</span></div>
<pre><code>$ git clone https://github.com/pointsav/pointsav-design-system.git
$ git clone https://github.com/pointsav/pointsav-monorepo.git
$ cd pointsav-monorepo &amp;&amp; cargo build --release -p app-privategit-design
$ DESIGN_VAULT_DIR=../pointsav-design-system/dtcg-vault \
  DESIGN_BIND=127.0.0.1:9094 \
  DESIGN_SITE_ORIGIN=https://design.example.com \
  ./target/release/app-privategit-design
<span class="tok-comment"># serving on 127.0.0.1:9094
# Tokens, Components, Writing, Paper + on-prem MCP endpoint, all from this process</span></code></pre>
</div>
</section>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">Why one binary</span></div>
<h2>One binary replaces the database, cache, and per-seat meter.</h2>
<p class="install-block__intro">A typical hosted design-system platform asks a
short-staffed team to run a second stack alongside the actual design work.</p>

<div class="compare-callout">
<div class="compare-callout__heading"><strong>Typical stack vs. this server</strong></div>
<div class="compare-callout__cols">
<div class="compare-callout__col compare-callout__col--them">
<div class="compare-callout__col-title">Typical hosted platform</div>
<ul>
<li>Managed Postgres instance to provision and back up</li>
<li>Redis (or similar) for sessions/cache</li>
<li>Per-seat monthly meter</li>
<li>Design data lives on a vendor's infrastructure</li>
<li>An AI agent query travels to a third party's servers for an answer</li>
</ul>
</div>
<div class="compare-callout__col compare-callout__col--us">
<div class="compare-callout__col-title">app-privategit-design</div>
<ul>
<li>No Postgres — state lives in the vault's own Git-tracked files</li>
<li>No Redis</li>
<li>No per-seat meter for the FSL-1.1-ALv2 source</li>
<li>One binary, your own infrastructure</li>
<li>On-prem MCP endpoint — agent queries stay on your own network</li>
</ul>
</div>
</div>
<p class="compare-callout__footnote">Comparing typical hosted-platform architecture in
general terms; verified against this crate's own <code>Cargo.toml</code> — no database
or cache driver dependency exists in the real dependency tree.</p>
</div>
</section>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">What it takes to run</span></div>
<h2>Modest hardware, real licensing terms.</h2>

<div class="note-strip"><div class="note-strip__body">
<p><strong>Hardware footprint:</strong> a single Rust binary with no database or cache
process to run alongside it — the dependency tree carries no Postgres/Redis driver.
No GPU or cluster is required to serve the design-system content itself.</p>
</div></div>

<div class="note-strip"><div class="note-strip__body">
<p><strong>License:</strong> the source ships under <strong>FSL-1.1-ALv2</strong>,
converting automatically to Apache-2.0 two years after each release. Design tokens are
licensed separately, under Apache-2.0. See the <a
href="/developing/license/overview">full licensing breakdown</a> for the commercial
tier and what FSL does and doesn't restrict.</p>
</div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>What's next</h3>
<p>Walk through the token set that ships with the binary, or see how an AI agent
connects to the on-prem MCP endpoint once it's running.</p></div>
<div class="closing-cta__actions">
<a href="/tokens" class="btn btn--secondary">Explore Tokens</a>
<a href="/developing/mcp/overview" class="btn btn--primary">Connect your AI agents</a>
</div>
</div>
