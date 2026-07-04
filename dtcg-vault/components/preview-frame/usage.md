# When to use Preview Frame

Use a preview frame to show a component's rendered output inside a bordered
canvas with a light/dark theme toggle in the toolbar — the way this
substrate's own `/components/*` pages show a live rendering of each
component's variants. It answers "what does this actually look like" without
requiring the reader to run code or open a separate tool.

## When to use

- Component documentation pages — the standard way this substrate shows a
  recipe's real rendered variants rather than a static screenshot.
- Anywhere a reader needs to compare how a piece of UI looks in both light
  and dark theme without switching the whole page's theme.
- Design-review surfaces where a reviewer flips between themes to check
  contrast and token behaviour on the same rendered content.

## When not to use

- Don't use a preview frame as a substitute for the component's own real
  container in production — it is a documentation/review affordance, not a
  layout primitive.
- Don't nest a preview frame inside another preview frame; the toggle
  toolbar assumes it is theming its own direct `.ps-preview__canvas`
  content, not another interactive frame.
- If the content needs to demonstrate live data or user interaction beyond a
  static rendered state, pair it with the actual component in a live
  sandbox rather than relying on the frame's own toggle alone.
