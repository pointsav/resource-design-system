---
title: Preview Frame — Code
---

# Code

## Dependencies

- Primitives: color (surface/border/inverse tiers), no motion or spacing
  primitives required.
- Assets: none.

## HTML + CSS recipe

```html
<div class="ps-preview" data-theme="light">
  <div class="ps-preview__toolbar">
    <button type="button" class="ps-preview__toggle" aria-pressed="true" data-ps-theme="light">Light</button>
    <button type="button" class="ps-preview__toggle" aria-pressed="false" data-ps-theme="dark">Dark</button>
  </div>
  <div class="ps-preview__canvas">{{content}}</div>
</div>
```

## Behaviour

Clicking a toggle button reads `data-ps-theme` off the clicked button, sets
`data-theme` on the parent `.ps-preview`, and updates `aria-pressed` on all
sibling toggle buttons so exactly one reads `true` at a time. No framework
dependency — plain DOM event listeners are sufficient.

## Related mechanism in this substrate

This app (`app-privategit-design`) renders each component's own recipe
variants live, in a sandboxed `<iframe srcdoc>` per variant
(`src/component_preview.rs`) — `sandbox="allow-same-origin"`, no
`allow-scripts`, so the previewed markup cannot execute script or navigate
the parent page, and a per-variant `title` attribute names the variant for
screen readers. That mechanism and this `ps-preview` recipe solve related
but distinct problems: the iframe sandbox isolates a component's CSS from
this site's own chrome; `ps-preview` is the themeable canvas a *consumer*
places around content they want to demo in both themes. Consumers who
also need iframe-level isolation should wrap the `.ps-preview__canvas`
content in their own sandboxed frame — this recipe does not itself sandbox
its content.
