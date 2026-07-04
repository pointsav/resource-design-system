# When to use Code Block With Copy

Use this component for any pre-formatted code, config, or command snippet a
reader might want to reuse verbatim — a shell command, a config file, an API
response example. The inset copy button removes the error-prone step of
manually selecting monospace text with a mouse.

## When to use

- Command-line snippets a reader is expected to paste into a terminal.
- Config file excerpts (YAML, JSON, TOML) meant to be copied whole.
- API request/response examples in reference documentation.

## When not to use

- Inline code references within a sentence (a variable name, a short
  expression) — use plain inline `code` styling, not a full block with its
  own copy affordance.
- Content that must never be copied verbatim without modification (a
  template with placeholders the reader must fill in first) — call this out
  explicitly in the surrounding prose instead, since the copy button implies
  "paste this as-is."
