<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">5 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A cross-cutting drafting-CONVENTION taxonomy for legal-document paper
artifacts &mdash; one shared base plus five per-category variant deltas
(commercial-agreement / constitutional-agreement / schedule-exhibit / letter /
preliminary-instrument). This register governs <em>how</em> a paper-legal document
should be drafted &mdash; heading form, numbering scheme, cross-reference grammar &mdash;
not just how it should be styled. One of seven templates in the
<a href="/paper/paper/overview">Paper</a> document-family register.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/paper-legal/recipe.json</code></div>
</div>

## What this component is

Paper Legal is a **convention register**, not a rendering stylesheet. Its job is to
make sure every legal document PointSav/Woodfine produces &mdash; regardless of which
tool or archive drafts it &mdash; follows the *same* heading conventions, numbering
scheme, and cross-reference grammar for its document type, so a reader (or a
downstream automated consumer) can rely on the convention holding, not just the
look. It was requested by project-documents, grounded in a blind two-reviewer
research pass (WebSearch, filed-exhibit and drafting-authority backed) plus a
direct check against the Master Engagement Agreement (JW8/JW9) pilot document.

This sits *alongside*, not *instead of*, the vault's existing concrete
per-document-type registers:

| Component | What it is |
|---|---|
| **Paper Legal** (this component) | The convention layer &mdash; heading/numbering/cross-ref rules, shared across document types |
| [Legal Agency Suite](/components/legal-agency-suite/usage) | A concrete MOU / Engagement Letter / Schedules A&ndash;E document register, with real CSS |
| [Legal Subscription Agreement](/components/legal-subscription-agreement/usage) | A concrete accredited-investor / Family &amp; Friends fill-in-booklet register, with real CSS |
| [Legal Prospectus](/components/legal-prospectus/usage) | A concrete NI 41-101 filing-document register, with real CSS |

A concrete document register should *conform to* Paper Legal's rules for its
category, not duplicate or contradict them. Two real overlaps with the existing
concrete registers surfaced while building this component &mdash; see
[Open questions](#open-questions) below; they are flagged for reconciliation with
project-documents, not silently resolved in either direction.

## Architecture: one shared base, five variant deltas

The base never drifts between document types (operator rule, carried over
verbatim from the source request). Each variant changes only its own delta:

- **Base** (heading-agnostic): Tinos type scale, the `.cl1`/`.cl2`/`.cl3`
  hanging-ordinal clause ladder, `.party-block`, `.recital`,
  `table.signature-block`, `table.fee-table`, `table.sched-table`,
  `.schedule-cover`, spacing, draft stamp, page geometry.
- **Variant delta**: heading convention only (Letter and the MOU form of
  preliminary-instrument also change document *structure*, not just heading
  style).

CSS tokens for the base and each delta live in project-documents' own
`templates/` directory (`bin/apply-token.py --token <name>`, zero code change
per document); this vault holds the **DTCG component identity** &mdash;
`{paper.semantic.paper-legal.legal-base.*}` plus `{paper.semantic.paper-legal.<variant>.*}`
&mdash; and the convention documentation below, which is the part of this request
this vault is directly responsible for keeping current.

## The 5 variants + per-category formatting lock

Each cell is marked **HARD** (never varies), **DOMINANT** (the default; strong
majority of filed-exhibit evidence), or **HOUSE** (an accepted alternative,
operator's call).

| Variant | Heading form | "Section"/"Article" word in heading | Cross-reference capitalization |
|---|---|---|---|
| **commercial-agreement** (agency / underwriting / placement / engagement) | Flat **`12. Termination.`** &mdash; bare number, bold **Title Case**, terminal period (DOMINANT). NOT all caps. Left-aligned (`h2` delta) | **No** &mdash; bare number (DOMINANT; Weagree: do not place "Section" before the number). `Section 12.` = HOUSE alternative | Capital for internal refs (`Section 12` / `Section 12(h)`); lowercase for external refs (`section 13.7 of NI 31-103`) (DOMINANT) |
| **constitutional-agreement** (Shareholder / USA / LP / Partnership) | Article line **`ARTICLE N`** + ALL-CAPS title, centered (DOMINANT); sub-level **`N.N Title`** Title Case (DOMINANT). The two levels are always case-distinct (HARD) | "Article" = **yes** (DOMINANT); "Section" at `N.N` = **HOUSE** (Canadian practice: bare `1.1`; US practice: `Section 1.01`) | Capital internal; lowercase external; include a convenience-construction clause (DOMINANT) |
| **schedule-exhibit** | `SCHEDULE A` caps label, centered; internal headings inherit the parent document's own scheme | The label **is** the heading (yes); pick one term &mdash; Schedule / Exhibit / Annex &mdash; and hold it consistent (HARD) | Capital, e.g. `Schedule A` / `Section 2.1 of Schedule A` |
| **letter** (engagement / proposal) | Numbered paragraph, bold Title-Case run-in if headed; never all caps | Usually **no** (bare `1.`) | Match the cross-ref word to whatever the divisions are actually called (HARD consistency): `Section N` if headed, `paragraph N` if bare |
| **preliminary-instrument** (MOU / LOI / term sheet) | MOU: numbered/lettered `A./B.`; LOI: letter-form; term sheet: table/bullets | Usually no | Same match rule as letter; capital internal |

**Heading case is a function of LEVEL, not document type.** ALL CAPS applies
only at the ARTICLE line (constitutional-agreement); every section-level
heading below that is bold Title Case; all-caps body text is a readability
defect regardless of document type (Adams/MSCD).

## Drafting-convention rules (apply across the whole family)

1. **No orphan subsection (near-hard rule).** Never a lone `N.1` with no
   `N.2` &mdash; a section that is a single undivided block stays bare, directly
   under its heading, with no decimal. Forcing an `N.1` onto a single-block
   section is a *style error*, not a fix. [Weagree; Canada Justice *Legistics*;
   US House *Manual on Drafting Style*; Adams/MSCD]
2. **Content-driven mixing is standard.** Subdivide only where 2+ co-ordinate
   provisions actually exist; uniform depth across a document is not
   required. [filed-exhibit: MDRNA/Canaccord 2009; Aptorum/H.C. Wainwright
   2020; placement-agent EX-10.10 CIK 1047153]
3. **Cross-reference address grammar &mdash; three depths, all coexist:**
   `Section N` (whole section) / `Section N.N` (subsection) / `Section N(x)`
   (lettered clause, cited THROUGH the section).
4. **Internal vs. external capitalization.** Capitalize references to THIS
   agreement's own parts (`Section`, `Article`, `Schedule`); lowercase
   references to statutes or other instruments (e.g. `section 13.7 of NI
   31-103` &mdash; the statute's own title stays capitalized, the pinpoint stays
   lowercase). This is the rule most often gotten wrong in practice &mdash;
   enforce it.
5. **External-reference disambiguation.** Always keep the `of <instrument>`
   qualifier on an external reference, so a same-numbered internal section
   is not misread as the target.
6. **Left-aligned heading is the orphaned-list fix mechanism.** A centered
   heading empties the left margin, so an indented clause list that follows
   it floats with nothing above it. Left-aligning the heading (the
   commercial-agreement `h2` delta) is what fixes this &mdash; it is intentional,
   not a stray override.
7. **Roadmap chapeau is acceptable.** An unnumbered lead-in paragraph under a
   subdivided section (e.g. a one-line roadmap before `6.1`) is common in
   filed agreements and is cited as the whole section.
8. **Don't formally define "Section"/"Article."** Capitalize without a
   definition; use a convenience-construction clause instead (e.g.
   "references to a Section are to a section of this Agreement; headings
   for convenience only" &mdash; the Mitel s.1.2 / SEC LPA s.11.05 pattern).
9. **The one HARD rule across the whole family.** Never two internal
   cross-reference pointers in different case within the same document.

## Market-practice citations

The commercial-vs-constitutional heading split (flat `Section` vs. `ARTICLE`)
is a real, filed-exhibit-backed convention, not house style:

- **[FILED-EXHIBIT]** StandardAero UA (2026); CST Brands UA (2013) &mdash; flat
  `1. Title.` Title-Case sections.
- **[FILED-EXHIBIT]** Ares CRE UA; Baxter Intl UA &mdash; `SECTION` label
  variants.
- **[FILED-EXHIBIT]** Smithfield/Shuanghui merger; Mitel Networks SHA
  (Ontario); SEC LPA CIK 1403528 &mdash; `ARTICLE` caps + `N.N`.
- **[FILED-EXHIBIT]** MDRNA/Canaccord; Aptorum/H.C. Wainwright placement
  agreements &mdash; mixed subdivided/bare sections.
- **[FILED-EXHIBIT]** Libang Underwriting Agreement EX-1.1 (2024); Placement
  Agent Agreement EX-10.10 (CIK 1047153, 2009) &mdash; flat `Section`/`N.N`/`(a)`,
  not `ARTICLE`.
- **[FILED-EXHIBIT]** Shareholders Agreement EX-10.19 (CIK 1500866); LP
  Agreement EX-10.21 (CIK 1403528) &mdash; `ARTICLE` + `N.N`.
- **[DRAFTING-GUIDE]** Adams, *A Manual of Style for Contract Drafting* &mdash;
  all-caps readability defect; internal/external capitalization cue;
  enumeration requires 2+ units; "article" is a grouping choice, not a
  reservation.
- **[DRAFTING-GUIDE]** Weagree &mdash; do not place "Section" before the number;
  capitalize internal references; articles advisable past roughly 7 sections
  or multiple topic groups.
- **[DRAFTING-GUIDE]** Canada Justice *Legistics*; US House *Manual on
  Drafting Style* &mdash; at-least-two-parallel-units rule; statute references
  stay lowercase.

## Token mapping (reference implementations, as they land)

- `templates/commercial-agreement.css` = base + Commercial delta. **First
  delivery expected**, reference implementation the Master JW9 pilot
  (`outputs/CURRENT_COMPLIANCE_MCORP_2026_05_28_Engagement_Agreement_JW9.html`,
  project-documents-side).
- `templates/legal-agreement.css` (project-documents-side filename) = base +
  Constitutional delta. Reference: the 3 Client A Shareholder Agreements,
  said to be in-sync already &mdash; do not reformat them. See the naming-collision
  note in [Open questions](#open-questions) before wiring this into the
  vault's own token layer under that name.
- `agency-form.css` = the Letter family; substantially covered by the
  existing [Legal Agency Suite](/components/legal-agency-suite/usage)
  component already (see oq-3).
- Schedule/Exhibit and preliminary-instrument (MOU) deltas: not yet
  delivered.

## Accessibility

Because this is a print artifact family, accessibility here means document
semantics that survive into the tagged PDF, not keyboard or focus behaviour.
Clause numbering should use real `<ol>`/`<li>` markup, not visual-only
numerals, so assistive technology can announce clause position &mdash; the same
approach the [Legal Agency Suite](/components/legal-agency-suite/usage)
component already takes for its `body-clauses` variant. Tables used purely
for print layout (signature blocks, schedule covers), not to convey
relational data, should carry `role="presentation"`.

The recipe records a **WCAG 2.2 AA target**.

## Print output and motion

Print-first static document family &mdash; no interaction states. Renders to PDF
via WeasyPrint, matching project-documents' existing pipeline.

## Open questions

Five items travel with anyone consuming this register &mdash; all surfaced
while building this component, not silently resolved:

- **`oq-1` &mdash; naming collision, real and unreconciled.** This vault's
  pre-existing `paper.semantic.legal-agreement.*` tokens back the
  *unrelated* [Legal Subscription Agreement](/components/legal-subscription-agreement/usage)
  component (accredited-investor fill-in booklets) &mdash; a completely
  different document family from what project-documents calls
  `legal-agreement.css` on their own side (the Constitutional/Shareholder-
  Agreement base). Same name, two different documents. This
  constitutional-agreement variant does **not** bind to the pre-existing
  `legal-agreement.*` tokens for that reason. Recommend project-documents
  rename their local file (e.g. `constitutional-agreement.css`) to avoid the
  collision going forward.
- **`oq-2` &mdash; schedule-exhibit overlaps an existing component.** The
  already-shipped Legal Agency Suite component has its own `schedule-cover`
  variant (`apage`&hellip;`epage` named page counters). Needs reconciliation
  with project-documents on which register is authoritative before either
  is built out further &mdash; not built as a silent duplicate here.
- **`oq-3` &mdash; letter overlaps an existing component.** Legal Agency Suite's
  `proposal-letter` and `mou-engagement-letter` variants cover the same
  ground. Same reconciliation recommendation as `oq-2`.
- **`oq-4` &mdash; commercial-agreement capitalization house-style, pending
  operator's final pick.** The source request flags a split: capital
  `Section` for ALL internal cross-references (candidate rule) vs. the
  current practice of capital whole-section / lowercase sub-tier. This
  component currently documents the ALL-capital candidate as DOMINANT per
  the source request's own recommendation; not yet operator-confirmed.
- **`oq-5` &mdash; CSS delivery status, informational.** Only
  commercial-agreement has a named reference implementation in progress
  (Master JW9). Constitutional-agreement has an existing CSS file on
  project-documents' side said to be correct but not yet reconciled into
  this vault's token layer (see `oq-1`). Schedule-exhibit, letter, and
  preliminary-instrument have no CSS delivery scheduled yet beyond the
  taxonomy recorded in this component.

## Related

- [Paper pillar &mdash; overview](/paper/paper/overview) &mdash; rule-weight ladder,
  geometry, and document-families table this register's base draws from.
- [Legal Agency Suite](/components/legal-agency-suite/usage) &mdash; concrete
  MOU/Engagement-Letter/Schedules register; see `oq-2`/`oq-3` for the
  overlaps with this component.
- [Legal Subscription Agreement](/components/legal-subscription-agreement/usage) &mdash;
  concrete fill-in-booklet register; see `oq-1` for the token-naming
  collision.
- [Legal Prospectus](/components/legal-prospectus/usage) &mdash; concrete
  filing-document register.
- [Tokens &mdash; Paper tier](/tokens#paper) &mdash; the `paper-legal` semantic
  namespace and the non-DTCG `paper-legal-conventions` block backing this
  component.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/paper-legal/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/paper-legal-token-map.md</a>
</div>
