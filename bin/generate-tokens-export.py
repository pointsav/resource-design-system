#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Woodfine Capital Projects Inc.
#
# Regenerates dtcg-vault/exports/{tokens.full.json,tokens.css,token-families.json,
# tokens.manifest.json} from the real granular source token files:
#   dtcg-vault/tokens/primitive.json, dtcg-vault/themes/pointsav-brand.json,
#   dtcg-vault/paper/{primitive,semantic}.json, dtcg-vault/writing/{primitive,semantic}.json,
#   tokens/tokens-woodfine-org-chart-extended.json (org-chart -- now a first-class source,
#   not spliced in only at deploy time by a separate Command-owned script).
#
# Added 2026-07-16 (token-completeness audit) — see git history for that original scope.
# Extended 2026-07-24 (canonical-id consolidation, Phase 1):
#   - tokens.css is now GENERATED, not hand-authored. Every leaf's $extensions
#     ["com.pointsav.tokens"].id (see lib_canonical_id.py) becomes its CSS custom
#     property name verbatim -- no translation layer. $value alias references
#     ("{paper.primitive.rule.standard}"-style) become `var(--the-referenced-id)`,
#     preserving the token composition relationship in the emitted CSS rather than
#     flattening everything to literals.
#   - NOTE on backward compatibility, checked directly rather than assumed: neither
#     this repo's own dist/tokens.css nor dtcg-vault/exports/tokens.css is loaded by
#     any live page -- app-privategit-design serves its OWN separately-maintained
#     static/tokens.css (--cds-* names, a hand-kept "theme skin" manually reconciled
#     to these same primitives, not a build output of this generator). So there is no
#     real runtime consumer of this file's old --ps-<group>-<name> var names to break,
#     and no legacy-alias block is emitted. The only old-name references found are
#     prose in this repo's own component recipe.json/guide.md docs -- a documentation
#     consistency cleanup, tracked separately, not a live-breakage risk.
#   - token-families.json: family registry (list_token_families()'s data source).
#   - tokens.manifest.json: content hash of the sources (mtime already proved
#     misleading once this session -- a stale export had a recent mtime).
#   - org-chart tiers folded in as first-class sources (previously: absent from this
#     repo's own export entirely, spliced in only at deploy time).

import hashlib
import json
import re
import sys
from pathlib import Path

# A real DTCG alias reference is exactly {dotted.path.of.identifier-segments} -- no
# spaces, commas, or nested braces, and (every real alias in this vault, checked)
# ALWAYS contains at least one dot, since it's a hierarchical path reference (e.g.
# "color.neutral-100", "paper.primitive.rule.standard"). Two real false positives
# found by running this against the actual vault, not assumed: writing/semantic.json
# has both a comma-separated fill-in template ("{role}, {entity}, {address}, {email},
# {phone}") and single-word camelCase page-title placeholders ("{siteDisplayName}",
# "{pageTitle} — {siteDisplayName}") -- writer-facing format strings, not token
# aliases. Requiring a literal dot excludes all of these while still matching every
# real alias.
ALIAS_PATTERN = re.compile(r"^\{[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+\}$")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_canonical_id import EXTENSION_NAMESPACE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "dtcg-vault"
GENERATOR_VERSION = 2

SOURCE_FILES = [
    VAULT / "tokens" / "primitive.json",
    VAULT / "themes" / "pointsav-brand.json",
    VAULT / "paper" / "primitive.json",
    VAULT / "paper" / "semantic.json",
    VAULT / "writing" / "primitive.json",
    VAULT / "writing" / "semantic.json",
    VAULT / "tokens" / "finance.tokens.json",
    ROOT / "tokens" / "tokens-woodfine-org-chart-extended.json",
]


def load(path):
    return json.loads(path.read_text())


def build_paper():
    prim = load(VAULT / "paper" / "primitive.json")
    sem = load(VAULT / "paper" / "semantic.json")
    paper = {}
    paper.update(prim["paper"])
    paper.update(sem["paper"])
    paper["$description"] = (
        "Paper pillar — print/document-formatting tokens. "
        f"Primitive layer: {prim['$description']} "
        f"Semantic layer: {sem['$description']}"
    )
    return paper


def build_writing():
    prim = load(VAULT / "writing" / "primitive.json")
    sem = load(VAULT / "writing" / "semantic.json")
    writing = {}
    writing.update(prim["writing"])
    writing.update(sem["writing"])
    writing["$description"] = (
        "Writing pillar — content/voice tokens. "
        f"Primitive layer: {prim['$description']} "
        f"Semantic layer: {sem['$description']}"
    )
    return writing


def build_orgchart():
    ext = load(ROOT / "tokens" / "tokens-woodfine-org-chart-extended.json")
    return ext["ibm-carbon-org-chart"], ext["org-chart-extended"]


def build_export():
    ibm_carbon, org_extended = build_orgchart()
    return {
        "primitive": load(VAULT / "tokens" / "primitive.json"),
        "theme": load(VAULT / "themes" / "pointsav-brand.json"),
        "paper": build_paper(),
        "writing": build_writing(),
        "wcp": load(VAULT / "tokens" / "finance.tokens.json")["wcp"],
        "ibm-carbon-org-chart": ibm_carbon,
        "org-chart-extended": org_extended,
    }


def collect_leaves(export):
    """Walk the full export tree; return (leaves, alias_index).
    leaves: list of (canonical_id, dtcg_path, value_raw, pillar, layer, family)
    alias_index: dtcg_path -> canonical_id, for resolving {a.b.c}-style $value refs."""
    leaves = []
    alias_index = {}

    def walk(node, dtcg_path):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            ext = node.get("$extensions", {}).get(EXTENSION_NAMESPACE)
            if ext is None:
                raise SystemExit(
                    f"FATAL: leaf at {dtcg_path} has no canonical $extensions -- "
                    "run migrate-canonical-ids.py"
                )
            leaves.append(
                (ext["id"], dtcg_path, node["$value"], ext["pillar"], ext["layer"], ext["family"])
            )
            alias_index[dtcg_path] = ext["id"]
            # primitive.json's own top-level keys (color, size, ...) have no tier
            # wrapper, so OTHER files reference its leaves with the tier prefix
            # dropped -- e.g. pointsav-brand.json's theme aliases use "{color.
            # neutral-100}", not "{primitive.color.neutral-100}". Register both
            # forms. No collision risk: theme/writing/paper have no "color" group
            # of their own to shadow this with.
            if ext["pillar"] == "primitive":
                bare_path = dtcg_path.removeprefix("primitive.")
                alias_index[bare_path] = ext["id"]
            return
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, f"{dtcg_path}.{k}")

    for tier_name, tier_val in export.items():
        if tier_name.startswith("$"):
            continue
        walk(tier_val, tier_name)

    return leaves, alias_index


def resolve_css_value(value_raw, alias_index):
    """A DTCG $value is either a literal (str/number) or an alias reference like
    "{paper.primitive.rule.standard}". Aliases become var(--the-referenced-canonical-id)
    so the CSS preserves the same composition relationship the JSON has."""
    if isinstance(value_raw, str) and ALIAS_PATTERN.match(value_raw):
        ref_path = value_raw[1:-1]
        target_id = alias_index.get(ref_path)
        if target_id is None:
            raise SystemExit(f"FATAL: alias reference {value_raw!r} does not resolve to any known leaf")
        return f"var({target_id})"
    if isinstance(value_raw, (str, int, float)):
        return str(value_raw)
    # Typography/other composite $value objects have no CSS custom-property shorthand
    # -- skip, these remain JSON-only (read via tokens.full.json / get_token).
    return None


def emit_css(leaves, alias_index):
    lines = [
        "/* GENERATED FILE -- do not hand-edit. Source: dtcg-vault/{tokens,themes,paper,writing}",
        "   + tokens/tokens-woodfine-org-chart-extended.json, produced by bin/generate-tokens-export.py.",
        "   Every custom property name below is a leaf token's canonical id",
        "   ($extensions['com.pointsav.tokens'].id) -- byte-identical to what MCP get_token",
        "   matches on and to the token's own DTCG $extensions id. No translation layer. */",
        ":root {",
    ]
    dark_lines = []
    skipped_composites = 0
    for token_id, dtcg_path, value_raw, pillar, layer, family in leaves:
        css_value = resolve_css_value(value_raw, alias_index)
        if css_value is None:
            skipped_composites += 1
            continue
        target = dark_lines if dtcg_path.startswith("theme.dark") else lines
        target.append(f"  {token_id}: {css_value};")
    lines.append("}")
    if dark_lines:
        lines.append('[data-theme="dark"] {')
        lines.extend(dark_lines)
        lines.append("}")
    if skipped_composites:
        lines.insert(
            5,
            f"/* {skipped_composites} typography/composite leaves are JSON-only (no CSS "
            "shorthand exists) -- read via tokens.full.json or get_token, not this file. */",
        )
    return "\n".join(lines) + "\n"


def build_families(leaves):
    families = {}
    for token_id, dtcg_path, value_raw, pillar, layer, family in leaves:
        if family is None:
            continue
        key = (pillar, layer, family)
        if key not in families:
            families[key] = {"pillar": pillar, "layer": layer, "family": family, "member_count": 0}
        families[key]["member_count"] += 1
    return sorted(families.values(), key=lambda f: (f["pillar"], f["layer"] or "", f["family"]))


def content_hash(export):
    # Canonicalize: sorted keys, no whitespace variance -- a hash over the export's own
    # serialized form so it reflects exactly what downstream consumers see, and changes
    # iff a served value changes.
    canon = json.dumps(export, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main():
    export = build_export()
    leaves, alias_index = collect_leaves(export)

    exports_dir = VAULT / "exports"
    exports_dir.mkdir(exist_ok=True)

    (exports_dir / "tokens.full.json").write_text(
        json.dumps(export, indent=2, ensure_ascii=False) + "\n"
    )

    (exports_dir / "tokens.css").write_text(emit_css(leaves, alias_index))

    families = build_families(leaves)
    (exports_dir / "token-families.json").write_text(
        json.dumps({"families": families}, indent=2, ensure_ascii=False) + "\n"
    )

    manifest = {
        "generatorVersion": GENERATOR_VERSION,
        "leafCount": len(leaves),
        "familyCount": len(families),
        "contentHash": content_hash(export),
        "generatedFrom": sorted(str(p.relative_to(ROOT)) for p in SOURCE_FILES),
    }
    (exports_dir / "tokens.manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    )

    print(f"Wrote {exports_dir}/tokens.full.json ({len(leaves)} leaves)")
    print(f"Wrote {exports_dir}/tokens.css")
    print(f"Wrote {exports_dir}/token-families.json ({len(families)} families)")
    print(f"Wrote {exports_dir}/tokens.manifest.json (hash {manifest['contentHash'][:12]}...)")


if __name__ == "__main__":
    main()
