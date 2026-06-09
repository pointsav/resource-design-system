# Design Research — Workplace Token Foundation (wp-*)

**Source:** DESIGN-TOKEN-CHANGE-wp-tokens-20260602.draft.md (totebox@project-workplace, 2026-06-02)
**Language protocol:** DESIGN-TOKEN-CHANGE
**Source commit:** 6ae5e97c (app-workplace-http-prototype/src/assets/style.css)
**master_cosign:** command@claude-code 2026-06-02
**ai_consumption_hint:** 27 design tokens in the --wp-* namespace for the app-workplace-* product family. Graphite bronze accent (#c89a4a), dark charcoal surface palette, 13px type base (VS Code-aligned), 4px spacing grid, 6-level z-index map. No existing consumers; zero migration burden. Tauri Wave 1 apps (app-workplace-memo, app-workplace-presentation, app-workplace-workbench) will consume these tokens at the native-parity pass.

---

## Design rationale

The `--wp-*` namespace establishes the token foundation for the `app-workplace-*`
product family: a professional AEC and construction desktop suite built on Tauri.

**Surface palette — dark charcoal:** Four-stop background scale from #1a1a1a (base) to
#333333 (overlay). Dark shell is appropriate for construction and AEC workflows where
users spend long hours in the application; reduces eye fatigue in site-office lighting
conditions. Deliberately neutral — avoids the blue-tinted darks of developer tooling.

**Accent — graphite bronze (#c89a4a):** Replaces the VS Code–derived `#007acc` blue.
Bronze is warm, material, and professional — connotes construction materials (metal,
timber) rather than software developer culture. It is visually distinct from productivity
suites (blue/green) and developer tooling (blue/purple). The "bronze rail" active-surface
indicator (`box-shadow: inset 0 3px 0 0 var(--wp-accent)`) is the primary affordance
distinguishing the active surface from inactive surfaces.

**Type scale — 13px base:** Matches VS Code and professional desktop IDEs — the
established legibility floor for information-dense tooling interfaces. Six steps
(11px–18px) provide adequate differentiation between label, body, and heading sizes
without requiring large display sizes.

**Spacing — 4px grid:** Base unit 4px; 7 named stops (4px–48px) following 1×/2×/3×/4×/6×/8×/12×
multiples. Covers all common layout distances without fractional values.

**Z-index map:** Six named levels prevent z-index collision across independently developed
surface modules. Gaps are intentional for surface-specific internal stacking.

---

## Downstream impact

- **Consumers at intake date:** app-workplace-http-prototype/src/assets/style.css only (prototype).
- **Planned consumers:** app-workplace-memo, app-workplace-presentation, app-workplace-workbench
  (Tauri Wave 1 native-parity pass; no timeline committed).
- **Migration burden:** Zero. No existing consumers to update.
- **Namespace collision risk:** None. `--wp-*` prefix is reserved for this family; no other
  token family in the design system uses `wp` prefix.
