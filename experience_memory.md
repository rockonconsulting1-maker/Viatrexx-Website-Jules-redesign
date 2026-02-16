# Experience Agent Memory

## Common Issues Identified
- Root level files often use redundant `../` in relative paths for assets located in the root.
- Missing `aria-current="page"` on active navigation links.
- Missing `aria-label` on icon-only buttons.
- Layout jumps due to `href="#"`.

## Standards to Follow
- Use `aria-current='page'` for active links.
- Add `aria-label` to buttons and social links.
- Inject global high-visibility focus ring style: `outline: 2px solid #005fcc; outline-offset: 2px;`.
- Replace `href='#'` with `href='javascript:void(0)'` in navigation/dropdowns.
- Reduce relative path depth by one level for root-level files if they incorrectly use `../`.
