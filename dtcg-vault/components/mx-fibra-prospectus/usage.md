<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">8 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print-first (WeasyPrint) Mexican FIBRA offering prospectus
(<em>Prospecto de Colocación de CBFIs</em>) — Spanish, LISR arts. 187–188 / LMV /
CNBV-RNV / Indeval, a CBFI/trust-securitization register distinct from a Canadian
share/unit prospectus.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/mx-fibra-prospectus/recipe.json</code></div>
</div>

## What this template is

Its closest existing relative is [Legal Prospectus](/components/legal-prospectus/usage)
(Canada NI 41-101), but this family is architecturally different: Spanish taxonomy
(Portada/Índice/Glosario/Personas Responsables) with no Canadian analogue; a two-column
Portada term-block; a bordered **AVISO IMPORTANTE** legend distinct from a lighter
interior **`.aviso`** notice box; a **Personas Responsables** signature register with
one-responsible-party-per-page pagination; and **no running header on any page**
(matched to the companion [Mexico FIBRA Trust](/components/mx-fibra-trust/usage)).

## Variants

| Variant | Role |
|---|---|
| **portada** | Cover with RNV/CNBV registration legends, logo, headline + Monto, and a two-column term-block (bold label left / justified value right). |
| **aviso-importante** | Mandatory cover legend box: bordered, bold, uppercase, centered head. |
| **indice** | Table of contents, bold-caps top-level rows, dot-leader convention. |
| **glosario** | Two-column borderless table (26%/74% term/definition split), hairline header rule only. |
| **body-section** | Numbered section heads bold/left/uppercase (deliberately NOT centered like the Trust's clause heads); the lighter `.aviso` interior notice box is a distinct sibling of the cover's `.aviso-importante`, not a duplicate. |
| **financial-data-table** | Right-aligned tabular figures, bold subtotal/total rows, 2pt double closing rule, footnote register at 9.5pt. |
| **org-chart-exhibit** | Section 4.4's "Relaciones intercorporativas" figure — styled and maintained as its own separate component, `org-chart-print`; this recipe only fixes the page-margin coupling and splices the figure into the section flow. |
| **personas-responsables** | Eight responsible-party signature blocks, one party per page. |

## The org-chart figure pins this family's page margin

`page-margin-inline` (0.625in — narrower than the Trust's ~1in) is **not** a free
choice for this register in isolation. It is pinned by the `org-chart-print`
component's fixed-pixel-width canvas (680px, needs ≥7.08in of column width), verified
empirically by pixel-measuring test renders at both margin widths. **Do not widen this
family's margins toward the Trust's without first revisiting `org-chart-print`'s canvas
width** — the two move together.

## Rule weight and color

Shares its body register (10.5pt/1.4 Times) and soft placeholder mark (`#FDF3B3`) with
[Mexico FIBRA Trust](/components/mx-fibra-trust/usage) via shared primitives. The
data-table row rule (`{...data-table-row-rule}`) resolves to
`paper.primitive.color.rule-grey-mid` — the same shared grey the Trust family uses for
its own table rules (the two drafts independently proposed this identical `#999999`
value under different names; reconciled to one primitive at landing).

## Accessibility

Índice entries, financial tables (`<table><caption>` + `<th scope>`), and the Glosario
are real structural markup, not images. Both notice boxes (`.aviso-importante`/`.aviso`)
are required statutory/informational disclosures, not decorative — must remain in the
accessibility tree. The org-chart exhibit's own aria requirements are owned by
`org-chart-print`. WCAG 2.2 AA target: pure black-on-white register; role/notice
distinctions are conveyed by border weight and text register (bold/uppercase vs.
sentence case), never by color alone.

## Print output and motion

Print-first static document — no interaction states. Renders via WeasyPrint through
`project-documents/bin/build-pdf.py`'s "shape 1" pipeline (single render — unlike the
Trust, this family needs no split-and-merge workaround since it has no per-schedule
page counters).

## Open questions

- Should the figure-wrapper conventions (`figure { break-inside: avoid; text-align:
  center }`, `figcaption` styling) be claimed by this recipe, by `org-chart-print`, or
  by a shared Paper figure primitive? Currently unclaimed by either — a real seam to
  close.
- Should the Portada/AVISO/Glosario conventions established here become the shared
  house default for future Mexican FIBRA/CBFI-style prospectuses, or are they specific
  to this offering?

## Related

- [Mexico FIBRA Trust](/components/mx-fibra-trust/usage) — the companion constitutional-document register.
- [Legal Prospectus](/components/legal-prospectus/usage) — the Canadian NI 41-101 sibling.
- [Tokens — Paper tier](/tokens#paper) — the full leaf-token list backing this template.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/mx-fibra-prospectus/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/mx-fibra-voice-and-drafting-conventions.md</a>
</div>
