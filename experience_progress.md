# Experience Progress

## Day 1: 2025-01-31

### Findings
- Assets in `index.html` have incorrect `../` prefixes.
- Navigation lacks ARIA attributes.
- Language dropdown uses `href="#"` which causes page jumps.

### Changes
- Initialized documentation files.
- Fixed relative links in `index.html` by removing incorrect `../` prefixes for root-level assets.
- Added `aria-current="page"` to Home navigation links in `index.html`.
- Added `aria-label` to mobile menu close button and footer social links.
- Replaced `href="#"` with `href="javascript:void(0)"` in the language dropdown to prevent unwanted page jumps.
- Implemented global focus styles to ensure keyboard focus is clearly visible on all interactive elements.
