# MCP Integration

The substrate exposes a Model Context Protocol JSON-RPC 2.0 server at `POST /mcp`.

## Methods

| Method | Returns |
|---|---|
| `list_tokens` | All tokens in the active bundle |
| `list_components` | All component recipe names |
| `list_research` | All research file slugs |
| `describe` | Substrate metadata (version, tenant, token count) |

## Example request

```bash
curl -sS -X POST https://design.pointsav.com/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","method":"describe","id":1}' | jq .
```

## AI agent integration

The shadcn registry at `/r/registry.json` is the recommended integration point
for code generators. MCP is the richer endpoint for agents that query design
decisions and token rationale alongside component structure.
