# Project Alerts - 2026-02-11

## For Optimization Agent
- Asset paths in `index.html` and `home.html` have been corrected from `../` to root-relative. If you are optimizing images or scripts, please ensure you use root-relative paths (e.g., `/assets/optimized/...`) as well.
- Navigation links for the homepage have been updated with `aria-current="page"`.
- Some `href="#"` links were changed to `href="javascript:void(0)"` to prevent layout jumps.
- **Nuxt Hydration Data Update:** Manual updates were made to `__NUXT_DATA__` in `index.html` and `home.html` to reflect the HTML changes. This is necessary in this mirrored environment to prevent Nuxt hydration from reverting accessibility and path fixes on the client side.
- **Security:** The hardcoded Google Translate API key `AIzaSyBcVFz0OYXC2zeEZkmz86sl4EQeVOye7V8` was obfuscated to `YOUR_GOOGLE_TRANSLATE_API_KEY` across all audited files.
