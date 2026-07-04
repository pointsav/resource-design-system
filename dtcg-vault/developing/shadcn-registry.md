# shadcn Registry

The substrate exposes a shadcn-compatible component registry.

## Endpoints

- `GET /r/registry.json` — full registry index
- `GET /r/{component}` — individual component entry

## Usage with code generators

**v0, Cursor, Claude Code, Windsurf:** add the registry URL to your editor's
component source configuration. Generated UI pulls component structure and token
references from the vault.

**Manual install:** fetch `/r/{component}` and copy the `html` and `css` fields
into your project.

## Component names

Component names match the slugs in the sidebar (e.g. `button`, `input-text`,
`navigation-bar`). See the [component overview](/components/overview/) for the
full list.
