# MEMO 02: Neurodiversity & Typographic Standards

**TARGET AUDIENCE:** UI/UX Contributors
**STANDARD:** WCAG 2.2 / Institutional Accessibility

## 1. System UI Fonts
We bypass external font requests (e.g., Google Fonts) to prevent layout shifts and network latency. The CSS font stack must strictly utilize native operating system fonts: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.

## 2. Cognitive Load Reduction
To accommodate neurodivergent readers (dyslexia, astigmatism) processing dense financial and technical disclosures:
* **Strict Left Alignment:** Text must remain left-aligned (ragged right). The CSS rule `text-align: justify;` is strictly forbidden as it creates erratic visual rivers of white space.
* **Line Height:** Must be locked between `1.6` and `1.8`.
* **Orphan Control:** Utilize `text-wrap: pretty` where supported by modern CSS Level 4 rendering engines.

## 3. Fluid Typography & Touch Targets
* **Font Scaling:** Typography must utilize the CSS `clamp()` function to scale mathematically across mobile, tablet, and desktop viewports without relying on rigid media query breakpoints.
* **Hit Areas:** All interactive elements (toggles, PDF links) must maintain a minimum 44x44 pixel physical boundary to prevent input errors on mobile devices.

## 4. The Institutional Print Engine
A `@media print` CSS block is mandatory. When a user executes a print command, the browser must instantly format the DOM into a physical white paper: removing navigation buttons, stripping backgrounds, and applying 1-inch margins for hardware printers or local PDF engines.
