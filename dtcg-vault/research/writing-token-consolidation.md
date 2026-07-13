---
schema: foundry-design-research-v1
component_or_token: writing
decision_type: token-consolidation
authored: 2026-07-13
authored_by: totebox@project-design
authored_with: claude-opus-4-8 (deep-read), claude-sonnet-5 (synthesis)
status: ratified
source: project-editorial DESIGN-RESEARCH-editorial-style-guide-bundle.draft.md (12-file style-guide bundle, MOUNTED not copied) + pointsav-design-system legacy tokens/linguistic/ (39 files) + pointsav-media-assets and woodfine-media-assets linguistic content
ai_consumption_hint: "Four addressable layers, not a merge: craft (writing.primitive) + register/lexicon/disclaimer rule SHAPES (writing.semantic, shipped empty of tenant values) + tenant VALUES (a per-brand media-assets theme override, fork-and-repoint like themes/<brand>.json for color) + prose exemplars (project-editorial's own register guides, mounted not copied). A codegen agent resolving writing.semantic.register.legal should follow its $extensions.guide pointer to the real mounted prose, not assume the token alone carries voice."
---

# Writing pillar — token consolidation rationale

## Real DTCG constraint that shaped this design

DTCG 2025-10 has no array/list primitive. Every list-shaped rule (banned-vocabulary
lists, required-vocabulary lists, thematic-anchor lists) is modeled as one token per
entry, with structural metadata (alternates, exceptions, scope) carried in a documented
`$extensions.com.pointsav.writing` namespace — a genuinely new surface for this repo
(the color/spacing token layers never needed `$extensions`). Flagged for confirmation
that the build tooling (`sync-design-tokens.sh`, `tokens_gallery.rs`) tolerates a
non-standard extensions namespace before treating this as fully load-bearing.

## Why genericize Woodfine's lexicon content instead of leaving it Woodfine-only

`woodfine-media-assets/tokens/linguistic/wf-protocol-lexicon.yaml` and its siblings
(disclaimer/trademark/contact templates) are real, live, production content — not
drafts. The rule SHAPES recur identically across PointSav and Woodfine's own
linguistic content (a banned-vocabulary list, a required-vocabulary list, a thematic-
anchor list, a parametrized disclaimer template, a trademark-footer template, a
contact-block template) — only the concrete values differ per tenant. Per operator
decision: the reusable STRUCTURE becomes a generic PointSav Design System token
(`writing.semantic.lexicon.*`, `.disclaimer.*`, etc.), shipped empty of any tenant's
real values; Woodfine's actual banned words, required phrases, "Five Fs" thematic
anchors, and entity/address strings become a `woodfine-media-assets` override layer —
the same fork-and-repoint pattern `themes/<brand>.json` already uses for color aliases.
Rationale, in the operator's own words: these tokens were originally built FROM
Woodfine's real production needs, and genericizing them is exactly what makes the
design system useful to other companies facing the same needs.

## Real philosophical conflict found, not silently resolved

The legacy `pointsav-design-system/tokens/linguistic/vocabulary-banned-*.yaml` files are
kill lists. The editorial style-guide bundle's own house-core.md explicitly rejects kill
lists in favor of a positive, WARN-only linter ("not a list of forbidden words").
Resolution applied: `writing.semantic.lexicon.banned` survives as a real, tenant-override
token (a brand's own voice legitimately needs banned words — e.g. Woodfine's
`but`/`however`/`despite`/`although` ban is a real, deliberate stylistic choice), but is
marked advisory/WARN-only in its `$description`, consistent with the editorial machine's
own philosophy rather than reintroducing a hard-gate kill list.

## Composition, stated explicitly (not a silent merge)

1. `writing.primitive.*` — objective craft constants (sentence length, casing, active
   voice). Tenant-agnostic, applies everywhere, owned by the design system.
2. `writing.semantic.register.*` — the SCALE of registers. Each token's
   `$extensions.guide` field points at the mounted editorial `guide-*.md` — it indexes
   the prose, it does not copy it. This is the seam that satisfies the editorial
   bundle's explicit "mount, don't fork the prose" requirement.
3. `writing.semantic.profile.*` — register + audience delta, mirroring house profiles.
4. `writing.semantic.{lexicon,disclaimer,page-title}.*` — generic rule shapes, shipped
   empty of tenant values.
5. A tenant theme override (media-assets, not this repo) binds real values into the
   semantic shapes.

## Explicitly out of scope, flagged not dropped

~20 legacy `*protocol*`/`ds-protocol*.yaml` files (e.g. `protocol-topic.yaml`,
`ds-protocol-comm.yaml`) are SLM extraction/publishing-pipeline enforcement
configuration, not writing-craft tokens — they were read during this consolidation and
deliberately excluded from `dtcg-vault/writing/`, not silently dropped. They belong with
the extraction/publishing services that actually consume them.

The `voice` block the editorial bundle's own draft asks to be removed from
`themes/pointsav-brand.json` was confirmed absent in this clone already (either already
removed, or never present) — worth re-verifying against the canonical repo and any
exported bundle before treating this as fully closed.
