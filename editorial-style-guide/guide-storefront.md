---
schema: foundry-doc-v1
title: "Storefront guide — commercial pages a customer buys from"
slug: guide-storefront
category: internal
type: reference
content_type: reference
quality: complete
status: active
audience: contributor
bcsc_class: public-disclosure-safe
governs: [pricing, catalog, product-detail, checkout, licensing-terms, storefront-policy]
last_edited: 2026-08-10
editor: pointsav-engineering
---

> The register guide for commercial storefront pages — pricing, catalog, product detail,
> checkout, licensing terms, and the policy/support pages that sit alongside them. Builds
> on [[house-core]]; restates nothing there. The reader here is a customer, not a
> colleague or a wiki reader — closer to a product page than an encyclopedia entry, which
> is why this register carves an explicit exception to house-core's default anti-
> promotional stance (see §6).

## 1. Purpose and audience

The reader is a prospective or existing customer on a commercial storefront: deciding
whether to buy, checking license terms, or resolving a payment/account question. They
bring no context from the organization's internal documentation and are not a wiki
reader. Unlike the corporate wiki's institutional allocator or the documentation wiki's
technical reader, this reader expects the company to address them directly, the way any
commercial storefront does.

## 2. The shape

Two page shapes, one voice. Transactional/marketing pages (catalog, pricing, licensing
terms, product detail, checkout) and policy/support pages (privacy, accessibility,
contact, disclaimer) need the same underlying voice; they differ only in whether "we" is
natural (§6). Neither shape inherits from communications' announcement/memo/email
genres — a pricing page is not a message moving a decision from writer to reader, it is a
standing commercial surface a customer arrives at with a question already in mind.

## 3. Opening

You-first, benefit-or-fact-first — not a scene-setting lead. The opening sentence should
be readable by a visitor who has seen nothing else on the site. Isolation test: lift the
first sentence out; if it only makes sense as a continuation of surrounding chrome, it
fails.

## 4. Paragraph and sentence rhythm

No delta from [[house-core]]'s default targets. Storefront/policy copy runs shorter in
practice (most surveyed passages ran 2–4 sentences per section) but that reflects the
content, not a distinct rhythm rule.

## 5. Headings and scannability

Numbered sections read naturally on policy pages (disclaimer, privacy, accessibility) —
keep as-is where already in use. Marketing/catalog pages use plain H2s per topic. No
delta from [[house-core]].

## 6. Voice and tone — the explicit house-core exception

[[house-core]] excludes "the promotional register of a product page" as its general
rule. This register is the named exception: a storefront page is a product page, and its
job is to move a purchase decision, not to teach a subject. Within that exception, one
rule still governs absolutely:

**Named actor, not narrating observer.** The subject of a sentence describing what the
company does is "you" (the reader), the brand name as a named actor ("PointSav
distributes..."), or "we" — never the impersonal site itself ("this site distributes...",
"this site collects..."). A sentence with "this site" as its subject reads as a third
party describing the company from outside, rather than the company speaking to the
reader — a measurably different effect, not just a wording preference.

**"We" placement is not uniform across the surface** — the one place this register
diverges internally. Verified against two live hyperscaler storefronts (AWS pricing,
Azure pricing, AWS contact-us, fetched 2026-08-02) before adoption, not assumed:

- On pricing/catalog/licensing pages: "you/your" address dominates, the brand name
  carries the actor role when one is needed, "we" is nearly absent.
- On support/policy pages (contact, accessibility, privacy-adjacent): "we" appears
  naturally alongside "you," without displacing it.
- Neither reference site ever used the impersonal "this site/it does X" register
  anywhere sampled.

**Legal-precision exception, not a loophole.** "This site" (or the local equivalent)
survives wherever it does real disambiguating work — distinguishing what *this specific
surface* does from what a parent company's *other* properties do, or where it is a
standard legal-drafting formula ("by using this site, you acknowledge..."). Test: would
removing the site-scoping silently widen a factual or legal claim to cover the whole
company rather than just this surface? If yes, keep it — reworded to keep it if needed
("on this site, we collect...") rather than deleted.

**Not yet verified beyond one surface.** The "we"-placement split above is derived from
software.pointsav.com plus two external reference sites — not yet confirmed to
generalize to a second internal commerce surface. Re-verify before assuming it applies
elsewhere in the catalog.

## 7. Code and examples

None expected. No code blocks were found on any storefront page surveyed.

## 8. Worked examples

**Impersonal narration → named actor / direct address** (licensing terms page):

> Weaker: "software.pointsav.com distributes pre-compiled binaries under four license
> tiers... Applies to `os-orchestration`... This is the company's stated commercial
> moat."
>
> Stronger: "PointSav distributes pre-compiled binaries under four license tiers... This
> tier applies to `os-orchestration`... It's PointSav's stated commercial moat."

**Impersonal narration → "we" on a policy page** (privacy page):

> Weaker: "This site collects payment-verification data only... This site does not use
> tracking cookies for analytics or advertising."
>
> Stronger: "On this site, we collect payment-verification data only... We don't use
> tracking cookies for analytics or advertising."
>
> *The "on this site" scoping survives the rewrite — dropping it would silently widen the
> "collects...only" claim from this surface to the whole company.*

**A claim deleted instead of re-voiced — a mistake to avoid, not a model:**

> An earlier pass deleted a real trust claim ("this catalog is rendered directly from the
> release catalog—what you see here is exactly what the download API serves") rather than
> re-voicing it, because the sentence also leaked an internal implementation detail ("the
> download API"). Corrected: "This catalog always matches what's actually available to
> download—nothing here is stale or hand-curated." Voice edits re-voice; they do not
> silently delete a claim that has an unrelated problem too — fix the two problems
> separately and visibly.

## 9. Pre-publish checklist

- Does every sentence describing what the company does have "you," the brand name, or
  "we" as its subject — never the impersonal site/page itself?
- On a pricing/catalog/licensing page: is "we" nearly absent, with "you" and the named
  brand carrying the voice instead?
- On a policy/support page: does "we" appear naturally, without displacing "you"?
- Wherever "this site" (or local equivalent) survived, does it do genuine disambiguating
  work — not left in by default?
- Did a voice edit ever also delete a factual or technical claim, rather than re-voicing
  it in place?
- Does the Spanish (or other locale) pair mirror the same voice shift sentence for
  sentence, not just the English side?
