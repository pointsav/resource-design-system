---
title: Edit On Github Link — Code
---

# Code

## Dependencies

- Primitives: color only.
- Assets: none.

## HTML recipe

```html
<a class="ps-edit-link" href="{{githubSourceUrl}}" target="_blank" rel="noopener noreferrer">Edit this page on GitHub</a>
```

`rel="noopener noreferrer"` is mandatory — it prevents the new tab from
accessing `window.opener`.

## Constructing `{{githubSourceUrl}}`

Not yet implemented in the rendering app (see Usage — Status). The URL should
be built from the same two fields the substrate's own theme already
publishes for exactly this purpose, `themes/pointsav-brand.json`'s `github`
block:

```json
"github": {
  "repo": "https://github.com/pointsav/pointsav-design-system",
  "edit_path_prefix": "edit/main/dtcg-vault"
}
```

i.e. `{repo}/{edit_path_prefix}/<path-to-current-page's-source-file>` — for
example, this very page would resolve to
`https://github.com/pointsav/pointsav-design-system/edit/main/dtcg-vault/components/edit-on-github-link/usage.md`.
