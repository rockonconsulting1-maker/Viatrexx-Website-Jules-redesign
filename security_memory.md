# Security Memory

## 2026-02-11
- Identified and obfuscated a hardcoded Google API key (`AIzaSyBc...`) used for translation across 94 mirrored HTML files. Replaced with `YOUR_GOOGLE_TRANSLATE_API_KEY`.
- Found multiple external links with `target="_blank"` missing `rel="noopener noreferrer"`. Used `harden_links.py` to automate the fix.
- Inspected `cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js`. It's standard Cloudflare email obfuscation, but we should keep an eye on its use of `innerHTML`.
- Removed `https://cdn.tailwindcss.com/` from `partner-program-signup.html` as it is a development-only script and potentially unsafe/redundant for a production mirror.
- Added a basic CSP to `index.html` as a starting point for hardening.
- Visual verification confirmed that security changes did not break the page layouts.
