---
schema: foundry-design-research-v1
component_or_token: wcp.finance.*, financial-report-layout
decision_type: token-consolidation
authored: 2026-07-29
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (architecture audit), claude-sonnet-5 (synthesis)
status: ratified
source: project-proforma DESIGN-TOKEN-CHANGE-wcp-finance-bundle.draft.md (2026-06-14/2026-07-23); operator review, 2026-07-29
ai_consumption_hint: "wcp.finance.* is a pure alias layer over paper.semantic.financial-report-layout.* — every leaf resolves via var() to the Paper-pillar token, never a literal value. A codegen agent looking up either namespace gets the same resolved value; wcp.finance.* exists only as an engine-facing CSS custom-property surface for tool-proforma-engine, not a second source of truth."
---

# wcp.finance.* — alias-layer decision (2026-07-29)

## Why this exists

The originating draft (`DESIGN-TOKEN-CHANGE-wcp-finance-bundle`) proposed a new,
hand-authored, literal-value token group (`wcp.finance.*` → `dtcg-vault/tokens/finance.tokens.json`)
duplicating the same V5 canonical values already landed as
`paper.semantic.financial-report-layout.*` this session. Its stated rationale:
`tool-proforma-engine` (the Rust renderer) generates self-contained, offline
HTML documents and needs a small, embeddable CSS variable mirror it can
compile in, without depending on the wider design system's build/path
structure.

That rationale is legitimate — the *namespace* is useful. Landing the
*literal values* as proposed is not: it recreates the exact two-copies-drift
failure this design system's 2026-07-17 token consolidation exists to
prevent (see `.agent/rules/design-tokens.md`), just inside
`pointsav-design-system` instead of across repos. An architecture review this
session (two independent Opus audits) confirmed: `wcp.finance.*`'s actual
values are brand-neutral document greys and type (`#111`, `#e3e3e3`, `#888`,
Carlito 10–17px) — no tenant color spine, not Woodfine-specific — so it
belongs in the Paper pillar's generic substrate, not a tenant's own repo, and
not as a second literal copy.

## What was landed instead

`dtcg-vault/tokens/finance.tokens.json` — every `wcp.finance.*` leaf is a
DTCG alias (`{paper.semantic.financial-report-layout.<leaf>}`) to the
already-canonical Paper token. The generated `tokens.css` resolves every
`--ps-wcp-finance-*` custom property to a `var(--ps-paper-semantic-financial-report-layout-*)`
reference — zero literal restatement. `paper.semantic.financial-report-layout.*`
remains the single source of truth; `wcp.finance.*` is a namespace, not a
second store of values.

## What this doesn't do yet

The draft's actual underlying need — a compiled-in Rust `CONST` the engine can
embed for fully offline HTML generation — is not built by this alias layer.
Landing the alias closes the *drift* risk and gives a stable namespace; a
future `xtask` codegen step (regenerating a Rust mirror from this file's
resolved export) is the remaining engine-side work, explicitly out of scope
here — the same boundary the original draft itself already drew ("this is
engine-side work, scoped out of this pass").

Also not built: the draft's proposed ES/MX jurisdiction theme overrides
(`finance-es.css`, `finance-mx.css`). Per the draft's own research trail,
these were never verified against a real ES/MX document — left as an
explicit future proposal, not fabricated here.

## Related architecture correction, same session

Landing this alias layer surfaced a broader finding: `pointsav-brand.json`'s
own `$description` previously invited a same-repo `themes/<brand>.json` fork
for adopting tenants. That pattern was corrected the same session — see
`.agent/rules/design-tokens.md`'s 2026-07-29 update. `wcp.finance.*` is
unaffected by that correction (it was never tenant-specific to begin with),
but the two findings share a root cause: a second copy of the same values,
wherever it lives, is the failure mode to design against — not the specific
repo boundary.
