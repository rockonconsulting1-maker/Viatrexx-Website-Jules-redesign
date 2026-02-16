# Design Memory

## Discoveries
- The site is an HTTrack mirror of a LeadConnector (GoHighLevel) site.
- `index.html` and other pages contain multiple nested `<html>` and `<body>` tags due to "custom code" blocks.
- Multiple versions of Font Awesome (5.15.4, 6.0.0) and Tailwind are being loaded.
- Styles are scattered across multiple `<style>` blocks, some in `<head>`, some in `<body>`.
- The header and footer are duplicated across all main HTML files.

## Guidelines
- Extract common components to `src/partials/`.
- Move CSS to `src/styles/`.
- Standardize on Font Awesome 6.x where possible.
- Use root-relative paths for assets in shared components.
