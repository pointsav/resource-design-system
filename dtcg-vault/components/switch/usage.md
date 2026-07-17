# When to use Switch

Use a switch for reversible binary settings that take effect
immediately — "Notifications", "Dark mode", "Show archived
records". The visual semantics communicate "this is live" in a
way a checkbox does not.

## When to use

- Settings panels: notifications, accessibility preferences,
  data filters, view modes.
- Per-row toggles in admin tables — feature flags, account
  enable/disable.

## When not to use

- Choices that submit later (form context): use a checkbox.
- Choices with three or more states (off / on / partial): use a
  segmented control or radio group.
- Destructive toggles: pair the switch with a confirmation step.
  An accidental toggle that deletes data is an anti-pattern.

## Status feedback

Switches that drive remote state should pair with a
[notification](/components/notification/usage) confirming
success or surfacing failure. Optimistic UI (flip immediately,
revert on error) is the common pattern; the failure-revert path
must communicate why.
