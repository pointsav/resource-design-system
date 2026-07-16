# Writing

Prose-governance tokens — voice, rhythm, casing, register, and disclaimer
templates — for the same reason color and spacing are tokenized: a house
style decided once should be enforceable everywhere, not re-argued in every
document review. Like Paper, Writing tokens ship generically and empty of
tenant-specific vocabulary; a brand override repoints the alias the same way
`themes/<brand>.json` repoints color.

## Voice

<div class="card-grid">
<div class="card"><span class="card__eyebrow eyebrow">Default</span><h3>Active voice</h3>
<p>Name the actor and the consequence. Default posture for every register below.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Forward-looking</span><h3>Planned / intended / may / target</h3>
<p>Not-yet-true capabilities wear their status visibly — the BCSC disclosure posture,
tokenized so it's mechanically enforceable rather than a style-guide sentence someone
has to remember.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Credibility</span><h3>Mechanism, number, verifiable claim</h3>
<p>Never borrow a named institution for prestige — support a claim with the mechanism
and a real number instead.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Concrete word</span><h3>Prefer concrete over abstract</h3>
<p><code>use</code> &gt; utilize &middot; <code>end</code> &gt; terminate &middot;
<code>explain</code> &gt; elucidate &middot; a named number &gt; a vague quantifier.</p></div>
</div>

## Rhythm

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Rule</th><th>Value</th></tr></thead>
<tbody>
<tr><td>Target sentence length</td><td>15–20 words (18-word house average)</td></tr>
<tr><td>Fact-of-record sentence ceiling</td><td>25 words — a target for a definition/compliance/legal claim, not a hard gate</td></tr>
<tr><td>Paragraph length</td><td>3–7 lines; past 7 a paragraph usually carries two ideas</td></tr>
<tr><td>Heading density</td><td>~1 heading per 120–140 body words</td></tr>
<tr><td>Lead length</td><td>100–400 words</td></tr>
</tbody>
</table>
</div>

## Casing

Title, heading, and slug casing follow one rule consistently: capitalize the
first word plus proper nouns, acronyms, and code identifiers only — never a
generic title-case pass, and no leading article ("the"/"a"/"an") on a title,
heading, or slug.

<div class="type-sample-grid">
<div class="type-sample"><div class="type-sample__label">Correct</div>
<p class="type-sample__text">Designing with the token registry</p></div>
<div class="type-sample"><div class="type-sample__label">Incorrect</div>
<p class="type-sample__text">The Designing With The Token Registry</p></div>
</div>

## Register

Six registers, each tied to a real content profile rather than a subjective
"tone":

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Register</th><th>Posture</th></tr></thead>
<tbody>
<tr><td>how-to</td><td>Operational imperative</td></tr>
<tr><td>reference</td><td>Neutral factual clause</td></tr>
<tr><td>communications</td><td>Institutional</td></tr>
<tr><td>journal</td><td>Academic</td></tr>
<tr><td>legal</td><td>Plain-language binding</td></tr>
<tr><td>specialist</td><td>Prescriptive normative</td></tr>
</tbody>
</table>
</div>

Content profiles compose registers rather than picking one in isolation:
documentation blends reference + how-to; corporate and project pages read as
reference throughout.

## Disclaimer templates

Four real, parameterized templates — placeholders resolve per tenant, never
hardcoded to PointSav or Woodfine at the token layer:

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Template</th><th>Shape</th></tr></thead>
<tbody>
<tr><td>Securities forward-looking</td><td><code>{corporate_entity} operates {technology_subsidiary} as {entity_relationship}...</code> — forward-looking-statement notice with material-risk and no-update-obligation clauses</td></tr>
<tr><td>Trademark footer</td><td><code>{marks} are trademarks of {owner_entity}, used in {jurisdictions}...</code></td></tr>
<tr><td>Privacy posture</td><td><code>This interface operates on a {telemetry_scope} architecture.</code></td></tr>
<tr><td>Contact block</td><td><code>{role}, {entity}, {address}, {email}, {phone}</code></td></tr>
</tbody>
</table>
</div>

## Lexicon — ships empty by design

The banned/required-term and thematic-anchor lists are a real, defined
structure with **no generic entries** — a brand override supplies actual
terms the same way a theme file repoints color aliases. There is currently
no PointSav- or Woodfine-specific term list published here; this page
intentionally does not invent one.

## Revision loop

One documented editorial pattern: <code>draft-improves-draft</code> — each
revision pass sets up a clearly better next pass, and a single pass revises
one altitude at a time (structure, then paragraph, then sentence), top-down
rather than mixing levels.

<p class="doc-footer-meta">Full token detail: <a href="/tokens#writing">Tokens — Writing tier</a>. Source: <code>dtcg-vault/writing/{primitive,semantic}.json</code> in the design-system repository.</p>
