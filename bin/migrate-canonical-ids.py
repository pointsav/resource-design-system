#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Woodfine Capital Projects Inc.
#
# One-time migration: stamps the canonical $extensions["com.pointsav.tokens"] block
# (see lib_canonical_id.py) onto every leaf token in the 4 pillar source files. Safe
# to re-run -- idempotent, and re-derives/overwrites rather than trusting any existing
# $extensions block, so a hand-edited id can never silently drift from what the real
# derivation rule would produce.
#
# Hard invariants enforced below (fails loudly, never silently drops a token):
#   - leaf count unchanged before/after, per file
#   - every derived id is globally unique across the whole run
#   - every $value leaf receives a non-empty id
#
# $value aliases ({paper.primitive.rule.standard}-style references) are untouched --
# this migration only ever adds/overwrites $extensions, never touches $value itself.

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_canonical_id import stamp_extensions  # noqa: E402

VAULT = Path(__file__).resolve().parent.parent / "dtcg-vault"

# (pillar, file path, root key to descend into before pillar's own groups start)
# The two org-chart entries share one file (tokens-woodfine-org-chart-extended.json,
# repo-root tokens/ -- not dtcg-vault/) with two independent top-level roots; processed
# sequentially, each write is read back by the next entry, so neither clobbers the other.
ORG_CHART_SRC = VAULT.parent / "tokens" / "tokens-woodfine-org-chart-extended.json"
SOURCES = [
    ("primitive", VAULT / "tokens" / "primitive.json", None),
    ("theme", VAULT / "themes" / "pointsav-brand.json", None),
    ("paper", VAULT / "paper" / "primitive.json", "paper"),
    ("paper", VAULT / "paper" / "semantic.json", "paper"),
    ("writing", VAULT / "writing" / "primitive.json", "writing"),
    ("writing", VAULT / "writing" / "semantic.json", "writing"),
    ("wcp", VAULT / "tokens" / "finance.tokens.json", "wcp"),
    ("ibm-carbon-org-chart", ORG_CHART_SRC, "ibm-carbon-org-chart"),
    ("org-chart-extended", ORG_CHART_SRC, "org-chart-extended"),
]


def count_leaves(node):
    if not isinstance(node, dict):
        return 0
    if "$value" in node:
        return 1
    return sum(count_leaves(v) for k, v in node.items() if not k.startswith("$"))


def walk_and_stamp(node, pillar, path_segments, ids_seen, stamped_count):
    """Recursively rebuild node, stamping $extensions on every $value leaf.
    Returns the rebuilt node."""
    if not isinstance(node, dict):
        return node

    if "$value" in node:
        new_leaf = stamp_extensions(node, pillar, path_segments)
        new_id = new_leaf["$extensions"]["com.pointsav.tokens"]["id"]
        if not new_id:
            raise SystemExit(f"FATAL: empty id derived for path {path_segments}")
        if new_id in ids_seen:
            raise SystemExit(
                f"FATAL: duplicate canonical id {new_id!r} "
                f"(second occurrence at path {path_segments})"
            )
        ids_seen.add(new_id)
        stamped_count[0] += 1
        return new_leaf

    out = {}
    for k, v in node.items():
        if k.startswith("$"):
            out[k] = v
            continue
        out[k] = walk_and_stamp(v, pillar, [*path_segments, k], ids_seen, stamped_count)
    return out


def main():
    ids_seen = set()
    total_before = 0
    total_after = 0
    changed_files = []

    for pillar, path, root_key in SOURCES:
        data = json.loads(path.read_text())
        # Scope the before/after leaf count to exactly the branch this entry processes
        # -- not the whole file. A file can hold multiple independent root keys (e.g.
        # tokens-woodfine-org-chart-extended.json has both ibm-carbon-org-chart and
        # org-chart-extended as siblings); counting the whole file here would compare
        # "leaves stamped in this branch" against "leaves in every branch", a mismatch
        # this invariant caught immediately when a second sibling root was added.
        scope_before = data[root_key] if root_key is not None else data
        before = count_leaves(scope_before)
        total_before += before

        stamped_count = [0]
        if root_key is not None:
            # paper/writing files: descend into the single top-level root_key first
            # (e.g. {"paper": {...}}), leaves live inside that.
            inner = data[root_key]
            data[root_key] = walk_and_stamp(inner, pillar, [], ids_seen, stamped_count)
        else:
            # primitive/theme files: leaves live directly under the top-level keys
            # (color, size, tenant, semantic, ...) -- no wrapper key to descend past.
            new_data = {}
            for k, v in data.items():
                if k.startswith("$"):
                    new_data[k] = v
                    continue
                new_data[k] = walk_and_stamp(v, pillar, [k], ids_seen, stamped_count)
            data = new_data

        scope_after = data[root_key] if root_key is not None else data
        after = count_leaves(scope_after)
        total_after += after
        if before != after:
            raise SystemExit(
                f"FATAL: leaf count changed for {path} -- before={before} after={after}"
            )
        if stamped_count[0] != after:
            raise SystemExit(
                f"FATAL: stamped {stamped_count[0]} leaves but counted {after} for {path}"
            )

        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        changed_files.append((str(path.relative_to(VAULT.parent)), after))

    if total_before != total_after:
        raise SystemExit(
            f"FATAL: total leaf count changed -- before={total_before} after={total_after}"
        )

    print(f"Stamped canonical ids on {total_after} leaf tokens across {len(SOURCES)} source files:")
    for rel_path, n in changed_files:
        print(f"  {rel_path}: {n} leaves")
    print(f"Total unique canonical ids: {len(ids_seen)} (== total leaves: {len(ids_seen) == total_after})")


if __name__ == "__main__":
    main()
