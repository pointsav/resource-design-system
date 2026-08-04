# When to use Tab

Use tabs to navigate between related views of the same subject —
the canonical example is the substrate's own component pages
(Usage / Style / Code / Accessibility tabs you're using right now).

The substrate's pattern is **URL-reflected**, not in-page state.
Each tab is a real `<a href>` link to a separate route. This
diverges from many tab libraries that hold state only in
client memory; the URL pattern is the canonical answer because:

- **Deep-linking works.** A user can share `/components/button/style/`
  and the recipient lands on the right tab without JS hydration.
- **Back/forward navigate naturally.** Browser history is the
  state container.
- **Crawlers, screen readers, MCP agents see all tabs.** Each tab
  is a discoverable URL on its own.
- **No JavaScript required for navigation.** Pages work with JS
  disabled.

## When to use

- 2–6 related views of the same subject.
- View switches that should be deep-linkable.
- Component documentation, settings panes, multi-step views where
  each step is a coherent surface.

## When not to use

- More than 6 views: redesign as a sidebar nav.
- Sequential workflow with progression: use a wizard pattern.
- View toggles that are temporary and don't need URL state: use
  a segmented control.

## URL-reflected = state-canonical

Tabs that hold state only in client memory are an architectural
choice that breaks the substrate's source-of-truth invariant.
Don't replicate that pattern.
