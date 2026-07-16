# MCP Integration

The substrate exposes a Model Context Protocol JSON-RPC 2.0 server at `POST /mcp`.

**Corrected 2026-07-15**: this page previously documented 4 methods
(`list_tokens`, `list_components`, `list_research`, `describe`) that do not
exist anywhere in the real server — found during a compliance audit. The 4
tools below are the real, implemented set (`src/mcp/tools.rs`).

## Tools

| Tool | Returns |
|---|---|
| `get_component_recipe` | A component's full recipe (HTML, CSS, ARIA guidance, tokens consumed, variants) by slug — the same `recipe.json` this site renders live previews from |
| `list_components` | All component slugs, optionally filtered by origin category (`components` generic, `map` GIS-origin, `wiki` wiki-engine-origin) |
| `get_token` | Resolve a single design token by CSS custom property name (`--cds-interactive`) or DTCG path (`semantic.interactive-primary`) |
| `search_design_system` | Full-text search across every indexed vault document — components, tokens, research, guidelines, developing, designing, about |

## Example request

```bash
curl -sS -X POST https://design.pointsav.com/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","method":"list_components","params":{"category":"components"},"id":1}' | jq .
```

```bash
curl -sS -X POST https://design.pointsav.com/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","method":"get_component_recipe","params":{"name":"button"},"id":1}' | jq .
```

## AI agent integration

MCP is the machine-readable entry point for agents that query components,
tokens, or full-text search directly, without parsing HTML. For a plain
JSON export of the full token bundle instead, see
[Get the tokens](/tokens#primitive) — `GET /bundles/tokens/tokens.full.json`.
