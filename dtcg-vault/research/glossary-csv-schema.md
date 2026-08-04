# Glossary CSV schema — term-display authority

Not a DTCG token (a CSV isn't a design token) — recorded here because it landed in the
same 2026-08-04 design round as the `index_group` field and `components-structural.yaml`
table/code-block extensions, and needed a documented home somewhere in the token system.

## Shape

One `glossary-<wiki>.csv` per content wiki, already read by
`app-mediakit-knowledge`'s `glossary.rs` auto-linker:

```
Term_EN,Term_ES,Definition,Display_Form,Styling
```

`Display_Form` and `Styling` are the term-display authority — the auto-linker uses them
to decide how a glossary-linked term renders wherever it's referenced in an article body,
rather than leaving that to per-article, per-author judgment (the defect this closes:
`systems/os-orchestration.md` had used inconsistent backtick-vs-plain styling for the same
referent, and lowercased a hyperlinked "Totebox Archive" reference).

- **`Display_Form`** — the term's one canonical capitalization/spelling, e.g. "Totebox
  Archive," not "totebox archive." Authoritative rendered text regardless of how the term
  is cased in the article's own prose.
- **`Styling`** — `code` | `prose` | `both`.
  - `code` — renders with inline code-formatting (backtick/monospace). Crate names, file
    paths, literal identifiers (e.g. `os-console`).
  - `prose` — renders as plain capitalized text. Product/concept names.
  - `both` — context-dependent; flagged for editorial judgment rather than mechanically
    applied.

`Display_Form` and `Styling` are populated only for rows with a real `Definition` — empty
for the undefined inventory rows some wikis carry as placeholders (not real glossary
entries yet).

## Reference implementation

`media-knowledge-documentation/glossary-documentation.csv` has both columns populated for
its 51 defined terms — the reference shape.

`content-wiki-corporate` and `content-wiki-projects` CSVs do not yet have these two
columns added. Flagged as follow-up work in `BRIEF-jennifer-to-wiki-backfill.md`
(project-editorial), not blocking this schema documentation.
