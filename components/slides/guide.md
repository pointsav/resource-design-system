# Slides

A full-screen slide-deck renderer for embedding a presentation inside
article prose, driven from a fenced `:::slides` markdown block.

## When to use

Use when an article needs to embed a short slide presentation (e.g. a
walkthrough, a pitch excerpt) without leaving the page. Do not use for
long-form standalone presentations — this is an in-article embed, not
a presentation authoring tool.

## Markup

````markdown
:::slides
## Slide 1 title
content

## Slide 2 title
more content
:::
````

Each `##` heading starts a new slide inside the deck container.

## Complete CSS

```css
.slide-deck {
  border: 1px solid var(--slide-border);
  border-radius: var(--slide-radius);
  background: var(--slide-bg);
  color: var(--slide-fg);
  overflow: hidden;
  margin: var(--sp-6) 0;
  outline: none;
}

.slide-deck__controls {
  display: flex;
  align-items: center;
  gap: var(--sp-2);
  padding: var(--sp-2) var(--sp-3);
  background: var(--slide-control-bg);
  color: var(--slide-control-fg);
}

.sd-prev,
.sd-next,
.sd-fullscreen {
  background: none;
  border: 1px solid rgba(255, 255, 255, 0.4);
  color: var(--slide-control-fg);
  cursor: pointer;
  padding: var(--sp-1) var(--sp-2);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  line-height: 1;
}

.sd-prev:hover,
.sd-next:hover,
.sd-fullscreen:hover { background: rgba(255, 255, 255, 0.15); }

.sd-prev[aria-disabled="true"],
.sd-next[aria-disabled="true"] { opacity: 0.4; cursor: default; }

.sd-fullscreen { margin-left: auto; }

.sd-progress {
  font-size: var(--text-sm);
  color: rgba(255, 255, 255, 0.85);
  min-width: 4ch;
  text-align: center;
}

.slide-deck__viewport {
  position: relative;
  aspect-ratio: var(--slide-aspect);
  overflow: hidden;
}

.slide {
  position: absolute;
  inset: 0;
  padding: var(--sp-8) var(--sp-10);
  overflow-y: auto;
  display: none;
}

.slide.active { display: block; }

.slide h1,
.slide h2 { font-size: 1.6em; margin-bottom: var(--sp-4); }
.slide p   { font-size: 1.1em; line-height: 1.5; }

.slide-deck__transcript {
  border-top: 1px solid var(--slide-border);
  padding: var(--sp-3) var(--sp-4);
  font-size: var(--text-sm);
  color: var(--fg-3);
}
.slide-deck__transcript summary { cursor: pointer; color: var(--fg-3); }
.sd-transcript__slide  { margin: var(--sp-4) 0; }
.sd-transcript__label  {
  font-size: var(--text-xs);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--fg-4);
  margin-bottom: var(--sp-1);
}

/* iOS Safari / CSS fullscreen fallback */
.sd-fullscreen--active {
  position: fixed;
  inset: 0;
  z-index: 9999;
  border-radius: 0;
  background: #000;
}
.sd-fullscreen--active .slide-deck__viewport {
  aspect-ratio: unset;
  height: calc(100% - 44px);
}
```

Root variables to set once per instance: `--slide-aspect: 16 / 9`,
`--slide-bg`, `--slide-fg`, `--slide-border`, `--slide-radius`,
`--slide-control-bg: rgba(0,0,0,.45)`, `--slide-control-fg: #fff`.

**Known gap:** `--sp-*`, `--radius-*`, `--text-*`, `--border`, `--bg-subtle`,
and `--fg-1`/`--fg-3`/`--fg-4` above are engine-local tokens in
`app-mediakit-knowledge/static/style.css`, not yet aliased to this
design-system's canonical spacing/radius/type-scale primitives. Registering
that alias chain is follow-up work, not done here — see this component's
research note.

## JS controller

`slide-deck.js` (90 lines, first-party) handles `←`/`→`/`F`/`Esc` keyboard
navigation, hash routing, and fullscreen toggle (including the iOS Safari
CSS-fullscreen fallback above). A `<details>` transcript is rendered
alongside the deck for accessibility — screen readers get the full slide
text without needing the visual deck. Not inlined here; consume from
`app-mediakit-knowledge/static/slide-deck.js` until it has a canonical
design-system home.

## Source

Implemented in `app-mediakit-knowledge`; registered here 2026-07-01 from
the Sovereign Editorial Phase 2→6 wiki redesign
(DESIGN-RESEARCH-sovereign-editorial-knowledge-wiki). Live on
documentation.pointsav.com, projects.woodfinegroup.com, corporate.woodfinegroup.com.
