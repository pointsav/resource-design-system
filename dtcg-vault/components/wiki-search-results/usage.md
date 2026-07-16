<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">2 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">The results surface for a documentation wiki's full-text
search — an ordered list of hits, each a linked article title over a ~180-character
plain-text excerpt, with a distinct zero-results state that prompts the reader to
retry. It renders whatever the wiki's Tantivy search index returns; it holds no query
logic of its own.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-search-results/recipe.json</code></div>
</div>

## When to use Wiki Search Results

Use Wiki Search Results to present the response to a full-text search
across a [Knowledge Platform](/products/knowledge-platform/overview)
wiki. It is the display layer for one specific data shape — the hit
list returned by the wiki's search index — and nothing else. Given a
query and a set of hits, it renders the count, the ranked list of
article links with excerpts, and, when the set is empty, a retry
prompt.

It is not a search *input*. The search box, its keyboard handling,
and the request to the index live elsewhere; this component consumes
the response. It is also not a general-purpose list — the markup,
excerpt length, and empty-state copy are all specific to the wiki
search contract described below.

## Variants

The recipe defines two variants, corresponding to the two states a
search response can be in.

| Variant | Shows |
|---|---|
| **with-results** | A count summary (`N results for "query"`) followed by an ordered list of hits — each an article-title link over a plain-text excerpt. |
| **zero-results** | An empty state with the message `No results for "query". Try fewer or different keywords.` and no list. |

The two states are mutually exclusive within a single render. The
zero-results block is toggled through the `[hidden]` attribute rather
than a `display` rule, which keeps the state change legible to
assistive technology (see [Accessibility](#accessibility)).

## Anatomy

The results set is a single `<section>` landmark labelled for the
active query. Inside it:

1. **Summary** — `N result(s) for "query"`, where the plural `s` is
   present only when the count is not 1.
2. **List** — an ordered list (`<ol>`), one `<li>` per hit. Each hit
   is a **title link** (`<a href="/{slug}">{title}</a>`) followed by
   a **plain-text excerpt** (`<p>{snippet}</p>`).
3. **Empty state** — a single message block, rendered in place of the
   list when the count is zero.

The excerpt is displayed as text, not HTML. The index returns the
first non-empty, non-heading paragraph of the article, roughly 180
characters, truncated at a word boundary with a trailing ellipsis
(`…`). No highlight markup is present today; see [Data source](#data-source).

## Data source

This component renders the response of the wiki's search index. Per
the recipe's research notes, that index is Tantivy, queried over the
same JSON-RPC-over-`/mcp` convention the substrate documents at
[MCP overview](/developing/mcp/overview): an HTTP `POST /mcp` carrying
a JSON-RPC 2.0 envelope. The wiki deployment exposes a `search`
method — `params: { q, limit }` (the HTML page requests `limit: 25`;
agent callers default to `10`).

The response shape the component is built against is:

```
{ "query": "…", "count": N, "hits": [ { "slug": "…", "title": "…", "snippet": "…" } ] }
```

Two properties of that contract shape the markup directly:

- **Snippets are plain text — there is no `<mark>` highlighting.**
  The excerpt is assigned as text content, never as innerHTML. Do not
  add client-side highlighting that assumes HTML in the snippet.
- **The relevance score is internal.** Tantivy computes a BM25 score
  to rank hits, but it is not part of the returned JSON. The list is
  already in rank order; the component does not display or re-sort by
  score.

## Tokens

Every colour, space, and type value in the recipe resolves to a
substrate token — no literal values are hard-coded except the 1px
hairline rule on each result divider. The recipe declares the
following token surface:

| Token | Tier | Drives |
|---|---|---|
| `{primitive.font.family.body}` | [primitive](/tokens#primitive) | Body typeface for the whole results section |
| `{semantic.text.primary}` | [theme](/tokens#theme) | Primary text |
| `{semantic.text.secondary}` | [theme](/tokens#theme) | Summary line, excerpt, and empty-state text |
| `{semantic.interactive.link}` | [theme](/tokens#theme) | Article-title link colour |
| `{semantic.interactive.link-hover}` | [theme](/tokens#theme) | Title link on hover |
| `{semantic.border.subtle}` | [theme](/tokens#theme) | Hairline divider between results |
| `{primitive.space.2}` | [primitive](/tokens#primitive) | Gaps between hits, list spacing |
| `{primitive.space.4}` | [primitive](/tokens#primitive) | Vertical padding of the empty state |

Because the palette values come entirely from theme tokens, the
component re-themes with the active tenant automatically — the same
markup carries whatever text, link, and border values the mounted
theme supplies.

## Accessibility

Target: **WCAG 2.2 AA**.

- **Live region.** The results `<section>` carries `aria-live="polite"`
  and `aria-atomic="true"`, and an `aria-label` naming the active
  query. When a new search replaces the contents, a screen reader
  announces the updated block — including the result count — without
  the reader having to move focus into it. `polite` (not `assertive`)
  lets the announcement wait for a pause in speech.
- **Empty state toggling.** The zero-results block is shown and hidden
  with the `[hidden]` attribute rather than a `display:none` CSS rule.
  `[hidden]` removes the block from the accessibility tree cleanly, so
  assistive technology never encounters a stale or duplicated empty
  message when results are present.
- **Excerpt text.** Snippets are plain text straight from the index,
  so there is no markup for a screen reader to stumble over and no
  sanitisation step required.
- **Links.** Each hit is a real anchor to the article's slug, so it is
  reachable by keyboard and exposed as a link — not a scripted
  click target — to assistive technology.

## When not to use

- Do not use this for a search *input* or autocomplete surface — it
  renders results only.
- Do not use it for a non-wiki result set. The excerpt length,
  empty-state copy, and plain-text snippet contract are specific to
  the wiki search index; a different data source needs a different
  component.
- Do not inject HTML into the excerpt. The current contract is
  plain-text-only; if the index later returns highlighted snippets
  (see below), that is a recipe change, not a per-consumer override.

## Open question

The recipe records one forward-looking item: a later Tantivy phase may
add query-aware snippet generation with `<mark>` highlights. If that
ships, the excerpt template will need a sanitised `innerHTML`
assignment in place of the current text assignment. Until then, treat
the plain-text snippet contract as fixed.

<div class="doc-footer-meta">
<span>data source:</span> <a href="/developing/mcp/overview">POST /mcp — JSON-RPC search</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>depends on:</span>
<a href="/tokens#theme">semantic.interactive.link</a>,
<a href="/tokens#theme">semantic.text.secondary</a>,
<a href="/tokens#theme">semantic.border.subtle</a>
</div>
