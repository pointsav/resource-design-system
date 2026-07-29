---
schema: foundry-design-research-v1
component_or_token: mx-fibra-trust, mx-fibra-prospectus
decision_type: qualitative-drafting-convention
authored: 2026-07-22
authored_by: totebox@project-documents (cross-archive exception)
authored_with: claude-sonnet-5
status: ratified
source: project-documents BRIEF_COMPLIANCE_PRO-MX-04-AST_2026_01_06_Agreement_Trust_JW1.md + BRIEF_COMPLIANCE_PRO-MX-04-AST_2026_01_06_Offering_Prospectus_JW1.md (both "Decisions locked (R4)" sections, 2026-07-22)
ai_consumption_hint: "Qualitative Spanish-language legal-drafting voice/consistency rules for the Mexico FIBRA document pair — deliberately separate from the numeric/visual DTCG tokens (see paper.semantic.mx-fibra-trust / mx-fibra-prospectus), matching how paper-legal already separates its qualitative HARD/DOMINANT/HOUSE tags from hard token values. Not specific to one document — should govern any future Mexico FIBRA or structurally similar foreign-jurisdiction trust/securitization drafting pass."
---

# Mexico FIBRA voice and drafting conventions — research rationale

> Cross-referenced from [Mexico FIBRA Trust](/components/mx-fibra-trust/usage) and
> [Mexico FIBRA Prospectus](/components/mx-fibra-prospectus/usage). This file captures the
> *qualitative* drafting and voice rules that produced the Trust (JW4) and Prospectus (JW6)
> rewrites — deliberately kept separate from the numeric/visual DTCG tokens.

## The governing principle — substance vs. form

A self-similar Direct-Hold Solution transplants its substantive terms 1:1 from the executed
home-jurisdiction instrument (here, the Professional Centres Canada LP Limited Partnership
Agreement, Seventh Amended), changed only where local law affirmatively forces a different
number or mechanism. Market-precedent samples from the target jurisdiction (here, the FIBRA
SOMA / FIBRA Plus samples) are **form-only** — Spanish legal voice, clause-numbering
convention, page layout — **never a source of substantive terms, figures, or covenants**.

This is not a hypothetical rule: an interim research pass violated it once — it pulled a
debenture leverage-covenant figure from the SOMA sample instead of the actual Canada LP
Agreement. Re-verification showed the Canada-sourced figures were already correctly
implemented; the SOMA-derived figure would have been a real drafting error had it landed.
Any future session drafting a foreign-jurisdiction Direct-Hold Solution instrument should be
told this rule explicitly, up front, before touching a market-precedent sample — the failure
mode is silent (the wrong document "looks" fine).

Worked example: Canada's LP Agreement sets a 90% contractual distribution; Mexico's LISR
Art. 188 statutorily requires ≥95% — so the Mexico Trust correctly deviates there, *because
law forces it*, not because a sample document does it differently.

## Voice register — "hyperscaler Mexico City law firm," execution-ready

The target voice is a complete, execution-ready draft for a receiving law firm to review
before finalizing — not a working/marked-up draft.

- **Zero Form Notes, zero counsel-flags, zero bracketed advisory commentary.** Every hedge
  like *"salvo que el dictamen legal correspondiente lo confirme..."* is rewritten as
  definitive, affirmative text.
- **Only true fill-in-later variables carry a placeholder** — dates, unchosen institution
  names, specific amounts not yet fixed at execution — using the single sentinel
  `<mark>[&#9679; description]</mark>` (literal U+25CF, never `&bull;`, never a bracket with
  no sentinel inside it). A genuinely undecided business question should be phrased as an
  honest placeholder framed as a real open commercial decision, not disguised as ordinary
  market boilerplate.
- **Idiomatic, native Mexican legal Spanish** — no translated-from-English feel. English
  cross-walk terms are acceptable once, at a defined term's home in the glossary, never
  repeated in body prose.
- **Never condense away operative machinery.** Triggers, deadlines, notice provisions,
  completion/closing mechanics, and carve-outs are the floor of a legal instrument — any
  accidentally-dropped trigger/deadline is a hard defect, not a stylistic simplification.

## Cross-document terminology consistency — the Trust is the constitutional document

When two documents describe the same underlying instrument (a Trust Agreement and its
companion Prospectus, or any "constitutional document + summary" pair), every defined term,
entity name, and figure in the summary document must match the constitutional document
exactly. The Prospectus *summarizes* the Trust; it does not restate it with its own
independent vocabulary.

| Wrong (found in the baseline) | Correct (per the Trust) | Why |
|---|---|---|
| Representante Común drafted as a bank | A **casa de bolsa** (brokerage), not a bank | Structural role confusion — a recurring, easy-to-miss error class |
| "Resultado Distribuible" | "Ingreso Distribuible" | Same underlying concept, two different coined names — the Trust's name governs |
| "Titleco" (an English coinage) | "Sociedad Tenedora" | A coined English brand name has no place as an operative defined term in an all-Spanish instrument, unlike a genuine Mexican statutory acronym (e.g. "CBFIs") |
| "Oferta de Toma de Control" | "Oferta de Adquisición" | Naming drift on the same 20%-threshold mechanism |
| "Cuenta de Colocación" | "Cuenta de Suscripción" | Same pattern |

**Practical rule for future sessions**: once a constitutional document (Trust, LP Agreement,
Shareholders' Agreement, etc.) is finalized, treat it as the single source of truth for every
defined term and figure in every companion document, and do a targeted cross-check pass — do
not assume a summary document drafted in parallel or beforehand is already consistent.

## Financial-figure discipline

Real, computed figures (once genuinely fixed) must be propagated consistently everywhere
they appear (cover, glossary, body prose, financial tables) — not left as a bare placeholder
in some sections while another section has the real number. Keep the "negotiated/prospective
target" framing intact when propagating — a computed proforma figure is not the same as a
legally fixed final price, and the language should say so consistently everywhere.

## Open questions

- **oq-1**: this file documents *Spanish*-language legal-drafting voice specifically. The
  Direct-Hold Solution platform also drafts in English (Canada, US) — a future session should
  confirm whether an analogous English-voice research file already exists elsewhere in this
  design system, or whether one is needed.
- **oq-2**: the "constitutional document governs its summary" cross-consistency rule is
  stated generically, but this design system does not yet have a named pattern/checklist for
  *how* to run that cross-check systematically (e.g., a defined-term diff pass) — worth a
  follow-up if this platform keeps producing constitutional-document + summary-document
  pairs, which it does routinely.
