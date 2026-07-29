---
schema: foundry-design-research-v1
component_or_token: interactive-pdf-binder
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-jennifer DESIGN-BUNDLE-Interactive-PDF-Binder-V1.md + tool-pdf-interactive/tool-pdf-interactive.py (canonical template, verified directly against the Python source, not just the draft's prose)
ai_consumption_hint: "Values here were pulled from the live Python constants, not the draft's own color table — one discrepancy found and corrected (a 7th color GREY_MID does not exist in code). This is a PDF-point-space component (612x792pt, origin bottom-left), a genuinely different rendering context from the CSS-print @page components elsewhere in the Paper pillar — do not force it to share paper.primitive.page.* geometry."
---

# Interactive PDF Binder Navigation — token consolidation rationale

Values in this component were extracted directly from `tool-pdf-interactive.py`'s own
Python constants (the authoritative source), not from the design draft's prose
description — one real discrepancy was found this way: the draft's color table lists a
7th token `GREY_MID` (`#666680`, described as "inactive entry subtitles"), but no
subtitle rows exist anywhere in the actual generator code. Dropped from this component's
token set rather than silently carried forward as a phantom value.

## Why this is a separate rendering context, not folded into paper.primitive.page.*

Every other Paper component in this consolidation is a CSS `@page`-based WeasyPrint
document. This component is generated directly in PDF point-space via `reportlab` +
`pypdf` — same physical units (points), genuinely different coordinate system (origin
bottom-left, not top-left; no `@page` box model). Kept as its own
`paper.primitive.pdf-nav.*` group rather than forced to share the CSS-print page
primitives, since the two are not interchangeable despite both using `pt`.

## Tool location and portability

The canonical template lives at
`project-jennifer/tool-pdf-interactive/tool-pdf-interactive.py` (258 lines) with
`README.md`/`README.es.md`. Seven filled-in production copies exist under
`project-jennifer/inputs/*/` for real Client A/Agency/MOU/Mexico-Prospectus binders —
those remain business-admin artifacts and do not move. The canonical template itself is
self-contained (only `pypdf`/`reportlab` dependencies, no project-jennifer-specific
paths or business content) and ports to `pointsav-monorepo/tool-pdf-interactive/` with
low rework — the main generalizing step is lifting its top-of-file `CONFIG` block into
CLI arguments or a manifest file, so one installed tool can build any binder without
editing source.

A second, more-developed copy of this tool (676 lines, including a `find_home_anchor`
feature via `pdfplumber`) already exists committed directly at
`pointsav-monorepo`'s repository root — a real, pre-existing `repo-layout.md` violation
(no scripts allowed at repo root) predating this consolidation. That copy, not the
project-jennifer template, is the better base for the actual `tool-*` port (Step 6a of
this initiative), since it is already more feature-complete and already properly
licensed/committed within the monorepo; the project-jennifer template's design values
were used for this token consolidation since it is the cleaner, generalized reference
the design draft actually describes.

## Update 2026-07-29 — geometry was never real, and a grouped-TOC pattern landed

Two corrections from project-jennifer, both verified against three shipped production
binders (MOU, Agency Agreements, MX Prospectus) plus the Client A reference generator,
not against the original draft this file's earlier content was based on:

**Geometry correction.** `toc-entry-first-y`, `toc-entry-step`, `toc-entry-width`,
`toc-num-x`, `toc-title-x`, and the INDEX-button `home-width`/`home-height`/
`home-corner-radius` never matched the shipped Python generators — the original recipe
values traced to an early draft, not measurement. Corrected to the values the production
binders actually render (see `usage.md`'s geometry table for old/new side by side).

**Grouped-TOC pattern.** Added `toc-group-header` and `toc-entry-child` variants — an
already-owner-ratified pattern (adopted 2026-07-17 as the house standard for TOC slip
sheets, not a proposal) extracted from the Client A reference's own existing use of it.
A full token audit against all 36 pre-existing `pdf-nav`/`pdf-binder` tokens found the
shipped design on-token except the geometry above; three off-token greys (footer ink,
subtitle ink, date ink — each within a few RGB-255ths of their token) were corrected in
the *generator code*, not the tokens, since the tokens were already right. Two design
alternatives were evaluated in full and rejected before landing this pattern — ISO 2145
decimal numbering, and a Times-based closing-binder register — see `usage.md`'s "Rejected
alternatives" for the reasoning, recorded so the questions are not reopened.

Also renamed the return button's label `HOME` → `INDEX` (zero geometry change) and
replaced the active-row marker from a WinAnsi-undefined glyph substitution to a drawn,
deterministic 7.2×7.2pt rectangle.
