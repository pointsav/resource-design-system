# docs-sidenav — Component Guide

**Type:** Left navigation column  
**Surface:** Product-documentation wiki  
**Carbon baseline:** None — intentional departure (see research file)  
**Research:** `dtcg-vault/research/component-docs-sidenav.md`  
**Source commit:** `914cd836` (app-mediakit-knowledge)

Persistent left navigation column for product-documentation surfaces. Two-level
hierarchy: uppercase category headings as `<details>` sections, article links inside.
Active page highlighted by border-left accent. Sticky-scrolls independently of article
content. Collapses to hidden below 1024px.

---

## HTML recipe

```html
<nav class="docs-sidenav" aria-label="Documentation navigation">
  <div class="docs-sidenav__inner">

    <!-- One <details> per category; server sets `open` for active category -->
    <details class="docs-sidenav__cat" open>
      <summary>Infrastructure</summary>
      <ul class="docs-sidenav__list">
        <li>
          <a href="/wiki/infrastructure/worm-ledger-design"
             class="docs-sidenav__link is-active"
             aria-current="page">
            WORM Ledger Design
          </a>
        </li>
        <li>
          <a href="/wiki/infrastructure/other-article"
             class="docs-sidenav__link">
            Other Article
          </a>
        </li>
      </ul>
    </details>

    <details class="docs-sidenav__cat">
      <summary>Applications</summary>
      <ul class="docs-sidenav__list">
        <li>
          <a href="/wiki/applications/app-privategit-workbench"
             class="docs-sidenav__link">
            PrivateGit Workbench
          </a>
        </li>
      </ul>
    </details>

  </div>
</nav>
```

The `<nav>` sits as the first column child in a CSS grid shell:
`grid-template-columns: var(--sidenav-w) minmax(0, 1fr)`.

---

## CSS

```css
/* Token ------------------------------------------------------------------ */
:root {
  --sidenav-w: 256px;   /* docs left navigation column width */
}

/* Shell grid (parent container) ------------------------------------------ */
.shell {
  display: grid;
  grid-template-columns: var(--sidenav-w) minmax(0, 1fr);
  align-items: start;
}

/* Sidenav container ------------------------------------------------------ */
.docs-sidenav {
  position: sticky;
  top: var(--header-h);
  align-self: start;
  height: calc(100vh - var(--header-h));
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 24px 22px 48px 0;
  border-right: 1px solid var(--rule);
  scrollbar-width: thin;
}

.docs-sidenav__inner { display: flex; flex-direction: column; gap: 2px; }
.docs-sidenav__cat   { margin-bottom: 4px; }

/* Category heading (the <summary>) --------------------------------------- */
.docs-sidenav__cat > summary {
  list-style: none;
  cursor: pointer;
  font-family: var(--font-display, var(--font-body));
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--fg-3);
  padding: 8px 10px 6px;
  border-radius: 7px;
  user-select: none;
  display: flex;
  align-items: center;
  gap: 6px;
}
.docs-sidenav__cat > summary::-webkit-details-marker { display: none; }
.docs-sidenav__cat > summary::before {
  content: "›";
  display: inline-block;
  font-size: 13px;
  color: var(--fg-4);
  transition: transform 0.15s ease;
}
.docs-sidenav__cat[open] > summary::before { transform: rotate(90deg); }
.docs-sidenav__cat > summary:hover { color: var(--fg-1); }

/* Article link list ------------------------------------------------------ */
.docs-sidenav__list { list-style: none; margin: 2px 0 8px; padding: 0; }
.docs-sidenav__list li { margin: 0; }

.docs-sidenav__link {
  display: block;
  padding: 6px 10px 6px 24px;
  border-radius: 7px;
  font-size: 13.5px;
  line-height: 1.35;
  color: var(--fg-2);
  text-decoration: none;
  border-left: 2px solid transparent;
  transition: background 0.12s ease, color 0.12s ease;
}
.docs-sidenav__link:hover  { background: var(--bg-hover); color: var(--fg-1); }
.docs-sidenav__link.is-active {
  color: var(--link, var(--navy));
  font-weight: 600;
  background: var(--bg-subtle);
  border-left-color: var(--link, var(--navy));
}

/* Responsive collapse ---------------------------------------------------- */
@media (max-width: 1023px) {
  .shell          { grid-template-columns: minmax(0, 1fr); }
  .docs-sidenav   { display: none; }
}
```

---

## ARIA checklist

| Requirement | Implementation |
|---|---|
| Landmark | `<nav aria-label="Documentation navigation">` |
| Active page | `aria-current="page"` on active `<a>` |
| Keyboard open/close category | Native `<details>`/`<summary>` — Enter/Space without JS |
| Active state not colour-only | `border-left` accent + `font-weight: 600` alongside colour |
| Hidden from accessibility tree below breakpoint | `display: none` at ≤1023px; article reachable via breadcrumb |
| Independent scroll | `overflow-y: auto` on nav itself |

---

## Open questions

1. **Mobile drawer vs. hidden.** Currently `display: none` below 1024px. Should a
   future sprint add a hamburger-triggered drawer, or is breadcrumb sufficient for
   mobile readers?
2. **Sub-navigation depth.** Current implementation: one level (category → articles).
   If content warrants section-level grouping, what is the maximum depth before the
   pattern should change?
