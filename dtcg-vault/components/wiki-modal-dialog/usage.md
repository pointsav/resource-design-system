<div class="doc-header">
<span class="eyebrow">Components</span>
<div class="doc-header__badges">
<span class="badge">3 variants</span>
<span class="badge badge--brand">Tokens-backed</span>
<span class="badge">WCAG 2.2 AA target</span>
</div>
<p class="doc-header__lead">A native <code>&lt;dialog&gt;</code> modal opened with
<code>showModal()</code>, so the browser provides the focus trap: content outside the
dialog is unreachable, Escape and a backdrop click both dismiss it. Used for an image
lightbox, a search overlay, and confirmation prompts across the documentation wiki.</p>
<div class="registry-note"><span>Rendered from</span> <code>components/wiki-modal-dialog/recipe.json</code></div>
</div>

## When to use Wiki Modal Dialog

Use Wiki Modal Dialog when a task must interrupt the page and hold
the reader's full attention until it is finished or dismissed —
enlarging an image, running a search, or confirming an action. It is
a component of the [Knowledge Platform](/products/knowledge-platform/overview)
wiki surface, built on the native `<dialog>` element rather than a
custom overlay, so the browser owns the focus trap, the top-layer
stacking, and Escape handling instead of hand-rolled JavaScript.

Reach for a modal only when the interaction genuinely warrants
seizing focus. If the content can sit inline on the page without
blocking the reader, keep it inline — see [When not to use](#when-not-to-use).

## Variants

The substrate ships three variants. All three share the same
`<dialog class="ps-wiki-dialog">` shell, header, and dismissal
behaviour; they differ only in what fills the body and whether a
footer is present.

| Variant | Content | Footer |
|---|---|---|
| **Default** | Title + body + optional footer actions. | Optional — `actions` slot for confirm/cancel controls. |
| **Image lightbox** | A full-width `<figure>` as content. | None. |
| **Search overlay** | A search input with live results as content. | None. |

## Anatomy

The dialog is a single `<dialog class="ps-wiki-dialog">` containing
a `ps-wiki-dialog__content` column with three regions:

1. **Header** (`ps-wiki-dialog__header`) — the visible `<h2>` title
   (`ps-wiki-dialog__title`) and a close button
   (`ps-wiki-dialog__close`) carrying `aria-label="Close dialog"`.
2. **Body** (`ps-wiki-dialog__body`) — the variant content; scrolls
   with `overflow-y: auto` when it exceeds the available height.
3. **Footer** (`ps-wiki-dialog__footer`) — an `actions` slot for
   trailing controls; omitted by the image-lightbox and
   search-overlay variants.

The dialog is capped at `min(90vw, 40rem)` wide and animates in with
a short opacity-and-translate `dialog-in` keyframe on `[open]`.

## Tokens

Every colour, radius, space, and motion value is token-backed — the
CSS references `var(--pds-*)` custom properties only, so the same
markup adopts any tenant theme without edits.

| Token | Role |
|---|---|
| [`{semantic.surface.layer}`](/tokens#theme) | Dialog background. |
| [`{semantic.text.primary}`](/tokens#theme) | Title and body text. |
| [`{semantic.text.secondary}`](/tokens#theme) | Close-button glyph. |
| [`{semantic.border.subtle}`](/tokens#theme) | Dialog border, header rule, footer rule. |
| [`{semantic.interactive.button-primary}`](/tokens#theme) | Primary action in the footer slot. |
| [`{primitive.radius.md}`](/tokens#primitive) | Corner radius. |
| [`{primitive.space.2}`](/tokens#primitive) | Header/footer block padding. |
| [`{primitive.space.4}`](/tokens#primitive) | Body padding, header/footer inline padding. |
| [`{primitive.motion.duration.base}`](/tokens#primitive) | Open animation duration. |
| [`{primitive.motion.easing.decelerate}`](/tokens#primitive) | Open animation easing. |

The backdrop is a fixed `rgba(0,0,0,0.5)` scrim on `::backdrop` and
is not themed.

## Behaviour

### Opening and the focus trap

Open the dialog with `dialog.showModal()`, never by toggling the
`open` attribute. `showModal()` places the dialog in the browser's
top layer and creates a **native focus trap** — every element
outside the dialog becomes inert and unreachable by Tab, pointer, or
assistive technology. This is the reason the component uses native
`<dialog>` rather than a custom overlay: the trap is the browser's,
not the application's.

### Dismissal

- **Escape** — the native `<dialog>` fires a `cancel` event on
  Escape; handle it by calling `dialog.close()`.
- **Backdrop click** — a click on the `::backdrop` scrim dismisses
  the dialog.
- **Close button** — the `ps-wiki-dialog__close` control calls
  `dialog.close()`.

Give the reader all three routes out; do not suppress Escape or the
backdrop click.

## Accessibility

Grounded in the recipe's own `aria` field and a `wcag.target` of
**2.2 AA**:

- **Labelling.** The dialog carries `aria-labelledby` pointing at the
  visible `<h2>` title and `aria-describedby` pointing at the body
  div, so assistive technology announces both the name and the
  content when the dialog opens.
- **Initial focus.** The close button is placed first in the DOM and
  carries `autofocus`, so focus lands on a labelled control
  (`aria-label="Close dialog"`) the moment the dialog opens.
- **Escape to cancel.** The native `cancel` event on Escape maps
  directly to `dialog.close()` — a keyboard user is never stranded
  inside the modal.
- **No focus escape.** Because the dialog is opened with
  `showModal()`, no `aria-modal` shim or manual Tab-cycling is
  required; the browser guarantees focus cannot leave the dialog
  while it is open.

## When not to use

- **Non-blocking content.** If the reader does not need to finish or
  dismiss the interaction before continuing, keep the content inline
  rather than seizing focus in a modal.
- **Passive notifications.** A modal demands a decision. For
  status that the reader can ignore, use a non-modal surface, not
  this component.
- **Stacked modals.** Do not open a second modal on top of an open
  one. Resolve or close the first; nested top-layer dialogs make the
  focus trap and Escape behaviour ambiguous.

<div class="doc-footer-meta">
<span>depends on:</span>
<a href="/tokens#theme">semantic.surface.layer</a>,
<a href="/tokens#theme">semantic.text.primary</a>,
<a href="/tokens#theme">semantic.border.subtle</a>,
<a href="/tokens#primitive">primitive.motion.duration.base</a>
</div>
