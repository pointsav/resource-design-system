# MEMO-04: Offline Print & PDF Typography
### *SIL Open Font License (OFL) Compliance & Brand Identity*

**Status: Active** | **Applies to: Offline PDF / Print Generators**
**Dependency:** `fleet-woodfine/woodfine-media-assets/tokens-typography-brand.yaml`

---

## 1. The Execution Boundary
To maintain Zero-Execution presentation state and absolute minimum latency, web interfaces strictly utilize native System UI fonts per **DS-ADR-07**. 

Brand Typography is strictly reserved for **Offline Print & PDF Disclosure Generation**. These fonts are embedded directly into physical PDF binaries during the `service-content` compilation phase to project institutional authority.

## 2. The OFL Typography Matrix
To guarantee Digital Asset Resolution Package (DARP) compliance, all proprietary vendor fonts have been replaced with 100% SIL Open Font License (OFL) equivalents. The physical `.ttf` binaries are securely air-gapped within the `woodfine-media-assets/fonts` vault.

### A. Formal Serif (The Caecilia Replacement)
* **Token:** `serif_primary`
* **Active Font:** **Zilla Slab**
* **Legacy Target:** Caecilia LT Std (Light, Roman)
* **Aesthetic:** Humanist Slab Serif.
* **Execution:** Utilized for high-level institutional trust. Applied to white paper covers, legal block headers, and primary formal document titles.

### B. High-Density Data (The Trade Gothic Replacement)
* **Token:** `sans_condensed`
* **Active Font:** **Barlow Condensed**
* **Legacy Target:** Trade Gothic LT Std Cn
* **Aesthetic:** Grotesque Sans-Serif Condensed. Industrial, structural, and mechanical.
* **Execution:** Utilized for mathematical precision. Applied strictly to financial ledgers, dense data tables, and capitalized micro-headers where horizontal space is constrained.

### C. Body Copy (The Avenir Replacement)
* **Token:** `sans_primary`
* **Active Font:** **Nunito Sans**
* **Legacy Target:** Avenir LT Std
* **Aesthetic:** Geometric Sans-Serif with humanist readable touches.
* **Execution:** The workhorse of the offline engine. Utilized for all standard paragraph body copy, corporate memos, and operational text.

### D. Editorial Serif (Native OFL)
* **Token:** `serif_secondary`
* **Active Font:** **Sahitya**
* **Execution:** Utilized as a high-contrast fallback for editorial pull-quotes or secondary aesthetic markers.

---
*© 2026 PointSav Digital Systems™ | Architecture & Design Protocols*
