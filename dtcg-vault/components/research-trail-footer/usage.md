<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">3 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
<span class="badge">Zero JavaScript</span>
</div>
<p class="doc-header__lead">A collapsible bottom-of-article disclosure that makes a wiki
article's epistemic frontier explicit — what was researched, what should be researched
next, and what remains an open question. Collapsed by default; the summary line carries
the counts, so a reader sees the shape of the evidence before expanding a single
section.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/research-trail-footer/recipe.json</code></div>
</div>

## When to use Research Trail Footer

Use Research Trail Footer at the foot of a documentation-wiki article
to disclose its research trail — the three fixed subsections
**Research done**, **Suggested research**, and **Open questions**. It
is the article-scale rendering of the same discipline every
DESIGN-DRAFT and wiki draft already carries in frontmatter: it takes
the three research-trail fields a draft must declare and turns them
into a reader-facing, machine-readable block at the point where a
reader has finished the prose and is deciding how much to trust it.

Place it at the bottom of the article, after *See also* and before
*References*. It is a single element per article — not a general
callout or a repeatable inline aside. If an article has no research
trail to disclose, it should not render the footer at all (see
*Suppressed* below), rather than render an empty one.

This component is part of the
[Knowledge Platform](/products/knowledge-platform/overview) surface —
it renders the epistemic-honesty convention that platform expects of
every article, at article scale.

## Variants

The three variants are states of one article's footer, selected at
render time — not styling options an author picks per instance.

| Variant | Renders |
|---|---|
| **Collapsed** | Default. The summary line with its counts is visible (`N done · N suggested · N open question(s)`); the three subsections are hidden until the reader expands. |
| **Expanded** | The full three-subsection content is visible — Research done, Suggested research, and Open questions, each with its list. |
| **Suppressed** | Nothing renders. The article frontmatter declares `research_trail: false`, or all three counts are zero. An article with no trail shows no footer rather than an empty one. |

## Anatomy

The footer is a native `<details>` / `<summary>` pair — no JavaScript.
The browser owns the collapse behaviour, the keyboard interaction, and
the expanded/collapsed state announced to assistive technology.

1. **Summary** — the always-visible line. It reads
   `Research trail — N done · N suggested · N open question(s)`, and
   is the click and focus target that toggles the body.
2. **Body** — an `aria-label`ed section holding three fixed
   subsections in fixed order. Each subsection is an `<h3>` followed
   by a list:
   - **Research done** — sources already consulted (academic,
     primary, secondary).
   - **Suggested research** — work that should be done next to
     strengthen or verify a claim.
   - **Open questions** — questions the article does not yet answer.

Each subsection heading carries a coloured leading rule so the three
categories are distinguishable at a glance: success for *done*, brand
blue for *suggested*, warn for *open* (see [Tokens](#tokens)).

## Counts are render-time, not author-maintained

The three counts in the summary line are derived from the article's
frontmatter fields — `research_done_count`, `research_suggested_count`,
and `open_questions_count` — and substituted at render time. Authors
do not hand-maintain the summary string, and it cannot drift out of
step with the frontmatter it summarises. These are the same three
research-trail fields the DESIGN-DRAFT and wiki-draft conventions
require on every real draft; the footer is where that convention
becomes visible to a reader on a live article.

## Machine-readable output

Alongside the visible block, the footer emits JSON-LD
`potentialAction` nodes: a `SearchAction` for each suggested-research
item and a `Question` for each open-question item. This lets an LLM or
other automated consumer identify an article's epistemic frontier —
what is settled, what is suggested, what is open — without parsing the
prose. The disclosure a human reads and the signal a machine reads
come from the same source.

## Tokens

Every colour, space, and type value is a token reference — the
component holds no hard-coded values.

| Token | Role |
|---|---|
| [`semantic.surface.layer-accent`](/tokens#theme) | Footer background |
| [`semantic.border.subtle`](/tokens#theme) | Left border of the footer container |
| [`semantic.text.primary`](/tokens#theme) | List-item text |
| [`semantic.text.secondary`](/tokens#theme) | Summary line text |
| [`semantic.interactive.focus-ring`](/tokens#theme) | Summary `:focus-visible` ring |
| [`primitive.color.status.success`](/tokens#primitive) | *Research done* heading rule |
| [`primitive.color.brand.blue.60`](/tokens#primitive) | *Suggested research* heading rule |
| [`primitive.color.status.warn`](/tokens#primitive) | *Open questions* heading rule |
| [`primitive.font.family.sans`](/tokens#primitive) | Summary and heading type |
| [`primitive.space.1`](/tokens#primitive), [`primitive.space.2`](/tokens#primitive), [`primitive.space.4`](/tokens#primitive) | Padding, margins, list indent |

## Accessibility

**Target: WCAG 2.2 AA.**

- **Native semantics.** The `<details>` / `<summary>` pair means the
  browser handles keyboard interaction (Enter and Space on the
  summary), the screen-reader announcement, and the `aria-expanded`
  state natively. There is no custom ARIA to keep correct and no
  JavaScript that can fail.
- **Heading level.** The three subsections use `<h3>` because the
  article's own `## Research trail` renders as an `<h2>` — the footer
  slots correctly beneath it in the document outline rather than
  breaking heading order.
- **Focus.** The summary shows a visible focus ring on
  `:focus-visible`, drawn from `semantic.interactive.focus-ring` with
  a 2px offset, so keyboard users can see the toggle target.
- **Colour is not the only signal.** The three subsections are
  distinguished by their headings and order, not by the coloured rule
  alone — the rule is a reinforcement, so the categories remain
  unambiguous without colour perception.

## When not to use

- Do not use it as a general-purpose callout or collapsible aside.
  It is a single, fixed, three-subsection article footer — for other
  disclosure patterns, use the substrate's generic disclosure
  primitives.
- Do not render it more than once per article, and do not reorder or
  omit the three subsections — the *done / suggested / open* order is
  fixed.
- Do not render an empty footer. An article with no research trail
  uses the *Suppressed* variant and renders nothing.

<div class="doc-footer-meta">
<span>surface:</span> wiki article foot
<span class="doc-footer-meta__sep">&middot;</span>
<span>depends on:</span>
<a href="/tokens#theme">semantic.surface.layer-accent</a>,
<a href="/tokens#theme">semantic.interactive.focus-ring</a>,
<a href="/tokens#primitive">primitive.color.status.warn</a>
</div>
