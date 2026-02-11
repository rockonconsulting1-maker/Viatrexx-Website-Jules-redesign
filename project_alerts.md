# Project Alerts - Content Audit 2026-02-11

## Broken Links / Missing Assets
The following assets are currently referenced with an incorrect `../` prefix in `home.html` and `index.html`. They exist in the root directory but the paths are broken in the HTML.

### Affected Assets (Examples):
- `../cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css`
- `../storage.googleapis.com/msgsndr/Wv6kWdgCt9mf9ZTVwPw4/media/68055cff29d62943f33635ea.webp`
- Multiple JS files in `../stcdn.leadconnectorhq.com/_preview/`

### Recommendation:
The Experience or Optimization agent should run a global search and replace to remove incorrect `../` prefixes from asset paths in the root HTML files.
