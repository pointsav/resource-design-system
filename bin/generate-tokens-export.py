#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 Woodfine Capital Projects Inc.
#
# Regenerates dtcg-vault/exports/tokens.full.json from the real granular source
# token files (dtcg-vault/tokens/primitive.json, dtcg-vault/themes/pointsav-brand.json,
# dtcg-vault/paper/{primitive,semantic}.json, dtcg-vault/writing/{primitive,semantic}.json).
#
# Added 2026-07-16 (token-completeness audit) — before this script existed,
# tokens.full.json was hand-edited directly with no generator keeping it in sync with
# its own source files. That let 37 real tokens (primitive.viewport.*,
# primitive.typography.wiki-*, theme.dark.*) exist only in the export with no source
# file behind them, and let the export drift out of sync across the vendor/deployment/
# cluster-clone copies of this repo. Run this after editing any source token file,
# before committing tokens.full.json — do not hand-edit tokens.full.json directly again.
#
# Scope: reproduces exactly the 4 tiers (primitive/theme/paper/writing) this repo's own
# source files define. Does NOT touch the ibm-carbon-org-chart/org-chart-extended tiers
# — those are merged in at deploy time from a separate root-level extension file by
# /srv/foundry/bin/sync-design-tokens.sh, a Command-Session-owned step outside this
# repo's own build.

import json
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent / "dtcg-vault"


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


def main():
    export = {
        "primitive": load(VAULT / "tokens" / "primitive.json"),
        "theme": load(VAULT / "themes" / "pointsav-brand.json"),
        "paper": build_paper(),
        "writing": build_writing(),
    }

    out_path = VAULT / "exports" / "tokens.full.json"
    out_path.write_text(json.dumps(export, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
