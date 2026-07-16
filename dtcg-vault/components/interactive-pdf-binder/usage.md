<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">4 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target (print/PDF)</span>
</div>
<p class="doc-header__lead">A print-first navigation system for assembled multi-document
PDF binders on US Letter (612×792pt, origin bottom-left). One component, three
navigation surfaces — a slip-sheet table-of-contents cover, TOC entries (active and
inactive), and a HOME return button stamped on every content page — that together turn
a stack of concatenated source PDFs into a document a reader can move through inside any
PDF viewer.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/interactive-pdf-binder/recipe.json</code></div>
</div>

## What it is

Interactive PDF Binder Navigation is not a DOM component. It is the design-system record
for the navigation layer that `tool-pdf-interactive.py` (reportlab + pypdf) stamps onto
an assembled binder of source PDFs. The recipe's `html`/`css` describe only the
design-system *preview* surface; the shipped artifact is a static PDF whose interactivity
lives entirely in PDF link annotations and the document outline.

Every value on this page — geometry, colour, type — is drawn from the canonical Python
constants in the generator, extracted directly rather than from prose, and consolidated
into the [Paper pillar](/paper/paper/overview) as the `paper.*.pdf-nav` / `pdf-binder`
token groups. See the [Paper tokens tier](/tokens#paper) for the leaf values.

This is the only member of the Paper document family that is genuinely *interactive*
within its viewer. The other five families are static CSS-print layouts:
[legal subscription agreement](/components/legal-subscription-agreement/usage),
[legal prospectus](/components/legal-prospectus/usage),
[legal agency suite](/components/legal-agency-suite/usage),
[financial report layout](/components/financial-report-layout/usage), and
[financial statement (year-end)](/components/financial-statement-yearend/usage).

## When to use

- **Assembling several source PDFs into one deliverable** — a binder of agreements,
  schedules, or statements that a reader must navigate between. The slip-sheet TOC gives
  each source document a cover and a jump target.
- **A binder that will be read on screen, in a PDF viewer.** The GoTo links and document
  outline are the point; a binder intended only for print does not need this layer.
- **When the reader needs to return to the index repeatedly.** The HOME button on every
  content page is the return path.

## When not to use

- **Do not use it for a single, authored document.** If there is nothing to bind, there
  is no TOC to generate — reach for the relevant CSS-print family instead.
- **Do not use it to restyle the source PDFs.** The generator overlays navigation; it
  does not reflow, re-tag, or re-typeset the documents it binds.
- **Do not treat the point-space geometry as CSS `@page` geometry.** This component is
  rendered in PDF point coordinates with a bottom-left origin — it deliberately keeps its
  own `paper.primitive.pdf-nav.*` group rather than sharing the CSS-print page primitives.

## The three navigation surfaces

The binder navigation is composed of three surfaces. Two of them (the TOC entry) have an
active and an inactive form, giving four variants in total.

### 1 · Slip-sheet TOC cover

A generated cover page inserted before each source document. It carries a header title,
an organisation subtitle, a 1.5pt rule, an optional right-aligned draft/version label
(first sheet only), and an italic footer instruction. A single slip sheet holds **up to 8
TOC entries**; that ceiling is currently a hard limit in the generator (see Open
questions).

### 2 · TOC entry

One navigable row per bound document, in two states:

- **Inactive** — a navy number and title for a document other than the current one, with
  an invisible full-rect GoTo link to that document's slip sheet.
- **Active** — the row for the current document: a grey-light highlight rectangle, black
  text, and a leading arrow indicator. It carries no link, because it points at itself.

### 3 · HOME return button

A 64×20pt navy rounded rectangle (4pt corner radius) with a white `HOME` label, placed
lower-right. It is stamped on every content page — never on a slip sheet — and carries a
transparent GoTo link back to page 0, top.

## Variants

| Variant | Surface | Description |
|---|---|---|
| **slip-sheet** | TOC cover | Generated cover preceding each source document: header title, org subtitle, 1.5pt rule, optional right-aligned draft label (first sheet only), italic footer instruction. Holds up to 8 TOC entries per sheet. |
| **toc-entry-inactive** | TOC entry | Navigable row for a non-current document: navy number + title, invisible full-rect GoTo link to that document's slip sheet. |
| **toc-entry-active** | TOC entry | Row for the current document: grey-light highlight rect, black text, leading arrow indicator; no link (self). |
| **home-button** | Return button | 64×20pt navy rounded-rect (4pt radius) with white HOME label, lower-right placement. Stamped on every content page (never slip sheets); transparent GoTo link to page 0 top. |

## Coordinate space and geometry

The binder is generated in PDF point-space on US Letter, **612×792pt, origin
bottom-left** — not a CSS `@page` box model. All geometry comes from
`paper.primitive.pdf-nav.*`:

| Primitive | Token | Value |
|---|---|---|
| Page width | `{paper.primitive.pdf-nav.page-width}` | 612pt |
| Page height | `{paper.primitive.pdf-nav.page-height}` | 792pt |
| Content zone | `margin-left` / `margin-right` | 72pt–540pt |
| First TOC entry baseline | `toc-entry-first-y` | 565pt |
| TOC entry step (centre-to-centre) | `{paper.primitive.pdf-nav.toc-entry-step}` | 65pt |
| TOC entry height | `toc-entry-height` | 46pt |
| TOC entry width | `toc-entry-width` | 530pt |
| HOME button width | `{paper.primitive.pdf-nav.home-width}` | 64pt |
| HOME button height | `{paper.primitive.pdf-nav.home-height}` | 20pt |
| HOME corner radius | `{paper.primitive.pdf-nav.home-corner-radius}` | 4pt |
| Slip-sheet rule stroke | `rule-stroke` | 1.5pt |

The 1.5pt slip-sheet rule is the **emphasis** step of the shared Paper
[rule-weight ladder](/paper/paper/overview) — the same 1.5pt used for cover rules and
summary-page borders elsewhere in the pillar.

## Colour and type tokens

Colour resolves through `paper.semantic.pdf-binder.*` to the `paper.primitive.color`
tier:

| Semantic token | Resolves to | Value | Role |
|---|---|---|---|
| `pdf-binder.toc-entry-inactive` | `pdf-nav-navy` | #002e63 | Inactive TOC number + title |
| `pdf-binder.toc-entry-active` | `ink` | black | Active-entry text |
| `pdf-binder.toc-entry-highlight` | `pdf-nav-grey-light` | #f5f5f5 | Active-entry highlight fill |
| `pdf-binder.home-button-fill` | `pdf-nav-navy` | #002e63 | HOME button rectangle |
| `pdf-binder.home-button-label` | `pdf-nav-on-navy` | #ffffff | HOME label |
| `pdf-binder.header-ink` | `ink` | black | Slip-sheet header title |
| `pdf-binder.supporting-ink` | `pdf-nav-grey-dark` | #4d4d4d | Subtitle + italic footer instruction |
| `pdf-binder.version-label-ink` | `pdf-nav-grey-label` | #737373 | Draft / version label |

Type is set in the PDF core-14 Helvetica stack (`Helvetica`, `Arial`) — no font
embedding required:

| Token | Size / weight | Applied to |
|---|---|---|
| `pdf-binder.binder-title-type` | 16pt bold | Slip-sheet header title |
| `pdf-binder.home-label-type` | 8pt bold | HOME label |
| `pdf-nav.subtitle` | 10pt regular | Org subtitle |
| `pdf-nav.toc-entry` | 11pt bold | TOC rows |
| `pdf-nav.footer` | 9pt regular, rendered italic (Helvetica-Oblique) | Footer instruction |
| `pdf-nav.draft-label` | 9pt regular | Draft / version label |

## Accessibility

This produces a **static PDF page**, so web-UI accessibility mechanisms — focus rings,
ARIA roles, keyboard tab order — do not apply. What applies is PDF-native accessibility,
and it is partial by design:

- **Navigation is `/GoTo` link annotations** plus a PDF document outline
  (`/PageMode /UseOutlines`), with `/DisplayDocTitle true` so viewers announce the
  document title rather than the filename.
- **Contrast is strong.** Navy #002e63 on white measures ~13:1, and white on navy ~13:1
  — both AAA. This is the print/PDF contrast target the recipe declares against WCAG 2.2
  AA.
- **Tagged-PDF reading order is not handled.** Source PDFs pass through **untagged** — the
  generator does not add Tagged-PDF structure, so reading-order conformance for assistive
  technology depends entirely on the tagging of the source documents. This is a known,
  open accessibility gap, not a solved property (see Open questions oq-3). Do not claim
  screen-reader conformance for a binder whose sources are untagged.

The artifact is static: no motion, no transitions.

## Open questions

Carried verbatim from the recipe so downstream consumers do not treat unresolved items as
settled:

- **oq-1 — phantom colour.** An earlier draft listed a 7th colour `GREY_MID` (#666680,
  "inactive entry subtitles") that does not exist in the canonical Python source (no
  subtitle rows are generated). It is dropped from this recipe; confirm no production
  instance relies on it before treating this as fully closed.
- **oq-2 — 8-entry ceiling.** The max-8-TOC-entries-per-slip-sheet limit is currently
  hard-coded. Whether it should become a token, and how binders with more than 8
  documents should paginate across multiple slip sheets, is undecided.
- **oq-3 — Tagged-PDF conformance.** Reading-order conformance for assistive technology is
  unhandled; source PDFs pass through untagged.
- **oq-4 — navy hex rounding.** The RGB constant `(0, 0.18, 0.39)` computes to ~#002f63;
  the design draft and this recipe both state #002e63. The value must be pinned
  definitively against the live Python source constant.

<div class="doc-footer-meta">
<span>part of</span> <a href="/paper/paper/overview">Paper pillar</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>tokens:</span>
<a href="/tokens#paper">paper.semantic.pdf-binder</a>,
<a href="/tokens#paper">paper.primitive.pdf-nav</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>rendered by</span> <code>tool-pdf-interactive.py</code>
</div>
