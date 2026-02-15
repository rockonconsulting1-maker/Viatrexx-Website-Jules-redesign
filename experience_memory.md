# Experience Agent Memory

## General Notes
- The site is an HTTrack mirror.
- Asset paths in root HTML files often have an extra `../` prefix.
- `index.html` and `home.html` are considered "gold standard" reference pages.
- Navigation links often use `href="#"` which causes layout jumps.
- **Mirror Asset Naming**: Some local directories use URL encoding (e.g., `%40` for `@`). Ensure paths in HTML match the actual directory names on disk.

## Accessibility Standards
- Use `aria-current="page"` for active navigation links.
- Use `aria-label` for buttons and social links.
- Global focus ring style: `outline: 2px solid #005fcc; outline-offset: 2px;`.

## UX Pain Points
- Redundant `../` in asset paths.
- `href="#"` in dropdowns/buttons.
- Mobile header z-index and positioning. Ensure `z-index: 1000` for the nav header.
- **Local Validation**: Always use `playwright` or custom scripts to verify that relative paths didn't break asset loading, as it's hard to spot in raw HTML.
