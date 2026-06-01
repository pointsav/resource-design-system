# doc-header — Component Guide

**Type:** Inline article header  
**Surface:** Product-documentation wiki  
**Carbon baseline:** None — intentional departure (see research file)  
**Research:** `dtcg-vault/research/component-doc-header.md`  
**Source commit:** `914cd836` (app-mediakit-knowledge)

Inline article header for product-documentation surfaces. Renders a breadcrumb
navigation, article `<h1>` title, optional lede standfirst, last-edited date with
history link, and an auth-gated edit/view-source row. No background fill — part of
the text flow, not a banner.

---

## HTML recipe

```html
<!-- Breadcrumb (sibling of doc-header, not nested inside) --------------- -->
<nav class="crumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/wiki/infrastructure/">Infrastructure</a></li>
    <li aria-current="page">WORM Ledger Design</li>
  </ol>
</nav>

<!-- Article header ------------------------------------------------------- -->
<header class="doc-header">
  <div class="doc-header__titlewrap">
    <h1 class="article__title">WORM Ledger Design</h1>
    <!-- Language switcher slot: flex sibling to h1, pushed right via margin-left: auto -->
  </div>

  <!-- Optional lede: promoted standfirst paragraph
       Render when frontmatter declares content_type: guide or content_type: research -->

  <div class="doc-header__meta">
    <span class="doc-header__edited">
      Updated
      <a href="/wiki/infrastructure/worm-ledger-design/history">
        <time datetime="2026-05-29">May 29, 2026</time>
      </a>
    </span>
    <!-- Additional meta slots (author, reading time) go here if added -->
  </div>
</header>

<!-- Article body --------------------------------------------------------- -->
<div class="article__body mw-parser-output">
  <!-- ... -->
</div>

<!-- Edit row (auth-gated — hidden for anon via CSS) --------------------- -->
<div class="doc-edit-row">
  <a href="/wiki/infrastructure/worm-ledger-design/edit"
     class="doc-edit-link">Edit this page</a>
  ·
  <a href="/wiki/infrastructure/worm-ledger-design/source"
     class="doc-edit-link">View source</a>
</div>
```

---

## CSS

```css
/* Article header --------------------------------------------------------- */
.doc-header { margin-bottom: 28px; }

.doc-header__titlewrap {
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 12px;
}

.doc-header .article__title { margin-bottom: 8px; }

.doc-header__meta {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 10px;
  font-size: 13px;
  color: var(--fg-3);
}

.doc-header__edited a { color: var(--fg-3); font-weight: 600; }
.doc-header__edited a:hover { color: var(--link, var(--navy)); }

/* Edit / View-source row (auth-gated) ------------------------------------ */
.doc-edit-row {
  margin: 48px 0 8px;
  padding-top: 20px;
  border-top: 1px solid var(--rule);
  font-size: 13px;
  color: var(--fg-3);
}

.doc-edit-link { color: var(--fg-3); font-weight: 600; text-decoration: none; }
.doc-edit-link:hover { color: var(--link, var(--navy)); text-decoration: underline; }

/* Hide edit row for unauthenticated sessions ----------------------------- */
html[data-auth="anon"] .doc-edit-row { display: none; }
```

---

## ARIA checklist

| Requirement | Implementation |
|---|---|
| Breadcrumb landmark | `<nav aria-label="Breadcrumb">` wrapping an `<ol>` |
| Current page in breadcrumb | `aria-current="page"` on final `<li>` |
| Unique page title | `<h1 class="article__title">` — one per page |
| Machine-readable date | `<time datetime="YYYY-MM-DD">` for last-edited value |
| Edit row not a phantom tab stop for anon | `display: none` removes from accessibility tree entirely |

---

## Open question

**Author attribution slot.** Should `doc-header__meta` include an author/contributor
field (e.g. "By Jennifer Woodfine · Updated May 29")? Decision required on whether
git-blame attribution should surface in the rendered header or the header stays
impersonal (documentation-style, no byline).
