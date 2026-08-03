---
schema: foundry-design-research-v1
component_or_token: financial-report-layout, proforma-vehicle-layout
decision_type: reproducibility-audit
authored: 2026-07-23
authored_by: totebox@project-proforma (cross-archive exception)
authored_with: claude-sonnet-5
status: ratified
source: internal design-component drafts (project-proforma cross-archive exception) + a private renderer-family audit (13 report renderers, client-specific details redacted)
ai_consumption_hint: "The reproducibility audit trail for the 2026-07-23 proforma bundle — which documents the current financial-report-layout tokens can and can't actually reproduce, and why. Exists in place of a blind-reconstruction verification loop (explicitly deferred by operator decision). A generation agent asked to reproduce a proforma from tokens should read this first to know whether the target document is one of the three verified-matching ones or one of the six with a live, uncorrected defect."
---

# Proforma reproducibility audit (2026-07-23)

## Purpose

The operator's request that triggered this bundle was blunt: "some of our
tokens todate where not made properly and are not able to reproduce the
documents." This file is the audit that makes that concrete — which documents
the current design-system content can and can't actually reproduce, and why —
so the next person to touch this family starts from a verified map instead of
an assumed one.

## Method

No Fable/Opus blind-reconstruction loop this round (deferred, operator
decision). Verification here means: every disposition below was reached by
reading the actual `<style>` block / HTML shell in the named Rust source file
directly, not by inference from filenames, comments, or the design system's
own (as this audit shows, sometimes wrong) claims about itself.

## The family, and what's actually in it

"Financial-report-layout family" turns out to mean three genuinely different
things that have been getting talked about as one:

1. **The print/PDF compliance-document family**
   ([financial-report-layout](/components/financial-report-layout/usage) +
   [proforma-vehicle-layout](/components/proforma-vehicle-layout/usage)) —
   landscape, tabular, line-numbered. This audit's actual subject.
2. **A separate classic-statement family** (`forecast_statements.rs`) —
   portrait, serif, pure black-and-white. Already tracked as its own thing
   ([financial-statement-yearend](/components/financial-statement-yearend/usage)
   in `pointsav-design-system`), correctly not conflated here, but flagged in
   this audit because it's easy to mistake for family 1 by proximity (same
   directory, similar name pattern). Note also: `forecast_statements.rs` lives
   in project-proforma's own top-level `tool-proforma-engine/`, a separate git
   history from the `pointsav-monorepo/tool-proforma-engine/` sub-clone every
   file in the audit table below lives in.
3. **A separate interactive-dashboard family** (`client_d_sensitivity_v7/v8.rs`,
   `tearsheet_alt_re_v2.rs`) — screen-first, Chart.js, CSS custom properties.
   Not a print document at all; not a candidate for either component above.

Disambiguating these three up front is itself a finding — before this audit,
"the financial-report-layout family" had no explicit boundary, which is part
of how drift went unnoticed for as long as it did.

## Audit table — family 1 only (the print/PDF compliance family)

| File | Disposition | Font | Borders | Gutter | Fills |
|---|---|---|---|---|---|
| `client_a_v1_proforma.rs` | **Canonical (V5)** | Carlito | rules only | server-rendered | banner only |
| `legacy_jv_proforma.rs` | Diverged, pre-V4 | system-ui → DejaVu (bug) | full grid | JS (broken under WeasyPrint) | th/total/subtotal/banner all tinted |
| `alloc_client_c_proforma.rs` | Diverged, pre-V4 | system-ui → DejaVu (bug) | full grid | JS (broken) | all tinted |
| `client_d_proforma.rs` | Diverged, pre-V4 | system-ui → DejaVu (bug) | full grid | JS (broken) | all tinted |
| `client_b_proforma.rs` | Diverged, pre-V4 | system-ui → DejaVu (bug) | full grid | JS (broken) | all tinted |
| `building_portfolio_v2.rs` | Diverged, pre-V4 | system-ui → DejaVu (bug) | full grid | JS (broken) | all tinted — comment claims "verbatim" DESIGN token, is not |
| `client_a_forecast_v1.rs` | Diverged, pre-V4 | system-ui → DejaVu (bug) | full grid | JS (broken) | all tinted, plus undocumented `tr.event` class |
| `d1_dev_classes_v2.rs` | Diverged, structural variant | system-ui → DejaVu (bug) | full grid | none | `td.grp`/`td.r` pattern, not `td.lbl`/`tr.section-banner` |

**Reading this table:** one file matches what the design system currently
documents as canonical. Six files are running a font that silently isn't the
one anyone chose (WeasyPrint's fallback for an unavailable `system-ui`), and a
line-number gutter mechanism that produces zero visible gutter in the same
engine's primary PDF render path. This isn't stale documentation catching up
to a reasonable variant — it's six files with a live, reproducible rendering
defect, undetected until this audit because nobody had compared all nine
files against each other before.

## What this means for "can the tokens reproduce the documents"

Strictly: **the corrected `financial-report-layout` V5 spec and this bundle's
tokens can reproduce three documents exactly** (Commission Paths, Club Deal,
Private SPV — all `client_a_v1_proforma.rs`) plus, by the same source, the other
`client_a_v1_proforma.rs`-family documents (SPV1, SPV2, Management,
ShareCapital). They **cannot** currently reproduce what the other six files
actually emit, because those six files emit something the corrected spec no
longer describes (the pre-V4 CSS). Landing this bundle as-is doesn't create
new drift — it correctly describes the one file that's already right — but it
also doesn't close the six-file gap, and shouldn't be read as having done so.

## Not fixed this pass — explicit, not silent

Per the no-silent-caps discipline: the following are known, catalogued, and
deliberately not addressed in this round (operator scope decision,
2026-07-22/23 session):

1. **The 6-file pre-V4 CSS defect itself** (table above) — not patched in
   Rust. Real documents generated via `direct-hold`, `wcp`, `dev-classes`,
   `legacy-jv-v1/v2`, `building-portfolio-v1/v2`, or the Ambassadors/AllocJW1
   paths are, as of this audit, still rendering with the wrong font and no
   line-number gutter whenever produced through WeasyPrint.
2. **The Rust-side CSS duplication itself** — 13 independent `<style>` blocks
   across 13 files, no shared constant. Cataloguing the drift (this document)
   doesn't prevent new drift; only a shared source in code does that, and
   that refactor is explicitly out of scope this round.
3. **The top-level-vs-sub-clone engine duplication** — structurally similar to
   the vendor-canonical-vs-project-design-clone problem this whole token
   consolidation effort exists to address. Not investigated further — flagged
   as a pattern worth someone's attention, not a claim that it's actively
   causing harm today.
4. **ES/MX jurisdiction locale tokens** — proposed in the token bundle, never
   built against a real document. Left as an explicit proposal, not implied
   as verified.
5. **`forecast_statements.rs`'s own token needs** — a real, separate, still-
   uncaptured family. Out of this pass's locked scope
   (financial-report-layout + proforma-vehicle-layout + wcp.finance tokens +
   the financial-disclosure writing register only).

## Research trail

### Done (9)
- Read the actual `<style>`/`HEAD` block in all 13 report-renderer files in
  `pointsav-monorepo/tool-proforma-engine/src/report/`, not just the 3 touched
  in the originating session.
- Established a clear three-family boundary (print-compliance /
  classic-statement / interactive-dashboard) where none existed explicitly
  before.
- Confirmed 6 of 9 print-compliance-family files carry the exact
  `system-ui`/JS-gutter defect V5 fixed in `client_a_v1_proforma.rs` — a live
  rendering defect, not documentation drift.
- Confirmed `d1_dev_classes_v2.rs` is a structural variant (different HTML
  pattern), not simply a stale copy of the same pattern.
- Confirmed `client_d_sensitivity_v7/v8.rs` and `tearsheet_alt_re_v2.rs` are
  correctly out of scope (different product entirely — interactive
  dashboards).
- Confirmed `forecast_statements.rs` is a real, separate, legitimate family —
  not a target for convergence with `financial-report-layout`.
- Confirmed `forecast_statements.rs` lives in a different git history
  (top-level clone) than the rest of the audited files (sub-clone) — flagged
  as a duplication-risk pattern.
- Confirmed the design-system draft's own prior claim ("engine drift closed,"
  2026-07-16) was accurate for one file, not the family it implied.
- Verified all three of the originating session's regenerated documents
  (Commission Paths, Club Deal, Private SPV) match the canonical V5 spec
  exactly — the audit's positive case, not just the negative findings.

### Suggested (2)
- When the 6-file pre-V4 defect is eventually fixed, re-run this exact audit
  table to confirm convergence rather than assuming the fix was complete.
- Investigate whether the top-level/sub-clone `tool-proforma-engine` split has
  caused any other silent divergence beyond `forecast_statements.rs` — not
  checked exhaustively this pass.

### Open questions (2)
- Should the 6-file defect be treated as urgent enough to fix outside the
  normal design-bundle cadence (it is, after all, a live rendering bug, not
  just a documentation gap)? Flagged to the operator, not resolved here.
- Should `forecast_statements.rs`'s family get its own DESIGN-RESEARCH audit
  of the same shape as this one, given it's a real, separate,
  currently-uncaptured family? Deferred to whoever next picks up
  `financial-statement-yearend`.
