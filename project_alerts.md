# Project Alerts

## 2026-02-11 - Medium: Hardcoded Google API Key (Security)
A hardcoded Google API key was found in multiple mirrored HTML files. This key is being obfuscated to prevent abuse.

## 2026-02-11 - High: Broken Links / Missing Assets (Content)
Assets were referenced with incorrect `../` prefixes in `home.html` and `index.html`.
*Update 2026-02-12:* Optimization and Experience agents have addressed this in `index.html` and `home.html`. A global search and replace for other pages is recommended.

## 2026-02-12 - SEO / Navigation Update (Experience/Optimization)
- Fixed systemic broken asset paths in `index.html` and `home.html`.
- Systematic path error confirmed: files in root use `../` (incorrect), and files in subdirectories (e.g., `product-details/`) use `../../` (incorrect). Both should be reduced by one `../` level.
- Improved link integrity by ensuring all internal navigation points to valid local files.
- Added `rel="noopener noreferrer"` to external links.
