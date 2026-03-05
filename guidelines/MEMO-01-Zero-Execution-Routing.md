# MEMO 01: Zero-Execution Routing & Presentation

**TARGET AUDIENCE:** Frontend Contributors
**STANDARD:** Leapfrog 2030 / DARP Compliance

## 1. The Zero-Execution Mandate
This platform strictly forbids the use of client-side JavaScript for DOM manipulation, language routing, or file serving. The architecture relies entirely on Deterministic Files and CSS Cascades to eliminate attack surfaces and guarantee SOC 3 compliance.

## 2. Bilingual Routing Architecture
We do not use IP-sniffing scripts or conditional server-side redirects to serve alternate languages.
* **Root Directory (`/`):** Contains the default English `index.html`.
* **Language Sub-Directory (`/es/`):** Contains the exact same `index.html` file, but with the HTML `<input type="checkbox" checked>` attribute natively applied.

## 3. The Pure CSS State Machine
Interactive elements (Language Toggles, Dynamic PDF Download Buttons) operate via a hidden CSS checkbox hack.
* The DOM loads all language blocks and button variations simultaneously.
* CSS `display: block` and `display: none` rules are tied to the `:checked` state of the hidden input.
* This creates the illusion of instantaneous Web 2.0 application rendering with zero execution latency.
