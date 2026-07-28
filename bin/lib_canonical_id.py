#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Woodfine Capital Projects Inc.
#
# Canonical token identifier derivation — shared by migrate-canonical-ids.py and
# generate-tokens-export.py so there is exactly one place the id/pillar/layer/family
# rule lives. Do not duplicate this logic elsewhere.
#
# Grammar: --ps-<pillar>-<path-segments...>
#   - pillar is the top-level tier (primitive, theme, paper, writing, orgchart).
#   - path-segments are the real DTCG object keys from the tier root to the leaf,
#     already lowercase-kebab (this repo's own convention) -- joined verbatim, no
#     re-casing, no re-delimiting. This is why a translation layer between the DTCG
#     path and the CSS var was the root cause of get_token's false negatives: this id
#     IS the css var, not a source you transform into one.
#   - layer/family are metadata (carried in $extensions, not part of the id string):
#     for paper/writing, the JSON genuinely nests under a primitive/semantic wrapper,
#     so layer = first path segment, family = second. primitive/theme have no such
#     wrapper -- their first path segment (color, size, tenant, semantic, dark, ...)
#     is the most useful grouping available, used as family with layer left unset.
#
# EXTENSION_NAMESPACE is a DTCG-sanctioned vendor-metadata key (reverse-DNS, per the
# 2025-10 draft spec's $extensions mechanism) -- never invent a second namespace.
EXTENSION_NAMESPACE = "com.pointsav.tokens"
SCHEMA_VERSION = 1

# Tiers whose JSON genuinely nests under a primitive/semantic wrapper before the real
# groups. Everything else (primitive, theme, orgchart) does not.
LAYERED_PILLARS = {"paper", "writing"}


def derive(pillar: str, path_segments: list[str]) -> dict:
    """Compute the canonical $extensions block for one leaf token.

    pillar: the tier name (primitive/theme/paper/writing/orgchart).
    path_segments: the real JSON keys from the tier root to this leaf, in order,
        already excluding any $-prefixed keys. Must be non-empty.
    """
    if not path_segments:
        raise ValueError(f"empty path_segments for pillar={pillar!r}")

    token_id = "--ps-" + "-".join([pillar, *path_segments])

    layer = None
    family = None
    if pillar in LAYERED_PILLARS and path_segments[0] in ("primitive", "semantic"):
        layer = path_segments[0]
        if len(path_segments) > 1:
            family = path_segments[1]
    else:
        family = path_segments[0]

    return {
        "id": token_id,
        "pillar": pillar,
        "layer": layer,
        "family": family,
        "schemaVersion": SCHEMA_VERSION,
    }


def stamp_extensions(leaf: dict, pillar: str, path_segments: list[str]) -> dict:
    """Return a new leaf dict (shallow copy) with the canonical $extensions block
    set/overwritten. Never mutates the input in place -- callers own their own
    copy-on-write discipline against the loaded JSON tree."""
    block = derive(pillar, path_segments)
    out = dict(leaf)
    extensions = dict(out.get("$extensions", {}))
    extensions[EXTENSION_NAMESPACE] = block
    out["$extensions"] = extensions
    return out


def family_block(pillar: str, path_segments: list[str]) -> dict:
    """$extensions block for a FAMILY node (one level above the leaves) -- same
    pillar/layer/family fields, no id (families aren't individually addressable
    tokens, list_token_families() reads this instead)."""
    d = derive(pillar, path_segments)
    d.pop("id")
    return {EXTENSION_NAMESPACE: d}
