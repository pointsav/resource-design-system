---
title: Badge — Accessibility
---

# Accessibility

Badges are used to highlight an item's status or for small amounts of information. They are purely visual indicators and must be accessible to screen readers.

## WCAG 2.2 Conformance

| Criteria | Status | Notes |
| :--- | :--- | :--- |
| **1.4.3 Contrast (Minimum)** | Pass | All 5 badge variants meet 4.5:1. **Corrected 2026-07-15**: this line previously claimed a blanket pass that was false for 2 of 5 variants — positive (`support-positive`) computed to 4.33:1 and caution (`support-caution`) to 3.72:1 against their own tinted backgrounds, both real AA failures. Fixed at the token layer (`support-positive`/`support-caution` moved from the `-60` to the `-70` step — positive 7.66:1, caution 6.91:1, both now real passes with margin) rather than documented as an open defect, since an existing, already-defined color-scale step covered the fix. |
| **1.3.1 Info and Relationships** | Pass | Badges use semantic color coding. |

## ARIA Roles

Badges typically do not require specific ARIA roles unless they represent a status change that needs to be announced. In those cases, use `role="status"`.

- Use `aria-label` to provide context if the badge text is ambiguous (e.g., "3" in a badge might need `aria-label="3 notifications"`).
