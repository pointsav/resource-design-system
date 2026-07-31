---
schema: foundry-design-research-v1
component_or_token: workplace-shell-chrome
decision_type: architecture-decision
authored: 2026-07-30
authored_by: totebox@project-design
status: ratified
source: DESIGN-RESEARCH-workplace-shell-chrome.draft.md (totebox@project-workplace, 2026-07-13)
ai_consumption_hint: "Decision record for a proposed shared app-workplace-* chrome crate.
  No crate exists yet -- this file ratifies the case for building it and the concrete shape
  (two crates, not one), but the actual Rust extraction is project-workplace's own follow-up,
  not done here."
---

# A shared chrome component for the app-workplace-* family — decision (2026-07-30)

## Decision — build it now, as two crates, plain lib style

**Yes, worth building now — do not wait for a third duplicated pattern.** The evidence
below is not one duplicated thing found twice; it is three separate duplicated things
(the get/set/has-config IPC triad, the error-state markup convention, and the
`tauri.conf.json` boilerplate/copy-paste drift) found independently across the same two
apps, plus a proven sibling precedent (`app-mediakit-shell`) that this pattern generalizes
well once extracted. Waiting compounds the cost: every app that ships before extraction is
retrofitting work later, and this session alone took two apps (gis, pdf) from empty stub to
first Rust code — the family is actively growing, not static.

**Split into two crates, not one**, per the research's own open question #1 — the
WebView-over-local-HTTP-server rendering model (workbench, and presumably memo/proforma/
presentation, which load a bundled local document) is a genuinely different shape from the
native-canvas model (gis's MapLibre canvas, pdf's PDFium render surface). Forcing both into
one shared abstraction risks the same mismatch a single uniform icon mark would have caused
for this family (see the companion `app-workplace-icon-family-decision.md` — differentiated
where the underlying thing genuinely differs, shared where it doesn't). The get/set/
has-config triad, error-state markup, and `tauri.conf.json` scaffold defaults are common to
both crates' consumers regardless of rendering model — those belong in whichever of the two
crates (or a small shared base both depend on) makes sense once project-workplace scopes the
actual code.

**Plain internal lib crate, not a `moonshot-*` full-stack-ownership target** — matching the
`app-mediakit-shell` precedent exactly (open question #3 in the source draft). Workplace's
own convention leans harder into full-stack ownership than mediakit's, but there's no
third-party dependency being replaced here — this is internal shared chrome, the same shape
mediakit already solved successfully as a plain lib crate.

## What this doesn't decide

- The exact crate name(s), directory placement, or API surface — that's project-workplace's
  own design pass once they pick this up.
- Sequencing against `BRIEF-workplace-workbench.md`'s consolidation-engine work (open
  question #2 in the source draft) — left as project-workplace's own call, not a
  project-design concern.
- Tauri v1.7→v2 migration standardization (open question #3, numbering collision with the
  above in the source draft's own list) — a reasonable thing for the shared crate(s) to
  eventually own, but not required for the initial extraction.
- The actual Rust code. This file ratifies the decision to build; it does not build it.

## Original research (verbatim from the source draft)

### Context

`project-workplace` owns seven Tauri desktop apps under one product family
(`app-workplace-workbench`, `-presentation`, `-memo`, `-proforma`, `-gis`, `-pdf`,
`-bim`), each an independent `src-tauri/` crate with its own `Cargo.toml`,
`tauri.conf.json`, and hand-rolled frontend (`src/index.html` + `src/app.js` or
equivalent) — no shared frontend crate or chrome component exists between them
today. This is the same shape of problem `app-mediakit-shell` was built to solve
for the `app-mediakit-*` family: a lib crate providing shared chrome (maud
header/footer, typed `Section` vocabulary, DTCG token loading), framework-agnostic,
consumed by `app-mediakit-marketing` (see project-workplace's own
`.agent/rules/project-registry.md`, App — MediaKit surface table).

This session touched six of the seven app-workplace-* apps directly (workbench,
presentation, memo, proforma, gis, pdf — bim remains untouched, Reserved-folder,
no code) and found the same first-run-configuration / error-state / IPC-command
shape reimplemented independently in at least two of them, verified directly in
source rather than assumed.

### Evidence — concrete duplication found this session

**1. Parallel "get/set/has-config" IPC command triads**

`app-workplace-workbench/src-tauri/src/main.rs`:
```
fn get_workbench_url(app_handle: tauri::AppHandle) -> String
fn set_workbench_port(app_handle: tauri::AppHandle, port: u16) -> Result<(), String>
fn has_workbench_config(app_handle: tauri::AppHandle) -> bool
```

`app-workplace-gis/src-tauri/src/main.rs`:
```
fn get_tile_endpoint(app_handle: tauri::AppHandle) -> String
fn set_tile_endpoint(app_handle: tauri::AppHandle, endpoint: String) -> Result<(), String>
fn has_gis_config(app_handle: tauri::AppHandle) -> bool
```

Both apps independently arrived at the identical `get_X` / `set_X` / `has_X_config`
IPC triad for "is there a saved endpoint/port; if not, show first-run config; let
the user set one; persist it to `$APPDATA`." Same shape, two hand-written
implementations, zero shared code.

**2. Parallel first-run / error-state frontend markup**

`app-workplace-workbench/src/index.html` uses an `.error-icon` / `.error-detail`
CSS pair to render an unreachable-server state (`⚠` + `${url} — ${detail}`).
`app-workplace-gis/src/app.js` independently uses an `.error-detail` class for the
same purpose (file-load error, tile-endpoint error) and additionally handles
MapLibre's own `map.on('error', ...)` event to surface "tile load error — check
endpoint" directly in the endpoint label when the configured tile source is
unreachable. Different apps, same "surface a connection/load failure inline near
the offending control" instinct, independently coded twice.

**3. Every app repeats the same Tauri v1.7 boilerplate**

All six code-bearing apps carry near-identical `tauri.conf.json` boilerplate:
`macOS.minimumSystemVersion: "10.13"`, `updater.active: false`,
`withGlobalTauri: true`, the same `beforeDevCommand`/`devPath`/`distDir` shape, and
copy-pasted `_notes` blocks — including a "copy icons from
app-workplace-memo/src-tauri/icons/" instruction repeated verbatim in workbench's,
gis's, and pdf's `tauri.conf.json`, even though memo itself has no committed icons
to copy (see the companion `asset-app-workplace-icons-v1` draft /
`app-workplace-icon-family-decision.md`). A shared chrome/scaffold crate is also
the natural place to fix that kind of copy-paste drift once, instead of
independently in each `tauri.conf.json`.

**4. Precedent already proven in a sibling surface**

`app-mediakit-shell` already plays exactly this role for `app-mediakit-*`: shared
chrome chassis, lib crate, framework-agnostic, consumed by `app-mediakit-marketing`,
adoption by sibling apps planned/underway. It shipped as a generalizable pattern
once, then sibling apps in the same family adopted it. The workplace family has not
yet done the equivalent, and — per the duplication findings above — is now actively
growing the amount of code that would need retrofitting later if a shared crate
lands after more apps ship.

### What a `workplace-shell` (or similarly named) crate could own

- A first-run endpoint/port configuration dialog component (generalizing the
  `get_X`/`set_X`/`has_X_config` triad into one typed Rust helper + one shared
  frontend widget), parameterized per-app by label/placeholder/validation rule
  (port number vs. URL).
- A shared error/unreachable-state presentation (the `.error-icon`/`.error-detail`
  pattern), so future apps get it for free instead of re-deriving the CSS class
  names and markup shape.
- A common window-title / connection-status convention.
- Shared Tauri v1.7 `tauri.conf.json` scaffold defaults (minimumSystemVersion,
  updater, withGlobalTauri, CSP skeleton) generated once rather than copy-pasted
  per app, closing the copy-paste drift found in finding 3 above.

## Research trail

### Done (4, from the original draft)
1. Read every code-bearing app-workplace-* app's `src-tauri/src/main.rs` IPC
   command signatures directly (not assumed) — confirmed the get/set/has-config
   triad duplication between workbench and gis with exact function names.
2. Read `app-workplace-workbench/src/index.html` and `app-workplace-gis/src/app.js`
   directly — confirmed the `.error-detail` class and unreachable-state handling
   duplication with exact line references.
3. Read `tauri.conf.json` `_notes` blocks across all six code-bearing apps —
   confirmed the "copy icons from app-workplace-memo" instruction is repeated
   verbatim in three apps' config files despite memo having nothing to copy.
4. Read project-workplace's `.agent/rules/project-registry.md` App — MediaKit
   surface table for the `app-mediakit-shell` precedent description (role,
   consumers, adoption status).

### Done (1, added at landing, 2026-07-30)
5. Cross-checked this decision against the same session's app-workplace icon
   family decision (differentiated-family, shared-treatment pattern) — confirmed
   the two-crate split (WebView-shell vs. native-canvas) follows the same
   "share what's genuinely shared, differentiate what genuinely differs"
   principle, not a coincidence of two unrelated calls landing the same day.

### Open questions (2, carried forward — not resolved here)
1. Timing beyond "now": whether presentation's and proforma's still-partial
   feature work (slide canvas, spreadsheet engine) surfaces a third duplicated
   pattern worth generalizing in the same extraction pass — project-workplace's
   own call once they scope the actual crates.
2. Sequencing against `BRIEF-workplace-workbench.md`'s consolidation-engine work
   — project-workplace's own call, not resolved here.
