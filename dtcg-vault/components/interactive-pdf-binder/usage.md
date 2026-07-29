<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">6 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target (print/PDF)</span>
</div>
<p class="doc-header__lead">A print-first navigation system for assembled multi-document
PDF binders on US Letter (612×792pt, origin bottom-left). One component, four
navigation surfaces — a slip-sheet table-of-contents cover, TOC entries (top-level and
grouped), and an INDEX return button stamped on every content page — that together turn
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
token groups. **Corrected 2026-07-29** (project-jennifer): the TOC-entry position/pitch
and INDEX-button size were re-verified against three shipped production binders and found
to have never matched the canonical values — the originals came from an early draft, not
measurement. See [Coordinate space and geometry](#coordinate-space-and-geometry) for the
corrected figures.

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
- **When the reader needs to return to the index repeatedly.** The INDEX button on every
  content page is the return path.
- **When several documents share a parent** — reach for the grouped-TOC variants
  (`toc-group-header` / `toc-entry-child`) rather than repeating the shared name in every
  child's title. A group of exactly one document stays a plain numbered row — a header
  over a single child costs a line and groups nothing.

## When not to use

- **Do not use it for a single, authored document.** If there is nothing to bind, there
  is no TOC to generate — reach for the relevant CSS-print family instead.
- **Do not use it to restyle the source PDFs.** The generator overlays navigation; it
  does not reflow, re-tag, or re-typeset the documents it binds.
- **Do not treat the point-space geometry as CSS `@page` geometry.** This component is
  rendered in PDF point coordinates with a bottom-left origin — it deliberately keeps its
  own `paper.primitive.pdf-nav.*` group rather than sharing the CSS-print page primitives.
- **Do not invent a numbered sub-level for grouped entries.** House style is a single
  number spine (`1.` `2.` `4.`, headers consume a number, children carry none) — see
  *Rejected alternatives* below for why a decimal scheme (`4.1`/`4.2`) was tried and
  dropped.

## The four navigation surfaces

### 1 · Slip-sheet TOC cover

A generated cover page inserted before each source document. It carries a header title,
an organisation subtitle, a 1.5pt rule, an optional right-aligned draft/version label
(first sheet only), and an italic footer instruction. A single slip sheet holds **up to 8
TOC entries**; that ceiling is currently a hard limit in the generator, though the real
constraint appears to be vertical space, not row count (see Open questions oq-2).

### 2 · TOC entry (top-level)

One navigable row per bound document, in two states:

- **Inactive** — a navy number and title for a document other than the current one, with
  an invisible full-rect GoTo link to that document's slip sheet.
- **Active** — the row for the current document: a grey-light highlight rectangle, black
  text, and a drawn 7.2×7.2pt filled-ink marker square (not a glyph — see below).

### 3 · Grouped TOC entries — group header and child

Added 2026-07-17, adopted as the house standard for TOC slip sheets. When several
documents share a parent, a `toc-group-header` row takes the next number in the spine and
labels the group; its `toc-entry-child` rows carry no number of their own, leading instead
with an en-dash. **One number spine, no exceptions** — everything else in the recipe (an
inactive/active top-level entry, a group header) shares column `toc-num-x`; a numbered
child would open a second number column and a second title column, and the page would
stop having a single left edge.

A clickable document can itself be the group's parent — a **doc-parented group** — when
schedules or annexes belong to one specific agreement rather than to a generic label (e.g.
Schedules A–D nested under the Long-Form Agreement they amend). In that case the parent
keeps its own PDF and slip sheet; its bookmark nests the children under its own outline
item (`parent=` its own `add_outline_item` return, never a synthetic group node), and its
own link rect narrows (`toc-docparent-link-dy`/`-height`) so it cannot overlap the first
child's link rect.

**Numbering the children `4.1`–`4.4` (or as new siblings `4.`–`7.`) would assert a false
relationship** — in a legal binder, that they are peers of the agreement rather than part
of it. This is a domain-correctness question, not a taste call.

### 4 · INDEX return button

A 54×14pt navy rounded rectangle (3pt corner radius) with a white `INDEX` label
(renamed from `HOME` 2026-07-17 — "HOME" read as browser/app vocabulary, the one word on
the page that broke the printed-instrument register; "INDEX" names the button's actual
destination and matches the binder's own footer sentence, *"Interactive Index: Click a
document title above…"*), placed lower-right. Stamped on every content page — never on a
slip sheet — and carries a transparent GoTo link back to page 0, top. The label change is
zero-geometry: at Helvetica-Bold 8pt, `HOME` measured 24.0pt wide and `INDEX` measures
24.4pt, well inside the 54pt button.

## Variants

| Variant | Surface | Description |
|---|---|---|
| **slip-sheet** | TOC cover | Generated cover preceding each source document: header title, org subtitle, 1.5pt rule, optional right-aligned draft label (first sheet only), italic footer instruction. Holds up to 8 TOC entries per sheet. |
| **toc-entry-inactive** | TOC entry | Navigable row for a non-current document: navy number + title, invisible full-rect GoTo link to that document's slip sheet. |
| **toc-entry-active** | TOC entry | Row for the current document: grey-light highlight rect, black text, drawn 7.2×7.2pt marker square; no link (self). |
| **toc-group-header** | Grouped TOC | Labels a group of following children: 11pt Helvetica-Bold, ink (not navy — it isn't navigable), title case, no highlight/marker/link/rule, takes the next number in sequence. A clickable document may itself be a doc-parented group header. |
| **toc-entry-child** | Grouped TOC | Nested under a group header: no number, an en-dash at `toc-child-dash-x`, title one 18pt step past `toc-title-x`. Same colour/type/marker/link rules as a top-level entry. |
| **home-button** | Return button | 54×14pt navy rounded-rect (3pt radius) with white `INDEX` label, lower-right placement. Stamped on every content page (never slip sheets); transparent GoTo link to page 0 top. |

## Coordinate space and geometry

The binder is generated in PDF point-space on US Letter, **612×792pt, origin
bottom-left** — not a CSS `@page` box model. All geometry comes from
`paper.primitive.pdf-nav.*`, **corrected 2026-07-29** against three shipped production
binders (MOU, Agency Agreements, MX Prospectus) plus the Client A reference generator:

| Primitive | Token | Value | Was (stale) |
|---|---|---|---|
| Page width | `{paper.primitive.pdf-nav.page-width}` | 612pt | — |
| Page height | `{paper.primitive.pdf-nav.page-height}` | 792pt | — |
| Content zone | `margin-left` / `margin-right` | 72pt–540pt | — |
| First TOC entry baseline | `toc-entry-first-y` | **595pt** | 565pt |
| TOC entry step (centre-to-centre) | `{paper.primitive.pdf-nav.toc-entry-step}` | **48pt** | 65pt |
| TOC entry height | `toc-entry-height` | 46pt | (unchanged) |
| TOC entry width | `toc-entry-width` | **468pt** | 530pt |
| TOC number x-position | `toc-num-x` | **96pt** | 64pt |
| TOC title x-position | `toc-title-x` | **114pt** | 82pt |
| INDEX button width | `{paper.primitive.pdf-nav.home-width}` | **54pt** | 64pt |
| INDEX button height | `{paper.primitive.pdf-nav.home-height}` | **14pt** | 20pt |
| INDEX corner radius | `{paper.primitive.pdf-nav.home-corner-radius}` | **3pt** | 4pt |
| Slip-sheet rule stroke | `rule-stroke` | 1.5pt | — |

Grouped-entry geometry (new 2026-07-17):

| Primitive | Token | Value |
|---|---|---|
| Child en-dash x-position | `toc-child-dash-x` | 120pt |
| Child rect x / width / height | `toc-child-rect-x/width/height` | 98pt / 442pt / 22pt |
| Child rect y-offset | `toc-child-rect-dy` | **-7pt** (not -25pt — see below) |
| Child row pitch | `toc-child-step` | 26pt |
| Doc-parented pitch to first child | `toc-docparent-to-child-step` | 36pt |
| Doc-parent's own link rect y-offset / height | `toc-docparent-link-dy` / `-height` | -15pt / 36pt |
| Active-row marker size | `active-marker-size` | 7.2×7.2pt |

**A bug in the original reference generator, not copied here:** its child rows use
`(98, y−25, 442, 24)` — a band that sits entirely below the text baseline at `y`, so the
highlight box and click target land under the wrong strip. It went unnoticed because those
children are rarely rendered active. `toc-child-rect-dy: -7pt` brackets the baseline
correctly; all binders shipped 2026-07-17 use the corrected value.

The 1.5pt slip-sheet rule is the **emphasis** step of the shared Paper
[rule-weight ladder](/paper/paper/overview) — the same 1.5pt used for cover rules and
summary-page borders elsewhere in the pillar.

## The active marker is a drawn rectangle, not a glyph

An earlier revision used `►` (U+25BA) as the active-row marker. That character is absent
from Helvetica's WinAnsi encoding (the encoding reportlab's core-14 fonts use), so readers
substituted `.notdef` — which happened to render as a filled black box in some viewers, but
`.notdef` rendering is undefined and reader-dependent (a hollow box, a different shape, or
nothing at all in another viewer). **Resolution: draw a 7.2×7.2pt filled-ink rectangle**
instead — same appearance, deterministic in every reader, measured directly off the
originally-rendered `.notdef` box. Do not pin a marker *glyph* in the recipe; pin the
rectangle.

**Known trade, flagged not resolved:** the earlier glyph lived in the text layer, so the
active row was machine-extractable. A drawn rectangle is graphics — slip-sheet text is now
byte-identical across every sheet, and the active row's only remaining signal for a
screen-reader user is the highlight shading plus ink-vs-navy text colour, not an
extractable character.

## Colour and type tokens

Colour resolves through `paper.semantic.pdf-binder.*` to the `paper.primitive.color`
tier:

| Semantic token | Resolves to | Value | Role |
|---|---|---|---|
| `pdf-binder.toc-entry-inactive` | `pdf-nav-navy` | #002e63 | Inactive TOC number + title |
| `pdf-binder.toc-entry-active` | `ink` | black | Active-entry text |
| `pdf-binder.toc-entry-highlight` | `pdf-nav-grey-light` | #f5f5f5 | Active-entry highlight fill |
| `pdf-binder.toc-group-header` | `ink` | black | Group-header text — **not** navy; a header isn't navigable, so navy (which means "this row links") would be a lie. |
| `pdf-binder.active-marker-fill` | `ink` | black | The drawn active-row marker square |
| `pdf-binder.home-button-fill` | `pdf-nav-navy` | #002e63 | INDEX button rectangle |
| `pdf-binder.home-button-label` | `pdf-nav-on-navy` | #ffffff | INDEX label |
| `pdf-binder.header-ink` | `ink` | black | Slip-sheet header title |
| `pdf-binder.supporting-ink` | `pdf-nav-grey-dark` | #4d4d4d | Subtitle + italic footer instruction |
| `pdf-binder.version-label-ink` | `pdf-nav-grey-label` | #737373 | Draft / version label |

Type is set in the PDF core-14 Helvetica stack (`Helvetica`, `Arial`) — no font
embedding required. A group header reuses the same `pdf-nav.toc-entry` token as any other
row (11pt bold) — differentiation is colour and grouping proximity, never a second type
voice:

| Token | Size / weight | Applied to |
|---|---|---|
| `pdf-binder.binder-title-type` | 16pt bold | Slip-sheet header title |
| `pdf-binder.home-label-type` | 8pt bold | INDEX label |
| `pdf-nav.subtitle` | 10pt regular | Org subtitle |
| `pdf-nav.toc-entry` | 11pt bold | TOC rows, including group headers and children |
| `pdf-nav.footer` | 9pt regular, rendered italic (Helvetica-Oblique) | Footer instruction |
| `pdf-nav.draft-label` | 9pt regular | Draft / version label |

## Accessibility

This produces a **static PDF page**, so web-UI accessibility mechanisms — focus rings,
ARIA roles, keyboard tab order — do not apply. What applies is PDF-native accessibility,
and it is partial by design:

- **Navigation is `/GoTo` link annotations** plus a PDF document outline
  (`/PageMode /UseOutlines`), with `/DisplayDocTitle true` so viewers announce the
  document title rather than the filename.
- **Grouped entries mirror their visual nesting structurally.** A group header's children
  nest under its outline item via `add_outline_item(..., parent=...)`. For a doc-parented
  group this is the *only* machine-readable statement that the children belong to that
  document rather than being its siblings — indent and dash alone don't carry that.
- **A group header is never its own link target.** It labels a group that begins at its
  first child; a GoTo there would land where clicking the child already lands. Its
  bookmark resolves to the first child instead, since an outline entry must resolve
  somewhere.
- **Contrast is strong.** Navy #002e63 on white measures ~13:1, and white on navy ~13:1
  — both AAA. This is the print/PDF contrast target the recipe declares against WCAG 2.2
  AA.
- **Tagged-PDF reading order is not handled.** Source PDFs pass through **untagged** — the
  generator does not add Tagged-PDF structure, so reading-order conformance for assistive
  technology depends entirely on the tagging of the source documents. This is a known,
  open accessibility gap, not a solved property (see Open questions oq-3). Do not claim
  screen-reader conformance for a binder whose sources are untagged.

The artifact is static: no motion, no transitions.

## Rejected alternatives — do not reopen

**ISO 2145 decimal numbering** (`4` / `4.1` / `4.2`, no trailing stop) for grouped entries:
verified correct as a standard, rejected as a house decision. Nothing in the corpus used
it, it solved no problem anyone had, and decimal children would open a second number
column, destroying the single-number-spine layout every binder in production actually
uses. House style is `1.` `2.` `4.` — Arabic, trailing stop, headers consume a number,
children carry none.

**A full closing-binder / offering-memorandum register** (Times, centred masthead,
thick-thin double rule, an `INDEX` cover label, dot-leader folios, a document-control foot
zone, navy demoted to folios only): mocked up in full against real reference points and
rejected. Folios are wrong for this product — every source document already carries its
own page numbers, so a second binder-level number confuses readers, and no folios means no
dot leaders (a leader exists only to carry the eye to a number). The grey highlight is
load-bearing wayfinding, not a "generated-UI tell" to remove. A centred index block reads
wrong under this masthead. The token cost (~10 changed + ~7 new, all requiring cosign) was
disproportionate to move one component off the system's own `font.pdf-nav`. Worth keeping
from the exercise: `paper.primitive.font.serif-legal` already exists for exactly the
legal-body-text role a Times-based binder would have wanted — the Paper pillar already
splits Helvetica-for-navigation from Times-for-legal-bodies, which is the correct split
for a generated artifact that must rebuild identically anywhere.

## Open questions

Carried verbatim from the recipe so downstream consumers do not treat unresolved items as
settled:

- **oq-1 (resolved 2026-07-17) — phantom colour.** An earlier draft listed a 7th colour
  `GREY_MID` ("inactive entry subtitles") that does not exist in the canonical Python
  source. Confirmed absent from every production instance; stays dropped.
- **oq-2 — 8-entry ceiling.** The max-8-TOC-entries-per-slip-sheet limit is currently
  hard-coded. Evidence from a real 8-row slip sheet shows the actual constraint is
  vertical space, not row count (a child row costs 26pt against a top-level row's 48pt) —
  recommend re-expressing the cap as a computed space budget; not yet done.
- **oq-3 — Tagged-PDF conformance.** Reading-order conformance for assistive technology is
  unhandled; source PDFs pass through untagged.
- **oq-4 (resolved 2026-07-17) — navy hex.** Pinned to #002e63, confirmed against the
  live Python source's exact RGB constant `(0.0, 0.18, 0.39)`.
- **oq-5 — no title wrapping.** Nothing wraps or ellipsizes; a long title silently runs
  past its box's right edge. Should the recipe specify wrapping, or a documented max
  length (~400pt ≈ 66 characters at the child level)?
- **oq-6 — doc-parented group depth.** Should a doc-parented group ever nest more than one
  level? No production instance does; recommend capping at one until a real case exists.
- **oq-7 — landscape slip sheets.** All current instances are portrait. Right-margin
  geometry is already expressed via `margin-right` rather than a literal value, so a
  landscape variant is lower-risk than it would otherwise be — not built, not requested.

<div class="doc-footer-meta">
<span>part of</span> <a href="/paper/paper/overview">Paper pillar</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>tokens:</span>
<a href="/tokens#paper">paper.semantic.pdf-binder</a>,
<a href="/tokens#paper">paper.primitive.pdf-nav</a>
<span class="doc-footer-meta__sep">&middot;</span>
<span>rendered by</span> <code>tool-pdf-interactive.py</code>
</div>
