# Current Website Gathering Report

## 1. Pages and Links
- Total Pages: 74
- Total Unique Links: 98
- Full list of pages available in `site_snapshot.json`.

## 2. Styles (Master Sheet)
- Total Unique CSS Classes: 756
- Consolidated styles list: `current_styles.txt`.
- Primary Frameworks: Tailwind CSS 2.2.19, FontAwesome 5/6, Animate.css.
- Inline styles are prevalent in the mirrored HTML, indicating a need for tokenization.

## 3. Copywriting (Master Content)
- Content extracted from all semantic tags across all pages.
- Full text dump: `current_copywriting.txt`.
- Observations: Copy is currently feature-focused; needs benefit-driven transformation.

## 4. Functions and Scripts
- Scripts found: 47
- Locations: Primarily in `stcdn.leadconnectorhq.com/_preview/`.
- These are mostly Nuxt/Vue-based hydration and UI logic from the original builder.

## 5. Components & Sections Identified
Based on frequency of IDs and classes across pages:
- **Navigation**: `#nav-menu-popup`, `.nav-menu`, `.close-menu`
- **Sections**: `.c-section`, `.fullSection`, `.inner`
- **Layout**: `.c-row`, `.c-column`, `.preview-container`
- **Special**: `#custom-code-...` blocks containing external widgets/HTML.
- **Modals**: Hidden divs with `popup` suffix.

## 6. Recommendations for Redesign
- Move to a unified Next.js App Router structure.
- Replace `.c-section` / `.c-row` with semantic components and Tailwind utility classes.
- Consolidate multiple FontAwesome versions into a single package.
- Abstract repeating Custom Code blocks into reusable React components.
