---
schema: foundry-design-research-v1
decision_type: linguistic
language_protocol: DESIGN-RESEARCH
authored: 2026-08-02
authored_by: totebox@project-software
landed_by: totebox@project-design
landed: 2026-08-03
status: research-landed — routing decision still open (see Open questions)
source_draft: project-software/.agent/drafts-outbound/DESIGN-RESEARCH-storefront-commerce-voice-profile.draft.md (commit 6af20b26f)
research_done_count: 4
research_suggested_count: 1
open_questions_count: 2
research_provenance: direct-observation
research_inline: true
ai_consumption_hint: >
  Voice-register research for commercial storefront/commerce surfaces (e.g.
  software.pointsav.com). Core rule: named actor ("you", the brand name, or
  "we") never the impersonal "this site/it does X" observer register. "We"
  placement differs between transactional/marketing pages (nearly absent) and
  policy/support pages (natural) — verified against live AWS/Azure pricing +
  AWS contact-us copy. Includes a pre-publish checklist and worked before/
  after examples. Does NOT resolve where this profile lives long-term in the
  Writing pillar (fifth register vs. layered on "communications") — that is
  project-editorial's structural call, flagged below, not made here.
---

# DESIGN-RESEARCH — Storefront/commerce voice profile

> **Provenance note (project-design, 2026-08-03):** this file lands the
> research content project-software staged and routed here per the
> DESIGN-RESEARCH artifact type. It is landed at the standard DESIGN-RESEARCH
> destination (`dtcg-vault/research/`) per `.agent/rules/token-intake-checklist.md`.
> **It does not resolve the two open structural questions below** — whether
> this becomes a fifth Writing-pillar register or a profile layered on
> "communications," and where the actual `profile-storefront.md` style-guide
> file should live (project-editorial owns `media-knowledge-documentation/
> .internal/style-guides/`). Those remain project-editorial's call. Notified
> via mailbox the same session this file was landed.

## 1. Purpose and audience

The reader is a prospective or existing customer on a commercial storefront —
someone deciding whether to buy, checking license terms, or resolving a payment/
account question. They are not a wiki reader and bring no context from the
organization's internal documentation. Unlike the corporate wiki's institutional
allocator or the documentation wiki's technical reader, this reader expects the
company to address them directly, the way any commercial storefront does.

## 2. The shape

No inherited register shape exists yet (open question — see §"Open questions"
below). In practice, page types on a storefront surface split into two shapes:
transactional/marketing pages (catalog, pricing, licensing terms, product detail,
checkout) and policy/support pages (privacy, accessibility, contact, disclaimer).
Both need the same voice; they differ only in whether "we" is natural (§6).

## 3. Opening

You-first, benefit-or-fact-first — not a scene-setting lead. The opening sentence
should be readable by a visitor who has seen nothing else on the site. Isolation
test: lift the first sentence out; if it only makes sense as a continuation of
surrounding chrome, it fails.

## 4. Paragraph and sentence rhythm

No delta from house-core's default targets identified. Storefront/policy copy
runs shorter in practice (most rewritten passages here were 2–4 sentences per
section) but that reflects the content, not a distinct rhythm rule.

## 5. Headings and scannability

Numbered sections read naturally on policy pages (disclaimer, privacy,
accessibility already use "1. X", "2. Y" — kept as-is). Marketing/catalog pages
use plain H2s per topic. No delta from house-core.

## 6. Voice and tone

**The core rule: named actor, not narrating observer.** The subject of a sentence
describing what the company does should be "you" (the reader), the brand name as
a named actor ("PointSav distributes..."), or "we" — never the impersonal site
itself ("this site distributes...", "this site collects...", "it does not use...").
The distinction is not stylistic pedantry: a sentence with "this site" as its
subject reads as a third party describing the company from outside, rather than
the company speaking to the reader. That register is measurably different in
effect, not just wording — see the Nielsen Norman Group tone-of-voice finding
already cited in [[TOPIC-writing-content-voice-as-design-tokens]] (tone changes
reader trust even when the underlying facts don't change).

**"We" placement is not uniform across the surface** — this is the one place a
storefront profile must diverge from a single fixed voice. Verified against two
real hyperscaler storefronts before adoption (not assumed):

- On pricing/catalog/licensing pages, "you/your" address dominates and the brand
  name is used as a named actor when a subject is needed; "we" is nearly absent.
  AWS's pricing page (`aws.amazon.com/pricing`, fetched 2026-08-02): *"With AWS you
  only pay for what you use..."* — direct address, brand as actor, zero "we" in
  the sampled body copy. Azure's pricing page (`azure.microsoft.com/en-us/pricing`,
  same date): *"Get the best value at every stage of your cloud journey..."* — same
  pattern.
- On support/policy pages (contact, accessibility, privacy-adjacent), "we" appears
  naturally alongside "you," without displacing it. AWS's contact-us page (same
  date): *"We can improve the quality of the content on our pages"* — "we" is
  present, but the page is still majority "you"-addressed.
- Neither hyperscaler's copy ever used the impersonal "this site/it does X"
  register anywhere sampled.

**Legal-precision exception, not a loophole.** "This site" (or the local
equivalent) is legitimate — and should not be edited out — wherever it is doing
real disambiguating work: distinguishing what *this specific surface* does from
what a parent company's *other* properties do (e.g., a software storefront's
disclaimer needs to state plainly that it doesn't sell securities, distinct from
the parent company's separate investor-facing properties), or where it is a
standard legal-drafting formula ("by using this site, you acknowledge..."). The
test: would removing the site-scoping silently widen a factual or legal claim to
cover the whole company rather than just this surface? If yes, keep the scoping —
reworded to keep it if needed ("on this site, we collect...") rather than deleted.

## 7. Code and examples

None expected on a storefront surface (no code blocks in any of the pages
surveyed).

## 8. Worked examples

**Impersonal narration → named actor / direct address** (licensing terms page):

> Weaker: "software.pointsav.com distributes pre-compiled binaries under four
> license tiers... Applies to `os-orchestration`... This is the company's stated
> commercial moat."
>
> Stronger: "PointSav distributes pre-compiled binaries under four license
> tiers... This tier applies to `os-orchestration`... It's PointSav's stated
> commercial moat."

**Impersonal narration → "we" on a policy page** (privacy page):

> Weaker: "This site collects payment-verification data only... This site does
> not use tracking cookies for analytics or advertising."
>
> Stronger: "On this site, we collect payment-verification data only... We
> don't use tracking cookies for analytics or advertising."
>
> *The "on this site" scoping survives the rewrite — dropping it would silently
> widen the "collects...only" claim from this surface to the whole company.*

**A claim deleted instead of re-voiced — a mistake caught on independent review,
not a model to follow:**

> An earlier pass of this rewrite deleted a real trust claim ("this catalog is
> rendered directly from the release catalog—what you see here is exactly what
> the download API serves") rather than re-voicing it, because the sentence also
> happened to leak an internal implementation detail ("the download API").
> Independent review (a second model, fresh context, checking the diff against
> this profile's own rules) flagged the deletion as a content change riding
> inside what should have been a pure voice change. Corrected version keeps the
> trust claim, drops only the internal-plumbing noun phrase: "This catalog
> always matches what's actually available to download—nothing here is stale
> or hand-curated." *Lesson for this profile: voice edits should be re-voicing,
> not silent deletion, even when the original sentence has an unrelated
> problem too — fix the two problems separately and visibly.*

## 9. Pre-publish checklist

- Does every sentence describing what the company does have "you," the brand
  name, or "we" as its subject — never the impersonal site/page itself?
- On a pricing/catalog/licensing page: is "we" nearly absent, with "you" and the
  named brand carrying the voice instead?
- On a policy/support page: does "we" appear naturally, without displacing "you"?
- Wherever "this site" (or local equivalent) survived, does it do genuine
  disambiguating work against the parent company's other properties, or is it a
  standard legal formula — not left in by default?
- Did a voice edit ever also delete a factual or technical claim, rather than
  re-voicing it in place?
- Does the Spanish (or other locale) pair mirror the same voice shift sentence
  for sentence, not just the English side?

## Research trail

### Done
1. Full survey of every customer-facing page on software.pointsav.com
   (`app-privategit-marketplace/src/ui/*.rs`, `static/*.html`) — identified the
   impersonal-narration defect pattern and its inconsistency (present on
   licensing.html, privacy.rs, accessibility.rs §1–2; already correct on
   contact.rs, accessibility.rs §3, checkout.rs, order.rs).
2. Checked the existing Writing pillar implementation
   (`project-editorial/media-knowledge-documentation/.internal/style-guides/`) —
   confirmed no register or profile covers a commercial storefront; `house-core.md`
   explicitly excludes "the promotional register of a product page."
3. Live-fetched and quoted AWS pricing, Azure pricing, and AWS contact-us
   (2026-08-02) to verify the proposed voice direction against real comparable
   sites rather than assuming it.
4. Independent adversarial review of the applied rewrite by a second model
   (Fable, fresh context, no shared history) against this profile's own rules —
   surfaced 6 real findings (content accidentally changed instead of just
   re-voiced, legal scope silently widened, a tense shift, a dropped
   disambiguating object, a Spanish subject-drop ambiguity), all fixed before
   commit. Findings folded into §8's worked examples and §9's checklist.

### Suggested
1. When a second commerce/storefront surface exists in the catalog, re-verify
   this profile's rules against it before assuming they generalize from a single
   surface (software.pointsav.com) — the "we"-placement split in particular
   was derived from two hyperscaler reference sites, not from a second internal
   surface.

### Open questions
1. Should this become its own fifth register (alongside reference/how-to/
   communications/legal), or a profile layered on the existing "communications"
   register? The existing four registers are all wiki/documentation-oriented; a
   storefront's "shape" (§2) doesn't cleanly inherit from any of them. This
   draft doesn't resolve that structural question — project-editorial/
   project-design's call.
2. Does the "we" placement split (marketing pages nearly-"we"-free, support
   pages "we"-natural) generalize to other PointSav commercial surfaces, or is
   it specific to a binary-distribution marketplace? Untested beyond the two
   hyperscaler reference points and the one internal surface this was derived
   from.
