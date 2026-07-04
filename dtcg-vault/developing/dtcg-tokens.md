# DTCG Token Consumption

Tokens are published in W3C Design Tokens Community Group (DTCG) format.

## Full bundle

`GET /tokens.json` — returns the complete token bundle, merging the primitive
layer and the active theme's semantic overrides.

## Typed per-theme bundle

`GET /api/tokens/{theme}.dtcg.json` — returns a typed DTCG bundle scoped to one
theme. The `{theme}` parameter is the filename in `vault/themes/` without the
`.json` extension. For the vendor instance: `pointsav-brand`.

## shadcn registry

`GET /r/registry.json` — shadcn-compatible registry index. Individual component
entries at `/r/{component}`. Works with v0, Cursor, Claude Code, and Windsurf
out of the box.

## CSS variables

Each token maps to a CSS custom property. The full variable set is available in
the page source and at `/tokens.json` under the `css` export key.
