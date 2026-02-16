# Design Progress - 2026-02-11

## Actions Taken
- Created `src/styles/` and `src/partials/` directories.
- Extracted header, mobile menu, and footer from `index.html` into reusable partials in `src/partials/`.
- Consolidated and cleaned CSS from `index.html` into `src/styles/main.css`.
- Fixed asset paths in `src/styles/main.css` to use relative paths correct for its new location.
- Deduplicated Font Awesome and Tailwind references in `index.html`, standardizing on FA v6.0.0 and a single Tailwind v2.2.19 reference.
- Verified changes with a Playwright visual check and confirmed assets (flags, molecule patterns) load correctly.

## Identified Bloated Tailwind Classes
- The current Tailwind implementation uses a massive pre-compiled CSS file (`tailwind.min.css` is ~2.8MB).
- Many sections use utility classes that are likely unused in the final site, but since we are using a full CDN version, they are all loaded.
- Specific blocks in `index.html` have deeply nested utility classes that could be simplified with custom components.

## Visual Regressions / Improvements
- **Improvement**: Page loads more cleanly with externalized CSS.
- **Improvement**: Redundant library versions removed, reducing network requests.
- **No regressions** identified during visual check.

## Pending Items
- Inject partials back into `index.html` (currently they are just extracted for migration preparation).
- Repeat process for `home.html` and `about.html`.
