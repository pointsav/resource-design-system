<div class="doc-header">
<span class="eyebrow">Components · Paper</span>
<div class="doc-header__badges">
<span class="badge">8 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A print-first (WeasyPrint) Mexican FIBRA <em>Contrato de
Fideicomiso</em> (Trust Agreement) — a Spanish-language civil-law notarial instrument,
the Mexico expression of the Woodfine Direct-Hold Solution's constitutional document.
Retypeset against the executed FIBRA SOMA (CIB/3332) precedent.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/mx-fibra-trust/recipe.json</code></div>
</div>

## What this template is

Mexico FIBRA Trust is a **print document register** for a civil-law notarial instrument
— not a Canadian securities document like [Legal Subscription Agreement](/components/legal-subscription-agreement/usage)
or [Legal Prospectus](/components/legal-prospectus/usage), and not the Tinos MOU
register of [Legal Agency Suite](/components/legal-agency-suite/usage). It carries
structure with no analogue among the other Paper families: a **portada** (cover) framed
by two heavy rules, an **Índice** with dot-leaders, flowing **Secciones/Cláusulas** (no
forced page break per section), parenthetically-enumerated **incisos**, a
**Definiciones** hanging-indent glossary, **comité-roster** governance tables, and
**Anexos**.

Sibling of [Mexico FIBRA Prospectus](/components/mx-fibra-prospectus/usage) — the two
share the body type register, the soft placeholder mark, and the draft-stamp
convention, but differ deliberately in page geometry (this family: ~1in margins vs. the
Prospectus's 0.625in, driven by an org-chart figure) and section taxonomy. Landed as a
coordinated pair, not merged.

## Variants

| Variant | Role |
|---|---|
| **portada** | Cover framed by two heavy rules; centered title/subtitle; parties stacked as "como &lt;rol&gt;" lines; place/date with honest `[●]` fill-ins. |
| **indice** | Auto-computed table of contents, dot-leader convention, right-aligned page numbers, own dedicated page. |
| **body-secciones** | Secciones I–XVII, flowing continuously (SOMA-verified — no forced page break per Sección). |
| **enumerated-incisos** | Three-legged inciso mechanism: parenthetical counter glyph, the 26pt indent grid, and `list-style-position: inside` — all three legs load-bearing together. |
| **definiciones** | Sección I hanging-indent glossary. |
| **comite-roster** | Governance tables (Comité Técnico / Auditoría / Prácticas Societarias). |
| **firmas** | Signature blocks as real `<table>` markup (never a bordered div), one per signatory role. |
| **anexo** | Anexos A–E — short integral lists, not paginated sub-documents. |

## The parenthetical inciso mechanism

Verified against the real executed FIBRA SOMA precedent: incisos are `(a)`, `(i)` —
parenthesized, never dot-suffixed `a.`/`i.`. Three CSS legs work together to produce
this: the `@counter-style` glyph rule (shared with
[Mexico FIBRA Prospectus](/components/mx-fibra-prospectus/usage) via
`paper.primitive.counter.fibra-alpha`/`fibra-roman`), the 26pt notarial indent grid
(`{...indent-notarial}`), and `list-style-position: inside` (`{...inciso-marker-position}`)
— dropping any one leg breaks the mechanism.

## Rule weight and color

Uses a dedicated cover-framing weight not shared with any other Paper family —
`{paper.primitive.rule.cover-heavy}` (2.25pt) — plus the standard rule ladder for
tables. The table row-separator grey (`{...table-rule-grey}`) resolves to
`paper.primitive.color.rule-grey-mid`, shared with Mexico FIBRA Prospectus (the two
drafts independently proposed this identical `#999999` value under different names;
reconciled to one shared primitive at landing).

## Accessibility

Índice entries are real anchor-equivalent structural navigation, not decorative.
Signature blocks are real `<table>` markup with cell-level text — not rasterized
images — so they remain selectable and screen-reader-legible in the PDF. The
`<mark>[●]</mark>` placeholder sentinel is a genuine fill-in-later marker and must stay
distinguishable in the accessibility tree from settled text. WCAG 2.2 AA target: pure
black-on-white register, no color-only meaning anywhere — the placeholder mark's soft
amber (`#FDF3B3`) is a visibility aid layered on real text, not a substitute for it.

## Print output and motion

Print-first static document — no interaction states. Renders via WeasyPrint 61.x
through `project-documents/bin/build-pdf.py`'s "shape 3" pipeline (cover + Índice +
body renumbered from 1 — a split-and-merge workaround for WeasyPrint's
`counter-reset: page` limitation).

## Open questions

- Should the Índice/cover/portada conventions established here become the shared house
  default for future Mexican civil-law instruments, or are they trust-specific? Not
  decidable from one document — this is the first.
- Both this family and Mexico FIBRA Prospectus deliberately keep their own body type
  composites (`type.legal-trust` vs `type.mx-fibra`) rather than merging them — they
  share only the base 10.5pt/1.4 register by coincidence, not evidence of a real
  duplication.

## Related

- [Mexico FIBRA Prospectus](/components/mx-fibra-prospectus/usage) — the companion
  offering-prospectus register.
- [Legal Prospectus](/components/legal-prospectus/usage) · [Legal Subscription Agreement](/components/legal-subscription-agreement/usage) · [Legal Agency Suite](/components/legal-agency-suite/usage) — the Canadian legal-document families in the Paper register.
- [Tokens — Paper tier](/tokens#paper) — the full leaf-token list backing this template.

<div class="doc-footer-meta">
<span>rendered from</span> <code>components/mx-fibra-trust/recipe.json</code>
<span class="doc-footer-meta__sep">&middot;</span>
<span>source research:</span>
<a href="/tokens#paper">research/mx-fibra-voice-and-drafting-conventions.md</a>
</div>
