# Experience Agent Memory

## Core Principles
- Accessibility: Focus on keyboard navigation and ARIA attributes.
- Mobile First: Ensure top banners and headers don't clash.
- Performance: Identify and fix layout shifts and slow interactions.

## Known Issues
- HTTrack mirror results in multiple `<html>`, `<head>`, and `<body>` tags in a single file.
- Redundant `home.html` and `index.html`.
- `href="#"` used in dropdowns causing layout jumps.
- Missing `aria-current="page"` on active navigation links.
- Focus rings are often missing or inconsistent.

## Key Assets
- Main Navigation: Header `desktop-nav` and `mobile-menu`.
- Language Dropdown: Top banner.
