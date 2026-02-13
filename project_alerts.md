# Project Alerts - 2026-02-13

## Experience Agent Alerts
- **Link Normalization:** Cleaned up relative paths in `index.html` and `home.html` (removed redundant `../` prefixes). Optimization Agent should verify if these changes affect any canonical URL logic or SEO metadata that might rely on specific relative path depths.
- **ARIA Attributes:** Added `aria-current="page"` and `aria-label`. These are primarily for accessibility but contribute to better semantic structure.
